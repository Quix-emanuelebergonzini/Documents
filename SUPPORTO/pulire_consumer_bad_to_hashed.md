1) recuperare xml con cui era stata aggiunta come hashata

SELECT *
FROM consumer_crm
WHERE pk_bms = 'MMJ_266800';

SELECT *
FROM pos_movimentazioni
WHERE pk_consumer = 'MMJ_266800';

SELECT *
FROM pos_consumer_negozio
WHERE pk_consumer = 'MMJ_266800'; -- tramite il cod_locale posso cercare nei file_name di importazione

SELECT *
FROM pos_dati_negozi -- il negozio è quello "fittizio", usare questo indicato nella query
WHERE tipo_dati = 'consumer' AND tipo_struttura = 'xml' AND negozio = '0801127' AND file_name LIKE '%7000003743709%'

2) modificare i dati sia su BMS che su CRM come da XML (indirizzi, contatti, nome e cognome UNCOMPLETED)
	- nome e cognome diventano UNCOMPLETED
	- sbiancare dati accessori tipo data di nascita, sesso
	- sbiancare i dati di indirizzo
	- eventualmente togliere i dati di indirizzo in lingua
	- eventualmente togliere nome e cognome in lingua
	- grado anonimato a 25 sulla consumer (CRM) / pos_consumer (BMS)

3) solo su CRM va rimossa la privacy
	DELETE FROM consumer_consenso_privacy WHERE pk_consumer=12495422;
	DELETE FROM consumer_firma_privacy WHERE pk_consumer=12495422;
4) solo su CRM bisogna anche adattare la consumer_contatto

5) in presenza di vendite per il pk_consumer mantenere i legami dei negozi
con quest'ultimo
altrimenti se non ha vendite
pulire tutto tranne la relazione con il negozio 0801127

6) part ai negozi MMJ di Consumer,ConsumerPrivacy nel pomeriggio dopo le 15
