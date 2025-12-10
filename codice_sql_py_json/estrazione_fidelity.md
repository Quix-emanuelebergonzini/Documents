https://jira.mmfg.it/browse/DTDD-10283

SELECT history.codice, fidelity.pk_consumer, (history.importo_corrente - history.importo_orig_corrente) AS punti_effettivi, (history.importo_congelato - history.importo_orig_congelato) AS punti_congelati,
CASE WHEN fidelity.attivo = 1 THEN 'SI' ELSE 'NO' END AS attivo, history.timestamp_modifica AS data_ora_operazione
FROM consumer_fidelity_history history
INNER JOIN consumer_fidelity fidelity ON fidelity.tipo = history.tipo AND fidelity.codice = history.codice -- AND fidelity.cod_negozio = history.cod_negozio
WHERE 1=1
AND fidelity.tipo = 'LOYALTY_CARD_NEW'
AND fidelity.data_inizio < '20200101'
AND history.timestamp_operazione BETWEEN '2020-01-01 00:00:01' AND '2020-01-15 23:59:59'
AND history.action NOT IN ('insert', 'assign')
-- AND fidelity.codice = '2130022380533'
ORDER BY history.codice, history.action DESC
;
