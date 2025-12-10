CRM

Le tabelle della privacy su BMS si chiameranno:
consumer_firma_privacy: contiene le firme, una firma è univoca per pk consumer / brand
consumer_consenso_privacy: contiene i consensi delle firme,
è legata alla pos_consumer_firma_privacy dall'id_firma_privacy.
Nel campo "tipo_consenso" ha il nome del flag, mentre in "consenso" ha 1 o 0

Quando si ricava la privacy per una consumatrice bisogna sempre cercarla per pk/brand
sulla consumer_firma_privacy e andare in join sulla consumer_consenso_privacy.


------------------------------------------------------------
CRM 

ITALIA e resto del mondo tranne cina.

due consensi: profiling (profilazione) e marketing

se un consenso è a null vuol dire che non è stato ancora dato o negato il consenso

profiling deve essere a 1 per poter staccare la vendita alla consumatrice e registrare i suoi dati
marketing è facoltativo ma se a 1 e profiling è a 0 permette cmq di staccare la vendita alla consumatrice e registrare i suoi dati

profiling a 1 su un negozio di un dato brand in realtà il suo consenso viene spalmato su tutti i brands del gruppo MMFG
marketing invece rimane solo per il brand del negozio su cui c'è stata la firma

profiling a 1 può diventare a 0 su un solo brand (successivamente allo spalmaggio) se la consumer non vuole che si profilino
i suoi dati su quel determinato brands. in questo caso l'effetto è portare sulla consumer_negozio un timestamp_fine diverso
da null. perché i suoi dati devono essere mantenuti per gli altri brand ma non vedersi l'associazione con qui negozi
del brand su cui non ha voluto la firma.


grado_anonimizzazione

0 - tutti i dati
20 - tutti i dati tranne indirizzo
30 - tutti i dati tranne indirizzo e telefono (tipo solo nome e cognome)

0, 20, 30 sono i gradi anonimati canonici di MMFG

40 sono le nazioni (pk da 2 a 248 e altri)
50 è solo il pk_consumer a 1 che rispecchia su posweb quando mettiamo anonima la consumatrice

100 - spiegazione da chiedere a MARCO

101 - sono quelle anonimizzate dopo la procedura di anonimizzazione



