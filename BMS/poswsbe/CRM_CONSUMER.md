# BMS
from poswsbe.locator import locator
crm_service = locator.get_service('CRMBackOffice')
negozio = '0501001'
consumers_crm = crm_service.get_consumer_of_negozi(
[negozio, ],
min_timestamp=None,
max_timestamp=None,
anonime=True, alfabeto_nazione_nomi=None,
alfabeto_nazione_indirizzi=None
)

# CRM
from initiative.locator import locator as loc
serv = loc.get_service('CRMBackOffice')
min_timestamp = None
max_timestamp = None
brand = "MM"
prefix_cli_fi="LIN"
serv.get_firma_consensi_privacy_for_clone(
    ['4401082'], brand,
    min_timestamp=min_timestamp,
    max_timestamp=max_timestamp,
    prefix_cli_fi=prefix_cli_fi
)
