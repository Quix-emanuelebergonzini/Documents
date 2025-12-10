Amministrazione di Maxima (Anna Sala) apre una ISSUE
il negozio non ha inviato all'agenzia questa vendita...(mancato invio)
oppure doppio invio!!!
loro hanno un report su bms (queryweb) e vanno su agenzia e confrontano

https://jira.mmfg.it/browse/REX-6730
https://jira.mmfg.it/browse/REX-6342

*** CUSTOM + TELEMATICO = DUE PALLE *** (by Demetrio)

# Per cominciare...
Leggere la issue per capire i riferimenti e collegarsi al negozio
    Incrociare il web/main.log con il cash_register/main.log in base alla data-ora della vendita su bms

# Una query sempre utile:
SELECT *
FROM pos_movimentazioni m
LEFT JOIN pos_movimentazioni_info_stampa i USING (cod_negozio, anno_transazione, id_transazione)
WHERE 1=1
AND m.cod_negozio = '0100014'
AND m.anno_transazione = 2021
AND m.data_documento = '20210927'
AND m.cod_documento = 'SALE_TICKET'
AND i.cod_negozio IS NULL  -- stampa fallita (mancato il join con pos_movimentazioni_info_stampa)
ORDER BY m.ora_documento
;
-- questa è la query che trova le vendite non inviate
-- pos_movimentazioni_info_stampa estensione della pos_movimentazioni (one to one)
-- ha i dati della stampa quando lo scontrino è andato a buon fine
e ci sono anche più campi per gli acconti (layby)

storno e vendita hanno un record di riferimento su pos_movimentazioni_info_stampa
gli acconti (layby) vengono stornati in batteria quindi ci sono le informazioni di storno
sulle righe originali
i campi *_annullo sono tutti riempiti con informazioni dalla stampante

A1 --> 3 --> 100 --> vuoto (5) --> vuoto (101 se annullato)
A2 --> 4 --> 100 --> vuoto (6) --> vuoto (101 se annullato)
l'annullo di A1 e A2 comporta il riempimento dei campi *_annullo

I doppi invii non si possono capire, ma si possono intuire
seguendo i log scritti in issue oppure controllando una cassa sul negozio
e noto un salto di numero di scontrino il numero mancante è stato inviato due volte..

1
2
3
4
6!!! il 5 è stato sovrascritto ecco perché non si vede ma bisogna incrociare i logs

l'orario del cash_register coincide l'orario del documento sul BMS
quindi aprendo i log della stampante potremmo trovare li i vari errori:
ERR 16 -> Fine Carta
ERR 999 -> Quasi Fine Carta (codice fittizio generato da noi)
ERR 64 -> Coperchio Aperto (capita in automatico quando cambiano il rotolo)
... questi tre abilitano la gestione del "Riprova" forzato, niente lista vendita

ERR 05 -> OPERAZIONE NON POSSIBILE: il comando va bene, ma "in questo momento" non si può eseguire
di norma si verifica nei resi telematici. tutti i comandi di un Reso sono identici ad una Vendita
cambia solo che il Reso ha un comando iniziale differente che abilita la stampante per
impostarla al RESO_TELEMATICO (comando 7101R)
questo errore dopo l'analisi ci dice di passarlo al help desk
(es, stampante non trovata...)
ERR 03 -> VALORE NON VALIDO: la stampante non riesce neanche ad interpretare il comando che le passate
(es, stampante nuova con comandi sintassi diversi...)
giriamo ad help desk per aggiornamento firmware tecnico o altro...

prima di ogni stampa viene eseguito
il comando 1209 è il check_common_erros e viene avviato a ogni connessione e prima di ogni stampa
esso restituisce 6 flags:
000000 - ok
con un 1 c'è l'errore (vedi sul codice a cosa corrisponde), in base alla posizione è 16 o 999 o 64
gli altri errori non si sono mai visti quindi si può girare al help desk

Stacco di Vendita - la stampante registra solo la stampa fiscale (non le bollettine)
e di notte avviene l'invio all'agenzia dell'entrate

# Note importanti:
Scontrino fiscale vs scontrino non-fiscale (RIGA_FISCALE_REP_IVA vs APERTURA_NON_FISCALE)
"Struttura" dei comandi di uno scontrino fiscale:
-> RIGA_FISCALE_REP_IVA per ogni item (+)
-> RIGA_PAGAMENTO_PREFISSATO per ogni forma di pagamento (-)
-> CHIUSURA_FISCALE registra la vendita sulla stampante
-> varie RIGA_CORTESIA per informazioni extra da mettere sullo scontrino
-> comando ESPULSIONE_SCONTRINO finalmente lancia fuori la vera stampa di carta

ZONA PERICOLOSA:
qualunque problema tra CHIUSURA_FISCALE ed ESPULSIONE_SCONTRINO può registrare la stampa sulla custom
(che a sera manda in Agenzia)
MA NON su posweb perché posweb aspetta che la stampante abbia concluso bene la stampa

l'errore fittizio Quasi fine carta è stato introdotto per segnalare di cambiarlo
prima che sia troppo tardi onde evitare errori....

in caso di errore fiscale si manifesta su posweb una popup diversa da quella
tradizionale con un messaggio rosso e un solo bottone Riprova

una vendita deve generare un solo documento fiscale e se si vuole una ristampa deve generare una stampa non fiscale

si può ristampare fiscalmente se si è nello stesso giorno, numero_stampa_documento è a vuoto e flag_stampa_documento a 0

Meccanismo da conoscere:
nato a seguito del Reso che è come una vendita solo con il comando cerca il riferimento con la vendita
e tutto quello che ti mando dopo lo interpreti come negativo invece di positivo.
tempo fa se si rompeva il Reso la stampante rimaneva bloccata in quella modalità...
quindi si è aggiunto e viene inviato prima di ogni ristampa e in automatico quando si rompe il Reso
Void All: comando lanciato in automatico per azzerare le operazioni fiscali in corso

Reso Telematico: il 7101R cambia la modalità della stampante fino a conclusione della stampa (da + passa a -)
vuole il riferimento ad uno scontrino esistente già registrato sulla stampante (oppure vanno passati i valori "jolly")
i valori jolly sono mockup che la stampante invia sulla vendita se non ha i riferimenti
ma non devono essere inviati molti all'agenzia perché si crea discrepanza tra vendite e resi lato fiscale
