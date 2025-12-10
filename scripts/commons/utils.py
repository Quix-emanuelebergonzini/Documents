# qui ci sono metodi comuni a diversi scripts

import datetime
import re
import json
import os.path
import pymysql.cursors
from decimal import Decimal

import sys
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

from credenziali_cloud import CONNECTIONS

def get_root_dir():
	check_string = 'mmfg'
	check_last_string = 'posweb'
	actdir = "/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb"
	last_dirname = ''
	outdir = ''
	while True:
		dirname = os.path.basename(os.path.abspath(actdir))
		if dirname == '/':
			break
		actdir = os.path.dirname(os.path.abspath(actdir))
		if dirname == check_string and last_dirname == check_last_string:
			outdir = actdir
			break
		last_dirname = dirname
	return outdir

# Funzione che dirige le scelnte per controllare import spool
def update_output(result, conn):
	# USARE SOLO PER LA QUERY DI import_spool
	if result:
		for out in result:
			# print(out)
			if out.get("import_message"):
				print("-" * 50)
				print("xml in errore: {file_name}".format(file_name=out["file_name"]))
				if "edi" in out["file_name"] and not "edicom" in out["file_name"]:
					print("FILE EDI --> METTERE IGNORED")
					continue
				if "Duplicate entry" in out["import_message"]:
					index_duplicate = out["import_message"].rfind("Duplicate entry")
					print(out["import_message"][index_duplicate:])
					search_keys = re.search("([0-9]+\\-[0-9]+\\-[0-9]+)", out["import_message"][index_duplicate:])
					keys = search_keys.group().split("-")
					if 'om' in out["file_name"] or 'sale' in out["file_name"]:
						if 'om' in out["file_name"]:
							print("FILE DI OM --> SMAZZARE")
						else:
							print("FILE DI SALE --> CONTROLLARE")
						query = """
							SELECT pis.file_name, pis.dati
							FROM pos_movimentazioni pm
							INNER JOIN pos_import_spool pis using(file_name)
							WHERE anno_transazione = '{anno}' and cod_negozio = '{cod_negozio}' and id_transazione = '{id_transazione}'
						""".format(anno=keys[1], cod_negozio=keys[0], id_transazione=keys[2])
					elif 'orderfill' in out["file_name"]:
						print("FILE ORDERFILL --> CONTROLLARE SE DI OM NEL CASO SMAZZARE ALTRIMENTI CONTROLLARE	")
						query = """	
							SELECT pis.file_name, pis.dati
							FROM pos_orderfill po
							INNER JOIN pos_import_spool pis using(file_name)
							WHERE anno_orderfill = '{anno}' and cod_negozio = '{cod_negozio}' and numero_orderfill = '{numero_orderfill}'
						""".format(anno=keys[1], cod_negozio=keys[0], numero_orderfill=keys[2])
					res = exec_query(query, conn)
					res = fix_resultset(res)
					if len(res) > 0:
						print("file name recuperato --> {file_name}".format(file_name=res[0]["file_name"]))
						files_names_equals = out['file_name'] == res[0]['file_name']
						dati_equals = out['dati'] == res[0]['dati']
						print("I nomi dei files sono uguali? {}".format(files_names_equals))
						print("I json sono uguali? {}".format(dati_equals))
					# if not (files_names_equals and dati_equals):
					# diff = jsondiff.diff(out['dati'], res[0]['dati'], syntax='symmetric')
					# diff = main.diff_files(out['dati'], res[0]['dati'], formatter=formatting.XMLFormatter())
					# print(diff)
					else:
						print("record non trovato")
					print("-" * 50)
				elif "importi non coerenti nella riga" in out["import_message"]:
					index_duplicate = out["import_message"].rfind("importi non coerenti nella riga")
					print(out["import_message"][index_duplicate:])
					print("CONTROLLARE SE IL FILE NON E' SALE ALTRIMENTI è DA CONTROLLARE. ")
					print(
						"Errore più comune è retail_price diverso da final_price quando non c'è discount o correzione_importo")
					print("-" * 50)
				else:
					print("Altro tipo di errore da gestire:")
					print(out["import_message"])


# Funzione per richeidere in input all'utente una conferma si/no
def ask(msg):
	user_resp = input(msg + " ")
	if user_resp.lower() not in ("y", "n", ""):
		return ask(msg)
	return user_resp.lower() == "y"


# Funzione per eseguire una query
def exec_query(sql, db_conn):
	with db_conn.cursor() as cursor:
		cursor.execute(sql)
		result = cursor.fetchall()
	return result


def fix_resultset(resultset):
	return [fix_result(result) for result in resultset]


def fix_result(result):
	return {fix_field(field_name): fix_field(field_val) for field_name, field_val in result.items()}


def fix_field(field):
	if isinstance(field, datetime.datetime):
		return field.strftime('%Y-%m-%d %H:%M:%S')
	elif isinstance(field, datetime.date):
		return field.strftime('%Y-%m-%d')
	elif isinstance(field, int) or isinstance(field, float) or isinstance(field, Decimal):
		return "{}".format(field)
	elif isinstance(field, datetime.timedelta):
		return (datetime.datetime.min + field).time().strftime("%H:%M:%S")
	return field


