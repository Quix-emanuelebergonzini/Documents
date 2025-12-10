## LA NASCITA DEL PARD ##
import config_store
pard = config_store.application_parameters(use_ws=True)

se devo aggiungere delle costanti dai file legacy non si dovrebbe importare config.env
va replicata la costante in un altro file il config_store.py
e poi richiamata da pard in questo modo --> pard[POS_CONFIG][MEDIA_PHOTO_URL]

**## OCCHIO AI TESSUTI BISOGNA RICORDARSI CHE OLTRE AI MOVIMENTI CAPI CI SONO ANCHE I TESSUTI ##**

########################################## STAMPE SU POSWEB #############################################################################
* stampe_utils ha il metodo vendita in cui passa nel momento di una vendita prima della stampa dei pdf/scontrini
* stampe_factory è il punto comune
* se le stampe pdf non vengono generate è possibile per via di una eccezione che compare ma il pdf viene generato in /rnd/pos/mmfg/posweb/var/spool/pdf/
    quindi controllare le righe, nei metodi di stampa in stampa_scontrini_pdf.py
    ~~~
    pdf.render_pdf()
    pdf.print_ticket(pard[POS_CONFIG].get(CASH_REGISTER_NAME, default_printer_name)...
    ~~~

* per avviare la console di python con struttura per posweb usare:
~~~
python site/bin/console.py
from backend import resi
~~~
es
~~~~
from backend.conteggio_banconote.locator import locator as loc
service = loc.get_service(ConteggioBanconote)
import logging
from config.env import LOGGER_BASE
from mmfg.service import Service
import json
import common_utils
import common.utils
service.prepara_json_conteggiobanconote({"cod_negozio": "0100051"})
~~~~

oppure VEDI: USE_MYSQL_IN_POSWEB.py

* per stampare il pard andare su chiudi_vendita e posizionarsi prima della chiusura del metodo,
    dentro il try except e stampare con pard[LOGGER].debug(pard)

* cerca barcode_tipo_vendita dentro stampe_custom per vedere dove stampa il barcode
    UNA STAMPA è PER SCONTRINO E PDF!!!! QUINDI ALLINERARE SEMPRE LE STAMPE!!!
* 
##############################################################################################################################
########################################## POSWEB se il catalogo è vuoto... #################################################
    * controllare sul bms la chiave AVAILABLE_BRANDS in pos_config_store
    * controllare sul bms la chiave BRANDS_CATALOGO in pos_config_store
    * controllare la tabella pos_regole_catalogo se per brand/annostag è attivo


!!!!!!!
Le traduzioni con cluster pos_cash_register
vanno sempre messe anche in italiano
!!!!!!!


eseguire sul negozio questa query in main.catalogo:

SELECT DISTINCT c.sku
FROM catalogo c
INNER JOIN prezzi p ON p.modello = c.modello AND p.pezzo = c.pezzo
AND p.tipo_prezzo = "V" AND p.data_inizio_validita <= "20190626"
WHERE 1=1 AND c.sku_padre = "" AND c.validita_variante IN ("V", "B")
AND c.versione_modello = "V" AND c.data_consegna IS NOT NULL
AND c.data_consegna <= 20190626 AND
((c.cod_marchio = MR AND c.annostag = 20191) OR (c.cod_marchio = MR AND c.annostag = 20192))
GROUP BY c.modello_principale, c.variante;
--> deve tornare valorizzata (cambiare marchio e annostag nel caso e anche data_inizio_validita)


questa query nasce da (da lanciare sulla macchina in cloud con il negozio installato così da avere
marchio, data, annostag valorizzati bene):
cd /rnd/pos/mmfg/posweb
./bin/run_python.sh bin/catalog_b2e_generator.py -f
è dentro una create_table


##############################################################################################################################
####################################################   FRANCIA   #############################################################
 * Cè una gestione particolare per via delle certificazioni dal 2018
 * Cè sotto il menù ConsulatazioneDB una sezione per mostrare le tabelle DB (alcune)
 * Per la gestione dei bottoni da aggiungere alle colonne vedasi consultazione-db.js con esempio anche di caricamento ajax e non
    e vedasi il modulo backend/frontend di consultazione_db (chiamata a servizi etc etc) e anche esempio di download_handler e ajax_handler
##############################################################################################################################
 * per tutti i servizi esterni guardare sempre se cè un simulate = False (nel service di backend!) nella classe perché si possa lavorarvi
    - coupon
    - barcode
    - resi_b2c (simulo un reso non una vendita)
########################################### SE SONO OFFLINE ################################################################
stop a tutti i demoni
tolgo i records con i proxy (tutti tranne CONN_STATUS e MACHINE_STATUS) dentro al global_status
e metto a 1 la CONN_STATUS
riavvio i demoni senza il keepalive
########################################### NUOVA VOCE DI MENU ################################################################
attivare nuovo modulo e programma
es, http://localhost:8000/?module=export_xml&program=export_xml

andare nel database main.custom_values e cercare per negozio e name = PROGRAMS_CASH_CASSIERA_ON e poi
per name = PROGRAMS_CASH_CASSIERA_OFF il record e modificare value così:

[(),(),...,(export_xml, \*)] --> solo * niente \
##############################################################################################################################
### INSERIMENTO NUOVA CASSIERA ###
INSERT INTO commesse (cod_negozio, commessa, descrizione, descrizione_kanji, descrizione_kana, data_nascita, data_assunzione, data_licenziamento, matricola_paghe, orario_gg_1, orario_gg_2, orario_gg_3, orario_gg_4, orario_gg_5, orario_gg_6, orario_gg_7, data_modifica) VALUES (0100051, U124488, TEST UNGHERIA, TEST UNGHERIA, TEST UNGHERIA, 1988-12-27, 2019-06-21, , , , , , , , , , 1561106378478);
##################################
########################################### POSWEB CONNESSO A OM_DEV ########################################################
-- SELECT @cod_negozio = 0100083;
-- mettere apici al cod_negozio

REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,connection_timeout,60,2019-06-05 16:00:00);
REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,enable_compression,0,2019-06-05 16:00:00);
REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,http_proxy,,20161101013-05-18 17:55:50);
REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,password,a166c0d011def85f2e,2019-06-05 16:00:00);
REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,req_content_type,application/json,2019-06-05 16:00:00);
REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,req_type,PASSWORD,2019-06-05 16:00:00);
REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,url,https://localhost:4443/,2019-06-05 16:00:00);
REPLACE INTO connection_parameter VALUES(@cod_negozio,ws_om,username,ws_om_pos,2019-06-05 16:00:00);
##############################################################################################################################
###################################################### CAMBIO CONTATTORE VENDITE #############################################
main --> store_config --> key = TRANSACTION_COUNTER
############################################ CAPIRE SE NEGOZIO TEST CHIAMA OM #################################################
aprire postman
effettuare il login sul negozio
http://dos-mr-be.posweb.mmfg.it/api/v1/sessions?username=assistenza&password=mmfg&cod_cassa=01
poi chiamare questo servizio
http://dos-mr-be.posweb.mmfg.it/api/v1/stock?filter[sku]=59410491060036&filter[details]=1
##############################################################################################################################
############################################ CAPIRE SE NEGOZIO TEST CHIAMA OM #################################################
fattura: cercare per CF: PZZDNT37T06D590G
<!-- #		ucap: u20855,
#		ucod_fiscale: uPZZDNT37T06D590G,
#		ucognome: uPIZZATI DANTE,
#		uid_soggetto: 12939,
#		uindirizzo: uVIA XXV APRILE,47,
#		ulocalita: uLESMO,
#		unome: u,
#		unumero_civico: u,
#		up_iva: u00485290969,
#		up_iva_cee: uIT00485290969,
#		uprovincia: uMI,
#		uragione_sociale_1: uPIZZATI DANTE,
#		uragione_sociale_2: u,
#		usoggetto_fisico: False,
#		ustato: uIT -->


