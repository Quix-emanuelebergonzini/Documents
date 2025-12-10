se voglio che il mio posweb comunichi:

OM DOCKER
REPLACE INTO connection_parameter VALUES('3201034','ws_om','connection_timeout','60','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_om','enable_compression','0','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_om','http_proxy','','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_om','password','a166c0d011def85f2e','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_om','req_content_type','application/json','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_om','req_type','PASSWORD','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_om','url','https://localhost:4443/','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_om','username','ws_om_pos','2016-05-18 17:55:50');

CRM ONLINE
works on dos-mm-au
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','connection_timeout','60','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','enable_compression','0','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','http_proxy','','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','password','25CC.sdc4t-cx#zcb15p','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','req_content_type','application/json','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','req_type','BASIC','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','url','http://crm-dev-ws.mmfg.it/api/','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('3201034','ws_crm','username','pos','2016-05-18 17:55:50');


MIO MAC CON CRM (SSL expired...c'è da capire...)
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','connection_timeout','60','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','enable_compression','0','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','http_proxy','','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','password','25CC.sdc4t-cx#zcb15p','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','req_content_type','application/json','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','req_type','BASIC','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','url','https://gw.ws.mmfg.it/crmws-t/api/','2016-05-18 17:55:50');
REPLACE INTO connection_parameter VALUES('0100083','ws_crm','username','pos','2016-05-18 17:55:50');
REPLACE INTO `connection_parameter` (`cod_negozio`, `key_group`, `key_name`, `key_value`, `data_modifica`)
VALUES
   ('0100083', 'ws_crm', 'client_cert', '{POSWEB_ROOT_DIR}/var/cert/cert_posweb_crm.crt', '2020-09-17 09:27:53'),
   ('0100083', 'ws_crm', 'client_cert_value', '-----BEGIN CERTIFICATE-----' || char(10) || 'MIIG4jCCBMqgAwIBAgICAJcwDQYJKoZIhvcNAQELBQAwgZsxCzAJBgNVBAYTAklU' || char(10) || 'MQ4wDAYDVQQIEwVJdGFseTEWMBQGA1UEBxMNUmVnZ2lvIEVtaWxpYTEfMB0GA1UE' || char(10) || 'ChMWTWF4IE1hcmEgRmFzaGlvbiBHcm91cDERMA8GA1UECxMIUkQgRGVwdC4xFDAS' || char(10) || 'BgNVBAMTC01NRkcgV0VCIENBMRowGAYJKoZIhvcNAQkBFgtub2NAbW1mZy5pdDAe' || char(10) || 'Fw0yMTA3MDExMTIzMjlaFw0yNDA2MzAxMTIzMjlaMIGkMQswCQYDVQQGEwJJVDEO' || char(10) || 'MAwGA1UECBMFSXRhbHkxFjAUBgNVBAcTDVJlZ2dpbyBFbWlsaWExHzAdBgNVBAoT' || char(10) || 'Fk1heCBNYXJhIEZhc2hpb24gR3JvdXAxETAPBgNVBAsTCFJEIERlcHQuMR0wGwYD' || char(10) || 'VQQDFBRjZXJ0X3Bvc3dlYl9jcm1fdGVzdDEaMBgGCSqGSIb3DQEJARYLbm9jQG1t' || char(10) || 'ZmcuaXQwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDGGe29N0qATtRq' || char(10) || 'TieR7kVtqACuO3vvLgmG8gIN2wl8HgyQNpLQL3VnujxYqd7iCO+TH0h7ZDLVEkQ6' || char(10) || '5N44o3JdA05jscKaJ6kQv7ockdPtns6PYYmjaTxckYD6YItcQ6YfJUcYuGYmQliW' || char(10) || 'T0GBu1foW0xihqX7C2dcATUmAC4P6uOJ7nTtweag9UDizQyzGt6BoZLDI1iOPTNu' || char(10) || 'dAGdcO09qVAPjAu8Kv5e6fTfURvj76G/5rXeH+GJ9dnXMA2jk3qWCZVnz5sU/upp' || char(10) || 'QCDBLcoKdS2MFFcnnOUlVcwHABxtxu9oBabD9Ad4DlXEcRJxRRpVV7AUNKcrTv5r' || char(10) || 'tUYCuDzUAaZfcmu0OIZdDHNs+WUpJqTrIutJwvChYjLG4PPeopasDn2eUl5dV9qg' || char(10) || 'N6Ke/oO7Nr/e1uHC0883FighbcOkVayq2O5k0vG22POSnIcV+A5UFybEJXEeQBF3' || char(10) || '6TbVGfmYoIL72r27fmauylNomBKgWyaLwgiu571KsOpUbGpe94nZo3acrxK/33Ny' || char(10) || 'Mlpu86gCOS8nVIZ1p5tMjvO9dFcAMFwXRBsb0YxzoVYkWR/OkesbRjk4YH2SChrB' || char(10) || 'uPbTVtAZaxgZjuedInhN3A9QxFsa9hjFxZQHMRZq4z6snlU0ZFra5NsjcMzqIum3' || char(10) || 'rg3F/Zun4LAanx8TYH6tiyz9lYv1vwIDAQABo4IBIzCCAR8wCQYDVR0TBAIwADAd' || char(10) || 'BgNVHQ4EFgQUAydI/91wHJRhaC7nerMKw1p+h8QwgdAGA1UdIwSByDCBxYAUF1Xo' || char(10) || 'OwQl8ylWWFo8ULbFVDh3hLOhgamkgaYwgaMxCzAJBgNVBAYTAklUMQ4wDAYDVQQI' || char(10) || 'EwVJdGFseTEWMBQGA1UEBxMNUmVnZ2lvIEVtaWxpYTEfMB0GA1UEChMWTWF4IE1h' || char(10) || 'cmEgRmFzaGlvbiBHcm91cDERMA8GA1UECxMIUkQgRGVwdC4xHDAaBgNVBAMTE01N' || char(10) || 'RkcgV0VCIENBIFJPT1QgRzIxGjAYBgkqhkiG9w0BCQEWC25vY0BtbWZnLml0ggEC' || char(10) || 'MAsGA1UdDwQEAwIFoDATBgNVHSUEDDAKBggrBgEFBQcDAjANBgkqhkiG9w0BAQsF' || char(10) || 'AAOCAgEAUqDsyf+arhftTHvI7AAQ0DblhdY4ffsNvkvQTDJMcqCnsEJjjvcJv+BL' || char(10) || 'cViRjw14JD4P8FtTAAkoPlxmETLjFj3NoVDw8gXlJLlfyQg5kgfZYztNCEPHV68w' || char(10) || 'U/94Ky0aQ26QhvO9sf3At+5tKTT/yUBONFAv2sDpRWztH23ris+wunZY9xLNioce' || char(10) || 'Utstu0WpynG3gO8dtt/vu4p1rfEch4GoF1xPoZCpowCAiZcoyoMqlME1zZVFqFDE' || char(10) || 'Ic91Ei9etQqfnVvV0mMuhZqnjYwMsaOakyf3ChXKCsYOUBfTfuAPEMLR2tIsfKsn' || char(10) || 'qJ7Y7sTajyZQCI2xzR8mvXdOCz6uQWwSTxMZY4ahCBl98MbEDy4KK9lZybUo/2Er' || char(10) || 'BrlBMYt8jKVt+9XBDn4nz49iVXgU7i32ITNW0wdvqd+ONXp4RSsShr2QHE2g0XQR' || char(10) || 'WNPzGTFBzdYXKe3HR2gIGywcd30/WXioXXlZtMAeNLrxI5Y7u9hHdThRiT0LfXm6' || char(10) || 'DlujTG8t1bVnQZ1P0C9ZCssJFWB/Pam0LaeoGmbNtay2RwUGW+ZgbGy9SdNQbEeJ' || char(10) || '0IjQM4ssYN/5KetcFxN1516lRzPJqfz6kg1Y2FwCvMtH/H8HmlwMEb7LdVHqPst2' || char(10) || 'phBHzbSJj5mQwRyxRDYiG/2glv3ARaWG+UzQ1jgT8e+APN/Vjv8=' || char(10) || '-----END CERTIFICATE-----', '2020-09-17 09:27:53'),
   ('0100083', 'ws_crm', 'client_key', '{POSWEB_ROOT_DIR}/var/cert/cert_posweb_crm.key', '2020-09-17 09:27:53');
   ('0100083', 'ws_crm', 'client_key_value', '-----BEGIN RSA PRIVATE KEY-----' || char(10) || 'MIIJKQIBAAKCAgEAxhntvTdKgE7Uak4nke5FbagArjt77y4JhvICDdsJfB4MkDaS' || char(10) || '0C91Z7o8WKne4gjvkx9Ie2Qy1RJEOuTeOKNyXQNOY7HCmiepEL+6HJHT7Z7Oj2GJ' || char(10) || 'o2k8XJGA+mCLXEOmHyVHGLhmJkJYlk9BgbtX6FtMYoal+wtnXAE1JgAuD+rjie50' || char(10) || '7cHmoPVA4s0MsxregaGSwyNYjj0zbnQBnXDtPalQD4wLvCr+Xun031Eb4++hv+a1' || char(10) || '3h/hifXZ1zANo5N6lgmVZ8+bFP7qaUAgwS3KCnUtjBRXJ5zlJVXMBwAcbcbvaAWm' || char(10) || 'w/QHeA5VxHEScUUaVVewFDSnK07+a7VGArg81AGmX3JrtDiGXQxzbPllKSak6yLr' || char(10) || 'ScLwoWIyxuDz3qKWrA59nlJeXVfaoDeinv6Duza/3tbhwtPPNxYoIW3DpFWsqtju' || char(10) || 'ZNLxttjzkpyHFfgOVBcmxCVxHkARd+k21Rn5mKCC+9q9u35mrspTaJgSoFsmi8II' || char(10) || 'rue9SrDqVGxqXveJ2aN2nK8Sv99zcjJabvOoAjkvJ1SGdaebTI7zvXRXADBcF0Qb' || char(10) || 'G9GMc6FWJFkfzpHrG0Y5OGB9kgoawbj201bQGWsYGY7nnSJ4TdwPUMRbGvYYxcWU' || char(10) || 'BzEWauM+rJ5VNGRa2uTbI3DM6iLpt64Nxf2bp+CwGp8fE2B+rYss/ZWL9b8CAwEA' || char(10) || 'AQKCAgEAxfoztd4D/qbJclQZB6ZwjF5SD84y1Z3Ut6A0nVRB7mC5fYaMwrIrSza8' || char(10) || 'CH/71znG8+lXrrk8c+SFe7Yuv7vZF0uuk8ObECSCudJiVRsICXmkRXbc7wrE4F4p' || char(10) || '4A+MNvEEnCvNGc9vhtzXW6BpfxWTjQtxEyYtyu5ipXgvfYLAhffg3oAJK3OU4Vc5' || char(10) || 'OXBjOLupkzO+UHaKkdxoAgK9enLZJb6H3IHBWJQ/EuwNZQDSNsHNjNMs/oguBopE' || char(10) || '4uGLP+arpDZ/sfewrRL1gaotEeKJAFqK4muRjm0mNGHCPVzHDI67w+GiAENpE3qA' || char(10) || 'DIpUPA8reg7gUdEtIAMaENpg1Wb6ocFOS9IO4NqkVFG8Dmd7HGph906XpaUVpT1i' || char(10) || 'SUJSOZ/U2It6UqzsgF5Imsg412TvzVw3Se1mYEeC6CA/5zdD6wcJ61tnzyF8Oppx' || char(10) || 'eyU0sOV+B4f7b6i5tySVDLfMWUcYox5mFv311TuzADO027Pc8IQbxvtku1ZBAkyG' || char(10) || '8bEDNo5zvwNbP63XZtFDgCNIbCb+BgG2yuW3Hi66jXzqeKerPK17JnqO5SQjIUCB' || char(10) || 'UntQdkMSww0irtETQqHP3SsyLKiGQB8ZXcKF0u3+uOnDsUYCaDaJltDOjbjrOITA' || char(10) || 'nTJnVFMromXfqhtEgHtxBtfusZ4kS/hWyPQPyAyTFu5L1jTM2MECggEBAPoJVJEg' || char(10) || 'dliXCKvyUuX1QDInmwPZj1+ajl1eC0h1VzR/7595pcnJ7eONjYYEO2XFEUXdWIvl' || char(10) || 'E1IsexJ8YpUqRZHWsmUSJnJOK/O/cZqCTTzhki4AbLGEsBUEVQZs1+vado4FIajs' || char(10) || '+/kknHSUf42yxjhw0F3EhOmSNa5sFHaWZoqlDxYWUpg4Rlulwkh/MGzKGsC4LBIB' || char(10) || 'L0GVST6XeyA0uTzitRkhWG8meeFxhN3ltMKMBLxplsNA/DiVHwlp8NJVtdZdnNJe' || char(10) || 'Lg5SJBzZ65LtY94MMSe+CL6nQJBuFckmIE50uENB/Hy0c7F2Az/Tdkn7DP61WT/5' || char(10) || 'Uw+kJfbBhdb3JvMCggEBAMrTfkL3zezsLOxGkMpy/Yo2U1cDg+4YdxFvLRWemH6y' || char(10) || '3HOx1YvdxZ76xMSdu+DCuEcbWQc5y2AaTw99kCoi+fkhWdXAX3yEifZiurNYp7vV' || char(10) || '71I7yynXewbDRgtvRe4LNL5fgA+ulv1km9SFqK+ZBrCfnNhSlYP7pQt2aIQ1UBDs' || char(10) || 'HjtZNfKdu11tX3aAqPAUKvNFXuWUvOqyAfiumZ+iLpbzGTnet3WAsIjRcX9nz2A0' || char(10) || 'scor9BZdbz5sJ7lHD8DY6bRV8CqvD4FllL9w03Dz9djo6bC7k8pL82JB3pVglReO' || char(10) || 'b1wUOjQr3bmleewgchwrBmYkpqAfKy0x0baeCyT5wQUCggEBAJ0xlHsQ/5Y+jfMc' || char(10) || 'C8YK4+skPy6ybpLaZjqIz2skakjVTd7i6bntO6Pd8GWa74TR2kQkHnEE+Zql4FIE' || char(10) || '5S2GP+qqIcmtGYKvZq59Y3ySAuENp4tINQ19r/3mlVXOxAjBddtfmoPLSbaer8YT' || char(10) || 'PgXlqPz+3+CzliQKCbm4tTzA3YK4tr1aF18fsgwYMAbH/7fFcABNSVegawc+RagW' || char(10) || 'MBBVVUfT96ru7dwjQmjbp36h1Xyh7rBNab0jc+5WwgZ3FjIGNKWqgNc44peaSJ3i' || char(10) || '21mp6SlGXPjxXioOmGa07vlhANqSQu315Di6cinVWcGcvjdQoCDZ/lxb8T5aIov5' || char(10) || 'qp01EMUCggEAUAnhu3+ajbItkBfQr3NtRgtmG+JRP7X71q9utSdeujDO+gDlakpb' || char(10) || '3/7Jg2VTbMCqg7TxDv7pmMUJCe3c5CPlTUCx+L3vcG3FG6ueTYPgvSkRRfw+kgZs' || char(10) || 'kCCjFYQVrnhRmgaJvKaDAv+e1uDfzluu3ig+dscwJWM6oClb2UBIlkT3MShlN5az' || char(10) || 'B41PrK3c/NCYmmN3rVVir6MLUB1mli4kAIFyJPoUn5PnFjbAeSx4E1j4B/YMXn8E' || char(10) || 'lTeM/XpjZxCyOO3o1o86qS9y4ZEef2ZmT/Cpt4puKdiK9O1VbtEsRJ16qHV6+neN' || char(10) || 'CeOZF2s+XItF/SzdbDagjTcpsMzxTOgaGQKCAQBMNrWZzVQh4NbeHEHTggRLB0a+' || char(10) || 'Jt8d8A0OqwtJWbUem3XBrG+z/ua0mETncdqvgVLV+b/PJL+uanLisJU9xDz4IGtB' || char(10) || '5JyHTIrW7l49OlWF+/W+PLuTZiW3MF1sV19CZ/Sn4n19meb2OkcjIUeid/cgmIbR' || char(10) || 'J4Xup/8QhRgAil7FKA/RboSiiN5MORbcD1Pw0M/dq2QPXENykvYNzbt9EzY26YkI' || char(10) || 'GKOd1mgxJNSi30Bc9VT+TtjeiApTQ2AVWOk0hciRUiXodBJ8jS4/k20tYGG9/IQC' || char(10) || 'SZkk/PudON24ORh+sQaEZr3F2AZYAQnBQRDvRcSMf9j6RI6rhdNol491lmrT' || char(10) || '-----END RSA PRIVATE KEY-----', '2020-09-17 09:27:53');

ULTIMO MA NON MENO IMPORTANTE:
SE ANCORA NON VA METTERE IL VALORE DEL CRT NEL CERTIFICATO
DENTRO A POSWEB in var/cert/cert_posweb_crm.crt
OLTRE CHE A METTERE IL VALORE DEL KEY NEL CERTIFICATO
DENTRO A POSWEB in var/cert/cert_posweb_crm.key

-- potrebbe esssere bene far partire lo scheduler di posweb per aggionrare
i certificati --

NOTE:

ws_crm diretto (con http_proxy): http://crm-dev-ws.mmfg.it/api/

valori per i proxy:
http://proxys.mmfg.it:8080
http://proxy3.mmfg.it:9000
