SELECT
	pc.cod_negozio AS codice,
	asm.nome AS negozio,
	pc.data_chiusura AS data_chiusura_cassa,
	JSON_UNQUOTE(json_extract(pc.dati, '$.initial_total_amount')) as saldo_cassa_iniziale,
	IF(contanti.tot IS NULL, 0.00, contanti.tot) AS contante_incassato_vendite,
	IF(contanti3.tot IS NULL, 0.00, contanti3.tot) AS contante_incassato_sospesi,
	(IF(assegni.tot IS NULL, 0.00, assegni.tot) + IF(assegni2.tot IS NULL, 0.00, assegni2.tot)) AS assegni_incassati,
	IF(versamenti.tot IS NULL, 0.00, versamenti.tot) AS versamenti,
	IF(acconti.tot is null, 0.00, acconti.tot) as acconti,
	IF(petty_cash_old.tot IS NULL, 0.00, petty_cash_old.tot)+IF(petty_cash_new.tot IS NULL, 0.00, petty_cash_new.tot) AS petty_cash,
	JSON_UNQUOTE(json_extract(pc.dati, '$.store_balance')) as saldo,
	'' AS start_date,
	'' AS end_date
FROM
	pos_chiusura pc
	JOIN ana_soggetti_master asm ON (pc.cod_negozio=asm.codice_gruppo)
	LEFT JOIN pos_movimentazioni t ON (t.cod_negozio=pc.cod_negozio AND t.data_documento=pc.data_chiusura)
	LEFT JOIN (SELECT
			t.cod_negozio,
			t.data_documento,
			SUM(coco.importo_finale) AS tot
		FROM
			pos_movimentazioni t
			JOIN pos_movimenti_contabilita coco ON (t.anno_transazione=coco.anno_transazione AND t.id_transazione=coco.id_transazione AND t.cod_negozio=coco.cod_negozio AND coco.cod_operazione='CONTANTI')
		WHERE
			t.cod_negozio=:VARLIMIT_codice
			and t.data_documento>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
			and t.data_documento<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
			and t.anno_transazione>=DATE_FORMAT(:PARLIMIT_start_date,"%Y")
			and t.anno_transazione<=DATE_FORMAT(:PARLIMIT_end_date,"%Y")
			and coco.codice_movimento!='CONTABILITA_PREPAGAMENTO'
			AND t.codice_stato NOT IN  ('VOIDED', 'REPLACED')
			and substr(substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)), LOCATE('"payment_date":',substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)))+17 , LOCATE('"', substr(substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)), LOCATE('"payment_date":',substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)))+17) )-1)=t.data_documento
		GROUP BY t.cod_negozio, t.data_documento) AS contanti ON (pc.data_chiusura=contanti.data_documento AND pc.cod_negozio=contanti.cod_negozio)
	LEFT JOIN (SELECT
			cod_negozio,
			data_pagamento AS data_documento,
			-SUM(importo) AS tot
		FROM
			pos_store_sospesi_contabilita
		WHERE
			cod_negozio=:VARLIMIT_codice
			and data_pagamento>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
			and data_pagamento<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
			and anno_transazione>=DATE_FORMAT(:PARLIMIT_start_date,"%Y")
			and anno_transazione<=DATE_FORMAT(:PARLIMIT_end_date,"%Y")
			and cod_operazione='CONTANTI'
			and sistema NOT IN ('SEDE')
		GROUP BY cod_negozio, data_pagamento) AS contanti3 ON (pc.data_chiusura=contanti3.data_documento AND pc.cod_negozio=contanti3.cod_negozio)
	LEFT JOIN (SELECT
			t.cod_negozio,
			t.data_documento,
			SUM(coas.importo_finale) AS tot
		FROM
			pos_movimentazioni t
			JOIN pos_movimenti_contabilita coas ON (t.anno_transazione=coas.anno_transazione AND t.id_transazione=coas.id_transazione AND t.cod_negozio=coas.cod_negozio AND coas.cod_operazione='ASSEGNI')
		WHERE
			t.cod_negozio=:VARLIMIT_codice
			and t.data_documento>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
			and t.data_documento<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
			and t.anno_transazione>=DATE_FORMAT(:PARLIMIT_start_date,"%Y")
			and t.anno_transazione<=DATE_FORMAT(:PARLIMIT_end_date,"%Y")
		GROUP BY t.cod_negozio, t.data_documento) AS assegni ON (pc.data_chiusura=assegni.data_documento AND pc.cod_negozio=assegni.cod_negozio)
	LEFT JOIN (SELECT
			cod_negozio,
			data_pagamento as data_documento,
			SUM(importo) as tot
 		FROM
 			pos_pagamenti
 		WHERE
 			cod_operazione='ASSEGNI'
 			AND cod_negozio=:VARLIMIT_codice
 			AND data_pagamento>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
 			AND data_pagamento<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
 			AND anno_transazione>=DATE_FORMAT(:PARLIMIT_start_date,"%Y")
 			AND anno_transazione<=DATE_FORMAT(:PARLIMIT_end_date,"%Y")
 		GROUP BY cod_negozio, data_pagamento) AS assegni2 ON (pc.data_chiusura=assegni2.data_documento AND pc.cod_negozio=assegni2.cod_negozio)
	LEFT JOIN (SELECT
 			cod_negozio,
 			data_documento,
			SUM(importo) AS tot
		FROM
			pos_versamenti
		WHERE
			cod_negozio=:VARLIMIT_codice
			and data_documento>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
			and data_documento<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
		GROUP BY cod_negozio, data_documento) AS versamenti ON (pc.cod_negozio=versamenti.cod_negozio AND pc.data_chiusura=versamenti.data_documento)
	LEFT JOIN (SELECT
			cod_negozio,
			data_documento,
			SUM(importo) AS tot
		FROM
			pos_reintegri
		WHERE
			cod_negozio=:VARLIMIT_codice
			and data_documento>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
			and data_documento<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
		GROUP BY cod_negozio, data_documento) AS petty_cash_old ON (pc.cod_negozio=petty_cash_old.cod_negozio AND pc.data_chiusura=petty_cash_old.data_documento)
	LEFT JOIN (SELECT
			cod_negozio,
			data_documento,
			SUM(importo) AS tot
		FROM
			pos_petty_cash
		WHERE
			cod_negozio=:VARLIMIT_codice
			and data_documento>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
			and data_documento<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
		GROUP BY cod_negozio, data_documento) AS petty_cash_new ON (pc.cod_negozio=petty_cash_new.cod_negozio AND pc.data_chiusura=petty_cash_new.data_documento)
	LEFT JOIN (SELECT
			cod_negozio,
			substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17 , LOCATE('"', substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17) )-1) as data_documento,
			SUM(pmc.importo_finale) as tot
		from
			pos_movimenti_contabilita pmc
			left join pos_movimentazioni pm using (anno_transazione, id_transazione, cod_negozio)
		where
			pmc.codice_movimento IN('CONTABILITA_PREPAGAMENTO', 'CONTABILITA_PAGAMENTO')
			and pmc.cod_operazione IN('CONTANTI', 'ASSEGNI')
			and pmc.dati_operazione !=''
			AND pm.codice_stato IN ('FINALIZED','VOIDED')
			and pm.anno_transazione= DATE_FORMAT(:PARLIMIT_start_date,"%Y")
			and substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17 , LOCATE('"', substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17) )-1)!=pm.data_documento
			and substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17 , LOCATE('"', substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17) )-1)>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
			and substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17 , LOCATE('"', substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17) )-1)<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
			and cod_negozio=:VARLIMIT_codice
		group by
			1,2) as acconti on (pc.cod_negozio = acconti.cod_negozio and pc.data_chiusura = acconti.data_documento)
