## request con tre capi a prezzo pieno e costi di sartoria e una promozione da -550pt ##

from fidelity.locator import locator as loc
from fidelity.controller import FidelityRest
controller = FidelityRest(locator=loc)
request = {
    "raw": "{\"data\": {\"pagamenti\": [{\"importo_finale\": 386.0, \"cod_operazione\": \"CONTANTI\"}], \"contabilita\": [{\"codice_movimento\": \"CONTABILITA_SARTORIA\", \"progressivo_capo\": 1, \"importo_finale\": 7.0, \"progressivo\": 1}, {\"codice_movimento\": \"CONTABILITA_SARTORIA\", \"progressivo_capo\": 1, \"importo_finale\": 12.0, \"progressivo\": 2}, {\"codice_movimento\": \"CONTABILITA_SARTORIA\", \"progressivo_capo\": 3, \"importo_finale\": 10.0, \"progressivo\": 3}, {\"codice_movimento\": \"CONTABILITA_SARTORIA\", \"progressivo_capo\": 0, \"importo_finale\": 10.0, \"progressivo\": 4}, {\"codice_movimento\": \"CONTABILITA_PROMOZIONE\", \"codice\": \"2130022454821\", \"tipo\": \"LOYALTY_CARD_NEW\", \"punti\": \"-550\", \"progressivo\": 5, \"importo_finale\": -25.0}], \"importo\": 386.0, \"id_operazione\": \"1359\", \"data_ora_operazione\": \"2019-04-02 16:40:36\", \"cod_negozio\": \"0100514\", \"divisa\": \"EUR\", \"extra_data\": {\"numero_documento\": \"9\", \"data_documento\": \"20190402\"}, \"operazione\": \"SALE\", \"pk_consumer\": \"9042519\", \"handle_duplicates\": 0, \"capi\": [{\"tipo_prezzo\": \"V\", \"variante\": \"003\", \"taglia\": \"3\", \"importo_finale\": 124.0, \"modello\": \"1011515706\", \"importo_iniziale\": 124.0, \"sku\": \"10115157060033\", \"nome\": \"7WALLY\", \"classe\": \"01\", \"progressivo\": 1, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"V\", \"variante\": \"003\", \"taglia\": \"3\", \"importo_finale\": 124.0, \"modello\": \"1011515706\", \"importo_iniziale\": 124.0, \"sku\": \"10115157060033\", \"nome\": \"7WALLY\", \"classe\": \"01\", \"progressivo\": 2, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"V\", \"variante\": \"003\", \"taglia\": \"3\", \"importo_finale\": 124.0, \"modello\": \"1011515706\", \"importo_iniziale\": 124.0, \"sku\": \"10115157060033\", \"nome\": \"7WALLY\", \"classe\": \"01\", \"progressivo\": 3, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}]}}",
    "REQUEST_METHOD": "PATCH",
    "PATH_INFO": "/v1/pos/fidelity/update"
}
controller._prepare_before_request(request,{})
controller.update(request,{})

## request con tre capi di cui due sono scontati e senza altri costi sartoria o promozioni ##

from fidelity.locator import locator as loc
from fidelity.controller import FidelityRest
controller = FidelityRest(locator=loc)
request = {
    "raw": "{\"data\": {\"pagamenti\": [{\"importo_finale\": 166.0, \"cod_operazione\": \"CONTANTI\"}], \"contabilita\": [], \"importo\": 166.0, \"id_operazione\": \"1364\", \"data_ora_operazione\": \"2019-04-03 12:13:13\", \"cod_negozio\": \"0100514\", \"divisa\": \"EUR\", \"extra_data\": {\"numero_documento\": \"10\", \"data_documento\": \"20190403\"}, \"operazione\": \"SALE\", \"pk_consumer\": \"9042519\", \"handle_duplicates\": 0, \"capi\": [{\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"2\", \"importo_finale\": 39.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060012\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 1, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"4\", \"importo_finale\": 39.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060014\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 2, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"V\", \"variante\": \"001\", \"taglia\": \"5\", \"importo_finale\": 88.0, \"modello\": \"1021035003\", \"importo_iniziale\": 88.0, \"sku\": \"10210350030015\", \"nome\": \"AGORA\", \"classe\": \"02\", \"progressivo\": 3, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}]}}",
    "REQUEST_METHOD": "PATCH",
    "PATH_INFO": "/v1/pos/fidelity/update"
}
controller._prepare_before_request(request,{})
controller.update(request,{})


