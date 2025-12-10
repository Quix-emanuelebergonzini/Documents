# Riempi user_cloud e pwd_cloud con i tuoi username e password de cloud
# Eseguire questi comandi
# - sudo python3 -m pip install PyMySQL
# - sudo python3 -m pip install sshtunnel
# Se dopo aver avviato lo script esce un errore con la libreria bcrypt:
# - sudo python3 -m pip install python-bcrypt
# Avvia lo script con: python3 unidb.py <args>

import sys
import readline
sys.path.extend(["/Users/emanuele.bergonzini/Documents/Documents/scripts"])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

import optparse
import pymysql.cursors
import json

import os.path
import warnings
from cryptography.utils import CryptographyDeprecationWarning
# Questa riga serve a sopprimere alcuni warning dati dalla libreria del tunnel
with warnings.catch_warnings():
	warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
	from sshtunnel import SSHTunnelForwarder

from credenziali_cloud import CONNECTIONS

from commons.utils import ask, split_queries, fix_resultset, exec_query

# Credenziali cloud
# user_cloud = "bergonzini.e"
# pwd_cloud = "OcgajVik}ow2"

# Parsing argomenti
usage = "usage: unidb.py [options]"
parser = optparse.OptionParser(usage)
parser.add_option(
	"-d", "--die", action="store_true", dest="die",
	help="Ferma l'esecuzione del programma al primo errore"
)
parser.add_option(
	"-n", "--no-transactions", action="store_true", dest="no_transactions",
	help="Di default le query vengono gestite in transazione, se questo flag viene passato invece non saranno usate"
)
parser.add_option(
	"-j", "--json", action="store_true", dest="json",
	help="Se passato, questo parametro permette di converire l'output, se mostrato, in json"
)
parser.add_option(
	"-p", "--pretty-print", action="store_true", dest="pretty_print",
	help="Se passato, in combinazione con il paramtro json stampa una modalità leggibile e formattata dell'output"
)
parser.add_option(
	"-o", "--output", action="store_true", dest="output",
	help=(
		"Di default viene mostrato il contatore di query eseguite, se viene passato questo parametro viene fatto "
		"vedere il vero output delle query"
	)
)
parser.add_option(
	"-f", "--file", action="store", type="string", dest="file",
	help="Esegue un file di query"
)
parser.add_option(
	"-q", "--query", action="store", type="string", dest="query",
	help="Esegue la query specificata"
)
parser.add_option(
	"-c", "--connections", action="store", type="string", dest="connections",
	help=(
		'Prende le connessioni da parametro invece che chiederle. Le connessioni sono in formato "env:nome", tipo '
		'"PROD:MA". Per specificare tutte le connessioni o tutti gli env si può usare l''asterisco tipo "*:MA".'
		'Per eseguire su tutte si può indicare solo l''asterisco o "all". Connessioni multiple vanno separate con la'
		'virgola, tipo "PROD:MA,UAT:LINMARA"'
	)
)
(options, args) = parser.parse_args()

print("-" * 100)
print("PER PRODUZIONE LINMARA FARE A MANO NON DIMENTICARLO!!!! ANZI FALLO PRIMA DEGLI ALTRI!!!!")
print("-" * 100)

parser.print_help()

# Input della query
if options.file:
	# Se deve essere presa da file, controllo che il file esista poi lo leggo
	if not os.path.isfile(options.file):
		print("File '{}' inesistente".format(options.file))
		exit()
	with open(options.file, "r") as f:
		query = f.read()
elif options.query:
	query = options.query
else:
	# Altrimenti chiedo all'utente la query
	print("Query:")
	query = ""
	while True:
		rd = sys.stdin.readline()  # studiare l'uso di input()
		if not rd:
			break
		query += rd
	print("")

# Niente query vuote
query = query.strip()
if not query:
	print("Query vuota")
	exit()

# Aggiungo il ";" finale se serve
if not query.endswith(";"):
	query += ";"

# Splitto le query
queries = split_queries(query)

