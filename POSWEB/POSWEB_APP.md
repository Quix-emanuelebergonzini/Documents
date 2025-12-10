## esporre su posweb (=su un negozio) un nuovo servizio ##

*i servizi sono esposti da rest se chiamati da app ma anche richiamabili da interfaccia posweb*

## PER LA INTERFACCIA #
se è un vecchio servizio togliere da:
1. mmfg/posweb/site/bin/ws_interface.py il metodo (es, ws_get_all_causali_sconti()
2. di conseguenza anche da mmfg/posweb/site/bin/lib/movim_db_access.py
3. modificare in mmfg/posweb/site/bin/lib/movim_utils.py
il servizio (es, get_all_causali_sconti)

ESEMPIO di nuovo servizio che chiama non il servizio Rest ma quello interno e poi viene usato a codice da qualche parte
~~~
def get_all_causali_sconti(pard):
    with discount_reason_locator.using_service(
            DiscountReasonService,
            COD_NEGOZIO=pard[POS_CONFIG][COD_NEGOZIO]
    ) as dr_service:
        x = dr_service.get_all_causali_sconti()
        causali_sconti = []
        for d in x[data]:
            causali_sconti.append(d[attributes])
        return causali_sconti
~~~

******************************************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************************************
******************************************************************************************************************************************************************************************************

## PER LA CHIAMATA DA REST (APP) #

esempio (postman): http://localhost:8000/api/v1/posweb/discount_reason con bearer auth

aggiungere a /mmfg/posweb/site/bin/ws.py il servizio alla lista
~~~
from backend.discount_reason.locator import locator as discount_reason_locator
(Service, DiscountReasonService): discount_reason_locator,
(Service, DiscountReasonServiceRest): discount_reason_locator,
~~~

creo dentro a /site/bin/frontend e /site/bin/backend il nuovo modulo /discount_reason (aggiungere file __init__.py e invocare git add __init__ -f)

creo dentro a /frontend/discount_reason/ il locator
ESEMPIO LOCATOR
~~~
from mmfg.locator import Locator
from config.env import DATABASE_DIR

_cfg = {
	services: [{
		package: backend.discount_reason.service,
		names: [Stock, DiscountReasonService],
	}, {
		package: backend.discount_reason.service,
		names: [DiscountReasonServiceRest]
	}],
	sources: [{
		package: backend.discount_reason.source,
		names: [DiscountReason],
		attributes: {
			connection_parameters: {
				dbdir: DATABASE_DIR,
			},
		},
		publicmethods: {
			DiscountReason: [get_all_causali_sconti,]
		}
	}]
}

locator = Locator(_cfg)
~~~

creo dentro al /backend/discount_reason il service
ESEMPIO DI SERVICE
~~~
import logging

from mmfg.service import Service, RESTService, transaction, ApplicationError
from config.env import LOGGER_BASE

logger = logging.getLogger(LOGGER_BASE + "." + __name__)

class DiscountReasonService(Service):

	COD_NEGOZIO = basestring

	def get_all_causali_sconti(self):
		return self.get_source_method(get_all_causali_sconti)()

class DiscountReasonServiceRest(RESTService):

	COD_NEGOZIO = basestring

	def get_all_causali_sconti(self):
		return self.get_service(DiscountReasonService).get_all_causali_sconti()
~~~


creo dentro al /backend/discount_reason il source
ESEMPIO DI SOURCE
~~~
import logging

from backend.source import POSWebSource
from config.env import LOGGER_BASE

logger = logging.getLogger(LOGGER_BASE + "." + __name__)

class DiscountReason(POSWebSource):

	def get_all_causali_sconti(self):
		mysql_query = """
			SELECT codice_causale, descrizione, data_modifica
			FROM causali_sconti
		"""
		logger.debug(mysql_query)
		# return sqlite_access.sqlite_dict(pard)
		return mysql_query
~~~

aggiungo dentro /site/bin/config/route.py

(lambda url: "/posweb/discount_reason" in url, frontend.rest.discount_reason),

aggiungo dentro /site/bin/frontend/rest.py
~~~
from frontend.discount_reason.controller import DiscountReasonController
discount_reason = DiscountReasonController(locator=Locator({
	services: [{
		package: backend.discount_reason.service,
		names: [DiscountReasonServiceRest],
		provider: ProxyProvider,
		attributes: {
			request_parameters: {
				configuration: ws_config[fwk],
			},
		},
	}],
}), resource_config={
	(discount_reason, 1): {
		service_name: DiscountReasonServiceRest,
		url: posweb/discount_reason
	}
}, allowed_methods=(GET,))
~~~

creo dentro a /frontend/discount_reason/ il controler
ESEMPIO DI CONTROLLER
~~~
from frontend.common.controller import POSJSONAPIController
from mmfg.controller.rest import route_handler

import logging
from config.env import LOGGER_BASE

logger = logging.getLogger(LOGGER_BASE + "." + __name__)

class DiscountReasonController(POSJSONAPIController):

	@route_handler("/v1/posweb/discount_reason", methods=(GET, ))
	def get_all_causali_sconti(self, request, config):
		self.enrich_context_with_resource_data(discount_reason, request)
		return self.get_service(DiscountReasonServiceRest).get_all_causali_sconti()
~~~

creo dentro a /frontend/discount_reason/ il locator
ESEMPIO DI LOCATOR
~~~
from mmfg.locator import Locator, ProxyProvider
from config.ws_client import ws_config

_cfg = {
	services: [{
		package: ,
		names: [DiscountReasonServiceRest],
		provider: ProxyProvider,
		attributes: {
			request_parameters: {
				configuration: ws_config[fwk],
			},
		},
	}],
}

locator = Locator(_cfg)
~~~
