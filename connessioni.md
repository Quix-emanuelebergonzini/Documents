from config import ws_client

dir(ws_client)

ws_client.ws_config --> json di tutto il ws_client senza if o altri...

e si confronta con

cat main/bin/config/secret (o configmaps)/wsclient.XXX


>> from config import mysql
>> mysql.db_config