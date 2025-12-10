from poswsbe.rest.locator import locator as loc
self = loc.get_service("RestService")

cod_negozio = '4401678'
pk_consumer_bms = ['LIN_540942']
negozio, insegna, gestione_vendite, nazione = self._get_negozio_info(cod_negozio)

consumer_service = self.get_service("Consumer",COD_NEGOZIO=cod_negozio,INSEGNA_NEGOZIO=insegna,GESTIONE_VENDITE=gestione_vendite)
result = self.get_source_method('get_pk_consumers_by_store_code')(cod_negozio, pk_consumer_bms)

pk_consumer_bms = [res['pk_consumer'] for res in result]
dati = self.componi_richiesta_bms(cod_negozio)
dati['pk_consumer_list'] = pk_consumer_bms


consumer_list = consumer_service.get_consumatrici_sede(dati, force_call_crm=False, pard={}, get_complete_privacy=True)