## request con 4 capi di cui due scontati e due pieni con uno sconto del 10% e un abbuono di 23 euro. no sartoria o promozioni ##

from fidelity.locator import locator as loc
from fidelity.controller import FidelityRest
controller = FidelityRest(locator=loc)
request = {"raw": "{\"data\": {\"pagamenti\": [{\"importo_finale\": 180.0, \"cod_operazione\": \"CONTANTI\"}], \"contabilita\": [{\"codice_movimento\": \"CONTABILITA_SCONTO\", \"importo_finale\": -51.0, \"progressivo\": 2}, {\"codice_movimento\": \"CONTABILITA_ABBUONO\", \"importo_finale\": -23.0, \"progressivo\": 3}], \"importo\": 180.0, \"id_operazione\": \"1363\", \"data_ora_operazione\": \"2019-04-03 13:55:48\", \"cod_negozio\": \"0100514\", \"divisa\": \"EUR\", \"extra_data\": {\"numero_documento\": \"11\", \"data_documento\": \"20190403\"}, \"operazione\": \"SALE\", \"pk_consumer\": \"9042519\", \"handle_duplicates\": 0, \"capi\": [{\"tipo_prezzo\": \"V\", \"variante\": \"001\", \"taglia\": \"5\", \"importo_finale\": 88.0, \"modello\": \"1021035003\", \"importo_iniziale\": 88.0, \"sku\": \"10210350030015\", \"nome\": \"AGORA\", \"classe\": \"02\", \"progressivo\": 1, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"V\", \"variante\": \"001\", \"taglia\": \"1\", \"importo_finale\": 88.0, \"modello\": \"1021035003\", \"importo_iniziale\": 88.0, \"sku\": \"10210350030011\", \"nome\": \"AGORA\", \"classe\": \"02\", \"progressivo\": 2, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"2\", \"importo_finale\": 39.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060012\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 3, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"4\", \"importo_finale\": 39.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060014\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 4, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}]}}", "REQUEST_METHOD": "PATCH", "PATH_INFO": "/v1/pos/fidelity/update"}
controller._prepare_before_request(request,{})
controller.update(request,{})


## request con 3 con due capi a sconto e uno pieno con pagamento contanti e giftcard. no sartoria o promozioni ##

from fidelity.locator import locator as loc
from fidelity.controller import FidelityRest
controller = FidelityRest(locator=loc)
request = {"raw": "{\"data\": {\"pagamenti\": [{\"importo_finale\": 154.0, \"cod_operazione\": \"GIFT_CARD_CORPORATE\"}, {\"importo_finale\": 100.0, \"cod_operazione\": \"CONTANTI\"}], \"contabilita\": [], \"importo\": 254.0, \"id_operazione\": \"1365\", \"data_ora_operazione\": \"2019-04-03 15:34:46\", \"cod_negozio\": \"0100514\", \"divisa\": \"EUR\", \"extra_data\": {\"numero_documento\": \"13\", \"data_documento\": \"20190403\"}, \"operazione\": \"SALE\", \"pk_consumer\": \"9042519\", \"handle_duplicates\": 0, \"capi\": [{\"tipo_prezzo\": \"V\", \"variante\": \"001\", \"taglia\": \"4\", \"importo_finale\": 88.0, \"modello\": \"1021035003\", \"importo_iniziale\": 88.0, \"sku\": \"10210350030014\", \"nome\": \"AGORA\", \"classe\": \"02\", \"progressivo\": 1, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"V\", \"variante\": \"001\", \"taglia\": \"4\", \"importo_finale\": 88.0, \"modello\": \"1021035003\", \"importo_iniziale\": 88.0, \"sku\": \"10210350030014\", \"nome\": \"AGORA\", \"classe\": \"02\", \"progressivo\": 2, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"3\", \"importo_finale\": 39.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060013\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 3, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"3\", \"importo_finale\": 39.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060013\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 4, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}]}}", "REQUEST_METHOD": "PATCH", "PATH_INFO": "/v1/pos/fidelity/update"}
controller._prepare_before_request(request,{})
controller.update(request,{})


