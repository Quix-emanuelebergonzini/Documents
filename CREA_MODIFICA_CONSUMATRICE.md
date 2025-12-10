se il negozio ha in store_config la chiave CONSUMER_MODE = ASYNC
questo si verifica per creazione e modifica consumatrice:

1) posweb chiama al salvataggio subito il CRM per staccare il pk_consumer,
quidi su CRM si crea un record vuoto con una anonimizzazione particolare
2) xml arriva in sede sul BMS
3) viene importato sul BMS
   4) poswsbe (ConsumerCommonService.make_full_consumer => consumer_service.set_resource => self.create_new_consumer)
5) Astronauta tramite self.create_new_consumer chiama RETAIL e salva sulla fr_consumatrici_spool un record con i dati
6) Astronauta importa i dati da RETAIL e aggiorna il record su CRM 
7) Gira ogni due ore sul CRM e si può invocare con questo comando
>>> python bin/runalone.py bin/astronauta --up

*** IN REALTA' su test la tabella fr_consumatrici_spool è sul CRM quindi avviene un passaggio in meno
perchè non esiste RETAIL di test ma solo di prod

se invece la modalità è SYNC la modifica avviene diretto su CRM (tutti i dati)

=====
una volta ripristinato astronauta, tutto si torna ad allineare...
il disallineamento può durare un giorno al max (cioè se recupero astronauta oggi, la modifica si riflette sui negozi
con il primo incrementale utile, cioè domani).

Cosa leggermente diversa per i sistemi esterni (che dipendono dalla frequenza dei job)...
Mentre per salesforce invece dipende dalla sua coda di smaltimento (10k al giorno)

