################ sono su BMS e avvio il suo docker per avviare un job su poswsbe #####################
~~~
docker ps
~~~~
mostra: docker (apache, runtime, proxy) con i rispettivi nomi delle immagini (es, docker_apache_1, docker_runtime_1)
***

cd bms/<BMS>
./docker/docker_images_init.sh
./docker/components_build.sh
./docker/compose_up.sh
*se dopo il primo avvio cè qualche errore che non trova degli import, fare laggiornamento dei proxy mmfg*

~~~
./docker/docker_images_init.sh
./docker/components_build.sh
./docker/compose_up.sh
~~~

# gcloud auth login --update-adc

una volta avviato si può aprire una nuova shell e aprire il runtime
>>> docker exec -it docker-runtime-1 bash

oppure avviare in una nuova shell il server apache2
>>> docker exec -it docker-apache-1 bash

### avviare il python con struttura (su BMS)
>>> python main/bin/console.py

### avviare il python con struttura (su POSWEB)
>>> python site/bin/console.py

## USARE IL LOGGER DURANTE IL DEBUG IN CONSOLE DI STRUTTURA ####
import logging
from . import LOGGER_BASE
logger = logging.getLogger(LOGGER_BASE + "." + __name__)

## POSWEB ##
cd /rnd/pos/mmfg/posweb
from backend.kpi.locator import locator as loc
from config import env
webservice_config={'SW_INSTALLED_VERSION': env['SW_INSTALLED_VERSION'],'WS_ERROR_CODE': env['WS_ERROR_CODE'],'WS_CONFIG_MMFG': env['WS_CONFIG_MMFG'],'WS_CONFIG_MASTER':env['WS_CONFIG_MASTER'],}

# se non va env... provare con
from config.utils import get_env
env = get_env()
webservice_config={'SW_INSTALLED_VERSION': env['SW_INSTALLED_VERSION'],'WS_ERROR_CODE': env['WS_ERROR_CODE'],'WS_CONFIG_MMFG': env['WS_CONFIG_MMFG'],'WS_CONFIG_MASTER':env['WS_CONFIG_MASTER'],}

kpi_service = loc.get_service('KpiService', webservice_config=webservice_config)

from backend.promo_engine.locator import locator as loc
promo_service = loc.get_service('PromoEngine')
vendita = {}
vendita['consumer'] = None
vendita['data'] = None
vendita['cod_negozio'] = '1101013'
vendita['items'] = []
promo_service.lista_promo(vendita)

## BOSS ##
import poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
from config.ws_client import ws_config
from storebackoffice.bin.boss.consumer_firma.locator import locator as loc
consumer_service = loc.get_service('Negozio')
consumer_service.cerca_negozi('1101119')

### BMS ### ##aggiornare i proxy se non va l'istanza del service
# filters = {
#     "stessa_insegna": True,
#     "extended_search": True,
#     "pk_esclusi": "[]",
#     "codice_proprietario": "MMJ",
#     "promotions": "SYNC",
#     "autocomplete_search": "DAIDAI",
#     "limit": 1,
#     "brand_consensi": "MM",
#     "search_BMS_only": True,
#     "telefono": "", "telefono_fullwidth": "",
#     "bypass_privacy_check": True,
#     "alfabeti_nomi": "[\"KANJI\", \"KANA\"]", "alfabeti_indirizzi": "[\"JAPA\"]",
#     "enabled_search_decoded": True, "search_extended_insegna": "MM"
# }
# filters = {
#   "stessa_insegna": True,
#   "extended_search": True,
#   "pk_esclusi": "[\"MMJ_160505\", \"MMJ_160516\", \"MMJ_160607\", \"MMJ_160608\"]",
#   "codice_proprietario": "MMJ",
#   "promotions": "SYNC",
#   "autocomplete_search": "SHIOZAWA",
#   "limit": 6,
#   "brand_consensi": "MM",
#   "search_BMS_only": True,
#   "telefono": "",
#   "telefono_fullwidth": "",
#   "bypass_privacy_check": True,
#   "alfabeti_nomi": "[\"KANJI\", \"KANA\"]",
#   "alfabeti_indirizzi": "[\"JAPA\"]",
#   "enabled_search_decoded": True,
#   "search_extended_insegna": "MM"
# }
# ricerca libera con caratteri giapponesi
# filters = {
        # "stessa_insegna": True, "extended_search": True, "pk_esclusi": "[]", "codice_proprietario": "MMJ", "promotions": "SYNC", "autocomplete_search": "\u30c0\u30a4\u30c0\u30a4", "limit": 10, "brand_consensi": "MM", "search_BMS_only": True, "telefono": "", "telefono_fullwidth": "", "bypass_privacy_check": True, "alfabeti_nomi": "[\"KANJI\", \"KANA\"]", "alfabeti_indirizzi": "[\"JAPA\"]", "enabled_search_decoded": True, "search_extended_insegna": "MM"
