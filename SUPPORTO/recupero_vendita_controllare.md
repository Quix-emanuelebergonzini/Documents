--
SELECT *
FROM pos_movimentazioni
WHERE cod_negozio = '4401434' AND numero_documento = '632' AND anno_transazione = '2022';

SELECT *
FROM pos_movimenti_capi
WHERE id_transazione = '3487406' AND cod_negozio = '4401434';

SELECT *
FROM pos_movimenti_contabilita
WHERE id_transazione = '3487406' AND cod_negozio = '4401434';

SELECT *
FROM pos_import_spool
WHERE id_orig = '8572872';