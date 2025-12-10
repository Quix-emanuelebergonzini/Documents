## LA BASE DA CUI PARTIRE PER POSWEB ##
# in caso ./bin/python site/bin/console non funzioni #

# riga 1-14 da qualsiasi python aggiungo "posweb" (è come usare il site/bin/console...)
import sys

for lib_dir in [
	'site/bin',
	'site/bin/lib',
]:
	if not lib_dir in sys.path:
		sys.path.insert(0, lib_dir)

import config_store
pard = config_store.application_parameters(use_ws=True)

# riga 17-19 aggiungo per un posweblite che non ha un negozio settato
cod_negozio = '1601001'
pard["POS_CONFIG"]["COD_NEGOZIO"] = '1601001'
config_store.load_config_from_ws(pard)