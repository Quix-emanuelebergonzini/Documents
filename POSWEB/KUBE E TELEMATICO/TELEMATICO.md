https://jira.mmfg.it/browse/REX-6559

recuperare codice negozio
(cercare possibilmente di accedere alla cassa su cui è stata staccata la vendita/reso)

aprirsi la connessione su due tabs (una per leggere web.log e cash_register.log)
e parallelamente su bms intanto eseguire questa query

SELECT *
FROM pos_movimentazioni m
LEFT JOIN pos_movimentazioni_info_stampa i USING (cod_negozio, anno_transazione, id_transazione)
WHERE 1=1
AND m.cod_negozio = '0100627'
AND m.anno_transazione = 2022
AND m.data_documento >= '20220201' AND m.data_documento <= '20220201'
AND m.cod_documento = 'SALE_TICKET'
AND m.cod_cassa = '01'
AND i.cod_negozio IS NULL
ORDER BY m.ora_documento
;

i record presenti sono vendite non inviate e tenere d'occhio i seguenti campi:
-- numero_documento
-- data_documento
-- ora_documento
-- codice_movimento
-- cod_cassa

sul db dell'ambiente possiamo cercare la VENDITA / STORNO in base ad un filtro (data, id_transazione,....)
SET @cod_negozio = '0100030';
SET @anno_transazione = '2022';
SET @id_transazione = '';
SET @data_documento = '20220404';
SELECT *
FROM pos_movimentazioni WHERE cod_negozio = @cod_negozio AND anno_transazione = @anno_transazione AND data_documento = @data_documento
ORDER BY id_transazione DESC
LIMIT 10;

cat var/log/web/main.log.10 | grep "^2021-09-08 16:"
cat var/log/web/main.log.9 | grep "^2021-09-12 15:"
dove 2021-09-0 è la data_documento e 16: è la prima parte dell'ora_documento


se non trova nulla guardare dove può essere il log in questo modo
head var/log/web/main.log.1
head var/log/web/main.log.2
head var/log/web/main.log.3
...
e quando noto che le date sono più o meno vicine allora
cat var/log/web/main.log.10 | grep "^2021-09-08 16:"

e qui cerco il punto in cui è stato staccato il reso
cercando ad esempio per
NUOVA TRANSAZIONE: XXXXXXXX

e trovo ad esempio

021-09-12 15:36:40,308	DEBUG   	153639930593		root	:	gerente		POS:.:	TOTALI VENDITA
2021-09-12 15:36:40,309	DEBUG   	153639930593		root	:	gerente		POS:.:	{u'ven_abbuono': 0.0, u'tot_costi_extra_detailed': 0.0, u'lordo_tessuto': 0.0, u'vendita_sconto': 0.0, u'tot_shopping_bags': 0.0, u'tot_sartoria': 0.0, u'ven_coupon': 0.0, u'ven_costi_extra': 0.0, u'tot_netto': 275.0, u'tot_sconti_abbuoni': 0.0, u'lordo_capi': 275.0, u'tot_lordo': 275.0, u'tot_gift_card': 0.0, u'tot_rettifiche_maggiorazioni': 0.0}
2021-09-12 15:36:40,311	DEBUG   	153639930593		root	:	gerente		POS:.:	Salvataggio XML: sale
2021-09-12 15:36:40,353	INFO    	153639930593		root	:	gerente		POS:.:	XML vuoto: tailoryqueue
2021-09-12 15:36:40,405	INFO    	153639930593		root	:	gerente		POS:.:	Locale per le traduzioni: consumer.locale = it; store.locale = it
2021-09-12 15:36:40,714	DEBUG   	153639930593		root	:	gerente		POS:.:	CONTANTE
2021-09-12 15:36:40,715	DEBUG   	153639930593		root	:	gerente		POS:.:	<type 'unicode'>
2021-09-12 15:36:41,143	DEBUG   	153639930593		root	:	gerente		POS:.:	CustomError('5', '5', "(message:'OPERAZIONE NON POSSIBILE', error number: 5)")
Errore 05 è tutto va bene ma la stampante non ha potuto inviare

idem cerchiamo dentro a cash_register
cat var/log/cash_register/main.log.* | grep "^2021-09-12 15:"
e per orario ora_documento (153640) lo trovo sicuramente lì  --|> 15:36:40

