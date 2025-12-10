# IVA_ITEM_DETAIL_ENABLED deve essere a 1 altrimenti non viene calcolato lo scorporo
cod_negozio = ""
id_transazione = 1

import sys
for lib_dir in ['site/bin', 'site/bin/lib', 'daemons']:
 if not lib_dir in sys.path:
  sys.path.insert(0, lib_dir)

import config_store
import movim_db_access

pard = config_store.application_parameters(use_ws=True)
pard["POS_CONFIG"]["COD_NEGOZIO"] = cod_negozio
config_store.load_config_from_ws(pard)
movim_db_access.salva_dettaglio_iva(pard, pard["POS_CONFIG"]["COD_NEGOZIO"], id_transazione)