################################################## CALL SEDE ##################################################################
chiamare la sede. vedi chiudi_vendita (invio xml a sede, con scrittura sulla mmfg_queue)
in questo metodo io da slave chiamo il master che chiamerà la sede
~~~
def save_config_store(pard, valori, invia_sede=False):
    ws = ws_utils.WebService(pard, pard[POS_CONFIG][WS_CONFIG_MASTER])
    if invia_sede:
        ws.send_request({
            program: ws_global_mmfg_put_data,
            ws_format: json,
            ws_type: signature,
            ws_content: json.dumps(valori),
            ws_remote_sid: pard[sid],
        })
        ##questa scrive sulla tabella mmfg_queue##
	ws = ws_utils.WebService(pard, pard[POS_CONFIG][WS_CONFIG_MASTER])
	return ws.send_request({
				program: ws_global_save_config_store,
				ws_valori: json.dumps(valori),
	})
    ##questo salva il valore sulla tabella del negozio store_config##
~~~

##################################################### pard[POS_CONFIG]  ######################################################################
si riempie con store_config e cash_config
sovrascrive i valori la config.py tranne
    - MMFG_WS_HOST
    - MMFG_WS_PROXY
si sovrascrive alla fine, come ultimo, dalla temp.global_status

nella ws_utils ci sono le chiamate a basso livello alla sede.

