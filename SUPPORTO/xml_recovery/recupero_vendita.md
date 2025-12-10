xml_recovery serve solo ad un caso
quando la vendita è su db del negozio
ma non è arrivata su BMS perchè tipo si è rotta la creazione dell'xml
altrimenti non va usato

Ocio solo ad una cosa

se è normale vai tranquillo con il comando

./bin/python bin/xml_recovery.py <id_transazione> --save

se è b2e andrebbe verificato preventivamente che non sia arrivata su OM
perchè se è già su OM, con l'xml_recovery ci riproverebbe
ed avremmo 2 ordini su OM a fronte di una sola vendita


molto difficile cmq perché se non arriva su bms non arriva a om
perché su om arriva un json che nasce dall'xml del bms.

nel caso arrivi qualcosa su bms e anche om però probabilmente su om c'è un errore e
in caso se om non riesce ad inviare la vendita arrivata su om mettere la data_invio così che non
invii più. poi una volta che su bms si importa bene anche su om si genera un ordine buono.