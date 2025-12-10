# COSA MANCA

-- non fare in prod --
INSERT INTO `ana_soggetti_negozi` (`id_soggetto`, `ubicazione_default`, `tipo_lettura_carico_default`, `distribuzione`, `stato_contabile`, `fatturazione_b2b_intermediari`, `default_shipping_packaging`, `dataora_modifica`, `utente_modifica`, `timedelta_utc`, `timezone`, `codice_esercente`, `id_soggetto_supervisor`, `abilitazione_scarico_promozionali`, `numero_vetrine`, `rsa`, `f_invio_mulesoft`, `dropship`, `negozio_conto_visione`)
VALUES
	(1395, NULL, '10', 'DIRECTED', 'Aperto', 0, NULL, '2022-05-19 08:00:23', 'bergonzinie', '', '', '', NULL, NULL, NULL, 0, 0, NULL, NULL);
-- non fare in prod --

INSERT INTO `pos_aliquote_iva` (`codice_proprietario`, `nazione`, `cod_negozio`, `target_type`, `target`, `iva`, `data_inizio_validita`, `data_fine_validita`, `modificato`)
VALUES
	('MMDE', 'SE', '', '', '', 25.00, '', '', current_timestamp);


INSERT INTO `pos_regole_catalogo` (`brand`, `nazione`, `anno`, `stagione`, `collezione`, `attivo`, `data_modifica`)
VALUES
	('MC', 'SE', '2021', '2', '', 1, '2021-05-03 12:02:53'),
	('MC', 'SE', '2022', '1', '', 1, '2021-11-08 14:14:15'),
	('MM', 'SE', '2021', '2', '', 1, '2021-04-14 15:23:25'),
	('MM', 'SE', '2022', '1', '', 1, '2021-11-15 13:29:33'),
	('MR', 'SE', '2021', '2', '', 1, '2021-05-03 11:59:28'),
	('MR', 'SE', '2022', '1', '', 1, '2021-10-18 14:07:30'),
	('PE', 'SE', '2021', '2', '', 1, '2021-05-03 11:59:28'),
	('PE', 'SE', '2022', '1', '', 1, '2021-10-18 14:07:30'),
	('SP', 'SE', '2021', '2', '', 1, '2021-04-14 15:23:25'),
	('SP', 'SE', '2022', '1', '', 1, '2021-11-15 13:29:33'),
	('WE', 'SE', '2021', '2', '', 1, '2021-04-14 15:23:25'),
	('WE', 'SE', '2022', '1', '', 1, '2021-11-15 13:29:33');


