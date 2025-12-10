https://jira.mmfg.it/browse/REX-314
è un problema noto che con troppi capi la kube non stampa (tutto o in parte)
lo scontrino
quindi di solito andiamo in lista vendite e ristampiamo il documento
che viene generato come pdf e poi lo scarichiamo e lo alleghiamo alla issue

se non ho modo di ristamparlo devo settare sulla store_config
a 1 il key_name = 'BROWSER_DOWNLOAD_PRINTS_ENABLED'

risposta:
Hi ....,
in the attached file you can find the pdf of the ticket, the document is too long to be printerd from the USB Kube.
Please let us know if you need other information.


https://jira.mmfg.it/browse/FGMMJ-393
nella query del venduto noi diamo come codice prodotto il 004 quando
sartoria, progressivo_capo è 0 (extra vendita), cod_operazione 99
non confondere classe con cod_operazione
in mmj indipendentemente dalla classe si può usare il cod_operazione 99
per codificare le spese di spedizione


https://jira.mmfg.it/browse/FGSDRETAIL-34760
errori di reti perpetui non hanno prodotto il numero scontrino
ma anche una difformità dei dati. leggere risposta di marco
confrontare tutte le informazioni legate alla stampa
pos_movimentazioni_info_stampa
