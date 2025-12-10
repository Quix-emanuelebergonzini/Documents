abilitare ogni pagina di posweb 

site/bin/lib/auth_db_access.py commentare la riga 250 circa
raise pos_errors.POSException(pos_errors.AUTHORIZATION_ERROR, msg, True)

## LAYBY --> compro un capo a rate e lo lascio a negozio. Ho X giorni per chiudere le rate sennò ciccia ##

cè su HK

per fare un layby nella pagina vendita devo fleggare la voce in alto a sinistra LAYBY
per recuperare un layby sotto la cliente si genera un popup con i layby aperti

cè una pagina di riepilo di layby

cè nello store_config una voce con LAYBY_EXPIRING_DAYS che setta il numero di giorni massimo per riscattare il capo

questa tabella vuole che per una movimentazione LAYBY esista un pk_consumer associato
se non funziona un primo motivo può essere che esista una movimentazione associata non tanto ad un non esistente pk_consumer sul bms
ma che questi abbia un grado di anonimato 100 e quindi non viene esportato sul negozio
