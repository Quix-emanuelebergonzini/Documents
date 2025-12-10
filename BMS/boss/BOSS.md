############ STOREBACKOFFICE (BOSS) ##############

https://localhost:4443/?module=boss.order.action&program=search_order&sid=awlb1878mq5kie#
una url così fatta mi dice:

vai sulle directory da boss >> order >> action.py
cerca la variabile search_order che sarà = un oggetto controller.py
qui ci sono i metodi invocati dalle varie azioni (es, pressione bottone cerca ordini)
quindi per sapere quale devo usare il network della console del browser
dal controller sempre passerò al service.py da cui farò la mia logica

quando lo chiamo in ajax devo chiamare il controller/service dellambiente in cui
sono poi fare altro...

 * TRADUZIONI: storebackoffice > bin > boss > common > view cè il metodo translate_label

> def traduci_label(cluster, id, label, escape=):
>>che accede al db (dev del bms in cui si opera) mmfg_translations
aggiungere le traduzioni presso storebackoffice > bin > db_scripts > translations.sql (anche se poco mantenuto)
le traduzioni sono nel view.py


MODIFICA AL FORM CONSUMATRICE:

https://localhost:4443/?module=boss.consumer_firma&program=main&sid=qq2nkxlmas84ga&from_portal=1

storebackoffice > bin > boss > consumer_firma > posweb

consumer_constants.py ci sono le costanti come:
* CONSENSI_PRIVACY e CONSENSI_PRIVACY_ADD: esse servono per registrare i consensi da mostrare in base alla lingua del sistema (bms). ADD aggiunge solo quelle spefiche per lingua, laltra costante è comune a tutte le lingue
es: "Profiling": {
    "tag": """<trad group="pos_common" id="profiling_agreement">Firma Consenso Profilazione e MKTG</trad>""",
    "to_update": True
},
"tag" è la label, "to_update" è se si vuole che tale privacy scenda al CRM per essere salvato. Se False non verrà salvato alcun dato a DB.

* consumer.js è il js che coordina le operazioni alla creazione, modifica di un form per le consumatrici.

* stampe_pdf.py e consumer_firma/constants.py sono in relazione perché uno definisce il template e laltra contiene il dizionario con cui creare il pdf

Release3: 2019-Jun-03: { --> definisco un nuovo nome
		en: {
			flag_consensi: {
				a: consenso_profiling, --> privacy da stampare
				b: consenso_direct_marketing,
				c: consenso_privacy_acknowledgement
			},
			language: en,
			sezione_1: {
				riga_1: u"""We would like to get to know you better in order to keep you updated about our personalised products and services. If you wish, you can register by filling in this form and selecting the consent options.""",
				riga_2: u"""Please read carefully our privacy notice on the back of this card."""
			},
			sezione_2: {
			}, --> sezioni per stampare i testi. guardare bene prendendo degli esempi
            ....
            footer: u"""Release3: 2019-Jun-03"""
        }

Per attivare la generazione del pdf deve esistere la tabella release_pdf_privacy e deve contenere il numero_negozio, nome_versione_release e data di creazione

es, 0501034	Release3: 2019-Jun-03	2019-06-03 12:04:38


## CONSUMATRICI NEW ##
linmara, spagna

per cercare una consumatrice che non è sul bms devo fare una query su bms

select mov.pk_consumer
from pos_movimentazioni mov
inner join pos_config_bundle config on mov.cod_negozio = config.valore
where mov.anno_transazione = 2019;

poi usare il pk_consumer su crm prendere il cognome/nome

per attivare i negozi nella tendina
~~~
SELECT valore FROM pos_config_bundle WHERE chiave = NEGOZIO; --> prendo i negozio

SELECT * FROM configurazioni WHERE tipo = abilitazione_popup_GDPR; --> se vuoto inserisco

INSERT INTO `configurazioni` (`tipo`, `chiave`, `valore`, `descrizione`, `upd_datetime`, `upd_user`)
VALUES
	(abilitazione_popup_GDPR, 1101013, 1, Se attivo abilita il popup di inserimento consumatrice per la GDPR per singolo negozio, 2019-08-02 16:41:11, bergonzinie),
	(abilitazione_popup_GDPR, 1101012, 1, Se attivo abilita il popup di inserimento consumatrice per la GDPR per singolo negozio, 2019-08-02 16:41:11, bergonzinie);
~~~

hk ---> pk_consumer HK_127877 (crm: 11134060)
hk ---> pk_consumer HK_127879 (crm: 11134062)

### TIPS ###

per conoscere in quale ambiente sono utilizzare

from config import codice_proprietario
