in
boss/bin/config/configmaps/wsclient.crm
sostituire con 

{"url": "https://mtls-ws-dev.crm.mmfg.it/", "http_proxy": "", "enable_compression": "0", "params": "{'module': 'crm_ws_server',\t'program': 'boss_interface'}", "req_type": "PASSWORD", "connection_timeout": "60", "server_ca_cert": "main/bin/config/configmaps/rootcert.pem", "client_cert": "guest/storebackoffice/bin/config/configmaps/gw_cert.crt", "client_key": "guest/storebackoffice/bin/config/secrets/gw_cert.key"}

I FILE VANNO DENTRO A boss/config