dopo una vendita (o un conteggio taglio banconote)
si genera un xml e posweb chiama il fe di poswsbe che chiama il be di poswsbe
il quale scrive sulla pos_dati_negozi
POI passa un job che è il pos_import_from_store.py che porta ciò che deve essere importato
dalla pos_dati_negozi (in base agli ID > dellultimo importato) che scriva sulla pos_import_spool
dopo di che, si legge questa tabella prende xml lo legge e splitta le informazioni sulla pos_movimentazioni etc etc etc.

avviare il docker e lanciare
LANDSCAPE=TESTING docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_import_from_store.py

##### JOB IMPORTATORE ##
posweb locale è collegato al BMS<nazione>TEST quindi...
quando si fa una vendita posweb crea un xml che viene scritto nella pos_import_spool
poswsbe --> pos_import_from_store.py --> import_data(self) --> prende da pos_import_spool e scrive su pos_dati_negozi
dopo di che --> istanza del parsatore che in base a [tipo_dati] se xml è un parse Xml e allinizio file
cè un dizionario con le classi di parsin per i vari tipi di documento (instance.process(d)) come ad esempio
pos_parser_common.XmlSale --> che rimanda a XmlMovimentazioniSale
dopo linit di XmlMovimentazioniSale si avvia il process --> da qui ci si può innestare (es, nel save)

per i TEST
dentro a kubermeters e al bms<nazione> cè cronjob.yml con i cron schedulati.
sono attivi quelli non commentati e con la schedulazione impostata. visitare il sito https://crontab.guru/
per vedere ogni quanto girano

(es, */3 * * * * --> significa ogni tre minuti)*

python httpd-chroot/guest/posws/bin/poswsbe/pos_import_from_store.py

#### POS_PARSER_CONSUMER ##
local = 0 --> online, pk ricevuto da sede
local = 1 --> pk staccato su negozio, ma negozio offline
local = 2 --> pk scaricato da sede


il negozio online direttamente comunica con la sede e il pk_consumer è subito allineato. BMS traduce i pk_consumer MCJ_XXX e HK_XXX in pk_consumer interi.
il negozio offline stacca un pk_consumer (locale) stile POS2019138 e poi quando torna online comunica alla sede (BMS) il quale stacca un pk_consumer e crea un mapping
tra quello locale e di sede. Tutte le sere poi arriva un incr sul negozio il quale allinea i suoi pk_consumer locali con quelli di sede. E il gioco è fatto.

in BMS il mapping tra pk_consumer locale e di sede è sulla tabella pos_mapping_id_pk_consumer
in BMS il mapping pk_consumer locale e negozio è sulla pos_consumer_negozio

con il CRM il discorso è simile. La sede chiama alla fine del parsing (pos_parser_consumer) il metodo make_full_consumer_poswsbe
il quale gli passa delle informazioni quali il consumer_negozio. Aggiungendo una chiave in dizionario automaticamente crm salva il dato nel campo in tabella con lo stesso nome della chiave
consumer_negozio = {
    "note_negozio": self["note_negozio"] or "",
    "cod_scheda": str(self["cod_scheda"])
    "cod_locale": "POS2019138" <-- nuova chiave aggiunta al dizionario (es scopo illustrativo)
}
quindi attenzione ai campi in tabella su CRM nella tabella consumer_negozio

in questo metodo (make_full_consumer_poswsbe) viene creato il nuovo consumer su crm con relativo mapping.
vedi tabelle consumer_negozio (mapping tra pk_consumer di crm e pk_consumer locale)
e consumer_cliente_finale (mapping tra pk_consumer di crm e quello di retail)
