## COLLEGARSI AL RUNTIME DI UN BMS CLOUD ##
aggiornare google project!!!
kubectl -n bms<XX>-test get pods
kubectl -n bms<XX>-test exec -it runtime-<XXX> bash

mmfgcloud mmj-test
kubectl -n bmsmmj-test get pods

mmfgcloud om-test
kubectl -n ordermanagement-test get pods

## JOB ##
*(fuori dal runtime)* quando è già caricato in test e devo entrare nel codice del bms (aggiornato)
~~~
LANDSCAPE=TESTING docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py full -f -p10 0000901210
LANDSCAPE=TESTING docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/fisco_frh_italia_manager.py -f 20190701 -t 20190731 -o emanuele.bergonzini@quix.it
~~~
oppure
*(dentro il runtime con LANDSCAPE=TESTING)* quando lo sto sviluppando e dentro al runtime sono su TESTING
~~~
python guest/posws/bin/poswsbe/fisco_frh_italia_manager.py -f 20190701 -t 20190731
~~~

## UPDATE MODULE CLOUD ##
1. tag release-*ultimo_della_sequenza* sul branch staccato da master generalmente
2. collegarsi a jenkins
3. build
4. deploy

**avviare una procedura su bms cloud**
1. aprire il codice del BMS di riferimento
2. aggiornare KUBERMETERS e DOCKER e posizionarsi sul tag release giusto
3. invocare il comando
~~~
./docker/python_container test /source/guest/posws/bin/poswsbe/pos_generate_custom_values.py -v
./docker/python_container test /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py part -t CustomValues,Negozi -p10 1101013
~~~
oppure
~~~
LANDSCAPE=TESTING MEMORY=2048 docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py part -t Commesse -f -p10 9003201252
~~~

## UPDATE POSWEB (CLOUD) ##
1. tag *numero_progressivo* (PROD) oppure *numero_progressivo_test* (TEST)
2. collegarsi a jenkins
3. progetto Build+deploy posweb package
3. build e deploy.
    tags/*numero_progressivo* oppure tags/*numero_progressivo_test*
    TESTING...
    *numero_progressivo* (anche in caso di test il numero_progressivo senza il post fisso *_test*)
    build_type --> sw

https://confluence.mmfg.it/display/POS/Breviario+Comandi+BMS+Cloud
## INVIARE UPDATE SW,DB AL NEGOZIO SENZA COLLEGARSI DA INTERFACCIA ##
1. aprire il progetto BMS di riferimento
2. portare il KUBERMETERS_BMS sul master e aggiornarlo allultimo commit
3. invocare il comando
~~~
LANDSCAPE=TESTING ./docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_sw.py full -p10 1101013 -f
~~~
4. sperare di avere i permessi...

oppure

1. aprire il progetto BMS di riferimento
2. invocare il comando
~~~
./docker/python_container test guest/posws/bin/poswsbe/pos_export_to_store_sw.py full -p10 1101013
~~~
3. sperare di avere i permessi...


installazione senza alcuni negozi
MEMORY=3000 LANDSCAPE=TESTING docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_sw.py full -p10 all 0000000502- 0000000526- 0000000550- 0000000590- -f





è un problema abbastanza comune
credo che con un precedente avvio di docker-compose il tuo file
/Users/emanuele.bergonzini/.config/gcloud/application_default_credentials.json (che all'epoca mancava)
sia stato sostituito da una directory come effetto del bind-mount  ed è una directory. Conviene cancellarla
poi fare la procedure di login con creazione delle ADC
così dovrebbe comparire un file

sì, con anche gcloud auth login --update-adc
