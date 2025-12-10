associazione pk_consumer (importato sul negozio tramite ricerca di gruppo) con il negozio su CRM

import datetime
from consumer.locator import locator as loc
serv = loc.get_service("Consumer")
cod_negozio = '0100711'
pk_consumer = int('40135')
consumer = {'pk_consumer': pk_consumer, 'nazione_iso': 'IT'}
data = { 'consumer': consumer, 'linked_id': False, 'ext_name': 'pos',   'cod_negozio': cod_negozio, 'pk_consumer': pk_consumer, 'non_aggiornare_risorse_collegate': True}
ext_base = { "ext_id": "", "ext_name": cod_negozio, "timestamp_modifica": datetime.datetime.now(), "user_modifica": cod_negozio, "data": {} }
serv.make_full_consumer_poswsbe(pk_consumer, data, ext_base, cod_negozio=cod_negozio, clean_linked=False)


import datetime
from consumer.locator import locator as loc
serv = loc.get_service("Consumer")
cod_negozio = '0100520'
pk_consumer = None
consumer = {'pk_consumer': pk_consumer, 'nazione_iso': 'IT', 'nome': "io sono", "cognome": "colui che sono no", "data_nascita": "1988-12-27"}
data = { 'consumer': consumer, 'linked_id': False, 'ext_name': 'pos',   'cod_negozio': cod_negozio, 'pk_consumer': pk_consumer, 'non_aggiornare_risorse_collegate': True}
ext_base = { "ext_id": "", "ext_name": cod_negozio, "timestamp_modifica": datetime.datetime.now(), "user_modifica": cod_negozio, "data": {} }
serv.make_full_consumer_poswsbe(pk_consumer, data, ext_base, cod_negozio=cod_negozio, clean_linked=False)