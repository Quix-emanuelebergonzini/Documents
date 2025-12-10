Da gestione_consumatrici creo una consumatrice
arriva file_export_spool

poi viene inviata al gcp --> CRM Test o CRM Prod --> bucket privacy--/schede_privacy

(storage_api.py)

STATIC_RESOURCES_CONF = {
	'schede_privacy': {
		'credentials': 'gcp.crm',
		'directory': BASE_DATA_DIR + 'schede_privacy/',
		'crm_resource': 'consumer_privacy',
		'bucket_name': {
			'DEVELOPMENT': 'privacy-2aee82239b95-test-592671868348',
			'TESTING': 'privacy-2aee82239b95-test-592671868348',
			'PRODUCTION': 'privacy-2aee82239b95-prod-1008342488062',
		}.get(env_name, '')
	}
}