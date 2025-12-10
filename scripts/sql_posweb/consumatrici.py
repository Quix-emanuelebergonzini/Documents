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

parser = argparse.ArgumentParser(description="consumer",
								 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-l", "--limit", help="limit query", default=10)
args = parser.parse_args()
config = vars(args)

pard = config_store.application_parameters(use_ws=True)
cod_negozio = pard['POS_CONFIG']['COD_NEGOZIO']

limit = config['limit']

result = []
try:
	pard['mysql_query'] = """
		SELECT c.*
		FROM consumer c
		WHERE grado_anonimato not in ('40', '50')
		LIMIT %s
	"""
	result = sqlite_access.sqlite_dict(pard, params=(limit,), dbname=pard['MAIN_DB_FILE'])
except:
	pass

print(pard['mysql_query'])
pprint.pprint(result)
