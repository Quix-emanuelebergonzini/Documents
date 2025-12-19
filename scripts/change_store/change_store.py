#!/usr/bin/env python3
import sys, argparse
import json
import os.path
from time import sleep
import sqlite3
import shutil
import subprocess
import re
import ast
from itertools import groupby
from operator import itemgetter

sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/scripts'])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

from commons.utils import get_root_dir
from credenziali_cloud import MAPPING_AMBIENTE_MMFG, MAPPING_ENV

daemons_path = os.path.join("/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/daemons")
if daemons_path not in sys.path:
	sys.path.append(daemons_path)
ROOT_DIR = get_root_dir()

from process_monitor import PosMonitor


# Funzione per costruire il dizionario strutturato
def costruisci_dizionario(dati):
	installazioni = {}
	for voce in dati:
		cod = voce['cod_installazione']
		neg = voce['negozio']
		chiave = voce['chiave']
		valore = voce['valore']
		if cod not in installazioni:
			installazioni[cod] = {}
		installazioni[cod]['COD_NEGOZIO'] = neg
		installazioni[cod][chiave] = valore
	return installazioni


def change_configuration(configurazione):
	config_file = "/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/conf/config.py"
	template_file = "/Users/emanuele.bergonzini/Documents/Documents/scripts/change_store/config_template.py"
	with open(config_file, "w", encoding="utf-8") as f:
		f.truncate(0)
		f.close()
	shutil.copyfile(template_file, config_file)
	with open(config_file, "a", encoding="utf-8") as f:
		for k, v in configurazione.items():
			f.write("\n{} = '{}'".format(k, v))
		f.close()


def clean_database():
	sqliteConnection = sqlite3.connect("/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/database/temp.db")
	cursor = sqliteConnection.cursor()
	cursor.execute("DELETE FROM global_status WHERE 1=1")
	sqliteConnection.commit()
	cursor.close()
	if (sqliteConnection):
		sqliteConnection.close()


def empty_conf_version():
	ROOT_DIR = '/Users/emanuele.bergonzini/repos/posweb'
	POSWEB_ROOT_DIR = os.path.join(ROOT_DIR, 'mmfg', 'posweb')
	sed_c = """sed -i '' 's/^\\(DB_.*=\\).*$/\\1""/' conf/version.py"""
	bash_clean = """cd {0} && {1}""".format(POSWEB_ROOT_DIR, sed_c)
	status, output = subprocess.getstatusoutput(bash_clean)
	if status != 0:
		raise Exception('Errore esecuzione clean: {0}'.format(output))


def stopping_posweb():
	PosMonitor().handle_input(ord('X'))


def starting_posweb():
	PosMonitor().handle_input(ord('Z'))


##################################################################
##################################################################
###################### STARTING PROCEDURE ########################
##################################################################
##################################################################

languages_enabled = ['ITAL', 'SPAG', 'PORT', 'FRAN', 'INGL', 'JAPA', 'TEDE', 'DANE', 'OLAN', 'CHIN', ]


