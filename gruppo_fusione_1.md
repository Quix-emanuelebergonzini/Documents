
da gruppo fusione 0 a 1
ho seguito la procedura     
https://maxmarafashiongroup.atlassian.net/wiki/spaces/KBOM/pages/3882749718/Migrazione+negozio+in+GF+1

dall'ultima query ho estratto i pk_consumer e poi fatto questo su crm_prod

crm@backoffice.crm.mmfg.it:~ $ /home/crm/virtualenv/bin/python bin/scripts/consumer_spool.py -a insert -p [15134757,15135143,15135307,15135582]
Populating pool for 1
Adding consumer
Consumer(pk_consumer=1)
Adding consumer_contact
ConsumerContact(id_contatto=6298542)
[[{'id_fusione': None, 'requestid': '755efef8-2ab4-46e0-99ad-af57c156d4b0', 'entita': 'consumer_negozio', 'id': '1', 'timestamp_inserimento': datetime.datetime(2022, 8, 12, 16, 26, 39, 916942), 'counter': 0, 'export_date': datetime.date(2022, 8, 12), 'ext_name': 'db_ru', 'millisecond_inserimento': 916942, 'ext_update_only': 0, 'action': 'API_UPSERT', 'pk_consumer': 1}, {'id_fusione': None, 'requestid': 'e1454ef9-45e2-443f-a020-4f0c1c8fb5af', 'entita': 'consumer', 'id': '1', 'timestamp_inserimento': datetime.datetime(2022, 8, 12, 16, 26, 39, 917030), 'counter': 0, 'export_date': datetime.date(2022, 8, 12), 'ext_name': 'db_ru', 'millisecond_inserimento': 917030, 'ext_update_only': 0, 'action': 'API_UPSERT', 'pk_consumer': 1}], [{'id_fusione': None, 'requestid': 'cd15f427-fed0-4f5e-bb47-5191edf867e8', 'entita': 'consumer_contact', 'id': '6298542', 'timestamp_inserimento': datetime.datetime(2022, 8, 12, 16, 26, 39, 931364), 'counter': 0, 'export_date': datetime.date(2022, 8, 12), 'ext_name': 'db_ru', 'millisecond_inserimento': 931364, 'ext_update_only': 0, 'action': 'API_UPSERT', 'pk_consumer': 1}]]


