import movim_db_access
import sqlite_access
import config_store
import common_db_access
pard = config_store.application_parameters(use_ws=True)
id_transazione = 327742
cod_negozio = 1101013
pard["ws_cod_negozio"] = cod_negozio
pk_consumer = "HK_1010"
import json
lista_alfabeti_nome_cognome = {}
lista_alfabeti_indirizzo = {}
movim_db_access.promo_engine_v2(pard,id_transazione)


from validation import locale
lista_alfabeti_nome_cognome = json.dumps(locale.get_multi_alphabet_config(pard, "CONSUMER_NAMES"))
lista_alfabeti_indirizzo = json.dumps(locale.get_multi_alphabet_config(pard, "CONSUMER_ADDRESSES"))

import config_store
pard = config_store.application_parameters(use_ws=True)
cod_negozio = '0100520'
id_transazione = '887'
from movim_db_access import get_testa_e_righe
testa, righe, mov_contabilita = get_testa_e_righe(pard, cod_negozio, id_transazione)
testa = testa[0]
import json
aliquote_d = json.loads(testa["dettaglio_iva"])["aliquote_d"]
pk_consumer = testa.get("cod_mitt_dest")
discount_fidelity = 0
from common.pos.constants import DISCOUNT_MAP_PROMO_ENGINE_V2
for k,v in DISCOUNT_MAP_PROMO_ENGINE_V2.items():
    discount_fidelity = sum(pag['importo_finale'] for pag in mov_contabilita if pag['codice_movimento'] == v)