accept = {}
if options.connections:
	connections_raw = options.connections.upper()
	if connections_raw in ("ALL", "*"):
		connections_raw = "*:*"
	for conn in connections_raw.split(","):
		if ":" not in conn:
			print("Formato connessioni non valido")
			exit()
		conn_env, conn_name = conn.strip().split(":")
		for k_env, v_conn_all in CONNECTIONS.items():
			for v_conn in v_conn_all.keys():
				if (k_env == conn_env or conn_env == "*") and (v_conn == conn_name or conn_name == "*"):
					accept.setdefault(k_env, set()).add(v_conn)
else:
	# Chiedo all'utente dove eseguire le query e memorizzo i risultati
	print('Digitando "y" si esegue la query, con "n" o lasciando vuoto non si esegue')
	if ask("Eseguire su tutti?"):
		accept = {k: set(CONNECTIONS[k].keys()) for k in CONNECTIONS.keys()}
	else:
		for k in CONNECTIONS.keys():
			print("=" * 10 + " " + k + " " + "=" * 10)
			for v in CONNECTIONS[k].keys():
				if ask("{}".format(v)):
					accept.setdefault(k, set()).add(v)

# print(accept)

# Se non ha scelto nulla mi fermo qui
if not accept:
	print("Nessuna connessione selezionata")
	exit()

# Ciclo di esecuzione delle query sulle connessioni selezionate
for k, c in accept.items():
	for cn in c:
		print("")
		print("=" * 10 + " " + k + " " + cn + " " + "=" * 10)
		conn_data = CONNECTIONS[k][cn]
		executed = False
		try:
			tunnel = None

			# Se richiesto dalla connessione apro il tunnel
			use_tunnel = conn_data.get("sshHost")
			if use_tunnel:
				tunnel = SSHTunnelForwarder(
					(conn_data["sshHost"], conn_data.get("sshPort", 22)),
					ssh_password=conn_data.get("sshPwd", ""),
					ssh_username=conn_data["sshUser"],
					remote_bind_address=(conn_data["host"], conn_data.get("port", 3306))
				)
				tunnel.start()

			# Apertura connessione al db
			connection = pymysql.connect(
				host='127.0.0.1' if use_tunnel else conn_data["host"],
				user=conn_data["user"],
				password=conn_data["pwd"],
				db=conn_data["db"],
				port=tunnel.local_bind_port if use_tunnel else conn_data.get("port", 3306),
				# charset='latin1',
				cursorclass=pymysql.cursors.DictCursor
			)
			# Esecuzione della query
			try:
				# Setto i dati di connessione per l'encoding
				exec_query("SET CHARACTER_SET_RESULTS=latin1;", connection)
				exec_query("SET CHARACTER_SET_CLIENT=latin1;", connection)

				# Avvio eventualmente la transazione
				if not options.no_transactions:
					connection.begin()

				# Esecuzione delle query vere e proprie
				n_queries = len(queries)
				idx_query = 0
				for q, cmd in queries:
					res = exec_query(q, connection)
					if options.output:
						if cmd in ("SELECT", "EXPLAIN"):
							res = fix_resultset(res)
							executed = True
							print(json.dumps(res, indent=4 if options.pretty_print else None) if options.json else res)
						else:
							res = exec_query("SELECT ROW_COUNT() as rc;", connection)
							print("Righe toccate: {}".format(res[0]["rc"]))
					else:
						clear_row = idx_query > 0
						idx_query += 1
						if clear_row:
							print("\033[A\033[A")
						print("Eseguo query {} di {}".format(idx_query, n_queries))

				# Applico eventualmente la transazione
				if not options.no_transactions:
					connection.commit()
			except Exception as ex_query:
				# Intercetto l'errore della query
				print("QUERY ERROR: {}".format(ex_query))
				# Lancio eventualmente il rollback della transazione
				if not options.no_transactions:
					try:
						connection.rollback()
					except:
						pass

			# Chiusura connessione
			connection.close()

			# Chiusura tunnel se era stato aperto
			if use_tunnel:
				tunnel.stop()
		except Exception as ex_conn:
			# Intercetto l'errore di connessione
			print("CONN ERROR: {}".format(ex_conn))

		# Se ha dato errore e l'opzione "die" è impostata, esco
		if not executed and options.die:
			exit()