2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Connecting to 192.168.1.200 on 9100 with protocol CUSTOMDLL...
2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Connected
2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Sent '\x02000120948\x03'
2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Received '\x06000000'
2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Response 000000
2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Processing list: [{'tipo_doc': 'R', 'rif_scontrino': u'8', 'command': 'ABILITA_DOCUMENTO', 'rif_data': u'20210828', 'operation': '8', 'rif_matricola': u'96MK3011615', 'rif_chiusura': u'712'}, {'tipo_operazione': 'VENDITA', 'id_vat': '22.0', 'command': 'RIGA_FISCALE_REP_IVA', 'importo': '275.00', 'testo': u'85460512060022 TG:[2]'}, {'stile': '3', 'command': 'RIGA_FISCALE_AGGIUNTIVA', 'testo': u'ISEO    Stola-foulard'}, {'stile': '3', 'command': 'RIGA_FISCALE_AGGIUNTIVA', 'testo': u'Rdv:U57677 '}, {'stile': '3', 'command': 'RIGA_FISCALE_AGGIUNTIVA', 'testo': u'    '}, {'command': 'SUBTOTALE'}, {'command': 'CHIUSURA_FISCALE'}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u'Cassiera:'}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u' U84505 '}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u' '}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u'Numero articoli   : 1'}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u'Numero cassa      : 01'}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u'Data documento    : 12/09/2021 15:36:40'}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u'Numero documento  : 8126'}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u' '}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u'           GRAZIE E ARRIVEDERCI           '}, {'stile': '3', 'command': 'RIGA_CORTESIA', 'testo': u''}, {'tipo_espulsione': 'TOTALE', 'command': 'ESPULSIONE_SCONTRINO'}]
2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Sending {'len_rif_matricola': '11', 'tipo_doc': 'R', 'rif_scontrino': u'0008', 'command': 'ABILITA_DOCUMENTO', 'rif_data': '280821', 'operation': '8', 'rif_matricola': u'96MK3011615', 'rif_chiusura': u'0712'}
2021-09-12 15:36:40	DEBUG   	pos.lib.cash_register.custom	Sent '\x020007101R0712000828082181196MK301161508\x03'
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Received '\x15ERR05' <|-- PER NOI TUTTO OK MA HA DATO ERRORE...MOTIVO BOOOHHHHH
2021-09-12 15:36:41	ERROR   	pos.lib.cash_register.custom	Invio una VOID ALL alla stampante (sta per lanciare ERR05)
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Sent '\x020003001896\x03'
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Received '\x06'
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Response True
2021-09-12 15:36:41	ERROR   	pos.lib.cash_register.custom	... VOID ALL eseguita
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Sent '\x02000120948\x03'
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Received '\x06000000'
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Response 000000
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Closing socket connection...
2021-09-12 15:36:41	DEBUG   	pos.lib.cash_register.custom	Closed

x15ERR05 - ERRORE INSPIEGABILE MA TUTTO OK
x15ERR99 - ATTESA PERIODO DI INATTIVITA' -- ??? TUTO OK ??? --

infine possiamo andare a vedere se la vendita c'è ed è su bms ed è tutto ok
(magari la vendita è talmente vecchia
che sul negozio non ci sono più i logs di quando è stata creata....)
come fare?

prendere da Processing list il primo dict
{
  'tipo_doc': 'R',
  'rif_scontrino': u'8', --|> campo numero_scontrino su pos_movimentazioni_info_stampa
  'command': 'ABILITA_DOCUMENTO',
  'rif_data': u'20210828',
  'operation': '8',
  'rif_matricola': u'96MK3011615', --|> campo misuratore_fiscale su pos_movimentazioni_info_stampa
  'rif_chiusura': u'712'
}
tutte queste info sono ciò che diciamo alla stampante per come reperire la vendita collegata (in caso di storno)

SELECT i.numero_chiusura
FROM pos_movimentazioni pm
LEFT JOIN pos_movimentazioni_info_stampa i USING (cod_negozio, anno_transazione, id_transazione)
WHERE pm.anno_transazione = '2021' AND pm.cod_negozio = '0100019'
AND i.misuratore_fiscale = '96MK3011615'
AND i.numero_scontrino = '8'
AND pm.data_documento = '20210828'

e confronto rif_chiusura con i.numero_chiusura che devono essere uguali

trovata la vendita si crea un file con i logs e si risponde in issue
