IMPORTANTE vedi prima ==> https://docs.google.com/document/d/1b9il1Ap2kSApTw_f-IX76-ldfSdRZtBtqzMCnmJAnzY/edit#heading=h.5jnr2le8rb6s

--------- CONSUMERS ---------
Fare una REPLACE INTO dentro forzatura_invio_dw inserendo i pk_consumers.



Query per controllare come sta proseguendo il rinvio di dati: SELECT COUNT(*) FROM _forzatura_invio_dw WHERE timestamp_forcing >= '2024-09-19' AND status is not NULL;

Considera che una volta lanciata la query, un job (già attivo) pesca, ogni 10 minuti, 625 consumatrici tra quelle che hai specificato
e ne fa il touch del timestamp in modo che venga trasmesso al prossimo invio (gli invii delle consumatrici sono schedulate ogni 3h).

Questo appunto era per le entita consumer, se sarà necessario farlo davvero, bisogna adattare i parametri per le iniziative, comunque Cri è preparato su EDW

--------- INIZIATIVE ---------

Tieni d'occhio la tabella export_log dalla quale vedi se gli invii delle consumer a EDW non sono andati a buon fine. 
Questo lo capisci dalla colonna status:
- se è in ERRORE 
- se rimane in ONGOING fino al giorno dopo (solitamente non impiega più di 3h) allora molto probabilmente è stato killato il pod che se ne occupava,
anche se dopo l'aumento della memoria del pod questo non è più successo (comunque controlla su Gcloud prima di ritrasmettere).

In questi due casi per ritrasmettere i dati è necessario collegarsi al pod di runtime di produzione e avviare il comando:

LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r consumer -a custom -f _data_inizio_ -z _data_fine_
(data inizio e data fine vanno nel formato YYYYmmddHHMMss, es: 20240627084400)

Le date di inizio e di fine corrispondono alla colonna "start_reference" e "end_reference" della tabella export_log.
Ad ogni modo non inviare più di 24h di dati alla volta.

Se devi recuperare dati di più giorni, lancia più volte il comando, una per ogni giorno. 

Allora non esiste un modo per reinviare puntualmente le iniziative (initiative, initiative_store, initiative_guest)

L'unico modo è reinviarle per range di date, ritrasmettendo il dato. Va capito in che range di date sono i dati che ti chiedono.

il comando è questo (mai mandare il comando con un range maggiore di un giorno):
LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative -a custom -f 20240506000000 -z 20240507000000

ti ricordo che le risorse legate alle iniziative sono tre (attenzione che vanno usate le label in inglese): 
initiative, initiative_store, initiative_guest

esempio: iniziativa 7305
(crm_iniziativa)
LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative -a single -k 7305

(crm_invitato)
LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_guest -a custom -f 20240909130944 -z 20240909131044
LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_guest -a custom -f 20240911113549 -z 20240911113649
LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_guest -a custom -f 20240912151026 -z 20240912151126
LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_guest -a custom -f 20240914151539 -z 20240914151639
LANDSCAPE=TESTING /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_guest -a custom -f 20240916111522 -z 20240916111622

SELECT id_resource, MAX(timest) AS timest
FROM (
    SELECT
        CONCAT(id_iniziativa, ":::", cod_negozio, ":::", progressivo_invitato) AS id_resource, i.dataora_modifica AS timest
    FROM crm_invitato i
    WHERE 1=1 AND i.dataora_modifica > '2024-09-03 07:09:00' AND i.dataora_modifica <= '2024-09-03 10:12:00' 
    UNION
    SELECT
        CONCAT(id_iniziativa, ":::", cod_negozio, ":::", progressivo_invitato) AS id_resource, GREATEST(i.dataora_modifica, COALESCE(a.dataora_modifica, 0)) AS timest
    FROM crm_invitato i
    JOIN crm_accoglimento a USING(id_iniziativa, cod_negozio, progressivo_invitato)
    WHERE 1=1 AND GREATEST(i.dataora_modifica, COALESCE(a.dataora_modifica, 0)) > '2024-09-03 07:09:00'
    AND GREATEST(i.dataora_modifica, COALESCE(a.dataora_modifica, 0)) <= '2024-09-03 10:12:00'
    UNION (
        SELECT
            id_resource,
            timestamp_cancellazione AS timest
        FROM crm_iniziativa_deleted
        WHERE resource IN ("invitato", "accoglimento") AND timestamp_cancellazione > '2024-09-03 07:09:00' AND timestamp_cancellazione <= '2024-09-03 10:12:00'
        GROUP BY id_resource
    )
) t GROUP BY 1 ORDER BY 2;

