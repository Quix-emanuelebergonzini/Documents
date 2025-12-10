su posweb immettere questa promo che si attiva su tutto e tutti di tipo GIFT

{"exclusivity": "CUMULABLE", "effect": { "type": "GIFT" }, "applicability": { "step": 5000, "type": "AMOUNT", "max": 5000, "min": 5000}}

sul negozio:

DELETE FROM promozioni WHERE 1;
REPLACE INTO promozioni (id, nome, descrizione, giorni_validita, regole_promo, attivo, tipologia) VALUES (7, 'test-gift', 'TEST GIFT', '1234567', '{"exclusivity": "CUMULABLE", "effect": { "type": "GIFT" }, "applicability": { "step": 5000, "type": "AMOUNT", "max": 5000, "min": 5000}}', 1, 'PROMO');

e posso testare...

vedi anche store_config---> OMAGGIO_B2E_ENABLED (attivo solo su hk)


== HK V2 ==
PROMO_ENGINE_ENABLED = 2
PROMO_ENGINE_PREVIEW_ENABLED = 1
PROMO_ENGINE_USER_SELECTION = 1

TEST ws_posweb / jn6Gzx8cQkX?3z3R%SNT

== LINMARA V2 ==
PROMO_ENGINE_ENABLED = 2
PROMO_ENGINE_PREVIEW_ENABLED = 1
PROMO_ENGINE_USER_SELECTION = 1

TEST ws_rule_engine / u2DcvtzVv7s+6=3JFEQL

backup linmara-uat (pos-uat) (da eliminare in futuro prossimo)
INSERT INTO `pos_connection_parameter_default` (`codice_proprietario`, `key_group`, `key_name`, `key_value`, `descrizione`, `data_modifica`)
VALUES
	('GDM', 'ws_promo_engine_v2', 'password', 'f9MQ3fxJmdMMPX8rBzCv', '', '2023-04-13 06:52:15'),
	('GDM', 'ws_promo_engine_v2', 'username', 'ws_posweb', '', '2023-04-13 06:52:15'),
	('GDM', 'ws_promo_engine_v2_admin', 'password', 'f9MQ3fxJmdMMPX8rBzCv', '', '2023-09-20 08:34:06'),
	('GDM', 'ws_promo_engine_v2_admin', 'username', 'ws_posweb', '', '2023-09-20 08:34:06');