import sys, argparse

sys.path.extend(["/Users/emanuele.bergonzini/Documents/Documents/scripts"])

for lib_dir in [
	"/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/site/bin",
	"/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/site/bin/lib",
	"/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/daemons",
	"/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/"
]:
	if not lib_dir in sys.path:
		sys.path.insert(0, lib_dir)

import pprint
import config_store
from lib import sqlite_access

pard = config_store.application_parameters(use_ws=True)

pard["mysql_query"] = """ DELETE FROM movimentazioni WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM movimenti_capi WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM movimenti_contabilita WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM movimentazioni_custom WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM movimentazioni_custom_multi WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM movimentazioni_relazioni WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM vendite_sospese WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM sospesi_contabilita WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM mmfg_queue WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM order_management_queue WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM data_queue WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['MAIN_DB_FILE'])
pard["mysql_query"] = """ DELETE FROM events WHERE 1; """
sqlite_access.sqlite_send(pard, dbname=pard['LOCAL_DB_FILE'])