UPDATE pos_config_store
SET valore = 'MM,WE,SP'
WHERE negozio = '4901045' AND chiave = 'AVAILABLE_BRANDS';

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'CONNECTION_CHECK_TIMER', '30000', 'I', 2, 'Intervallo polling connection_status_check in millisecondi', '2022-01-11 14:09:44'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'CONNECTION_CHECK_TIMER', '30000', 'I', 2, 'Intervallo polling connection_status_check in millisecondi', '2022-01-11 14:09:44'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'CONNECTION_CHECK_TIMER', '30000', 'I', 2, 'Intervallo polling connection_status_check in millisecondi', '2022-01-11 14:09:44'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'CONNECTION_CHECK_TIMER', '600000', 'I', 2, 'Intervallo polling connection_status_check in millisecondi', '2022-01-11 14:09:44');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'SE', 'CURRENCY_CODE', 'SEK', 'S', 2, '', '2022-01-11 14:27:59');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'DATA_VISIBILITY_EXTENDED', '1', 'I', 2, 'Abilitazione visibilità estesa consumatrici', '2022-01-13 08:43:20'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'DATA_VISIBILITY_EXTENDED', '1', 'I', 2, 'Abilitazione visibilità estesa consumatrici', '2022-01-13 08:43:20'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'DATA_VISIBILITY_EXTENDED', '1', 'I', 2, 'Abilitazione visibilità estesa consumatrici', '2022-01-13 08:43:20'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'DATA_VISIBILITY_EXTENDED', '0', 'I', 2, 'Abilitazione visibilità estesa consumatrici', '2022-01-13 08:43:20');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'MAX_DISCOUNT_PERC', '50', 'I', 2, 'Percentuale massima di sconto applicabile in fase di vendita', '2014-02-10 18:08:42'),
       ('MMDE', '', 'HU', 'MAX_DISCOUNT_PERC', '50', 'I', 2, 'Percentuale massima di sconto applicabile in fase di vendita', '2014-02-10 18:08:42'),
       ('MMDE', '', 'AT', 'MAX_DISCOUNT_PERC', '50', 'I', 2, 'Percentuale massima di sconto applicabile in fase di vendita', '2014-02-10 18:08:42'),
       ('MMDE', '', 'SE', 'MAX_DISCOUNT_PERC', '99', 'I', 2, 'Percentuale massima di sconto applicabile in fase di vendita', '2014-02-10 18:08:42');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'MAX_MONEY_AMOUNT', '100000.00', 'F', 2, '', '2014-02-10 18:08:42'),
       ('MMDE', '', 'HU', 'MAX_MONEY_AMOUNT', '100000.00', 'F', 2, '', '2014-02-10 18:08:42'),
       ('MMDE', '', 'AT', 'MAX_MONEY_AMOUNT', '100000.00', 'F', 2, '', '2014-02-10 18:08:42'),
       ('MMDE', '', 'SE', 'MAX_MONEY_AMOUNT', '45000.00', 'F', 2, '', '2014-02-10 18:08:42');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'MAX_MONEY_AMOUNT_EXTRA_COUNTRY', '100000.00', 'F', 2, 'Massimo importo in contanti accettabile senza dati per Antiriciclaggio (stranieri)',
        '2020-01-09 14:08:32'),
       ('MMDE', '', 'HU', 'MAX_MONEY_AMOUNT_EXTRA_COUNTRY', '100000.00', 'F', 2, 'Massimo importo in contanti accettabile senza dati per Antiriciclaggio (stranieri)',
        '2020-01-09 14:08:32'),
       ('MMDE', '', 'AT', 'MAX_MONEY_AMOUNT_EXTRA_COUNTRY', '100000.00', 'F', 2, 'Massimo importo in contanti accettabile senza dati per Antiriciclaggio (stranieri)',
        '2020-01-09 14:08:32'),
       ('MMDE', '', 'SE', 'MAX_MONEY_AMOUNT_EXTRA_COUNTRY', '0', 'F', 2, 'Massimo importo in contanti accettabile senza dati per Antiriciclaggio (stranieri)',
        '2020-01-09 14:08:32');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'MAX_MONEY_AMOUNT_EXTRA_EUROPE_AML', '15000.00', 'F', 2, 'Massimo importo accettato in contanti per Antiriciclaggio Soggetti Extra-EU',
        '2015-02-19 10:55:41'),
       ('MMDE', '', 'HU', 'MAX_MONEY_AMOUNT_EXTRA_EUROPE_AML', '15000.00', 'F', 2, 'Massimo importo accettato in contanti per Antiriciclaggio Soggetti Extra-EU',
        '2015-02-19 10:55:41'),
       ('MMDE', '', 'AT', 'MAX_MONEY_AMOUNT_EXTRA_EUROPE_AML', '15000.00', 'F', 2, 'Massimo importo accettato in contanti per Antiriciclaggio Soggetti Extra-EU',
        '2015-02-19 10:55:41'),
       ('MMDE', '', 'SE', 'MAX_MONEY_AMOUNT_EXTRA_EUROPE_AML', '0', 'F', 2, 'Massimo importo accettato in contanti per Antiriciclaggio Soggetti Extra-EU', '2015-02-19 10:55:41');


INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'MENU_SELECTED_COLOR', '#111111', 'S', 2, '', '2014-03-12 16:44:59'),
       ('MMDE', '', 'HU', 'MENU_SELECTED_COLOR', '#111111', 'S', 2, '', '2014-03-12 16:44:59'),
       ('MMDE', '', 'AT', 'MENU_SELECTED_COLOR', '#111111', 'S', 2, '', '2014-03-12 16:44:59'),
       ('MMDE', '', 'SE', 'MENU_SELECTED_COLOR', '#000290', 'S', 2, '', '2014-03-12 16:44:59');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'POS_CONNECTED', '1', 'I', 2, 'Collegamento con terminale POS', '2016-12-12 11:31:34'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'POS_CONNECTED', '1', 'I', 2, 'Collegamento con terminale POS', '2016-12-12 11:31:34'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'POS_CONNECTED', '1', 'I', 2, 'Collegamento con terminale POS', '2016-12-12 11:31:34'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'POS_CONNECTED', '0', 'I', 2, 'Collegamento con terminale POS', '2016-12-12 11:31:34');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'POS_GT', 'NETS', 'I', 2, 'GT carte di credito in uso', '2017-05-24 14:23:30'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'POS_GT', 'NETS', 'I', 2, 'GT carte di credito in uso', '2017-05-24 14:23:30'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'POS_GT', 'NETS', 'I', 2, 'GT carte di credito in uso', '2017-05-24 14:23:30'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'POS_GT', 'OLD', 'I', 2, 'GT carte di credito in uso', '2017-05-24 14:23:30');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'De', 'SALE_INVOICE_AMB_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura Ambasciatori', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'SALE_INVOICE_AMB_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura Ambasciatori', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'SALE_INVOICE_AMB_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura Ambasciatori', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'SALE_INVOICE_AMB_ENABLED', '0', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura Ambasciatori', '2020-11-03 15:38:22');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'De', 'SALE_INVOICE_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'SALE_INVOICE_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'SALE_INVOICE_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'SALE_INVOICE_ENABLED', '0', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura', '2020-11-03 15:38:22');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'SALE_INVOICE_EU_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura UE', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'SALE_INVOICE_EU_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura UE', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'SALE_INVOICE_EU_ENABLED', '1', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura UE', '2020-11-03 15:38:22'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'SALE_INVOICE_EU_ENABLED', '0', 'S', 2, 'Abilitazione per chiudere le vendite con una Fattura UE', '2020-11-03 15:38:22');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'SCHEDULE_USAGE', '1', 'I', 2, 'gestione presenze', '2014-02-10 18:08:42'),
       ('MMDE', '', 'HU', 'SCHEDULE_USAGE', '1', 'I', 2, 'gestione presenze', '2014-02-10 18:08:42'),
       ('MMDE', '', 'AT', 'SCHEDULE_USAGE', '1', 'I', 2, 'gestione presenze', '2014-02-10 18:08:42'),
       ('MMDE', '', 'SE', 'SCHEDULE_USAGE', '2', 'I', 2, 'gestione presenze', '2014-02-10 18:08:42');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'SHOPPING_BAGS_COST', '0.0', 'F', 2, 'Costo Shopping bag', '2019-09-12 11:39:07'),
       ('MMDE', '', 'HU', 'SHOPPING_BAGS_COST', '0.0', 'F', 2, 'Costo Shopping bag', '2019-09-12 11:39:07'),
       ('MMDE', '', 'AT', 'SHOPPING_BAGS_COST', '0.0', 'F', 2, 'Costo Shopping bag', '2019-09-12 11:39:07'),
       ('MMDE', '', 'SE', 'SHOPPING_BAGS_COST', '0.5', 'F', 2, 'Costo Shopping bag', '2019-09-12 11:39:07');


INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'SHOPPING_BAGS_MODE', '', 'S', 2, 'Gestione shopping bags', '2019-09-12 11:38:57'),
       ('MMDE', '', 'HU', 'SHOPPING_BAGS_MODE', '', 'S', 2, 'Gestione shopping bags', '2019-09-12 11:38:57'),
       ('MMDE', '', 'AT', 'SHOPPING_BAGS_MODE', '', 'S', 2, 'Gestione shopping bags', '2019-09-12 11:38:57'),
       ('MMDE', '', 'SE', 'SHOPPING_BAGS_MODE', 'QUANTITY', 'S', 2, 'Gestione shopping bags', '2019-09-12 11:38:57');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'SHOW_DETAIL_CONSUMER', '2', 'I', 2, 'Modalità visualizzazione icona dettaglio storico acquisti consumatrice', '2022-03-01 10:54:46'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'SHOW_DETAIL_CONSUMER', '2', 'I', 2, 'Modalità visualizzazione icona dettaglio storico acquisti consumatrice', '2022-03-01 10:54:46'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'SHOW_DETAIL_CONSUMER', '2', 'I', 2, 'Modalità visualizzazione icona dettaglio storico acquisti consumatrice', '2022-03-01 10:54:46'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'SHOW_DETAIL_CONSUMER', '0', 'I', 2, 'Modalità visualizzazione icona dettaglio storico acquisti consumatrice', '2022-03-01 10:54:46');


INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'SOSPESI_CHECK_TIMER', '180000', 'I', 2, 'Intervallo polling check sospesi in millisecondi', '2020-12-15 16:07:00'),
       ('MMDE', '', 'HU', 'SOSPESI_CHECK_TIMER', '180000', 'I', 2, 'Intervallo polling check sospesi in millisecondi', '2020-12-15 16:07:00'),
       ('MMDE', '', 'AT', 'SOSPESI_CHECK_TIMER', '180000', 'I', 2, 'Intervallo polling check sospesi in millisecondi', '2020-12-15 16:07:00'),
       ('MMDE', '', 'SE', 'SOSPESI_CHECK_TIMER', '600000', 'I', 2, 'Intervallo polling check sospesi in millisecondi', '2020-12-15 16:07:00');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'STORE_CREDIT_DAYS', '180', 'I', 2, 'Giorni validita dei buoni emessi', '2014-02-10 18:08:42'),
       ('MMDE', '', 'HU', 'STORE_CREDIT_DAYS', '180', 'I', 2, 'Giorni validita dei buoni emessi', '2014-02-10 18:08:42'),
       ('MMDE', '', 'AT', 'STORE_CREDIT_DAYS', '180', 'I', 2, 'Giorni validita dei buoni emessi', '2014-02-10 18:08:42'),
       ('MMDE', '', 'SE', 'STORE_CREDIT_DAYS', '90', 'I', 2, 'Giorni validita dei buoni emessi', '2014-02-10 18:08:42');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'STORE_CREDIT_NUMBER', '1000', 'I', 1, 'Contatore buoni (ultimo buono emesso)', '2014-02-10 18:08:42'),
       ('MMDE', '', 'HU', 'STORE_CREDIT_NUMBER', '1000', 'I', 1, 'Contatore buoni (ultimo buono emesso)', '2014-02-10 18:08:42'),
       ('MMDE', '', 'AT', 'STORE_CREDIT_NUMBER', '1000', 'I', 1, 'Contatore buoni (ultimo buono emesso)', '2014-02-10 18:08:42'),
       ('MMDE', '', 'SE', 'STORE_CREDIT_NUMBER', '0', 'I', 1, 'Contatore buoni (ultimo buono emesso)', '2014-02-10 18:08:42');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'TAXFREE_MIN', '300000', 'F', 2, 'Minimo fatturabile', '2014-02-10 18:08:42'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'TAXFREE_MIN', '300000', 'F', 2, 'Minimo fatturabile', '2014-02-10 18:08:42'),
       ('MMDE', 'POSWEB_OFFLINE', 'At', 'TAXFREE_MIN', '300000', 'F', 2, 'Minimo fatturabile', '2014-02-10 18:08:42'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'TAXFREE_MIN', '99999999', 'F', 2, 'Minimo fatturabile', '2014-02-10 18:08:42');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'SE', 'DATE_FORMAT_CODE', 'EU', 'S', 2, '', '2022-01-11 11:28:33');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'SE', 'GUI_LANGUAGE', 'INGL', 'S', 2, '', '2022-01-11 11:31:30');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'SE', 'NUMBER_FORMAT_CODE', 'US', 'S', 2, '', '2022-01-11 14:29:59');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', 'POSWEB_OFFLINE', 'DE', 'POS_CONNECTION_TYPE', 'ECR37', 'I', 2, 'Tipo di comunicazione con il terminale POS', '2016-12-12 11:31:46'),
       ('MMDE', 'POSWEB_OFFLINE', 'HU', 'POS_CONNECTION_TYPE', 'ECR37', 'I', 2, 'Tipo di comunicazione con il terminale POS', '2016-12-12 11:31:46'),
       ('MMDE', 'POSWEB_OFFLINE', 'AT', 'POS_CONNECTION_TYPE', 'ECR37', 'I', 2, 'Tipo di comunicazione con il terminale POS', '2016-12-12 11:31:46'),
       ('MMDE', 'POSWEB_OFFLINE', 'SE', 'POS_CONNECTION_TYPE', '', 'I', 2, 'Tipo di comunicazione con il terminale POS', '2016-12-12 11:31:46');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'DE', 'POS_TERMINAL_TYPE', 'INGENICO', 'S', 2, 'Tipo POS', '2014-02-10 18:08:42'),
       ('MMDE', '', 'HU', 'POS_TERMINAL_TYPE', 'INGENICO', 'S', 2, 'Tipo POS', '2014-02-10 18:08:42'),
       ('MMDE', '', 'AT', 'POS_TERMINAL_TYPE', 'INGENICO', 'S', 2, 'Tipo POS', '2014-02-10 18:08:42'),
       ('MMDE', '', 'SE', 'POS_TERMINAL_TYPE', '', 'S', 2, 'Tipo POS', '2014-02-10 18:08:42');

INSERT INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES ('MMDE', '', 'SE', 'PRINT_LANGUAGE', 'UNGH', 'S', 2, '', '2022-01-11 14:30:31');

-- RECUPERARE SCONTRINO AU