# }
# email
# filters = {
#     "stessa_insegna": True, "extended_search": True, "pk_esclusi": "[]", "codice_proprietario": "MMJ", "promotions": "SYNC", "email": "kdaidai@maxmara.co.jp", "limit": 10, "brand_consensi": "MM", "search_BMS_only": True, "telefono": "", "telefono_fullwidth": "", "bypass_privacy_check": True, "alfabeti_nomi": "[\"KANJI\", \"KANA\"]", "alfabeti_indirizzi": "[\"JAPA\"]", "enabled_search_decoded": True, "search_extended_insegna": "MM"
# }
# filters = {
#     "stessa_insegna": True, "extended_search": True, "pk_esclusi": "[]", "codice_proprietario": "MMJ",
#     "promotions": "SYNC", "limit": 10, "brand_consensi": "MM",
#     "telefono": "8100334444", "telefono_fullwidth": "\uff18\uff11\uff10\uff10\uff13\uff13\uff14\uff14\uff14\uff14",
#     "search_BMS_only": True, "bypass_privacy_check": True,
#     "alfabeti_nomi": "[\"KANJI\", \"KANA\"]", "alfabeti_indirizzi": "[\"JAPA\"]",
#     "enabled_search_decoded": True, "search_extended_insegna": "MM"
# }
import poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
import json
from config.ws_client import ws_config
from poswsbe.consumer.locator import locator as loc
consumer_service = loc.get_service("PosWsBeConsumerService")
filters = {
    "stessa_insegna": True, "extended_search": True, "pk_esclusi": "[]",
    "codice_proprietario": "MMJ", "promotions": "SYNC", "email": "xxx.v3v.xoxo@gmail.com",
    "limit": 10, "brand_consensi": "MM", "search_BMS_only": True, "telefono": "",
    "telefono_fullwidth": "", "bypass_privacy_check": True,
    "alfabeti_nomi": "[\"KANJI\", \"KANA\"]", "alfabeti_indirizzi": "[\"JAPA\"]",
    "enabled_search_decoded": True, "search_extended_insegna": "MM"
}
consumer_service.ricerca_consumatrici_BMS(filters, negozi_l=['9000801234',], limit=filters["limit"])

### CRM ###
from fidelity.locator import locator as loc
from fidelity.controller import FidelityRest
controller = FidelityRest(locator=loc)

## CRM ##
from initiative.locator import locator as loc
serv = loc.get_service("CRMBackOffice")
filtro = {
    "cognome": "ZUNTINI",
    "nome": "MARTA", # OPPURE "LUCA"
    "enabled_search_decoded": True,
    "cod_negozio": "0100400",
    "search_extended_insegna": "MA",
}
serv.ricerca_consumatrici_da_pos(filtro, limit=100)

## oppure ##
from initiative.locator import locator as loc
serv = loc.get_service("CRMBackOffice")
filtro = {
    "cod_negozio": "0100051", # negozio DT hu
    "barcode": "2130022384401",
    "codice_proprietario": "DT",
    "promotions": "SYNC"
}
group_pools = [
	["LOYALTY_CARD", "LOYALTY_CARD_NEW",
	 "LOYALTY_INTREND_AT", "LOYALTY_INTREND_ES",
	 "LOYALTY_INTREND_FR", "LOYALTY_INTREND_HU",
	 "LOYALTY_INTREND_NL"]
]
type_to_search = serv.get_source_method('get_type_fidelity_to_search')(filtro["cod_negozio"])
type_searchable = []
for type in type_to_search:
    for pool in group_pools:
	       if type in pool:\
               type_searchable += pool
if not type_searchable:
    type_searchable = type_to_search
