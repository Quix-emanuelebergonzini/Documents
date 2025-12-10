# collegarsi al runtime di OM e non preoccuparsi dei warning

## num spedizione S0000000000000089265

from config.locator import locator as loc
report = loc.get_service(ReportService)
import datetime
from common.constants import StatoVettore, StatoSpedizione

# se desidero un ricerca diretta
# spedizione = report.get(Spedizione,id_spedizione=89265)
spedizione = report.get_some(Spedizione,e.id_spedizione == 89265)

#se simulo una consegna al cliente o negozio devo commentare luno o altro
#la prima riga se uso la get e non la get_same
#spedizione.data_consegna_negozio = datetime.datetime.now()

spedizione[0].data_consegna_cliente = datetime.datetime.now()
#spedizione[0].data_consegna_negozio = datetime.datetime.now()

#simulo un aggiornamento di stato altrimenti devo commentare la prossima riga
#consegnato al cliente
spedizione[0].stato_vettore = StatoVettore.CONSEGNATO

#consegnato al negozio
#spedizione[0].stato_vettore = StatoVettore.CONSEGNATO_NEGOZIO

#report.set_spool_click_collect(spedizione=spedizione)
report.set_spool_click_collect(spedizione=spedizione[0])
oppure
report.upload_spool_to_bucket() --> altrimenti invocarlo come job
