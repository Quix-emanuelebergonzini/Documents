resource.type="k8s_container"
resource.labels.cluster_name="gke-milan"
resource.labels.container_name="runtime"
resource.labels.namespace_name="possedemn-prod"
"iva_corretta"


https://itmn.bms.maxmara.com/?module=afc.frontend.actions.corrispettivi_new&program=controller


-- PossedeMN
SELECT * FROM pos_movimentazioni  WHERE anno_transazione='2024' AND cod_negozio='0100112' AND data_documento='20241009' AND numero_documento IN ('4129');
SELECT * FROM pos_movimenti_contabilita  WHERE anno_transazione='2024' AND cod_negozio='0100112' AND id_transazione=260173; 
SELECT * FROM pos_movimenti_capi WHERE anno_transazione='2024' AND cod_negozio='0100112' AND id_transazione=260173;
-- 2 capi da 99 + 2 capi da 119 = 436
-- coupon per 68 euro di sconto (ma guardando in dati_operazione, la somma è solo di 66)
-- 2 sartorie da 2 euro su 2 capi diversi e con causali/note diverse
-- totale = pagamento = 372
-- ma su dati_documenti di pos_movimentazioni le somme non tornano


-- Corrispettivi
SELECT pm.*, '||', cp.*, '||', c.*, '||', ct.*,'||', t.*  
FROM pos_movimentazioni pm
LEFT JOIN `bmsstd_magnum_contabilizzatore_pos` cp ON cp.`cod_negozio`=pm.cod_negozio AND cp.`id_transazione_pos`=pm.id_transazione AND pm.anno_transazione=cp.anno
LEFT JOIN `bmsstd_magnum_contabilizzatore` c USING(id_contabilizzatore)
LEFT JOIN `bmsstd_magnum_content` ct USING(`id_contabilizzatore`)
LEFT JOIN `bmsstd_magnum_transaction` t  USING(id_content)
WHERE pm.id_transazione = '260173' AND pm.`cod_negozio` = '0100112' AND pm.anno_transazione= '2024'
-- oppure file_name in (?)
;


QUANDO LA SQUADRATURA IVA si crea il log sopra ricercabile e poi bisogna cambiare nel dettaglio iva di una movimentazione
iva di un capo (non adeguare il totale) con la differenza che c'è tra iva_corretta e iva_modelli.
in pratica iva_corretta è quella che viene dai capi e iva_modelli quella che afc ricalcola.