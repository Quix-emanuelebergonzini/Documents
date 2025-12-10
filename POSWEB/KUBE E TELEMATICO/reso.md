Fino alla versione 14.02.48 il funzionamento della Kube NON rispettava de facto quanto descritto nel manuale.
Quindi presumo che anche il nostro software, per passare gli UAT, fosse stato modificato di conseguenza
(aderendo quindi NON alla documentazione ma all'esperienza), ma non saprei in quale misura.

Dalla versione 14.02.62, il funzionamento è stato modificato da Custom senza avvisare preventivamente
(vedere thread mail "Aggiornamento versione firmware Kube" di gennaio 2024).

7101 R 0912 0001 020221 9 11 96MK3003257  → col 9, la Kube controlla se possibile o meno fare il reso; non lo apre,
ma ci dà una info per poterlo poi aprire correttamente (anticipa possibili problematiche)

se mi risponde 0 → il reso è apribile, ma sarà NON CONFORME (succede quando la matricola del
reg. fiscale dello scontrino è diverso da quello a cui si manda il comando) --> reso da altro negozio
--> per i test
bisogna staccare una vendita con reale stampa su una kube poi cambiare sulla
pos_movimenti_info_stampa la matrico dopo che arriva a sede.
recuperare la vendita sul negozio di test e chiudere il reso

se mi risponde 1 → il reso è apribile, è sarà CONFORME (succede quando la matricola del
reg. fiscale dello scontrino combacia, e nella memoria fiscale è presente quel preciso scontrino).
NB: se per caso verrà superata l'iva o qualsiasi altro subtotale, non si scopre con questo comando
che lo apre e basta, ma con le righe successive, e dovremo quindi gestire l'errore nel corpo del documento
--> reso normale

se mi risponde 2 → il reso NON E' APRIBILE con questi parametri, per nessun motivo.
(succede quando a partità di matricola del reg. fiscale, è stata cambiata la memoria fiscale,
per cui la Kube cerca nella propria memoria, ma non trova quello scontrino, e non consente l'apertura di quel reso). 
Per forzare l'apertura del nostro reso (che a questo punto renderemo noi stessi NON CONFORME a prescindere),
si può procedere con l'operatore 8 (vedi punto successivo), dando però il riferimento della matricola fake
per forzare un reso non conforme
--> non trova nella memoria fiscale la vendita

7101 R 0912 0001 020221 8 11 96MK3003257 → con l'8 la Kube apre il reso direttamente
il comando dato con operatore 8, visto che abbiamo controllato prima col 9,
non darà MAI risposta con codice 2 perchè l'abbiamo proprio evitato. A questo punto andranno tutti bene, infatti:

quelli che mi avevano dato 0, mi daranno ancora 0 quindi stampa -> userà i dati non fake
quelli che mi avevano dato 1, mi daranno ancora 1 quindi stampa --> reso normale
quelli che mi avevano dato 2, siccome è stata forzata la matricola Fake, mi darà in risposta 0 quindi stampa
    con dati fake

prima i casi di errori erano 0 e 2 ora solo 2. solo con il 2 si mettono i dati fake
(vedi site/bin/common/constants.py VALID_REPLIES_DOC_ABILITATO_STAMPA)