TODO POSLITE:

- SOLO IN PROD: Ricorda a loro di disattivare il job del BMS installazione-db-posweb-container
- Controllare la versione a db: (Esempio di connessione a DB poswebonline): 
- Controllare che i job siano tornati su
- Dare un occhio ai log che non si rompa uploader (per il discorso fix di Massimo di agosto)
- Dare un occhio ai log del runtime 
- Fai giro, da browser, i poslite se hai un utenza amministrativa puoi scegliere tutti i negozi
- Controlla iframe dal BMS su Posweb basta trovarne uno che funzioni: 
- Check vendita, ricerca consumatrici, 
- Ultimo check, provare a eliminare i record dalla globlal status
- Verificare che funzioni uploder, facendo una vendita e verificando sul bms che xml arrivi in sede, controllare sul bms sulla tabella pos_dati_negozi


TODO BMS:

Controlla la chat e vedi cosa stanno facendo
Quando hanno detto che ha migrato:
Controlla il db del bms  (test,staging(quando c'è) o prod), query: SELECT version();
Poi, facciamo un giro sull'interfaccia del bms da browser: SOLO SU TEST prova a lanciare un incr su un negozio a caso

Ricorda che se lanci un INCR su un negozio poslite, poi nella lista negozi ne vedrai parechi perchè la macchina è la stessa:

Poi qualche giro di check su delle funzionalità (SOLO LETTURA) sulle pagine di boss:

PAGINE BOSS / PAGINE STOREBACKOFFICE, ricorda che nelle nostre nel percorso c'è /boss , tipo la ricerca ordini:

Riepilogo Versamenti
Riepilogo Reintegri
Configurazione Promozioni
Chiusura giornaliera
Resi Ordini Online
Vendite di oggi
B2E Avanzamento Ordini
Recupero Punti Fidelity
Forcing punti fidelity
Antiriciclaggio

Crediti Sospesi
Aggiornamenti negozi
Configurazione casse
Configurazione negozi
Lista Acconti

Gestione Incassi
Petty Cash

- Check dei log del DB su GCP: Controlla dalla tab log se ci sono pezzi rossi o disastri sul container: runtime, importazione_xml_negozi