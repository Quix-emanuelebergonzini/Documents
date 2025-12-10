Sopra i 100000 fiorini ungheresi di IVA obbligo di CF

In ogni caso se è compilato deve essere validato con la regex \d{8}-\d-\d{2}
esempio:
12345678-8-89
10625790-4-44 (reale della Mol Group Ungheria but not works)
10625790-2-44 (works)

------------------------------------------------------------------------------------------------------------------------------------------------------------------
importare una vendita / capi / contabilita poi...

INSERT INTO pos_vat_notification (tipo, stato_invio, user_modifica, content) 
VALUES ("FATTURA_POS", 'TO_SEND', 'VatNotificationInsert', '\{\"cod_negozio\":\"0100051\",\"anno_transazione\":\"2025\",\"id_transazione\":\"124982\"}')

INSERT INTO `pos_vat_notification_movimentazioni` (`anno_transazione`, `id_transazione`, `cod_negozio`, `id_notifica`)
VALUES
	('2025', 7924, '0100051', 124982);

python guest/posws/script/job_vat_notifier.py -n HU -l 1 -d -s 0100051
dentro al docker usare print per il debug


INSERT INTO `parametri` (`tipo`, `chiave`, `valore`, `descrizione`, `upd_datetime`, `upd_user`)
VALUES
	('api_hu', 'data_attivazione_v2', '2020-04-01', 'data attivazione api v2 per fisco HU', '2020-01-20 16:00:00', 'bergonzinie');

INSERT INTO `parametri` (`tipo`, `chiave`, `valore`, `descrizione`, `upd_datetime`, `upd_user`)
VALUES
	('api_hu', 'api_version', 'v2', 'versione api per fisco HU', '2020-01-20 16:00:00', 'bergonzinie');


------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------
