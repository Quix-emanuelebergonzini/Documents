from itertools import groupby
from operator import itemgetter
from poswsbe.vat_notification.ws_client import VatSOAPClient
from poswsbe.vat_notification.locator import locator as loc
self = loc.get_service("VatNotifier")

self.nazione = 'HU'  # oppure 'DE'

negozi = loc.get_service("CommonService").get_negozi_of_nazione(self.nazione)
lista_stati_invio = ('DONE',) # ('TO_SEND', 'SENT', 'TO_RESEND')

messaggi = self.get_source_method("get_messaggi")(negozi=negozi,stati=lista_stati_invio)

pars = self._get_ws_config()
self.api_version = 'v3'
opt_attrs = {"remove_ns": True}
pars["api_version"] = self.api_version
self.SOAP_CLIENT = VatSOAPClient(pars["url"], **opt_attrs)

for tipo, lista_messaggi in messaggi.items():
    print(lista_messaggi)
    for stato, coda in groupby(lista_messaggi, key=itemgetter("stato_invio")):
        print(stato)
        queue = list(coda)
        print(queue[0])
        self._get_token_HU(pars, queue[0])

# se l'errore è nel get token bisogna andare più in profondità
from itertools import groupby
from operator import itemgetter
from poswsbe.vat_notification.ws_client import VatSOAPClient
from poswsbe.vat_notification.locator import locator as loc
self = loc.get_service("VatNotifier")

self.nazione = 'HU'  # oppure 'DE'

pars = self._get_ws_config()
self.api_version = 'v3'
opt_attrs = {"remove_ns": True}
pars["api_version"] = self.api_version
self.SOAP_CLIENT = VatSOAPClient(pars["url"], **opt_attrs)

from poswsbe.vat_notification.xmls.HU import TokenExchangeRequest, ManageInvoice, QueryInvoiceStatus, QueryTransactionStatus, invoice_api_to_class, QueryTaxpayer
token_xml = TokenExchangeRequest(**pars)
request_xml = token_xml.make()
path = "/invoiceService/{}/tokenExchange".format(self.api_version)
resp, res_token_xml = self.SOAP_CLIENT.do_request(path=path, body=request_xml)