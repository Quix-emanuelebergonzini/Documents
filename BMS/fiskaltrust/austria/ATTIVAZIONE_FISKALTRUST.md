AUSTRIA (BMSDE)
Inizializzare FISKALTRUST per la comunicazione dei dati al fisco

1) Devono essere richiesti alla sede di Fiskaltrust, l'"Access token" e "CashBoxId" che vanno messi nei secrets
Per i secrets bisogna passare dalle Operations. Quando fatto (c'è la loggata sul kube) bisogna riavviare il deploy da jenkins
Per controllare che sia presente il negozio e i relativi Access token e CashBoxId bisogna collegarsi
in ssh al bmsde (usare i pods) e invocare
>>>> cat guest/poswsfe/bin/config/secrets/wsclient.fiskaltrust
tutto ok se c'è questo output
{
  "params": "{\"0701113\": {
        \"cashboxid\": \"d6955b3e-dc06-4177-90b8-95cda936af9a\",
        \"accesstoken\": \"BOZJm7oFczOIBLvl6qXa9GdXV0weCnM+IXidRDxeg4LsDqVjwGF21SbtWtzA/7CavACc6zQuyxcPlkz/c5ZL0Ao=\"
    }}"
}
"Access token" e "CashBoxId" se corrispondo a quelli forniti da Fiskaltrust siamo relativamente tranquilli
(di solito riportati in issue)

!!! occhio a sostiture il cod_negozio ove serve !!!!

2) Chiamata "INITIAL" (serve abilitazione per posws@filiali-fe-01.mmfg.it):
La chiamata è da eseguire obbligatoriamente in fase di inizializzazione del negozio
e per facilitare l'operazione è stato creato uno script su FE che consente di inviare comandi da riga di comando.
Lo script è alla risorsa:
    – python ~/httpd-chroot/guest/poswsfe/script/fiskaltrust_send_request.py

E per lanciare il comando di "initial" utilizzare la seguente sintassi:
    – python ~/httpd-chroot/script/fiskaltrust_send_request.py -c 01 -n 0701113 -t INITIAL
I parametri dello script sono:
    -c: codice cassa: ad esempio 01
    -n: codice negozio: ad esempio 0701113
    -t: tipo di richiesta da inviare, che sia compreso nel seguente set di richieste: INITIAL, MONTHLY, ANNUAL, ZERO

Oppure lanciare questi comandi:
>>> cd $bmsde
>>> open -a docker
>>> LANDSCAPE=PRODUCTION/TESTING docker/run_job.sh /env/bin/python /source/guest/poswsfe/script/fiskaltrust_send_request.py -c 01 -n 0701113 -t INITIAL

tale chiamata è bloccante quindi riavviarla fin tanto che funziona. (90% secrets errati)

output servizio...esempio risposta positiva....
{
    "fiskaltrust_input": {
        "cbChargeItems": [],
        "cbPayItems": [],
        "cbReceiptMoment": "2022-03-11 14:00:36",
        "cbReceiptReference": "",
        "cbTerminalID": "01",
        "transaction_type": "INITIAL"
    }
}
------------------------------------------------------------
------------------------------------------------------------
Risposta da Fiskaltrust:
{
    "cbReceiptReference": "",
    "cbTerminalID": "01",
    "ftCashBoxID": "d6955b3e-dc06-4177-90b8-95cda936af9a",
    "ftCashBoxIdentification": "fiskaltrust5",
    "ftQueueID": "eeb435e7-072b-4fe6-b83d-60534f645e9e",
    "ftQueueItemID": "64a8face-1ed4-438f-8bb3-e8de19ece83e",
    "ftQueueRow": 1,
    "ftReceiptIdentification": "ft0#1",
    "ftReceiptMoment": "2022-03-11T14:00:37.8793269Z",
    "ftSignatures": [
        {
            "caption": "www.fiskaltrust.at",
            "data": "_R1-AT1_fiskaltrust5_ft0#1_2022-03-11T15:00:37_0,00_0,00_0,00_0,00_0,00_q/bxNvA=_359aff00_P5AumsFgq2E=_2LQKxOBDshUlYY0RBHh88G1ROimoWvuADlR2ecxIoMkhvvCZ119ldjf2zwUfxaVFsSjhvCiE5v1qCUW9EkPelg==",
            "ftSignatureFormat": 3,
            "ftSignatureType": 4707387510509010945
        }
    ],
    "ftState": 4707387510509010944
}
e sulla tabella fiskaltrust_log si può vedere il record corrispondente

