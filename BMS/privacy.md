## STAMPA DELLA PRIVACY dalla form della consumatrice ##
per la stampa della privacy in linmara come anche in hk, si desumono le traduzioni dello store (lingua dela gui o inglese) e della consumatrice (se non impostata uguale a quella dello store)
quindi store e consumatrice se la lingua non è tra quelle conosciute si impone a INGLESE.
dopo di che, si prende la release della privacy, in inglese, se la lingua richiesta non è presente tra quelle esistenti, altrimenti stampa la privacy nella lingua richiesta e in più in INGLESE
se la lingua stampata non è inglese

SPIEGAZIONE PER PUNTI:
    PRIVACY:
        "ReleaseX" : {
            "it": {
                "language" : "it"
            },
            "en": {
                "language" : "en"
            }
            ...
        }
    * recupero delle traduzioni del negozio e della consumatrice
        - se la lingua del negozio non è conosciuta: inglese o gui del bms
        - se la lingua della consumatrice non è conosciuta: come il negozio (oppure inglese o gui del bms)
    * acquisisco il dizionario contenente la release delle PRIVACY in base al cod_negozio
    * prima valuto la lingua della consumatrice e se la lingua è conosciuta, stampo la PRIVACY nella lingua della consumatrice
    * altrimenti valuto la lingua del negozio e se la lingua non è conosciuta, stampo la PRIVACY in INGLESE
    * infine, se la lingua della PRIVACY stampata è diversa dalla lingua INGLESE, stampo una privacy in INGLESE


**storebackoffice/bin/boss/consumer_firma/posweb/stampe_pdf.py(01/09/2019)**

info_negozio = common_utils.get_store_data(pard[POS_CONFIG][COD_NEGOZIO])[pard[POS_CONFIG][COD_NEGOZIO]]

release_v = common_utils.get_release_version(pard[POS_CONFIG][COD_NEGOZIO])
if not release_v:
    raise ApplicationError(Versione di release per stampa pdf non trovata per il negozio {}.format(pard[POS_CONFIG][COD_NEGOZIO]))

# Recupero le traduzioni
transl_defs = stampe_utils.get_translation_defs(pard, consumatrice)

**stampe_utils.get_translation_defs(pard, consumatrice)**
def get_translation_defs(pard, consumer_data):
	"""
		Restituisce i dati per le traduzioni, dato il pard e il codice della consumatrice.
	"""
	# STORE LANG
	store_lang = pard[POS_CONFIG][STORE_ISO_COUNTRY]
	store_lang = LINGUE_ISO_TO_CRM.get(store_lang, INGL) **--> {ITAL:ITAL,INGL:INGL,...}**
	store_locale = LINGUE_CRM_TO_ISO[store_lang] **--> {IT:ITAL,EN:INGL,...}**
	store_translations = get_translations(pard, store_locale) --> se la lingua non è presente viene presa pard[POS_CONFIG][GUI_LANGUAGE_LOCALE]

	# CONSUMER LANG
	consumer_lang = consumer_data.get(lingua, )

	if not consumer_lang:
		consumer_lang = store_lang

	if consumer_lang not in LINGUE_CRM_TO_ISO:
		consumer_lang = INGL

	consumer_locale = LINGUE_CRM_TO_ISO[consumer_lang]
	consumer_translations = get_translations(pard, consumer_locale)

	return {
		store: {
			locale: store_locale,
			translations: store_translations,
			language: store_lang
		},
		consumer: {
			locale: consumer_locale,
			translations: consumer_translations,
			language: consumer_lang
		}
	}
********************************************************

# priorità alla lingua della consumatrice:
consumer_locale = transl_defs[consumer][locale]
store_locale = transl_defs[store][locale]
try:
    release_translations = PRIVACY_TRANSLATIONS[release_v]
except KeyError as ex:
    raise ApplicationError(Impossibile generare il pdf per la seguente versione di release: {}.format(release_v))
admitted_languages = release_translations.keys() **--> queste sono le lingue registrate nei testi della privacy**
if consumer_locale and consumer_locale.lower() in admitted_languages:
    language = consumer_locale
    dettaglio_informativa_privacy = informativa_privacy(consumer_locale, release_translations)
else:
    if store_locale.lower() not in admitted_languages:
        store_locale = en
    language = store_locale
    dettaglio_informativa_privacy = informativa_privacy(store_locale, release_translations)
....
# se la lingua consumatrice/negozio è diversa da inglese, stampa una copia in inglese:
if dettaglio_informativa_privacy[language] != en:
    pdf.set_font_for_language(en, en)
    dettaglio_informativa_privacy = informativa_privacy(en, release_translations)
    genera_documento(pard, consumerdata, path_file_firma_consumatrice, en, pdf, dettaglio_informativa_privacy, dati_contatto_privacy_negozio, info_negozio)



la popup_privacy (o popup privacy) che si apre quando i dati sono vecchi
o manca una firma sono anagrafica.selectConsumerHandler in vendita.js
quel punto ci arriva quando seleziono dall'autocomplete della vendita

vedi esempio is_uncompleted (utils.uncompletedFields)
