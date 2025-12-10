lista_cod_negozio = []

# TEST
# SET {url}='https://promo-test.mmfg.it';
# SET {url_admin}='https://promo-test-admin.mmfg.it';
# SET {username}='iOm3mbJBHZwQ8cCpMmz2syktYq4Ub4eF';
# SET {password}='VLuJvJnqqdx1yLSWXrvUHJ4PPu3cSPYk';

# PROD COMUNICATE DA VERROCCHIO NON TESTATE
url = "https://promo.mmfg.it";
url_admin = "https://promo-admin.mmfg.it";
username = "d5b1dbbddbd9479d89e7a454ba1bbec9";
password = "46bc4f79dfa2e4a720b1b247def5773e";

output = f"""

UPDATE pos_connection_parameter_default
SET key_value = '{username}'
WHERE key_group = 'ws_promo_engine_v2' and key_name = 'username';

UPDATE pos_connection_parameter_default
SET key_value = '{password}'
WHERE key_group = 'ws_promo_engine_v2' and key_name = 'password';

UPDATE pos_connection_parameter_default
SET key_value = 'OAUTH2'
WHERE key_group = 'ws_promo_engine_v2' and key_name = 'req_type';

UPDATE pos_connection_parameter_default
SET key_value = '{url_admin}'
WHERE key_group = 'ws_promo_engine_v2' and key_name = 'url';

INSERT INTO pos_connection_parameter_default (cod_proprietario, key_group, key_name, key_value)
VALUES (
    'FRH',
    'ws_promo_engine_v2',
    'req_type_config',
    '{{"login_service": "/oauth2/token",   
      "login_response_field": "access_token",
      "token_request_content_type": "application/json",
      "service_token_position": {{"HEADER": "Authorization"}},
      "db_name": "main",
      "db_rdbms": "sqlite",
      "db_query_foo": "backend.promo_engine.service.promo_token_query_execute"}}'
);
"""

print(output)
