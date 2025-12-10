
SET @cod_proprietario = 'MMAU';

INSERT INTO `pos_aliquote_iva` (`codice_proprietario`, `nazione`, `cod_negozio`, `target_type`, `target`, `iva`, `data_inizio_validita`, `data_fine_validita`, `modificato`)
VALUES
	(@cod_proprietario, 'NZ', '', '', '', 15.00, '', '', current_timestamp);

INSERT INTO `pos_regole_catalogo` (`brand`, `nazione`, `anno`, `stagione`, `collezione`, `attivo`, `data_modifica`)
VALUES
	('MM', 'NZ', '2023', '2', '', 1, current_timestamp),
	('SP', 'NZ', '2023', '2', '', 1, current_timestamp),
	('WE', 'NZ', '2023', '2', '', 1, current_timestamp);


-- ATTENZIONE: eliminare i record vecchi senza la specializzazione per tipologia_istanza o nazione se necessario
REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_proprietario, '', 'AU', 'GST_FREE_ALL_TRANSACTIONS_ENABLED', '0', 'I', 2, 'Abilitazione alla registrazione di transazioni SOLO con esenzione iva', current_timestamp),
       (@cod_proprietario, '', 'NZ', 'GST_FREE_ALL_TRANSACTIONS_ENABLED', '1', 'I', 2, 'Abilitazione alla registrazione di transazioni SOLO con esenzione iva', current_timestamp);

REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_proprietario, '', 'AU', 'GST_FREE_ENABLED', '0', 'I', 2, 'Abilitazione alla registrazione di transazioni con esenzione iva', current_timestamp),
       (@cod_proprietario, '', 'NZ', 'GST_FREE_ENABLED', '1', 'I', 2, 'Abilitazione alla registrazione di transazioni con esenzione iva', current_timestamp);

REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_proprietario, '', 'AU', 'MAX_DISCOUNT_PERC', '50', 'I', 2, 'Percentuale massima di sconto applicabile in fase di vendita', current_timestamp),
       (@cod_proprietario, '', 'NZ', 'MAX_DISCOUNT_PERC', '60', 'I', 2, 'Percentuale massima di sconto applicabile in fase di vendita', current_timestamp);

REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_proprietario, '', 'AU', 'PAYMENT_NUMBER', '0', 'I', 1, 'ultima boll. saldo/incasso', current_timestamp),
       (@cod_proprietario, '', 'NZ', 'PAYMENT_NUMBER', '90000', 'I', 1, 'ultima boll. saldo/incasso', current_timestamp);

REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_proprietario, '', 'AU', 'RETURNS_ENABLED', '1', 'I', 2, 'Abilitazione degli storni nella pagina delle vendite', current_timestamp),
       (@cod_proprietario, '', 'NZ', 'RETURNS_ENABLED', '0', 'I', 2, 'Abilitazione degli storni nella pagina delle vendite', current_timestamp);

REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_proprietario, 'POSWEB_OFFLINE', 'AU', 'STORE_CREDIT_USAGE', '1', 'I', 2, 'Flag utilizzo BUONO come forma di pagamento', current_timestamp),
       (@cod_proprietario, 'POSWEB_OFFLINE', 'NZ', 'STORE_CREDIT_USAGE', '0', 'I', 2, 'Flag utilizzo BUONO come forma di pagamento', current_timestamp);

REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `tipologia_istanza`, `nazione`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_proprietario, 'POSWEB_OFFLINE', 'AU', 'SARTORIE_ENABLED', '1', 'I', 2, 'Abilitazione vendita sartorie extra e su capo', current_timestamp),
       (@cod_proprietario, 'POSWEB_OFFLINE', 'NZ', 'SARTORIE_ENABLED', '0', 'I', 2, 'Abilitazione vendita sartorie extra e su capo', current_timestamp);

-- post installazione negozio
# UPDATE pos_config_store
# SET valore = 'MM,SP,WE'
# WHERE negozio = '3301016' AND chiave = 'AVAILABLE_BRANDS';