4) Inserire un record sulla tabella fiskaltrust_negozi di BMSDE:
SET @negozio = '0701113';
SET @data_inizio = '20220311';
INSERT INTO `fiskaltrust_negozi` (`cod_negozio`, `data_inizio`, `data_fine`, `attivo`, `upd_datetime`) VALUES (@negozio, @data_inizio, '29991231', 1, now());

es:
vedi issue https://jira.mmfg.it/browse/REX-11059



from fiskaltrust.locator import locator
from config.ws_client import ws_config

import sys
sys.path.insert(0, '/source/main/bin')
sys.path.insert(0, '/source/guest')

from fiskaltrust.config_fiskaltrust import REQUEST_CONFIG

from poswsfe.bin.config.ws_client import ws_config

SERVER_CONFIG = {}
neg_config = ws_config['fiskaltrust']['params']

SERVER_CONFIG['fiskaltrust'] = ws_config['fiskaltrust']

SHOPS_CREDENTIALS = {}

for neg, values in neg_config.items():
	SHOPS_CREDENTIALS[neg] = tuple((key, value) for key, value in values.items())

from poswsfe.bin.fiskaltrust.config_fiskaltrust import REQUEST_CONFIG

s = locator.get_service('FiskaltrustWs',
connection_parameter=SERVER_CONFIG,
request_config=REQUEST_CONFIG,
shops_credentials=SHOPS_CREDENTIALS
)

self = s

import json
import time

data_documento_full = time.strftime("%Y-%m-%d %H:%M:%S")

cod_cassa = '01'
transaction_type = 'INITIAL'
dati_richiesta_fiskaltrust = {
	"fiskaltrust_input": {
		"cbPayItems": [],
		"cbChargeItems": [],
		"cbReceiptReference": "",
		"cbReceiptMoment": data_documento_full,
		"cbTerminalID": cod_cassa,
		"transaction_type": transaction_type
	}
}

cod_neg = '0701126'
numero_documento_stampato = '000'
data_documento = '20221129'
id_transazione = '000'
request_type = 'SIGN'
method_params={
	'cod_negozio': cod_neg,
	'cod_cassa': cod_cassa,
	'dati_richiesta_fiskaltrust': json.dumps(dati_richiesta_fiskaltrust),
	'numero_documento': numero_documento_stampato,
	'data_documento': data_documento,
	'id_transazione': id_transazione,
	'request_type': request_type
}

message = json.loads(method_params.get('dati_richiesta_fiskaltrust'))
message_completed = self.edit_fiskaltrust_request(message, method_params["cod_negozio"])

method_name = 'publishDocument'

payload = getattr(self, method_name)(message=message_completed['fiskaltrust_input'], **method_params)

payload


config = {
	'fiskaltrust': {
		'req_type': 'URL',
		'username': '',
		'password': '',
		'url': 'https://signaturcloud-sandbox.fiskaltrust.at/',
		'http_proxy': '',
		'connection_timeout': '60',
		'enable_compression':'0',
		'req_content_type': 'application/json',
		'additional_headers': (
			('accesstoken', "BNht1sdLKfTlVaOUseCF53jKjKTbQqHgq/tneuDCX6cSk2gJWE1Mlav1RR8ki5XvpuXPtlEYHq+rb7mYwrI9OFQ="),
			('cashBoxId', "893dd309-272e-438e-97d0-abff5f427eea")
		)
	}
}

shop_credentials = SHOPS_CREDENTIALS[cod_neg]
config['fiskaltrust']['additional_headers'] = tuple((SafeString(h[0]) if not isinstance(h[0], SafeString) else h[0], h[1]) for h in shop_credentials)
from mmfg.webservice import client
response = client.request('fiskaltrust', message, config=config)
response.get_data()


