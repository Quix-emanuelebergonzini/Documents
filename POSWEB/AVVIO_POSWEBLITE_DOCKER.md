https://drive.google.com/drive/folders/1xqn6rlKNgAJkaM8MNpCBSyvt8c8FiI6P?usp=drive_open

https://docs.google.com/document/d/1pAucHYxUlmynGhzG34imNP0G0ONkw3cYEya9ucKYHH0/edit?tab=t.0

partiamo....

1) togliere config.py locale

posizionarsi su feature/py312 (poi in futuro non servirà....)
tutti i sottomoduli app, core, struttura con feature/py312
docker su posweb_containerization_fe_vue

2) config.py:
COD_INSTALLAZIONE = '9000000016'
CASH_ID = '01'
CASH_ROLE = 'MASTER'
LOCAL_IP = '127.0.0.1'
MASTER_IP = '127.0.0.1'
BACKUP_IP = ''
MASTER_PORT = '8000'
MMFG_WS_HOST = 'https://pos-ws-itmm-dev.bms.maxmara.com/bin/driver_ws'
MMFG_WS_PROXY = ''
GUI_THEME = 'RICH'
ON_CONTAINER = True
DEPLOY_ENV = 'demo'
DEBUG = 1
POS_CONTROLLER_PASS = 'zinc0st4'
FEATURE_SET = 'ONLINE'
LOCAL_CALLS = True
ENABLE_APP_MONITORING = False
DDTRACE_DEBUG = False
ENABLE_APP_PROFILING = False
POS_SCHEDULER = 0
BROWSER_DOWNLOAD_PRINTS_ENABLED = 1

3) creo i due mysql.pos dentro site/bin/config/configmaps
{
 "MYSQL_CONN_POOL": 1,
 "MYSQL_CONN_POOL_SIZE": 10,
 "MYSQL_HOST": "10.255.5.26",
 "MYSQL_PORT": 3306
}
e /secrets
{
 "MYSQL_PASSWD": "",
 "MYSQL_USER": "bergonzini.e"
}

4) aggiungo in config_store.py - come prima riga della fz
   # WORKAROUND DOCKER
   pard["POS_CONFIG"].pop('LISTA_COD_NEGOZIO', None)

5) dentro la dir /docker

6) requirements.txt (docker)
gunicorn
mysqlclient
# future

google-cloud-storage
google-cloud-logging
python-json-logger

# datadog tracer
# ddtrace==1.9.2
ddtrace

oss2

pyjwt
cryptography

pyyaml

python3-saml --no-binary=python3-sasl
lxml==>
xmlsec==>

# per conoscere lista dei pacchetti che il python integra
>> ./bin/python -m pip list

# avviare il docker e collarsi al kube di riferimento e avviare compose_build e compose_up
>> open -a docker
>> mmfgcloud maxima-test
> 
> ./docker/compose_build.sh
> 
> ./docker/compose_up.sh
> 

# il docker è raggiungibile a questo indirizzo
https://localhost:4443