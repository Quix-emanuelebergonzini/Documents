SET @codice_propritario = 'MMJ';
SET @cod_installazione = '9000801999';
SET @cod_negozio = '0801999';

DELETE FROM pos_config_bundle
WHERE cod_installazione = @cod_installazione AND valore = @cod_negozio;

DELETE FROM pos_config_store
WHERE negozio = @cod_negozio AND codice_proprietario = @codice_propritario;

DELETE FROM pos_config_cash
WHERE negozio = @cod_negozio AND codice_proprietario = @codice_propritario
AND cod_cassa = '01';

DELETE FROM pos_users
WHERE cod_installazione = @cod_installazione;


