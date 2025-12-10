import sys, argparse

sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/scripts'])

for lib_dir in [
	'/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/site/bin',
	'/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/site/bin/lib',
	'/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/daemons',
	'/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/'
]:
	if not lib_dir in sys.path:
		sys.path.insert(0, lib_dir)

import pprint
import config_store
from lib import sqlite_access

parser = argparse.ArgumentParser(description="catalogo_prezzi",
								 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-l", "--limit", help="limit query", default=10)
parser.add_argument("-p", "--price", help="price query", default=100)
parser.add_argument("-m", "--minor", action='store_true', help="p.prezzo < %s")
args = parser.parse_args()
config = vars(args)

pard = config_store.application_parameters(use_ws=True)
cod_negozio = pard['POS_CONFIG']['COD_NEGOZIO']

limit = config['limit']
price = config['price']

try:
	pard['mysql_query'] = """
		SELECT c.sku, c.modello, p.prezzo
		FROM catalogo c
		INNER JOIN prezzi p ON c.modello = p.modello
		WHERE {wh}
		LIMIT %s
	""".format(wh="p.prezzo < %s" if config['minor'] else "p.prezzo > %s")
	result = sqlite_access.sqlite_dict(pard, params=(price, limit,), dbname=pard['CATALOG_DB_FILE'])
except:
	pard['mysql_query'] = """
		SELECT c.sku, c.modello, p.prezzo
		FROM catalogo c
		INNER JOIN prezzi p ON c.modello = p.modello
		WHERE {wh}
		LIMIT {limit}
	""".format(
		wh="p.prezzo > {price}".format(price=price) if config['major'] else "p.prezzo < {price}".format(price=price),
		limit=limit
	)
	result = sqlite_access.sqlite_dict(pard, dbname=pard['CATALOG_DB_FILE'])

print(pard['mysql_query'])
pprint.pprint(result)
