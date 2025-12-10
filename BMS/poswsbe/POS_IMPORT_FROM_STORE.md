per farlo andare in locale
bisogna guardare sul main/bin/config/wsclient.cloud-local

{"url": "http://localhost:8000/bin/driver_ws", "http_proxy": "", "enable_compression": "0", "params": "{'module': 'ws_interface'}",
"req_type": "PASSWORD", "connection_timeout": "60"}

poi bisogna spegnere auth su bin/poswsbe/ws_interface.py

c = self.user_permissions[user]
if not ('' in c['codice_proprietario'] or all(i in c['codice_proprietario']
                        for i in pard['codice_proprietario_list'])):
  raise ApplicationError('codice_proprietario non ammesso per {0}: {1}'.format(
    pard['ws_client_user'],pard['codice_proprietario_list'])
  )

tutto da commentare
testato su bmsjp

-----

COME INVOCARE DA RUNTIME DI BMS (LOCALE CARICATO IN DOCKER) I DATI ARRIVATI
SULLA POS_DATI_NEGOZI E SIMULARE LA SUA IMPORTAZIONE

devo mettere dentro a guest/posws/bin/poswsbe/pos_utils.py riga circa 900
def send_request_ws(ws_name, ws_params):
	from poswsbe.mmfg.webservice.client import send_request
	from config.ws_client import ws_config

	ws_config['pos-ws-mmj-be']['url'] = 'https://mmj-ws-dev.bms.maxmara.com:443/bin/driver_ws'
	ws_config['pos-ws-mx-be']['url'] = 'https://itmm-ws-dev.bms.maxmara.com:443/bin/driver_ws'
    ws_config['pos-ws-mn-be']['url'] = 'https://itmn-ws-dev.bms.maxmara.com:443/bin/driver_ws'
	ws_config['pos-ws-ma-be']['url'] = 'https://itma-ws-dev.bms.maxmara.com:443/bin/driver_ws'
	ws_config['pos-ws-mmfr-be']['url'] = 'https://fr-ws-dev.bms.maxmara.com:443/bin/driver_ws'
    ws_config['pos-ws-useit-be']['url'] = 'https://usa-ws-dev.bms.maxmara.com:443/bin/driver_ws'
    ws_config['pos-ws-dt-be']['url'] = 'https://itdt-ws-dev.bms.maxmara.com:443/bin/driver_ws'

    --> !!!! questo url lo prendo da app_container.yml un DRIVER_WS di TESTING (almeno credo) !!!! <----

	...

quindi invocare:
python guest/posws/bin/poswsbe/pos_import_from_store.py -v

alternativamente in pos_import_from_store.py
aggiungere questo metodo 