(crm_iniziativa_negozio)
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240909130944 -z 20240909130948
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240911113542 -z 20240911113544
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240912172017 -z 20240912172018
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240913123040 -z 20240913123042
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240914145052 -z 20240914145054 
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240920115029 -z 20240920144124
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240921154022 -z 20240921154024 
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240922154037 -z 20240922154039
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240923081052 -z 20240923152028
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240926090036 -z 20240926140042
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240927073016 -z 20240927145025
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240928132010 -z 20240928180010
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240929094024 -z 20240929170040
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20240930083031 -z 20240930171105
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241001082108 -z 20241001082110
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241002135055 -z 20241002163034
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241003083114 -z 20241003083116
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241007124027 -z 20241007164100
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241008085553 -z 20241008085555
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241009151839 -z 20241009151842
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241010094126 -z 20241010094128 
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241011093111 -z 20241011123124
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241017082831 -z 20241017083032
LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r initiative_store -a custom -f 20241029163732 -z 20241029163738


(SELECT CONCAT(id_iniziativa, ':::', cod_negozio), dataora_modifica
    FROM crm_iniziativa_negozio
    WHERE 1=1 AND dataora_modifica > '2024-0911 11:35:00' AND dataora_modifica <= '2024-0911 11:35:50') UNION 
(SELECT id_resource, timestamp_cancellazione
    FROM crm_iniziativa_deleted
    WHERE resource = "iniziativa_negozio" AND timestamp_cancellazione > '2024-0921 11:35:00' AND timestamp_cancellazione <= '2024-09-11 11:35:50')
ORDER BY 2, 1


(fidelity) # not working #

LANDSCAPE=PRODUCTION /Users/emanuele.bergonzini/repos/backoffice/docker/run_job.sh /env/bin/python bin/scripts/crm_dw.py -r fidelity -a custom -f 20241029163732 -z 20241029163738

SELECT tipo, codice
FROM consumer_fidelity
-- FROM consumer_fidelity_history
WHERE tipo IN ('LOYALTY_CARD_NEW', 'LOYALTY_MC_IT', 'LOYALTY_MC_IT_24', 'LOYALTY_PB_IT', 'LOYALTY_PB_IT_24', 'LOYALTY_INTREND_FR', 'LOYALTY_INTREND_ES', 'LOYALTY_INTREND_AT', 'LOYALTY_INTREND_HU', 'LOYALTY_INTREND_NL', 'LOYALTY_CARD_JP')
AND pk_consumer IS NOT NULL 
-- AND action != 'insert'
AND timestamp_modifica >= '2024-09-01 16:24:13' AND timestamp_modifica <= '2024-09-01 16:26:39'


2025-03-11
Ciao,
l'invio verso edw coinvolge varie risorse e per ciascuna c'è una situazione diversa:
consumer --> se ne occupa datastream
eventi (initiative+initiative_guest+initiative_store) --> sta inviando i dati datastream,
ma il flusso di crm è ancora attivo per sicurezza (viene considerato solo il flusso di datastream)
fidelity (fidelity+fidelity_history) --> se ne occupa crm
Attenzione: datastream è un submodule di crm!! (semplicemente se ne occupa energee3)