WHERE
	pc.cod_negozio=:VARLIMIT_codice
	and pc.data_chiusura>=DATE_FORMAT(:PARLIMIT_start_date,"%Y%m%d")
	and pc.data_chiusura<=DATE_FORMAT(:PARLIMIT_end_date,"%Y%m%d")
GROUP BY pc.cod_negozio, pc.data_chiusura


--------------------------

SELECT
	pc.cod_negozio AS codice,
	asm.nome AS negozio,
	pc.data_chiusura AS data_chiusura_cassa,
	JSON_UNQUOTE(json_extract(pc.dati, '$.store_balance')) AS saldo
FROM
	pos_chiusura pc
	JOIN ana_soggetti_master asm ON (pc.cod_negozio=asm.codice_gruppo)
	LEFT JOIN pos_movimentazioni t ON (t.cod_negozio=pc.cod_negozio AND t.data_documento=pc.data_chiusura)
	LEFT JOIN (SELECT
			t.cod_negozio,
			t.data_documento,
			SUM(coco.importo_finale) AS tot
		FROM
			pos_movimentazioni t
			JOIN pos_movimenti_contabilita coco ON (t.anno_transazione=coco.anno_transazione AND t.id_transazione=coco.id_transazione AND t.cod_negozio=coco.cod_negozio AND coco.cod_operazione='CONTANTI')
		WHERE
			t.cod_negozio='0100018'
			AND t.data_documento>='20210821'
			AND t.data_documento<='20210821'
			AND t.anno_transazione>='2021'
			AND t.anno_transazione<='2021'
			AND coco.codice_movimento!='CONTABILITA_PREPAGAMENTO'
			AND t.codice_stato NOT IN  ('VOIDED', 'REPLACED')
			AND substr(substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)), LOCATE('"payment_date":',substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)))+17 , LOCATE('"', substr(substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)), LOCATE('"payment_date":',substr(coco.dati_operazione, LOCATE("payment_date",coco.dati_operazione)))+17) )-1)=t.data_documento
		GROUP BY t.cod_negozio, t.data_documento) AS contanti ON (pc.data_chiusura=contanti.data_documento AND pc.cod_negozio=contanti.cod_negozio)
	LEFT JOIN (SELECT
			cod_negozio,
			data_pagamento AS data_documento,
			-SUM(importo) AS tot
		FROM
			pos_store_sospesi_contabilita
		WHERE
			cod_negozio='0100018'
			AND data_pagamento>='20210821'
			AND data_pagamento<='20210821'
			AND anno_transazione>='2021'
			AND anno_transazione<='2021'
			AND cod_operazione='CONTANTI'
			AND sistema NOT IN ('SEDE')
		GROUP BY cod_negozio, data_pagamento) AS contanti3 ON (pc.data_chiusura=contanti3.data_documento AND pc.cod_negozio=contanti3.cod_negozio)
	LEFT JOIN (SELECT
			t.cod_negozio,
			t.data_documento,
			SUM(coas.importo_finale) AS tot
		FROM
			pos_movimentazioni t
			JOIN pos_movimenti_contabilita coas ON (t.anno_transazione=coas.anno_transazione AND t.id_transazione=coas.id_transazione AND t.cod_negozio=coas.cod_negozio AND coas.cod_operazione='ASSEGNI')
		WHERE
			t.cod_negozio='0100018'
			AND t.data_documento>='20210821'
			AND t.data_documento<='20210821'
			AND t.anno_transazione>='2021'
			AND t.anno_transazione<='2021'
		GROUP BY t.cod_negozio, t.data_documento) AS assegni ON (pc.data_chiusura=assegni.data_documento AND pc.cod_negozio=assegni.cod_negozio)
	LEFT JOIN (SELECT
			cod_negozio,
			data_pagamento AS data_documento,
			SUM(importo) AS tot
 		FROM
 			pos_pagamenti
 		WHERE
 			cod_operazione='ASSEGNI'
 			AND cod_negozio='0100026'
 			AND data_pagamento>='20210821'
 			AND data_pagamento<='20210821'
 			AND anno_transazione>='2021'
 			AND anno_transazione<='2021'
 		GROUP BY cod_negozio, data_pagamento) AS assegni2 ON (pc.data_chiusura=assegni2.data_documento AND pc.cod_negozio=assegni2.cod_negozio)
	LEFT JOIN (SELECT
 			cod_negozio,
 			data_documento,
			SUM(importo) AS tot
		FROM
			pos_versamenti
		WHERE
			cod_negozio='0100018'
			AND data_documento>='20210821'
			AND data_documento<='20210821'
		GROUP BY cod_negozio, data_documento) AS versamenti ON (pc.cod_negozio=versamenti.cod_negozio AND pc.data_chiusura=versamenti.data_documento)
	LEFT JOIN (SELECT
			cod_negozio,
			data_documento,
			SUM(importo) AS tot
		FROM
			pos_reintegri
		WHERE
			cod_negozio='0100018'
			AND data_documento>='20210821'
			AND data_documento<='20210821'
		GROUP BY cod_negozio, data_documento) AS petty_cash_old ON (pc.cod_negozio=petty_cash_old.cod_negozio AND pc.data_chiusura=petty_cash_old.data_documento)
	LEFT JOIN (SELECT
			cod_negozio,
			data_documento,
			SUM(importo) AS tot
		FROM
			pos_petty_cash
		WHERE
			cod_negozio='0100018'
			AND data_documento>='20210821'
			AND data_documento<='20210821'
		GROUP BY cod_negozio, data_documento) AS petty_cash_new ON (pc.cod_negozio=petty_cash_new.cod_negozio AND pc.data_chiusura=petty_cash_new.data_documento)
	LEFT JOIN (SELECT
			cod_negozio,
			substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17 , LOCATE('"', substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17) )-1) AS data_documento,
			SUM(pmc.importo_finale) AS tot
		FROM
			pos_movimenti_contabilita pmc
			LEFT JOIN pos_movimentazioni pm USING (anno_transazione, id_transazione, cod_negozio)
		WHERE
			pmc.codice_movimento IN('CONTABILITA_PREPAGAMENTO', 'CONTABILITA_PAGAMENTO')
			AND pmc.cod_operazione IN('CONTANTI', 'ASSEGNI')
			AND pmc.dati_operazione !=''
			AND pm.codice_stato IN ('FINALIZED','VOIDED', 'OPEN')
			AND pm.anno_transazione= '2021'
			AND substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17 , LOCATE('"', substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17) )-1)>='20210821'
			AND substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17 , LOCATE('"', substr(substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)), LOCATE('"payment_date":',substr(pmc.dati_operazione, LOCATE("payment_date",pmc.dati_operazione)))+17) )-1)<='20210821'
			AND cod_negozio='0100026'
		GROUP BY
			1,2) AS acconti ON (pc.cod_negozio = acconti.cod_negozio AND pc.data_chiusura = acconti.data_documento)
WHERE
	pc.cod_negozio='0100018'
	AND pc.data_chiusura>='20210821'
	AND pc.data_chiusura<='20210821'
GROUP BY pc.cod_negozio, pc.data_chiusura
;

SELECT pmc.*
FROM pos_movimentazioni
JOIN pos_movimenti_contabilita pmc USING(cod_negozio, anno_transazione, id_transazione)
WHERE cod_negozio = '0100018' AND anno_transazione = '2021' AND data_documento = '20210821'
ORDER BY id_transazione DESC
LIMIT 10;