##################################################### RICERCA CONSUMATRICI DI NEGOZIO ##########################################################

solo HK per la ricerca delle consumatrici, POSWEB, chiama il BMS e poi il CRM (search_BMS_only) passando per la chiamata al FRONT-END
il resto del mondo chiama POSWEB --> CRM

quando trovo una consumatrice, mi arrivano i consensi (i consensi non hanno bisogno di cod_negozio) per BRAND. Quindi se la mia consumatrice
ha già firmato e dato i consensi (sono due cose differenti) in un negozio questa non deve rifirmare e deve vedere i consensi come nellaltro negozio.

quando importo una consumatrice (locale = 2 è di SEDE) diventa di negozio (locale = 0) solo dopo la prima vendita, quindi è normale
non vedere il bottone modify se locale = 2

################################### VARIE ##############################################
su HK posweb non cè...

consumers = ws.send_request({
    program: ws_ricerca_consumatrici,  # nome fz gianluca
    ws_data: dati,
})
questa è un esempio di chiamata a poswsbe. Quale BMS? ad esempio HK di Test quindi i dati arrivano da lì
per vedere il codice di ws_ricerca_consumatrici bisogna guardare il progetto poswsbe

metodo old per abilitare set prezzi V e S:
    andare sulla tabella prezzi
    individuare un modello
    eseguire una insert con modello selezionato e data recente ma nel passato di 2/3gg e un prezzo di vendita ribassato
    rispetto al più recente
    - SELECT * FROM prezzi LIMIT 10;
    - INSERT INTO "main"."prezzi" ("cod_negozio", "modello", "pezzo", "tipo_prezzo", "data_inizio_validita", "data_fine_validita", "prezzo", "divisa", "perc", "tot", "annostag", "data_modifica")
    VALUES (0100514, 1221515806, 0, S, 20190408, , 42, EUR, 0, 0, 20191, 2018-09-28 00:00:00);
    dopo sempre con il modello identificare sulla tabella catalogo gli sku associati
    - SELECT sku FROM catalogo where modello = ;

per la stampa deve essere a 1 la chiave CASH_REGISTER_ENABLED sul config oppure se non cè nel config
nella tabella store_config
per la stampa sul kube deve essere KUBE la chiave CASH_REGISTER_TYPE sul config oppure sul store_config
per la stampa sul pdf deve essere KUBEUSBPDF la chiave CASH_REGISTER_TYPE sul config oppure sul store_config

altre stampe pdf con formati carta più grandi KUBEUSBJP - JAPAN
                                              EPSONUSBPDF - USA
                                              KUBEUSBPDFK3

SIMULAZIONE GIFTCARD:
per simulare le giftcard inserite in fase di vendita bisogna mettere a True la variabile simulate = True
dentro a /rnd/pos/mmfg/posweb/site/bin/backend/giftcard/service.py

non so se è prod o test...
INSERT INTO `pos_connection_parameter` (`codice_proprietario`, `cod_negozio`, `key_group`, `key_name`, `key_value`, `descrizione`, `data_modifica`)
VALUES
	('FRH', '0189085', 'ws_amilon', 'client_id', 'gcmwsuserinternalapi', '', '2021-09-02 16:58:44'),
	('FRH', '0189085', 'ws_amilon', 'client_secret', 'cb8bf8ac1c', '', '2021-09-02 16:58:44'),
	('FRH', '0189085', 'ws_amilon', 'http_proxy', '', '', '2020-01-03 16:52:07'),
	('FRH', '0189085', 'ws_amilon', 'password', 'Marfrhpompei2020', '', '2020-01-03 16:52:07'),
	('FRH', '0189085', 'ws_amilon', 'req_content_type', 'text/json', '', '2021-09-02 16:58:45'),
	('FRH', '0189085', 'ws_amilon', 'soap_debug', '1', '', '2020-01-03 16:52:07'),
	('FRH', '0189085', 'ws_amilon', 'soap_version', '1.2', '', '2020-01-03 16:52:07'),
	('FRH', '0189085', 'ws_amilon', 'url', 'https://gcmstg-web.amilon.eu/GCMWebApi', '', '2021-09-02 16:58:44'),
	('FRH', '0189085', 'ws_amilon', 'url_auth', 'https://b2bstg-sso.amilon.eu', '', '2021-09-02 16:58:44'),
	('FRH', '0189085', 'ws_amilon', 'username', 'Pompei073', '', '2020-01-03 16:52:07');

