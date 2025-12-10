attivo per Austria Germania (e un negozio Ungherese)

posweb

pos.chiudi_vendita
in particolare movim_utils.set_transaction
di cui la chiamata a ws_global_get_movim_hash_fiskaltrust
e poi a ws_publish_document_fiskaltrust

se vendita o storno in stato CHIUSO allora invoco fiskaltrust

c'è un tag dell'xml chiamato austria_fiscal_data che poi lato bms
viene valutato durante il parser


secrets: sono la rappresentazione del negozio quando arriva dal gestore del fisco
come si presenta il negozio al servizio fiscale

bisogna chiedere a Giulia che ci fornisca CashBoxId e AccessToken
poi le Ops di modificare wsclient.fiskaltrust mettendo i nuovi valori
(aprendo un ticket) - si intende il secrets nel kube

Bisogna comunicargli su quale negozio usare (sta nel secrets)
il codice negozio è codificato nella stringa del segrets nel kube

esempio di configmaps per i dati del servizio fiscale
{"url": "https://signaturcloud-sandbox.fiskaltrust.at/json/sign",
"http_proxy": "http://proxy.mmfg.it:8080", "enable_compression": "0",
"req_content_type": "application/json", "req_type": "URL"}

esempio di segrects con i dati del negozio e i due parametri
{"username": "", "password": "",
"params": "{\"0301119\": {\"cashboxid\": \"56bb128c-ed9a-4516-a2ef-6873ee57504a\", \"accesstoken\": \"BPg0hdi7E3vu2eNAGwug984kY73cboWvEuB2PN7L9INtAC90B29BZiAE9/h8unYtbC4eDXOC2ldlWdiCgRgO5Eo=\"}}"}


xml si crea quando si chiude un credito sospeso
il credito sospseo si genera quando la forma di pagamento è CREDITO_SOSPESO (Paper credit notes)
pagamento_sospeso è alla pagina Cash In&Out - Paper credit notes

--------

come studiare un secretes
fare una invocazione di (dentro bmsde)
python guest/poswsfe/script/fiskaltrust_send_request.py -c 01 -n 0301119 -t INITIAL

oppure avviare lo script dentro poswsfe o il mio schrecht test_germania
