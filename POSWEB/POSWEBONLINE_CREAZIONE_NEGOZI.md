creazione negozi concession (poswebonline o posweblite)
se bms cloud collegarsi con l'uso dei pods

lancio il seguente comando:
python /source/guest/posws/bin/poswsbe/pos_generate_negozio.py -v -l PORT
-i 0000000001 -n 2501009 -n 2501011 -n 2501012 -n 2501017 -n 2501020 -n 2501022
-n 2501023 -n 2501025 -n 2501028 -n 2501040 -n 2501054 -n 2501055
-c 1 -z PT -t POSWEB_ONLINE

-l --> JAPA, ITAL, INGL, PORT (lingua)
-i <cod_installazione> mi deve essere dato
-n per ogni negozio
-z JP (nazione)

è interattivo quindi fare <invio> per ogni negozio quando chiede parametri
per la cassa

poi allineare il db di produzione con quello di test

generare il menù (utilizzare a livello di job non da UI)

full db

full sw (verificando la versione in produzione attualmente in uso sull'ambiente)
