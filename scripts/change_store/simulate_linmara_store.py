#!/usr/bin/env python3
import sys, argparse
import json
import sqlite3
import shutil

sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/scripts'])

from change_store import change_configuration

config = {
	'COD_INSTALLAZIONE': '9000000004',
	'LISTA_COD_NEGOZIO': '4401927',
	'MMFG_WS_HOST' : 'https://pos-ws-bms-uat.linmara.com/bin/driver_ws',
	'MMFG_WS_PROXY': '',
	'GUI_LANGUAGE' : 'CHIN',
	'CASH_ROLE'    : 'MASTER',
	'CASH_ID'      : '01',
	'MASTER_PORT'  : '8000',
	'MASTER_IP'    : '192.168.1.107',
}
user_data = json.dumps({"SID_PROJECT_DATA": {}, "SID_PROJECT_LIST": ["RUOLO"], "USER": "assistenza",   "UTENTE_COGNOME": config["LISTA_COD_NEGOZIO"], "UTENTE_DATA_CAMBIO_PASSWORD": "2015-10-01 15:09:59", "UTENTE_EMAIL": "", "UTENTE_FORMATO_DATA": "EU", "UTENTE_FORMATO_NUMERO": "US", "UTENTE_ID_RADIUS": "", "UTENTE_INDIRIZZO_IP": "", "UTENTE_LINGUA": "INGL", "UTENTE_MATRICOLA": "", "UTENTE_NOME": "ASSISTENZA", "auth_list": {}})
auth = json.dumps({"POS:::Super": {"FUNZIONE": ["RUOLO:::POSSuper"], "NEGOZIO": [config["LISTA_COD_NEGOZIO"]]}})


##################################################################
##################################################################
###################### STARTING PROCEDURE ########################
##################################################################
##################################################################

change_configuration(config)

query_update = """
	REPLACE INTO negozi
	VALUES ('4401927', '4401927', '', '-四川省成都市高新区天府大道北段1199号成都银泰中心in99一层106', '0000', '2722 9631', '', 'INGL', '', 'CN', '', 'CHENGDU IN99 MM', 'HONG KONG', '200 CONNAUGHT ROAD ROOM   1711, CHINA MERCHANT TOWER,  SHUN TAK CENTRE,    CENTR', '', '+852 2545 2008 ', 'HK', '', 'MMNF', '', '', '20190221');

	UPDATE users
	SET user_data = '{user_data}', auth = '{auth}';
	
	UPDATE store_config
	SET cod_negozio = '4401927';
	
	UPDATE custom_values
	SET cod_negozio = '4401927';
	
	UPDATE commesse
	SET cod_negozio = '4401927';
	
	UPDATE store_config
	SET key_value = 'MM,WE,SP' 
	WHERE key_name = 'AVAILABLE_BRANDS';
	
	UPDATE store_config
	SET key_value = '1' 
	WHERE key_name = 'B2E_ENABLED';
	
	UPDATE store_config
	SET key_value = 'MM,WE,SP' 
	WHERE key_name = 'BRANDS_CATALOGO';
	
	UPDATE store_config
	SET key_value = 'ASYNC' 
	WHERE key_name = 'CONSUMER_MODE';
	
	UPDATE store_config
	SET key_value = 'CN' 
	WHERE key_name = 'COUNTRY_CODE';
	
	UPDATE store_config
	SET key_value = 'CNY' 
	WHERE key_name = 'CURRENCY_CODE';
	
	UPDATE store_config
	SET key_value = 'https://bms-uat.linmara.com/bin/driver' 
	WHERE key_name = 'MMFG_WEB_HOST';
	
	UPDATE store_config
	SET key_value = 'ws_gbmax_om' 
	WHERE key_name = 'OM_TYPE';

	UPDATE store_config
	SET key_value = 'NF' 
	WHERE key_name = 'STORE_CHANNEL';
	
	UPDATE store_config
	SET key_value = 'Negozi Franchising' 
	WHERE key_name = 'STORE_CHANNEL_DESC';
	
	UPDATE store_config
	SET key_value = '1' 
	WHERE key_name = 'WECHAT_ENABLED';
	
	UPDATE store_config
	SET key_value = 'GDM' 
	WHERE key_name = 'OWNER';	
	
	UPDATE store_config
	SET key_value = '1' 
	WHERE key_name = 'CREDITO_SOSPESO_ENABLED';	
""".format(user_data=user_data, auth=auth)

path_database = '/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/database/main.db'
sqliteConnection = sqlite3.connect(path_database)
cursor = sqliteConnection.cursor()
cursor.executescript(query_update)

path_database = '/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/database/temp.db'
sqliteConnection = sqlite3.connect(path_database)
cursor = sqliteConnection.cursor()
cursor.execute("""
	DELETE FROM global_status WHERE 1
""")

sqliteConnection.commit()
cursor.close()
if (sqliteConnection):
	sqliteConnection.close()

print("Simulazione del negozio linmara 4401927 conclusa con successo")
print("Le consumatrici, il catalogo sono di HK !!!")