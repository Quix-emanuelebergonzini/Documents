hk pos_import_spool id_orig = '118014'

-- CONSUMER NUOVO SENZA AGGIUNTE --
firma: {'channel': 'Store', 'brand': 'MR', 'date': '20220228', 'store': '1101012', 'authorize_contact': '0', 'new': '1', 'agreements': {'agreement': [{'type': 'Direct Marketing', 'value': '1'}, {'type': 'Profiling', 'value': '1'}]}}
firma_agree: [{'type': 'Direct Marketing', 'value': '1'}, {'type': 'Profiling', 'value': '1'}]
cb_agree: []

CHIAMATA AL make_full_consumer_poswsbe
service ConsumerCommonService
user: pos
cod_negozio: 1101012
cassiera: E1054
system: poswsbe
reason: GEN_INSERT
reqid: 9e80d533-8132-4e50-889a-8d02c2c10750
pk_consumer: 0

method make_full_consumer_poswsbe(0,{'linked_id': False, 'ext_name': 'pos', 'cod_negozio': '1101012', 'pk_consumer': 0, 'consumer_negozio': {'note_negozio': '', 'cod_scheda': '2'}, 'consumer': {'cognome': 'FUNG', 'nome': 'DAISY', 'nazione_iso': 'HK', 'sesso': 'F', 'lingua': 'INGL', 'data_firma_scheda': '20220228', 'negozio_firma_scheda': '1101012', 'anno_nascita': 1995, 'mese_nascita': 1, 'giorno_nascita': 1, 'preferenze_contatto': '', 'salutation': 'Sig.ina', 'nazionalita': '', 'note': '', 'anno_nascita_presunto': 0, 'interessi': '', 'professioni': '', 'pk_consumer': 0, 'data_ultimo_aggiornamento': '2022-02-28', 'data_prima_registrazione': '2022-02-28'}, 'consumer_address': [{'pk_consumer': 0, 'alfabeto': 'LATIN', 'indirizzo': '', 'cap': '', 'localita': '', 'nazione': 'HK', 'numero_civico': '', 'edificio': '', 'provincia': '', 'note_indirizzo': '', 'tipo_indirizzo': 'Residence', 'main': 1}], 'consumer_contact': [{'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'phone_primary', 'valore': ''}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'phone_work', 'valore': ''}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'mobile_primary', 'valore': '+85390019001'}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'mobile_work', 'valore': ''}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'email_primary', 'valore': 'FUNGDAISY@YAHOO.COM'}], 'consumer_name_alphabet': [{'nome': '', 'cognome': '', 'alfabeto': 'CHINESE', 'pk_consumer': 0}], 'consumer_cliente_finale': {'cliente_finale': 'HK_127927'}, 'cassiera': 'E1054', 'consumer_device': {'id_applicazione': '01', 'tipo_applicazione': 'POSWEB'}, 'consumer_privacy': {'brand': 'MR', 'canale': 'Store', 'negozio_firma': '1101012', 'data_firma': '20220228', 'pk_consumer': 0, 'consensi': [{'consenso': 1, 'pk_consumer': 0, 'tipo_consenso': 'Direct Marketing'}, {'consenso': 1, 'pk_consumer': 0, 'tipo_consenso': 'Profiling'}]}},{'ext_id': '', 'ext_name': '1101012', 'timestamp_modifica': datetime.datetime(2022, 3, 1, 8, 30, 19, 911444), 'user_modifica': '1101012', 'data': {}, 'user_inserimento': '1101012', 'timestamp_inserimento': datetime.datetime(2022, 3, 1, 8, 30, 19, 911444)},1101012,False)

-- CONSUMER NUOVO CON CROSS BORDER A 1 --
firma: {'channel': 'Store', 'brand': 'MR', 'date': '20220228', 'store': '1101012', 'authorize_contact': '0', 'new': '1', 'agreements': {'agreement': [{'type': 'Direct Marketing', 'value': '1'}, {'type': 'Profiling', 'value': '1'}]}}
firma_agree: [{'type': 'Direct Marketing', 'value': '1'}, {'type': 'Profiling', 'value': '1'}, {'type': 'Cross Border', 'value': '1'}]
cb_agree: [{'type': 'Cross Border', 'value': '1'}]
pk_bms: 0
pk_crm: 0
CHIAMATA AL make_full_consumer_poswsbe
service ConsumerCommonService
user: pos
cod_negozio: 1101012
cassiera: E1054
system: poswsbe
reason: GEN_INSERT
reqid: 89061705-2911-4e00-8535-240a6be5e514
pk_consumer: 0
method make_full_consumer_poswsbe(0,{'linked_id': False, 'ext_name': 'pos', 'cod_negozio': '1101012', 'pk_consumer': 0, 'consumer_negozio': {'note_negozio': '', 'cod_scheda': '2'}, 'consumer': {'cognome': 'FUNG', 'nome': 'DAISY', 'nazione_iso': 'HK', 'sesso': 'F', 'lingua': 'INGL', 'data_firma_scheda': '20220228', 'negozio_firma_scheda': '1101012', 'anno_nascita': 1995, 'mese_nascita': 1, 'giorno_nascita': 1, 'preferenze_contatto': '', 'salutation': 'Sig.ina', 'nazionalita': '', 'note': '', 'anno_nascita_presunto': 0, 'interessi': '', 'professioni': '', 'pk_consumer': 0, 'data_ultimo_aggiornamento': '2022-02-28', 'data_prima_registrazione': '2022-02-28'}, 'consumer_address': [{'pk_consumer': 0, 'alfabeto': 'LATIN', 'indirizzo': '', 'cap': '', 'localita': '', 'nazione': 'HK', 'numero_civico': '', 'edificio': '', 'provincia': '', 'note_indirizzo': '', 'tipo_indirizzo': 'Residence', 'main': 1}], 'consumer_contact': [{'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'phone_primary', 'valore': ''}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'phone_work', 'valore': ''}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'mobile_primary', 'valore': '+85390019001'}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'mobile_work', 'valore': ''}, {'id_contatto': 0, 'pk_consumer': 0, 'tipo_contatto': 'email_primary', 'valore': 'FUNGDAISY@YAHOO.COM'}], 'consumer_name_alphabet': [{'nome': '', 'cognome': '', 'alfabeto': 'CHINESE', 'pk_consumer': 0}], 'consumer_cliente_finale': {'cliente_finale': 'HK_127927'}, 'cassiera': 'E1054', 'consumer_device': {'id_applicazione': '01', 'tipo_applicazione': 'POSWEB'}, 'consumer_privacy': {'brand': 'MR', 'canale': 'Store', 'negozio_firma': '1101012', 'data_firma': '20220228', 'pk_consumer': 0, 'consensi': [{'consenso': 1, 'pk_consumer': 0, 'tipo_consenso': 'Direct Marketing'}, {'consenso': 1, 'pk_consumer': 0, 'tipo_consenso': 'Profiling'}, {'consenso': 1, 'pk_consumer': 0, 'tipo_consenso': 'Cross Border'}]}},{'ext_id': '', 'ext_name': '1101012', 'timestamp_modifica': datetime.datetime(2022, 3, 1, 8, 43, 10, 31471), 'user_modifica': '1101012', 'data': {}, 'user_inserimento': '1101012', 'timestamp_inserimento': datetime.datetime(2022, 3, 1, 8, 43, 10, 31471)},1101012,False)

-- CONSUMER NUOVO CON CROSS BORDER A 0 --
firma: {'channel': 'Store', 'brand': 'MR', 'date': '20220228', 'store': '1101012', 'authorize_contact': '0', 'new': '1', 'agreements': {'agreement': [{'type': 'Direct Marketing', 'value': '1'}, {'type': 'Profiling', 'value': '1'}]}}
firma_agree: [{'type': 'Direct Marketing', 'value': '1'}, {'type': 'Profiling', 'value': '1'}, {'type': 'Cross Border', 'value': '0'}]
cb_agree: [{'type': 'Cross Border', 'value': '0'}]
CHIAMATA AL make_full_consumer_poswsbe
service ConsumerCommonService
user: pos
cod_negozio: 1101012
cassiera: E1054
system: poswsbe
reason: GEN_INSERT
reqid: 1e7d3588-0b93-42b5-82dd-feae66862a18
pk_consumer: 0
method make_full_consumer_poswsbe(0,{'linked_id': False, 'ext_name': 'pos', 'cod_negozio': '1101012', 'pk_consumer': 0, 'consumer_negozio': {'note_negozio': '', 'cod_scheda': '2'}, 'consumer': {'pk_consumer': 'HK_127927', 'nazione_iso': 'HK'}, 'consumer_cliente_finale': {'cliente_finale': 'HK_127927'}, 'cassiera': 'E1054', 'consumer_device': {'id_applicazione': '01', 'tipo_applicazione': 'POSWEB'}, 'consumer_privacy': {'brand': 'MR', 'canale': 'Store', 'negozio_firma': '1101012', 'data_firma': '20220228', 'pk_consumer': 0, 'consensi': [{'consenso': 1, 'pk_consumer': 0, 'tipo_consenso': 'Direct Marketing'}, {'consenso': 1, 'pk_consumer': 0, 'tipo_consenso': 'Profiling'}, {'consenso': 0, 'pk_consumer': 0, 'tipo_consenso': 'Cross Border'}]}},{'ext_id': '', 'ext_name': '1101012', 'timestamp_modifica': datetime.datetime(2022, 3, 1, 8, 44, 41, 402705), 'user_modifica': '1101012', 'data': {}, 'user_inserimento': '1101012', 'timestamp_inserimento': datetime.datetime(2022, 3, 1, 8, 44, 41, 402705)},1101012,False)



# pk_consumer = "HK_127914"
# from poswsbe.locator import locator as loc
# poswsbe_consumer_service = loc.get_service("PosWsBeConsumerService")
# transcode_pks = poswsbe_consumer_service.transcode_pks([pk_consumer], system_from="BMS", reverse=True)
# pk_crm = transcode_pks[pk_consumer]
# pk_consumer_negozi = poswsbe_consumer_service.get_pk_consumer_negozi(pk_consumer, negozi_attivi=True)
