# se vogliamo che quel negozio abbia le gift card in test (come ha in prod),
# occorre configurare correttamente i parametri:

# alzare tutti i flag di processo

REPLACE INTO `pos_config_store` (`codice_proprietario`, `negozio`, `chiave`, `valore`, `utente`, `modificato`)
VALUES
	('DT', '0100518', 'GIFT_CARD_ENABLED', '1', '', now()),
	('DT', '0100518', 'GIFT_CARD_MAX_AMOUNT', '2000', '', now()),
	('DT', '0100518', 'GIFT_CARD_MIN_AMOUNT', '25', '', now()),
	('DT', '0100518', 'GIFT_TAILORY_NUMBER', '0', '', now()),
	('DT', '0100518', 'GIFT_USAGE', '1', '', now());

# configurare i parametri di connessione, copiandoli da un altro negozio di test
# (non abbiamo le credenziali di test per tutti i negozi, quindi le cpiamo da uno già esistente.
# Questo significa che le GC sul portale test amilon risulteranno emesse dal codice negozio diverso,
# ma è tutto spiegabile non deve essere oggetto di verifica da parte degli utenti)

INSERT INTO `pos_connection_parameter` (`codice_proprietario`, `cod_negozio`, `key_group`, `key_name`, `key_value`, `descrizione`, `data_modifica`)
VALUES
	('DT', '0100518', 'ws_amilon', 'client_id', 'gcmwsuserinternalapi', '', now()),
	('DT', '0100518', 'ws_amilon', 'client_secret', 'cb8bf8ac1c', '', now()),
	('DT', '0100518', 'ws_amilon', 'http_proxy', '', '', now()),
	('DT', '0100518', 'ws_amilon', 'password', 'Catto0509!', '', now()),
	('DT', '0100518', 'ws_amilon', 'req_content_type', 'text/xml', '', now()),
	('DT', '0100518', 'ws_amilon', 'soap_debug', '1', '', now()),
	('DT', '0100518', 'ws_amilon', 'soap_version', '1.2', '', now()),
	('DT', '0100518', 'ws_amilon', 'url', 'https://gcmstg-web.amilon.eu/GCMWebApi', '', now()),
	('DT', '0100518', 'ws_amilon', 'url_auth', 'https://b2bstg-sso.amilon.eu', '', now()),
	('DT', '0100518', 'ws_amilon', 'username', 'dt0509', '', now());

# insegna in base allo STORE_SIGN dei negozi coinvolti
INSERT INTO `pos_tagli_gift_card` (`insegna`, `valore`, `descrizione`, `data_modifica`)
VALUES
	('PB', '0.00', '', current_timestamp),
	('PB', '50.00', '50', current_timestamp),
	('PB', '100.00', '100', current_timestamp),
	('PB', '150.00', '150', current_timestamp),
	('PB', '200.00', '200', current_timestamp);