consumer_fidelity --> anagrafica delle fidelity ---> punti reali / punti congelati
consumer_fidelity_calcolo_punti --> id_calcolo_punti quanto esiste significa che
a fronte di uno checkout ci sono le operazioni collegate (vedi query sotto)
consumer_fidelity_history --> storia delle operazioni


2 operazioni possibili ---> da posweb / da website (b2c)

da posweb SALE / RETURN / FINALIZE
**solo su un negozio reale sono inserite come FINALIZE la quale genera i punti reali**

SALE / RETURN sono diverse se provengono da Posweb o B2C

QUOTATION è per avere la stima dei punti guadagnati e persi in anticipo (precalcolo)

da POSWEB da SALE a stato FINALIZE direttamente (e non servono gli altri stati)

B2C (da postman o website)
    - operazione: QUOTATION: è un servizio che simula il calcolo dei punti fidelity di un cliente.
    - operazione: CHECKOUT: ordine confermato ma non è detto che tutto verrà spedito, stato: PENDING.
        Tutti sono punti congelati tranne le GIFT CARD che già sono punti reali (perché non esiste reso)
    - operazione: ASSIGMENT: arrivano da OM, so quanti ne verranno spediti e quanti no.
        In questo i punti dei capi si scongelano, ma solo di quelli effettivamente spediti e si assegnano solo questi.
        Sovrascrive CHECKOUT (nei punti reali / congelati). ASSIGMENT è in stato PENDING.
        - il CHECKOUT va in stato: CANCELLATED
    - nei seguenti 30gg dopo arrivano i RETURN (in stato PENDING) con importo NEGATIVO
    >>>> forse non più.... più o meno dopo 30gg gira un job che porta ASSIGMENT in stato FINALIZE (e qui i punti vengono scongelati) <<<<<<
        - il RETURN va in stato: CANCELLATED
        - il ASSIGMENT va in stato: FINALIZE

    - operazione: SALE: avviene solo per le chiamate postweb e vengono subito FINALIZZATE le altre invece arrivano da chiamate
        ai servizi REST (FidelityRest chiama sempre un servizio Fidelity appunto)

- è permesso mandare più CHECKOUT che sostituiscono i CHECKOUT precedenti
- è permesso mandare più ASSIGMENT ma non sostituiscono gli ASSIGMENT precedenti **
- un ASSIGMENT vuoto è l'annullo

i punti usati vengono subito detratti dagli importi reali. i punti guadagnati invece vengono congelati.

** PULIRE UN ASSIGNMENT ERRATO:
- FINALIZED della vendita errata
- FORCE riaccredito punti (utilizzati - guadagnati)
api_request_log con body like id_operazione --> trovo le operazioni che il b2c ci ha inviato (al crm)
prendo il request e gli cambio da assigment a finalized così chiudo quella vendita
poi faccio un force mettendoci una nota!!!!!


nota bene:
id_operazione è univoco

    select *
    from calcolo_punti                          ==> per avere le righe collegate (in base a id_ref) di un dato checkout (id)
    where id = <checkout> || id_ref = <checkout>

se rimane un checkout pending con punti congelati
si manda un assignment vuoto (capi, contabilita, etc) così da azzerare i punti congelati (che si perdono....)
(e poi finalizzarlo)
https://maxmarafashiongroup.atlassian.net/browse/AMSB2C-48179
oppure
https://maxmarafashiongroup.atlassian.net/browse/AMSB2C-59269
{ --> prendere il da api_request_log il body del checkout e pulirlo (più sicuro)
    "data": {
        "operazione": "ASSIGNMENT", --> poi si rifa con stesso body ma FINALIZED
        "cod_negozio": "0133008",
        "importo": 0.00,
        "divisa": "EUR",
        "pk_consumer": "16582935",
        "id_operazione_ref": "1083091668",
        "data_ora_operazione": "2023-11-06 08:16:23",
        "cod_negozio_ref": "0133008",
        "anno_operazione_ref": "2023",
        "contabilita": [],
        "pagamenti": [
            
        ],
        "capi": [
            
        ]
    }
}

################# inviare i dati su salesforce #################

2025- MEOTODO VELOCE per iniviare a SLF:

-- inserire nella consumer_export_spool un record relativo a ciò che manca
-- in questo esempio è preso dalla consumer_fidelity_history e nel ext_name è una quadrupla "pk, tipo, codice, id dell'entità"
-- generare un uuid dalla console py di crm prod
# import uuid
# str(uuid.uuid4())
-- counter a 0

INSERT INTO `consumer_export_spool` (`entita`, `pk_consumer`, `id`, `ext_name`, `action`, `timestamp_inserimento`, `millisecond_inserimento`, `timestamp_modifica`, `export_date`, `ext_update_only`, `counter`, `requestid`, `id_fusione`)
VALUES
	('consumer_fidelity_history', '6468749', '6468749,LOYALTY_MC_IT_24,2230026077641,18749370', 'slf', 'API_UPSERT', '2024-01-02 14:32:00', '816397', '', '', '0', '0', '495995e0-3b8b-48e1-89c8-628005afe07a', '');

# se tutto va OK il record viene eliminato altrimenti va in LOCK e non viene MAI più processato (quindi safe)
# se tutto va OK si crea un record in api_request_log con request_id pari al uuid()

=== altri appunti per invio a SLF ===

nella consumer/spool.py nel metodo \_get_master_data_with_cache
trovo if messaggio.entita == consumer dove posso specializza quale entita sto inviato a salesforce e introdurre ad esempio
altre chiavi da inviare

poi per testarlo bisogna:
1. trovare in consumer/spool.py il punto del codice SenderEsb().send(url, mth, message) e sostituire con
print (debug)
print (message)
# SenderEsb().send(url, mth, message)
print ("fine simulazione chiamata a Salesforce")

2. poi devo andare sul db e controllare se esiste nella consumer_export_spool la mia entita o crearla
SELECT * FROM consumer_export_spool WHERE entita LIKE consumer_fidelity%;

3. se cè devo inserire una riga uguale
4. poi chiamare dalla root del login sullambiente
python bin/scripts/consumer_spool.py -a run -l 1 -v 2 -r consumer_fidelity,consumer_fidelity_history

# service.popola_spool()

[crm@posweb-be-dev-01 ~]$ python bin/scripts/consumer_spool.py -a run -l 1 -v 2 -r consumer_fidelity_history
2019-11-27 16:27:09.299742 -  debug della entity consumer_fidelity_history
PUT
{data: {attributes: {data: {action: update,
                                  cod_negozio: 0133007,
                                  custom_data: {uanno_operazione: 2019,
                                                  ucod_negozio: u0133007,
                                                  uid_operazione: u11234007,
                                                  utipo_operazione: uCHECKOUT},
                                  id_operazione: 11234007,
                                  importo_congelato: 260.0,
                                  importo_corrente: 0.0,
                                  importo_orig_congelato: 232.0,
                                  importo_orig_corrente: 0.0,
                                  tipo_operazione: CHECKOUT},
                         ext_name: slf,
                         requestid: b21248fc-e5f2-418f-a074-1939072e8231},
          id: 8344681,LOYALTY_CARD_NEW,2130022455392,198085,
          type: consumer_fidelity_history}}
fine simulazione chiamata a Salesforce
Fine elaborazione in 0:00:00.045277. 0 errori.