def main():
	parser = argparse.ArgumentParser(description="Cambio del negozio in locale configurato su Posweb",
									 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("-a", "--ambiente", choices=MAPPING_AMBIENTE_MMFG, help="define type store", required=True)
	parser.add_argument("-ld", "--landscape", choices=['TEST', 'STAGING', 'test', 'staging'], help="define type landscape", required=True)
	parser.add_argument("-l", "--language", choices=languages_enabled, help="define gui language store")
	parser.add_argument("-s", "--skipdb", action="store_true", help="no change to db local")
	parser.add_argument("-sl", "--slave", action="store_true", help="store on slave terminal")
	parser.add_argument("-c", "--copy", action="store_true", help="configura solo il config.py")
	args = parser.parse_args()
	config = vars(args)
	print(config)

	result = None
	i = 0

	ambiente = MAPPING_ENV.get(config['ambiente'])
	if not ambiente:
		ambiente = config['ambiente']
	else:
		print(f"Ambiente convertivo in {ambiente}")
	ambiente = ambiente.upper()

	landscape = config["landscape"].upper()

	key_search = ['STORE_SIGN', 'COUNTRY_CODE', 'STORE_CHANNEL', 'B2E_ENABLED', 'AVAILABLE_BRANDS', 'BRANDS_CATALOGO',
				  'GUI_LANGUAGE', 'PRINT_LANGUAGE']
	print("Desideri cercare qualche parametro specifico?")
	filtro = input("Inserire il filtro di ricerca (lasciare vuoto per nessuno): ")
	if filtro:
		split_filtro = filtro.split(',')
		if len(split_filtro) > 1:
			key_search_add = []
			for f in split_filtro:
				key_search.append(f.strip().upper())
		else:
			key_search.append(filtro.upper())
	key_search = ', '.join([f"'{k}'" for k in key_search])

	comando = f'python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/utility/unidb.py -o -c "{landscape}:{ambiente}" -q "SELECT pcb.cod_installazione, pcs.negozio, pcs.chiave, pcs.valore FROM pos_config_bundle pcb JOIN pos_config_store pcs ON pcb.valore = pcs.negozio AND pcs.chiave IN ({key_search}) where pcb.tipologia_istanza = \'POSWEB_OFFLINE\' order by pcb.cod_installazione;"'
	# print(comando)
	result = subprocess.run(comando, shell=True, capture_output=True, text=True)
	stdout = result.stdout
	match = re.search(r"(\[\{'cod_installazione':.*\}\])", stdout)
	if match:
		result = ast.literal_eval(match.group(1))
		# print(result)
		for key, group_var in groupby(result, itemgetter("cod_installazione", "negozio")):
			gr = list(group_var)
			print(f"{i}) Configurazione negozio per installazione: {key[0]} - negozio: {key[1]}")
			for item in gr:
				print("  {}: {}".format(item["chiave"], item["valore"]))
			i += 1

	selezione = input("Selezionare la configurazione che si vuole installare: ")
	installazioni = costruisci_dizionario(result)
	list_cods = list(installazioni.keys())
	# print(installazioni[list_cods[int(selezione)]])
	try:
		cod_installazione = list_cods[int(selezione)]
	except IndexError:
		print("Selezione non valida!")
		sys.exit(1)
	print("Configurazione selezionata: {}".format(cod_installazione))
	cod_params = installazioni[list_cods[int(selezione)]]
	print("Parametri negozio selezionato: {}".format(cod_params))

	comando = f'python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/utility/unidb.py -o -c "{landscape}:{ambiente}" -q "SELECT key_value from pos_dynamic_config where key_name = \'MMFG_WS_HOST\' ;"'
	mmfg_ws_host = subprocess.run(comando, shell=True, capture_output=True, text=True)
	stdout = mmfg_ws_host.stdout
	match = re.search(r"(\[\{'key_value':.*\}\])", stdout)
	if match:
		mmfg_ws_host = ast.literal_eval(match.group(1))

	configurazione = {
		'ambiente': config['ambiente'],
		'cash_id': '01' if not config['slave'] else '02',
		'cod_installazione': cod_installazione,
		'lista_cod_negozio': cod_params['COD_NEGOZIO'],
		'mmfg_ws_host': mmfg_ws_host[0]["key_value"],
		'gui_language': cod_params['GUI_LANGUAGE'] if not config['language'] else config['language'],
		'cash_role': 'MASTER' if not config['slave'] else 'SLAVE',
		'master_ip': '192.168.1.107' if not config['slave'] else 'dos-mm-de.posweb.mmfg.it',
		'master_port': '8000' if not config['slave'] else '80',
	}

	print("Configurazione selezionata:")
	print(json.dumps(configurazione, indent=4))

	copy = config.get("copy", False)

	#comando = f'python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/utility/unidb.py -o -c "{landscape}:{ambiente}" -f /Users/emanuele.bergonzini/Documents/Documents/scripts/invoke/unidb_check_installazioni.sql'
	#mmfg_ws_host = subprocess.run(comando, shell=True, capture_output=True, text=True)
	#stdout = mmfg_ws_host.stdout
	#print(stdout)

	starting_procedure = input("Interrompere l'avvio della procedura (default: no) ")
	if not starting_procedure:
		stop_process = input("Avviare i demoni alla fine del cambio negozio (default: si) ")
		if not copy:
			print("Starting procedure")
			stopping_posweb()
			sleep(1.00)
		if not copy:
			print("Stopping all!")
			clean_database()
			sleep(1.00)
		if not copy:
			print("STEP 1) Global status empty DONE")
			if not config['skipdb']:
				empty_conf_version()
				sleep(1.00)
				print("STEP 2) Version file empty DONE")

		change_configuration({
			'COD_INSTALLAZIONE': configurazione['cod_installazione'],
			'LISTA_COD_NEGOZIO': configurazione['lista_cod_negozio'],
			'MMFG_WS_HOST': configurazione['mmfg_ws_host'],
			'GUI_LANGUAGE': configurazione['gui_language'],
			'CASH_ROLE': configurazione['cash_role'],
			'CASH_ID': configurazione['cash_id'],
			'MASTER_PORT': configurazione['master_port'],
			'MASTER_IP': configurazione['master_ip'],
		})
		sleep(1.00)
		print("STEP 3) Config file changed DONE")

		if not stop_process and not copy:
			starting_posweb()
			print("STEP 4) Starting Posweb DONE")

		print("Ending procedure")
	else:
		print("Do nothing bye bye")


if __name__ == "__main__":
	main()
