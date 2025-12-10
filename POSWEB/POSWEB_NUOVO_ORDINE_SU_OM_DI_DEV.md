Avviare POSWEB per inviare un ordine su OM di DEV
poi da OM (docker) leggerlo da DEV

1. avvio il mio pos per scaricare un db di un negozio ITALIANO
2. eseguo su posweb dentro main.db

select id,cod_negozio,data_format,data_type,data_invio from mmfg_queue;
*così lordine è stato inviato al BMS di riferimento*
select * from connection_parameter;
*così lordine è stato inviato a OM*

~~~
REPLACE INTO connection_parameter VALUES(1401359,ws_om,connection_timeout,60,2016-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(1401359,ws_om,enable_compression,0,2016-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(1401359,ws_om,http_proxy,,20161101013-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(1401359,ws_om,password,a166c0d011def85f2e,2016-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(1401359,ws_om,req_content_type,application/json,2016-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(1401359,ws_om,req_type,PASSWORD,2016-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(1401359,ws_om,url,https://localhost:4443/,2016-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(1401359,ws_om,username,ws_om_pos,2016-05-18 17:55:50);
~~~

3. apro un terminale per FARE UNA VENDITA B2E (sale_b2e se la faccio da negozio è solo sale)
~~~
cd /rnd/pos/mmfg/posweb
python bin/CeC.py -l 62460289060014 -a 5072202
~~~
*poi ci sono delle domande, invio vale la prima risposta suggerita --> contesto b2e*

NOTA BENE:
62460289060014 - sku
5072202 - consumatrici la cui informativa sulla privacy è accettata (vedi tabella consumer_consenso_privacy in main.db)
-l è lista degli sku suddivisi da , senza spazi
-a risposta fissa (non per forza un pk_consumer)
-u mettere cashier in caso di negozio estero

>> OCCHIO IN QUALE BRANCH SONO POSIZIONATO SU POSWEB (mettersi sulla master)

>> PRENDERE UNO SKU DA UN MODELLO DELLA TABELLA PREZZI!!!

esempio di risposta:
Capi in store:
Capi out store: 1
Spedizione (1 consumer, 0 store): 0
Stato (1 chiusa, 0 sospesa):
Pagamento con carta (1 carta, 0 contanti):
Chiusura con scontrino (1 scontrino, 0 fattura):
Login
[]
True
Consumatrice: 5072202 XIN MING
Capo out store (62460289060014)                 159
Totale                                        159.0
==================================================================================================== KEY ====================================================================================================
WyI1MDcyMjAyIiwgIiIsICIxIiwgIjAiLCAiIiwgIiIsICIiXQ==
==================================================================================================== INPUT ====================================================================================================
{
    "data": {
        "attributes": {
            "cod_documento": "SALE_TICKET",
            "codice_movimento": "VENDITA",
            "data_documento": "201965",
            "cod_vettore": "",
            "data_modifica": "2019-06-05 10:12:29",
            "dati_aggiuntivi": "",
            "importo_finale": 159.0,
            "codice_stato": "CLOSED",
            "dati_documenti": "{\"nome_contatore\": \"\", \"flag_stampa_scontrino_cortesia\": 0, \"valore_contatore\": 113, \"numero_scontrino\": \"\", \"flag_no_iva\": 0, \"numero_documento_stampato\": \"R051800113\", \"shipping_destination\": \"STORE\", \"dati_documento\": {\"comune_nascita\": \"\", \"stato_nascita\": \"\", \"nominativo\": \" \", \"nome\": \"\", \"stato\": \"\", \"cognome\": \"\", \"data_nascita\": \"\", \"cod_fiscale\": \"\"}}",
            "id_utente": "cassiera",
            "ora_documento": "101229",
            "data_creazione": "2019-06-05 10:12:29",
            "nota": "",
            "tipo_applicazione_chiusura": "DSMOBILE",
            "sid": "0z8kfltpsm9gtd",
            "divisa": "EUR",
            "importo_pagato": 0,
            "pk_consumer": "5072202",
            "id_postazione_apertura": "01",
            "tipo_applicazione_apertura": "DSMOBILE",
            "numero_documento": 113,
            "pagamenti": [
                {
                    "codice_movimento": "CONTABILITA_PAGAMENTO",
                    "tipo_applicazione": "DSMOBILE",
                    "progressivo_capo": 0,
                    "barcode": "",
                    "data_modifica": "2019-06-05 10:12:29",
                    "data_creazione": "2019-06-05 10:12:29",
                    "id_postazione": "01",
                    "progressivo": 1,
                    "nota": "",
                    "dati_operazione": "{\"payment_date\": \"201965\", \"esito\": \"ESITO_POSITIVO\", \"pos_tran_id\": \"sale-44-3-0-1449153300824\", \"tipo\": \"AUTOMATICO\", \"dati_carta\": {\"online_transaction_id\": \"000412\", \"flag_multicurrency\": \"0\", \"tipo_carta_ingenico\": \"2\", \"scontrino\": \"       MAXIMA SRL            REGGIO EMILIA                                      ACQUISTO                 AMEXCO         DATA 00/00/00  ORA 00:00ESERC.        9624301438ACQ.ID       00000000002N.OP.000412 TML 52211685PAN      375200*****0003EXP                 ****STAN 000366  AUT. 584305I.C. MAG                IMPORTO  EUR        0,00                         C/M SIGNATURE - FIRMA                          ........................                          CARIPARMA E PIACENZA                                     CIM          \", \"response_code\": \"E\", \"terminal_id\": \"12345678\", \"transaction_time\": \"0952\", \"transaction_type\": \"MAG\", \"authorization_number\": \"584305\", \"transaction_date\": \"20151126\", \"esito_transazione\": \"00\", \"id_acquirer\": \"00000000002\", \"stan\": \"000366\", \"codice_compagnia\": 2, \"pan\": \"0000375200*****0003\", \"desc_acquirer\": \"AMEXCO\"}, \"raw_response\": \"123456780E000000375200*****0003MAG58430503300952200000000002000366000412\"}",
                    "cod_negozio": "0100083",
                    "divisa": "EUR",
                    "importo_finale": 159.0,
                    "codice_stato": "CLOSED",
                    "cod_operazione": "CARTA",
                    "importo_iniziale": 159.0
                }
            ],
            "numero_stampa_documento": "",
            "capi": [
                {
                    "codice_movimento": "VENDITA",
                    "data_modifica": "2019-06-05 10:12:29",
                    "iva": 22.0,
                    "ean": "",
                    "id_transazione": 0,
                    "flag_divisa": 0,
                    "sku_splitted": 0,
                    "cod_commessa": "U116299",
                    "tipo_importo": "V",
                    "correzione_importo": 0,
                    "sku_created": 0,
                    "importo_finale": 159,
                    "codice_stato": "CLOSED",
                    "importo_iniziale": 159,
                    "sku": "62460289060014",
                    "nome": "XDOLL",
                    "cod_negozio": "0100083",
                    "classe": "32",
                    "progressivo": 1,
                    "data_creazione": "2019-06-05 10:12:29",
                    "flag_promo": 0,
                    "sconto": 0,
                    "composizione": "7:028PL072VI",
                    "nota": "",
                    "sku_read": "62460289060014",
                    "importo_custom": 159,
                    "custom_data": "{\"stock_type\": \"OUT_STORE\", \"desc_classe\": \"Abito in maglia\", \"desc_taglia\": \"MN\", \"variante\": \"002\", \"annostag\": \"20171\"}",
                    "tipologia_merce": "GARMENTS"
                }
            ],
            "flag_stampa_documento": 0,
            "importo_iniziale": 159.0,
            "id_postazione_chiusura": "01",
            "cod_cassiera": "U116299",
            "cod_negozio": "0100083",
            "cod_cassa": "01"
        },
        "type": "sales"
    }
}
==================================================================================================== OUTPUT ====================================================================================================
{
    "data": {
        "attributes": {
            "cod_documento": "SALE_TICKET",
            "codice_movimento": "VENDITA",
            "data_documento": "20190605",
            "cod_vettore": "",
            "data_modifica": "2019-06-05 09:00:20",
            "dati_aggiuntivi": "",
            "importo_finale": 549.1,
            "codice_stato": "CLOSED",
            "dati_documenti": "{\"nome_contatore\": \"\", \"flag_stampa_scontrino_cortesia\": 0, \"valore_contatore\": 1, \"source_type\": \"B2E\", \"numero_scontrino\": \"0\", \"shipping_address\": {\"province\": \"TS\", \"city\": \"Muggia\", \"contact_number\": \"040/9235089\", \"surname\": \"\", \"name\": \"\", \"reference_name\": \"DT Muggia\", \"zipcode\": \"34015\", \"county\": \"\", \"state\": \"\", \"address\": \"STRADA PROVINCIALE FARNEI, 42/A\", \"country\": \"IT\"}, \"flag_no_iva\": 0, \"numero_documento_stampato\": \"U052000001\", \"shipping_destination\": \"STORE\", \"dati_documento\": {\"stato_nascita\": \"\", \"nome\": \"\", \"cognome\": \"\", \"data_nascita\": \"\", \"comune_nascita\": \"\", \"nominativo\": \" \", \"stato\": \"\", \"cod_fiscale\": \"\"}}",
            "id_utente": "cassiera",
            "ora_documento": "110020",
            "data_creazione": "2019-06-05 09:00:20",
            "nota": "",
            "tipo_applicazione_chiusura": "DSMOBILE",
            "sid": "0z8kfltpsmbohy",
            "divisa": "EUR",
            "importo_pagato": 0.0,
            "pk_consumer": "5381489",
            "id_postazione_apertura": "01",
            "tipo_applicazione_apertura": "DSMOBILE",
            "numero_documento": 1,
            "pagamenti": [
                {
                    "codice_movimento": "CONTABILITA_PAGAMENTO",
                    "tipo_applicazione": "DSMOBILE",
                    "data_modifica": "2019-06-05 09:00:20",
                    "barcode": "",
                    "progressivo": 1,
                    "data_creazione": "2019-06-05 09:00:19",
                    "id_postazione": "01",
                    "nota": "",
                    "id_transazione": 524,
                    "dati_operazione": "{\"payment_date\": \"20190605\", \"esito\": \"ESITO_POSITIVO\", \"raw_response\": \"123456780E000000375200*****0003MAG58430503300952200000000002000366000412\", \"pos_tran_id\": \"sale-44-3-0-1449153300824\", \"tipo\": \"AUTOMATICO\", \"dati_carta\": {\"online_transaction_id\": \"000412\", \"flag_multicurrency\": \"0\", \"tipo_carta_ingenico\": \"2\", \"scontrino\": \"       MAXIMA SRL            REGGIO EMILIA                                      ACQUISTO                 AMEXCO         DATA 00/00/00  ORA 00:00ESERC.        9624301438ACQ.ID       00000000002N.OP.000412 TML 52211685PAN      375200*****0003EXP                 ****STAN 000366  AUT. 584305I.C. MAG                IMPORTO  EUR        0,00                         C/M SIGNATURE - FIRMA                          ........................                          CARIPARMA E PIACENZA                                     CIM          \", \"response_code\": \"E\", \"terminal_id\": \"12345678\", \"transaction_time\": \"0952\", \"transaction_type\": \"MAG\", \"authorization_number\": \"584305\", \"transaction_date\": \"20151126\", \"esito_transazione\": \"00\", \"id_acquirer\": \"00000000002\", \"stan\": \"000366\", \"codice_compagnia\": 2, \"pan\": \"0000375200*****0003\", \"desc_acquirer\": \"AMEXCO\"}}",
                    "progressivo_capo": 0,
                    "divisa": "EUR",
                    "importo_finale": 549.1,
                    "codice_stato": "CLOSED",
                    "cod_negozio": "0100520",
                    "cod_operazione": "CARTA",
                    "importo_iniziale": 549.1,
                    "reso": 0
                }
            ],
            "numero_stampa_documento": "0",
            "capi": [
                {
                    "codice_movimento": "VENDITA",
                    "iva": 22.0,
                    "id_transazione": 524,
                    "data_modifica": "2019-06-05 09:00:20",
                    "cod_commessa": "U105992",
                    "correzione_importo": 0.0,
                    "sku_created": 0,
                    "importo_finale": 549.1,
                    "codice_stato": "CLOSED",
                    "sku": "24660269060014",
                    "flag_tassabile": 0,
                    "nome": "CALTE",
                    "prezzo_listino_vendita": 549.1,
                    "flag_promo": 0,
                    "data_creazione": "2019-06-05 09:00:20",
                    "sconto": 0,
                    "composizione": "T:100AA,F:055VI045CU",
                    "nota": "",
                    "importo_custom": 0.0,
                    "tipologia_merce": "GARMENTS",
                    "ean": "",
                    "flag_divisa": 0,
                    "sku_splitted": 0,
                    "tipo_importo": "V",
                    "importo_iniziale": 549.1,
                    "cod_negozio": "0100520",
                    "classe": "46",
                    "progressivo": 1,
                    "sku_read": "24660269060014",
                    "custom_data": "{\"stock_type\": \"OUT_STORE\", \"desc_classe\": \"Pelliccia\", \"desc_taglia\": \"H\", \"variante\": \"001\", \"annostag\": \"20162\"}",
                    "sconto_listino_vendita": 0.0,
                    "reso": 0
                }
            ],
            "flag_stampa_documento": 0,
            "importo_iniziale": 549.1,
            "id_postazione_chiusura": "01",
            "cod_cassiera": "U105992",
            "cod_negozio": "0100520",
            "id_transazione": 524,
            "cod_cassa": "01"
        },
        "type": "sales",
        "id": "0100520,524"
    }
}