else:
	type_searchable = list(set(type_searchable))
pks = serv.get_source_method('consumatrici_con_promozione_sync')(filtro["barcode"], type_searchable)
print(pks)

## ricerca su log_tax_free ##
import posws.bin.poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
import json
from config.ws_client import ws_config
from posws.bin.poswsbe.globalblue.locator import locator as loc
service = loc.get_service(GlobalBlueConfig)
negozio = {}
negozio[codice_negozio] = 0100076
log_tax_free = service.search_log_tax_free(negozio,ISSUE_OFF,12003231412237281785)
print log_tax_free[0].id_log

## ricerca resi su bms ##
import posws.bin.poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
import json
from config.ws_client import ws_config
from posws.bin.poswsbe import pos_store_db_access as call
pard['ws_cod_negozio'] = '0901173'
pard['ws_pk_consumer'] = '4278911'
pard['ws_sku'] = '21311780040567'
pard['ws_data_documento_da'] = '20201229'
pard['ws_data_documento_a'] = '20201229'
call.get_vendite_rendibili(pard)
## non può chiamare crm quindi si spacca quando cerca di chiamarlo ##
## sui bms che chiamano crm ##
## usare un mockup come alternativa o trovare soluzione ##

import posws.bin.poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
import json
from config.ws_client import ws_config
from posws.bin.poswsbe import pos_store_db_access as call
pard['ws_cod_negozio'] = '0100011'
pard['ws_pk_consumer'] = '3852110'
pard['ws_sku'] = '11310782060034'
pard['ws_data_documento_da'] = '20201201'
pard['ws_data_documento_a'] = '20201229'
call.get_vendite_rendibili(pard)

import posws.bin.poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
import json
from config.ws_client import ws_config
from posws.bin.poswsbe import pos_store_db_access as call
pard['ws_cod_negozio'] = '0901042'
pard['ws_pk_consumer'] = '5171393'
pard['ws_data_documento_da'] = '20210101'
pard['ws_data_documento_a'] = '20210110'
call.get_vendite_rendibili(pard)

## ##
import posws.bin.poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
import json
from config.ws_client import ws_config
from posws.bin.poswsbe import pos_store_db_access as call
call.insert_reso_b2c(pard, ...)

## per provare un singolo metodo con collegamento a db attivo sul bms con docker ##
import posws.bin.poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
import json
from posws.bin.poswsbe.pos_store_db_access import get_vendite_rendibili as access
pard[ws_cod_negozio] = "0501001"
pard[ws_data_documento_da] = "20180515"
pard[ws_data_documento_a] = "20180515"
access(pard)

## se non va la connessione al db per i bms in cloud bisgna andare in main/bin/configmaps e main/bin/secret ##
e cambiare mysql.bmshk e mysql.web e cambiare host con "cloud-sql-proxy"
e password con "drejPeuvMic8" (es, per bmshk)
e in compose_up commentare le righe che spianano i dati di connessione

## CRM - ANONIMIZZAZIONE ##
from initiative.locator import locator as loc
serv = loc.get_service("CRMBackOffice")
min_timestamp = None
max_timestamp = None
negozi_l = ['0100501']
result = serv.get_consumer_anonimizzate(negozi_l=negozi_l, min_timestamp=min_timestamp, max_timestamp=max_timestamp, from_export=True)

## BMS - SCRIVERE SULLA POS_FATTURE_HU_XML ##
from posws.bin.poswsbe.invoice_storage_xml.locator import locator as loc
service = loc.get_service(InvoiceStorageXmlService)
service.store_invoice_xml({})

## BMS - ##
import posws.bin.poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={}) # per avere il pard con le info di base del db e connessione attiva

in pos_utils nel caso eliminare il terzo parametro retail perché chiama il db non locale
così facendo chiama il db dev di benelux collegato al mio docker
per i job impostare main_project_home = /source/log/%s....

## BMS - pos_generate_negozi ##
from boss.delega_negozi.locator import locator as loc
serv = loc.get_service("DelegaNegoziPOSWS")
serv.generate_negozio({'cod_installazione': '9002401006', 'lingua': 'SPAN', 'tipologia_istanza': 'POSWEB_OFFLINE', 'nazione': 'ES', 'cod_negozi': ['2401006'], 'casse': '1'})