da prod degli usa febbraio 2024...
INSERT INTO `pos_connection_parameter` (`codice_proprietario`, `cod_negozio`, `key_group`, `key_name`, `descrizione`, `data_modifica`, `key_value`)
VALUES
	('USEIT', '0201280', 'ws_amilon', 'client_id', '', '2023-10-18 08:39:19', 'gcmwsuserinternalapi'),
	('USEIT', '0201280', 'ws_amilon', 'client_secret', '', '2023-10-18 08:39:19', 'fe43f5a06b'),
	('USEIT', '0201280', 'ws_amilon', 'http_proxy', '', '2023-10-18 08:39:19', ''),
	('USEIT', '0201280', 'ws_amilon', 'password', '', '2023-10-18 08:39:19', 'GC1280POPUPCA1!'),
	('USEIT', '0201280', 'ws_amilon', 'req_content_type', '', '2023-10-18 08:39:19', 'text/json'),
	('USEIT', '0201280', 'ws_amilon', 'soap_debug', '', '2023-10-18 08:39:19', '1'),
	('USEIT', '0201280', 'ws_amilon', 'soap_version', '', '2023-10-18 08:39:19', '1.2'),
	('USEIT', '0201280', 'ws_amilon', 'url', '', '2023-10-18 08:39:19', 'https://giftcard.amilon.eu/GCMWebApi'),
	('USEIT', '0201280', 'ws_amilon', 'url_auth', '', '2023-10-18 08:39:19', 'https://b2bsales-sso.amilon.eu'),
	('USEIT', '0201280', 'ws_amilon', 'username', '', '2023-10-18 08:39:19', 'POPUPCA11280');

sugli usa (credo) ci sono anche gli store_credits e ci vuole la connessione ws_amilon_store_credits

da prod degli usa febbraio 2024...
INSERT INTO `pos_connection_parameter` (`codice_proprietario`, `cod_negozio`, `key_group`, `key_name`, `descrizione`, `data_modifica`, `key_value`)
VALUES
	('USEIT', '0201008', 'ws_amilon_store_credit', 'client_id', '', '2021-09-17 13:25:10', 'gcmwsuserinternalapi'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'client_secret', '', '2021-10-20 16:09:29', 'fe43f5a06b'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'http_proxy', '', '2020-08-13 13:17:47', ''),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'password', '', '2020-08-13 13:17:47', 'Toronto1008!20'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'req_content_type', '', '2021-10-20 11:53:19', 'text/json'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'soap_debug', '', '2020-08-13 13:17:47', '1'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'soap_version', '', '2020-08-13 13:17:47', '1.2'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'url', '', '2021-10-20 11:53:18', 'https://giftcard.amilon.eu/GCMWebApi'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'url_auth', '', '2021-10-20 11:53:16', 'https://b2bsales-sso.amilon.eu'),
	('USEIT', '0201008', 'ws_amilon_store_credit', 'username', '', '2020-08-13 13:17:47', 'toronto1008');

MA TEST amilon
INSERT INTO `pos_connection_parameter` (`codice_proprietario`, `cod_negozio`, `key_group`, `key_name`, `key_value`, `descrizione`, `data_modifica`)
VALUES
	('MA', '0100400', 'ws_amilon', 'client_id', 'gcmwsuserinternalapi', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'client_secret', 'cb8bf8ac1c', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'http_proxy', '', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'password', 'marella404', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'req_content_type', 'text/xml', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'soap_debug', '1', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'soap_version', '1.2', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'url', 'https://gcmstg-web.amilon.eu/GCMWebApi', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'url_auth', 'https://b2bstg-sso.amilon.eu', '', current_timestamp),
	('MA', '0100400', 'ws_amilon', 'username', 'Milano404', '', current_timestamp);

----
dentro un qualsiasi BMS cè il modulo posws (poswsbe)

la logica vuole che ci sia uno script chiamato pos_generazione_negozio che crea la configurazione
del negozio partendo da valori di default per negozio e per ogni cassa del negozio

(db) pos_store_config_default
(db) pos_store_cash_default

per ogni cassa vengono raddoppiati i valori nella tabella (db) pos_store_cash
i valori di pos_store_config_default vanno dentro a pos_store_config

dopo la generazione si va a leggere il valore della chiave store_sign e lo si butta dentro a brands_catalogo
tranne per MM che deve avere la sua configurazione di default
attenzione. anche i negozi outlet devono avere la sua config di default che non è pari al brand.
per sapere se è un negozio outlet leggo la chiave store_channel e se inizia con O è un outlet

----------

tabella catalogo su sede e negozio
su sede modello_retail corrisponde a modello su negozio
es, 1131093106 di 10 cifre

un ND si guarda catalogo_prezzi
per i posweblite pos_prezzi_negozi_<annostag> e per fare il join
si guarda la colonna modello su catalgoo e modello sulla prezzi
es, 11310931 di 8 cifre