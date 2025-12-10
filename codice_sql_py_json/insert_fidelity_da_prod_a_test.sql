SET @rownum := 1062089;
SELECT '' AS id,
history.tipo,
history.codice,
history.cod_negozio,
history.action,
history.importo_orig_corrente,
history.importo_corrente,
history.importo_orig_congelato,
history.importo_congelato,
history.custom_data,
history.timestamp_operazione,
history.timestamp_modifica,
history.utente_modifica,
history.id_calcolo_punti
-- @rownum := @rownum + 1 AS new_id_calcolo_punti
FROM consumer_fidelity_history history
INNER JOIN consumer_fidelity_calcolo_punti punti ON history.id_calcolo_punti = punti.id
WHERE history.tipo="LOYALTY_CARD_NEW" AND history.codice IN ('2130022634711','2130022908683','2130023758164', '2130023123047', '2130023269578')
;

-- mettere in una tabella temporante i due campi e fare poi il mapping (con la query sopra)
SET @rownum := 1062089;
SELECT punti.id, @rownum := @rownum + 1 AS id_calcolo_punti
FROM consumer_fidelity_calcolo_punti punti
INNER JOIN consumer_fidelity_history history ON history.id_calcolo_punti = punti.id
WHERE punti.tipo="LOYALTY_CARD_NEW" AND punti.codice IN ("2130022634711", "2130023758164",  "2130023123047",  "2130022908683", "2130022478926");



-- stampa delle colonne da usare
SELECT concat(concat('punti.', COLUMN_NAME), ',')
FROM information_schema.columns
WHERE  TABLE_NAME = 'consumer_fidelity_calcolo_punti';

-- stampa delle colonne da usare
SELECT concat(concat('history.', COLUMN_NAME), ',')
FROM information_schema.columns
WHERE  TABLE_NAME = 'consumer_fidelity_history';

-- reperimento di 4/5 fidelity
SELECT alfa.pk_consumer
FROM (
SELECT fid.tipo, fid.codice, fid.pk_consumer, punti.id AS id_calcolo_punti
FROM fid_prod fid
INNER JOIN consumer_fidelity_calcolo_punti punti ON fid.`codice` = punti.codice AND fid.`tipo` = punti.tipo
WHERE 1=1 AND fid.pk_consumer IN ('277956','1383033','2860008','252472','4709854')
) alfa
GROUP BY alfa.pk_consumer
HAVING count(alfa.codice) > 40 AND count(alfa.codice) < 45
ORDER BY count(alfa.pk_consumer) DESC;