def split_queries(q, query_delimiter=";"):
	ql = len(q)
	ret = []
	buffer = ""
	command = ""
	in_command = False
	escaped = False
	in_str_delimiter = None
	in_single_line_comment = False
	in_multi_line_comment = False
	char_at = lambda i: q[i] if i < ql else None
	for idx, ch in enumerate(q):
		buffer += ch
		# Se sono dentro un commento single line e trovo l'andata a capo, esco dal commento
		if in_single_line_comment:
			if ch in ("\n", "\r"):
				in_single_line_comment = False
		# Se sono dentro un commento multi line e trovo la sequenza di fine, esco al commento
		elif in_multi_line_comment:
			if ch == "*" and char_at(idx + 1) == "/":
				in_multi_line_comment = False
		# Se sono dentro una stringa e trovo il quote di fine stringa, esco dalla stringa
		elif in_str_delimiter:
			# Se è escapato non faccio nulla
			if escaped:
				escaped = False
			# Registro l'escape
			elif ch == "\\":
				escaped = True
			elif ch == in_str_delimiter:
				in_str_delimiter = None
		# Commento inline
		elif ch == "#" or (ch == "-" and char_at(idx + 1) == "-" and (char_at(idx + 2) or ".").isspace()):
			in_single_line_comment = True
		# Commento multiline
		elif ch == "/" and char_at(idx + 1) == "*":
			in_multi_line_comment = True
		# Se trovo l'inizio di una striga, segno il quote che devo cercare per verficare che sia terminata
		elif ch in ("`", '"', "'"):
			in_str_delimiter = ch
		# Se trovo il delimitatore della query, aggiungo il buffer al risultato e lo svuoto
		elif ch == query_delimiter:
			if buffer and buffer != ";":
				ret.append((buffer, command.upper()))
			in_command = False
			buffer = ""
			command = ""
		else:
			if ch.isalpha():
				if not command:
					in_command = True
					command += ch
				elif in_command:
					command += ch
			else:
				in_command = False
	if buffer and buffer != ";":
		ret.append((buffer, command.upper()))
	if in_str_delimiter:
		print("Stringa non chiusa")
		exit()
	elif in_multi_line_comment:
		print("Commento non chiuso")
		exit()
	return ret


def clean_resp_text(resp_text):
	resp_text = resp_text.replace('\t', '')
	resp_text = resp_text.replace('\n', '')
	resp_text = resp_text.replace('<b>', '')
	resp_text = resp_text.replace('</b>', '')
	resp_text = resp_text.replace('FGNEG-', '')
	resp_text = resp_text.replace('.local', '')
	return resp_text


# Esecuzione della query
def exec_query_evolute(args, queries, connection):
	result = None

	try:
		# Setto i dati di connessione per l'encoding
		exec_query("SET CHARACTER_SET_RESULTS=latin1;", connection)
		exec_query("SET CHARACTER_SET_CLIENT=latin1;", connection)

		# Avvio eventualmente la transazione
		if not args.no_transactions:
			connection.begin()

		# Esecuzione delle query vere e proprie
		for q, cmd in queries:

			result = exec_query(q, connection)
			if cmd in ("SELECT", "EXPLAIN"):
				result = fix_resultset(result)

				# qui deve solo ritornare output poi a seconda di chi lo chiama faccio le mie asserzioni
				if args.query not in ("import_spool", ""):
					print(json.dumps(result, indent=4))
				elif args.query != "":
					update_output(result, connection)

			else:
				result = exec_query("SELECT ROW_COUNT() as rc;", connection)
				print("Righe toccate: {}".format(result[0]["rc"]))

		# Applico eventualmente la transazione
		if not args.no_transactions:
			connection.commit()

	except Exception as ex_query:
		# Intercetto l'errore della query
		print("QUERY ERROR: {}".format(ex_query))
		# Lancio eventualmente il rollback della transazione
		if not args.no_transactions:
			try:
				connection.rollback()
			except:
				pass

	return result


def execute_query(args, queries):
	accept = {}
	if args.query == 'consumer_fidelity' or args.query == 'call_crm':
		accept = {"CRM": set(CONNECTIONS["CRM"].keys()) for k in CONNECTIONS["CRM"]["TEST"].keys()}
	elif args.connections:
		connections_raw = args.connections.upper()
		if connections_raw in ("ALL", "*"):
			connections_raw = "*:*"
		print(connections_raw)
		for conn in connections_raw.split(","):
			if ":" not in conn:
				print("Formato connessioni non valido")
				exit()
			conn_env, conn_name = conn.strip().split(":")
			for k_env, v_conn_all in CONNECTIONS.items():
				# print(k_env, v_conn_all)
				# print(v_conn_all)
				for v_conn in v_conn_all.keys():
					# print(conn_env, conn_name)
					if (k_env == conn_env or conn_env == "*") and (v_conn == conn_name or conn_name == "*"):
						accept.setdefault(k_env, set()).add(v_conn)

	# Se non ha scelto nulla mi fermo qui
	if not accept:
		print("Nessuna connessione selezionata")
		exit()

	exec_query_accept(accept, args, queries)


def exec_query_accept(accept, args, queries):
	result = None

	# Ciclo di esecuzione delle query sulle connessioni selezionate
	for k, c in accept.items():
		for cn in c:
			print("")
			print("=" * 10 + " " + k + " " + cn + " " + "=" * 10)
			conn_data = CONNECTIONS[k][cn]
			executed = False
			try:
				# Apertura connessione al db
				connection = pymysql.connect(
					host=conn_data["host"],
					user=conn_data["user"],
					password=conn_data["pwd"],
					db=conn_data["db"],
					port=conn_data.get("port", 3306),
					# charset='latin1',
					cursorclass=pymysql.cursors.DictCursor
				)

				result = exec_query_evolute(args, queries, connection)

				# Chiusura connessione
				connection.close()

			except Exception as ex_conn:
				# Intercetto l'errore di connessione
				print("CONN ERROR: {}".format(ex_conn))

			# Se ha dato errore e l'opzione "die" è impostata, esco
			# if not executed:  # and args.die:
			#	exit()

	return result
