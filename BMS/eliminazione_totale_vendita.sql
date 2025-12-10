SET @cod_negozio = "";
SET @anno_transazione = "";
SET @id_transazione = "";

SELECT id_capo FROM pos_movimenti_capi WHERE cod_negozio=@cod_negozio AND anno_transazione=@anno_transazione AND id_transazione=@id_transazione;

-- ATTENZIONE !!!!
-- controllare pos_movimenti_capi perché se id_capo è valorizzato
-- bisogna de-storicizzati i capi allineati alle vendite, quindi
-- passare ad OT-AFC la richiesta di sanificare la giacenza e cancellarli
-- dalla mov_capi. Poi c'è da annullare la vendita su EDW (operations)
-- https://maxmarafashiongroup.atlassian.net/wiki/spaces/KBOM/pages/3882749584/EDW+-+Cancellazioni+vendite+BMS

DELETE
m,
pos_movimenti_capi,
pos_movimenti_contabilita,
pos_store_credits,
pos_store_credits_contabilita,
pos_store_sospesi,
pos_store_sospesi_contabilita
FROM pos_movimentazioni m
LEFT JOIN pos_movimenti_capi USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimenti_contabilita USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimentazioni_custom USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimentazioni_custom_multi USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimentazioni_info_stampa USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimentazioni_relazioni USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimentazioni_split USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimenti_capi_split USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_movimenti_contabilita_split USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_store_credits USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_store_credits_contabilita USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_store_sospesi USING (cod_negozio, anno_transazione, id_transazione)
LEFT JOIN pos_store_sospesi_contabilita USING (cod_negozio, anno_transazione, id_transazione)
WHERE m.cod_negozio=@cod_negozio AND m.anno_transazione=@anno_transazione AND m.id_transazione=@id_transazione;