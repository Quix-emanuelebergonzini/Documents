release_pdf_privacy il campo cod_assegnazione è una etichetta che va cercata in ana_soggetti_raggruppamenti
(con valore_raggruppamento). Quindi ad una etichetta sono associati alcuni negozi


1. creare file attuale.json ed incollare da BMS la versione attuale
2. creare file nuova.json e incollare il medesimo contenuto di attuale.json
3. prendere una parte di testo "nuova"
4. aprire python3 su proprio mc
>> test = '<nuovo_testo>' oppure "<nuovo_test>"
>> import json
>> json.dumps(test)
 
5. Prendere il testo racchiuso negli apici (senza apici)
6. eliminare \\u con \u e controllare che non ci siano cose tipo \u2013 o \u2019 questi sono caratteri tipo - oppure '
7. sostituire in nuova.json poco a poco il testo
8. copiare tutto il json
9. portare il json dentro https://jsonviewer.stack.hu/ e compattarlo
10. copiarlo ed aggiornare il record su Poslite (tabella release_pdf_privacy_template)

Quando si è arrivati alla versione definitiva si porta su BMS ma bisogna mettere la giusta codifica e poi
aggiornare il record