## request con 2 capi a prezzo pieno. senza costi aggiuntivi ##

from fidelity.locator import locator as loc
from fidelity.controller import FidelityRest
controller = FidelityRest(locator=loc)
request = {"raw": "{\"data\": {\"pagamenti\": [{\"importo_finale\": 176.0, \"cod_operazione\": \"CONTANTI\"}], \"contabilita\": [], \"importo\": 176.0, \"id_operazione\": \"1367\", \"data_ora_operazione\": \"2019-04-03 15:56:51\", \"cod_negozio\": \"0100514\", \"divisa\": \"EUR\", \"extra_data\": {\"numero_documento\": \"14\", \"data_documento\": \"20190403\"}, \"operazione\": \"SALE\", \"pk_consumer\": \"9042519\", \"handle_duplicates\": 0, \"capi\": [{\"tipo_prezzo\": \"V\", \"variante\": \"001\", \"taglia\": \"4\", \"importo_finale\": 88.0, \"modello\": \"1021035003\", \"importo_iniziale\": 88.0, \"sku\": \"10210350030014\", \"nome\": \"AGORA\", \"classe\": \"02\", \"progressivo\": 1, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"V\", \"variante\": \"001\", \"taglia\": \"4\", \"importo_finale\": 88.0, \"modello\": \"1021035003\", \"importo_iniziale\": 88.0, \"sku\": \"10210350030014\", \"nome\": \"AGORA\", \"classe\": \"02\", \"progressivo\": 2, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}]}}", "REQUEST_METHOD": "PATCH", "PATH_INFO": "/v1/pos/fidelity/update"}
controller._prepare_before_request(request,{})
controller.update(request,{})

## request con 2 capi scontati di cui uno ha una sartoria da 7 euro, laltro ha uno sconto personale di 10%. solo contatnti ##

from fidelity.locator import locator as loc
from fidelity.controller import FidelityRest
controller = FidelityRest(locator=loc)
request = {"raw": "{\"data\": {\"pagamenti\": [{\"importo_finale\": 81.0, \"cod_operazione\": \"CONTANTI\"}], \"contabilita\": [{\"codice_movimento\": \"CONTABILITA_SARTORIA\", \"progressivo_capo\": 1, \"importo_finale\": 7.0, \"progressivo\": 1}], \"importo\": 81.0, \"id_operazione\": \"1367\", \"data_ora_operazione\": \"2019-04-03 16:57:13\", \"cod_negozio\": \"0100514\", \"divisa\": \"EUR\", \"extra_data\": {\"numero_documento\": \"15\", \"data_documento\": \"20190403\"}, \"operazione\": \"SALE\", \"pk_consumer\": \"9042519\", \"handle_duplicates\": 0, \"capi\": [{\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"3\", \"importo_finale\": 39.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060013\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 1, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}, {\"tipo_prezzo\": \"S\", \"variante\": \"001\", \"taglia\": \"3\", \"importo_finale\": 35.0, \"modello\": \"1021015406\", \"importo_iniziale\": 39.0, \"sku\": \"10210154060013\", \"nome\": \"ELLADE\", \"classe\": \"02\", \"progressivo\": 2, \"annostag\": \"20151\", \"tipologia_merce\": \"GARMENTS\"}]}}", "REQUEST_METHOD": "PATCH", "PATH_INFO": "/v1/pos/fidelity/update"}
controller._prepare_before_request(request,{})
controller.update(request,{})

from fidelity.locator import locator as loc
serv = loc.get_service("Fidelity")
fidelity_example = serv.get_fidelity(LOYALTY_CARD_NEW,2130022454982)
fidelity_history_example = serv.get_fidelity_history(LOYALTY_CARD_NEW,2130022454982, cod_negozio=0133007)
serv.popola_spool([fidelity_example,],[fidelity_history_example,])
