sono eventi in negozio o roba simile

le tabelle su posweb interessate sono

crm_iniziativa
crm_invitato (id_iniziativa, pk_consumer, negozio)
crm_iniziativa_negozio (id_iniziativa, negozio, data_inizio_validita, data_fine_validita)

se è un SALDO_PRIVATO il prezzo a listino è il C

il listino e il prezzo riferito al modello devono essere collegati.

PRICE_LIST_MODE sul negozio deve essere a 2 e gli incrementali devono essere correttametne intstallati sul negozio

----

utilizzando l'app ad esempio viene invocato un metodo
set_accoglimento_consumer che importa una consumatrice sul negozio
ma il flusso si aggancia al flusso della ricerca di sede


consumer_export_spool è una tabella su crm che contiene gli export verso salesforce

consumer_negozio
consumer_gm
consumer_cliente_finale

sembrano le uniche che modificando il timestamp invia a slf

----

gli eventi si gestiscono da CRM
da posweb c'è l'alterazione

tramite un foglio excel caricano la lista dei negozi per una iniziativa
una inizativa può differire tra data_inizio generale e data_inizio del singolo negozio

poi carico la lista delle invitate da crm (la lista può essere aperta o chiusa quindi il negozio può aggiungere o togliere)
ma un negozio A non può aggiungere una che è invitata da B (crm_invitato)

il negozio riceve la lista degli invitati. VALIDO - caricato e sono sicuro che c'è
VALIDO_POS - contattato e dovrebbe partecipare
VALIDO_IMBUCATO - non previsto

invece la partecipazione all'evento può essere aperta a tutti (crm_accoglimento)


____________________________

se creo una iniziativa essa poi la trovo su
crm_iniziativa

se carico una lista esse vanno dentro a
crm_invitato
e su crm_iniziativa_negozio c'è il riferimento a quali negozio è collegata l'iniziativa

se da gui eliminano un negozio su crm_iniziativa_negozio lo stato di quel negozio passa ad ELIMINATO e tutti i pk sulla crm_invitato
passano 