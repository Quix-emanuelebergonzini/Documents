# Riempi user_cloud e pwd_cloud con i tuoi username e password de cloud
# Eseguire questi comandi
# - sudo python3 -m pip install PyMySQL
# - sudo python3 -m pip install sshtunnel
# Se dopo aver avviato lo script esce un errore con la libreria bcrypt:
# - sudo python3 -m pip install python-bcrypt
# Avvia lo script con: python3 unidb.py <args>

# querycustom -q import_spool -c "PROD:*"
# querycustom -q consumer_fidelity -l 4 -cn 0100509 -t LOYALTY_CARD_NEW

import sys
sys.path.extend(["/Users/emanuele.bergonzini/Documents/Documents/scripts"])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

import argparse
# import pymysql.cursors
import json
import warnings
# from cryptography.utils import CryptographyDeprecationWarning

from credenziali_cloud import user_cloud, pwd_cloud, QUERIES
from commons.utils import execute_query, split_queries

usage = "usage: query_custom.py [args]"
parser = argparse.ArgumentParser(usage)

parser.add_argument(
	"-notran", "--no-transactions", action="store_true", dest="no_transactions",
	help="Di default le query vengono gestite in transazione, se questo flag viene passato invece non saranno usate"
)

parser.add_argument(
	"-l", "--limit", dest="limit",
	help="Imposta un limit alla query (default, 5)"
)

parser.add_argument(
	"-q", "--query", type=str, choices=["consumer_fidelity", "import_spool", "config_bundle", "count_import_spool"],
	help="Obbligatorio, indica quale query vuole essere eseguite"
)

parser.add_argument(
	"-i", "--info", action="store_true",
	help="Informazioni sullo scripts"
)

parser.add_argument(
	"-c", "--connections", action="store", type=str, dest="connections",
	help=(
		'Prende le connessioni da parametro invece che chiederle. Le connessioni sono in formato "env:nome", tipo '
		'"PROD:MA". Per specificare tutte le connessioni o tutti gli env si può usare l''asterisco tipo "*:MA".'
		'Per eseguire su tutte si può indicare solo l''asterisco o "all". Connessioni multiple vanno separate con la'
		'virgola, tipo "PROD:MA,UAT:LINMARA"'
	)
)

parser.add_argument(
	"-n", "--cod_negozio", dest="cod_negozio",
	help="Se query è consumer_fidelity allora obbligatorio il cod_negozio"
	# Action fa che il parametro venga iniettato come boolean a True se passato.
	# Altrimenti si aspetta un valore dopo il parametro action="store_true"

	# action="count"
	# se passiamo -ccc il valore immesso al parametro è 3 (numero di volte che passiamo il parametro)
)
parser.add_argument(
	"-t", "--tipo_fidelity", dest="tipo",
	help="Se -q è consumer_fidelity allora è obbligatorio il tipo (fidelity)"
)

parser.add_argument(
	"-cod", "--cod_installazione", type=str,
	help="Codice installazione di un negozio"
)

args = parser.parse_args()
config = vars(args)

# debug stampa help
if config.get("info"):
	parser.print_help()
	exit(1)

limit = 5 if not args.limit else args.limit  # tengo un limite basso per la leggibilità sul terminale

if args.query == "consumer_fidelity" and not (args.cod_negozio or args.tipo):
	print("Per la query di ricerca consumer con fidelity è necessario il cod_negozio e tipo (fidelity)")
	exit(1)

if args.query == "config_bundle" and not (args.cod_negozio or args.cod_installazione):
	print("Per la query di config_bundle è necessario il cod_negozio oppure il codice_installazione")
	exit(1)

print("Query:")
query = QUERIES[args.query]

if args.query == "consumer_fidelity":
	query = query.format(cod_negozio=args.cod_negozio, tipo=args.tipo, limit=limit)
elif args.query == "config_bundle":
	where_conditions = ""
	if args.cod_negozio:
		where_conditions += "valore = '{cod_negozio}'".format(cod_negozio=args.cod_negozio)
	if args.cod_installazione:
		where_conditions += "{cond} cod_installazione = '{cod_installazione}'".format(
			cond="AND" if args.cod_negozio else "",
			cod_installazione=args.cod_installazione
		)
	query = query.format(where_conditions=where_conditions)
else:
	query = query.format(limit=limit)

print(query)

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

execute_query(args, queries)