def _get_dati(pard, table=None):
	"""
	codice_proprietario: filtro su codice_proprietario (MX MA MR MN DT)
	negozio: filtro su negozio (0100xxx); e' possibile passare una lista di elementi separati da virgola
	last_id: ultimo id ricevuto, verrano restituiti solo record con id>last_id
	limit: numero massimo di record restituiti (max 10000)
	ip_address: filtro su ip che ha generato il file
	tipo_dati: filtro su tipo di xml (sale, schedule...); e' possibile passare una lista di elementi separati da virgola
	origine: filtro sul sistema che ha generato l'xml (POS, SEDE)
	validita: 0 non valido, 1 valido (default)
	single: se 1, viene richiesto solo l'xml con id=last_id
	societa_industriale: MM, MN, MA, MR, DT
	legame_commerciale: COMMISSIONE_VENDITA
	"""

	start_time = time.time()
	codice_proprietario = pard.get('codice_proprietario', '')
	negozio = pard.get('negozio', '')
	last_id = pard.get('last_id', '')
	limit = pard.get('limit', '')
	ip_address = pard.get('ip_address', '')
	tipo_dati = pard.get('tipo_dati', '')
	origine = pard.get('origine', '')
	origine_excluded = pard.get('origine_excluded', '')
	origine_included = pard.get('origine_included', '')
	validita = pard.get('validita', '1')
	single = pard.get('single', '')
	societa_industriale = pard.get('societa_industriale', '')
	legame_commerciale = pard.get('legame_commerciale', '')

	where_clause = []

	# se non ho origine_excluded, ma chiama Tinterri escludo di default le origini
	if not origine_excluded and pard['ws_client_user'] in ('maxima', 'cbmmx'):
		origine_excluded = "EDI"

	max_limit = 10000  # numero massimo di record restituiti
	limit = min(max_limit, int(limit or max_limit))
	last_id = int(last_id or 0)

	if validita:
		validita = int(validita)
		where_clause.append("validita={0}".format(validita))

	if origine:
		origine = pos_utils.sanitize_db(origine)
		where_clause.append("origine='{0}'".format(origine))

	if origine_excluded:
		origine_excluded_l = "','".join(pos_utils.sanitize_db(i) for i in origine_excluded.split(','))
		where_clause.append("origine NOT IN ('{0}')".format(origine_excluded_l))

	if origine_included:
		origine_included_l = "','".join(pos_utils.sanitize_db(i) for i in origine_included.split(','))
		where_clause.append("origine IN ('{0}')".format(origine_included_l))

	if codice_proprietario:
		codice_proprietario_l = "','".join(pos_utils.sanitize_db(i) for i in codice_proprietario.split(','))
		where_clause.append("codice_proprietario IN ('{0}')".format(codice_proprietario_l))

	if negozio:
		negozio_l = "','".join(pos_utils.sanitize_db(i) for i in negozio.split(','))
		where_clause.append("negozio IN ('{0}')".format(negozio_l))

	if ip_address:
		ip_address = pos_utils.sanitize_db(ip_address)
		where_clause.append("ip_address='{0}'".format(ip_address))

	if tipo_dati:
		tipo_dati_l = "','".join(pos_utils.sanitize_db(i) for i in tipo_dati.split(','))
		where_clause.append("tipo_dati IN ('{0}')".format(tipo_dati_l))

	if single == '1':
		where_clause.append("id={0}".format(last_id))
	else:
		where_clause.append("id>{0}".format(last_id))

	if societa_industriale or legame_commerciale:
		negozi_l = pos_utils.get_negozi_socind_legcomm(pard, societa_industriale, legame_commerciale)
		if negozi_l:
			where_clause.append("negozio IN ({})".format(",".join("'{}'".format(neg) for neg in negozi_l)))
		else:
			where_clause.append("1=0")

	where_clause = ' AND '.join(where_clause) or '1'
	query = """
		SELECT
			id, counter, cod_installazione, negozio, codice_proprietario, tipo_struttura, tipo_dati, file_name,
			data_creazione, ip_address, origine, validita, dati, modificato
		FROM {table}
		WHERE {where_clause}
		ORDER BY id
		LIMIT {limit}
	""".format(table=table, where_clause=where_clause, limit=limit)
	pard["LOGGER"].info("query finale {}".format(query))
	res = pos_utils.send_query_d(pard, query)
	return res

poi devo cambiare...

da
result = pos_utils.send_request_ws(ws_name, {
    'module'				: 'ws_interface',
    'program'				: 'get_dati_negozi',
    'codice_proprietario'	: codice_proprietario,
    ...
})
a
pard.update({
    'module'				: 'ws_interface',
    'program'				: 'get_dati_negozi',
    'codice_proprietario'	: codice_proprietario,
    'negozio'				: negozio,
    'last_id'				: last_id,
    'limit'					: limit,
    'ip_address'			: ip_address,
    'tipo_dati'				: tipo_dati,
    'validita'				: validita,
    'origine_included'		: origine_included,
    'ws_client_user'        : 'ciccio'
    #'origine'				: ORIGINE,
})
result = _get_dati(pard, table='pos_dati_negozi')
result = json.dumps(result)
