from poswsbe.consumer.locator import locator as loc
consumer_service = loc.get_service("PosWsBeConsumerService")
consumer_service.ricerca_consumatrici_BMS({'barcode': '5000000000012'}, negozi_l=['0801237',])

filters = {}
from poswsbe.consumer.locator import locator as loc
consumer_service = loc.get_service("PosWsBeConsumerService")
pk_consumers_fidelity = consumer_service.get_service('FidelityREST').get_consumer_details('0801237', codice='5000000000012', tipo='LOYALTY_CARD_JP')
pk_consumer = pk_consumers_fidelity[0]['pk_consumer']
result = consumer_service.get_source_method('transcode_pks')([pk_consumer])
result = map(dict, result)
filters['pk_consumer'] = result[0]['pk_bms']

# CRM
from fidelity.locator import locator as loc
rest = loc.get_service('FidelityREST')
rest.get_consumer_fidelity_fascia_vip(['MCJ_160517'])
rest.get_loyalty_program('2020-03-19', 'LOYALTY_CARD_JP')
or
rest.get_consumer_fidelity_fascia_vip(['MCJ_160517'])

# BMS
from datetime import datetime
from posws.bin.poswsbe.ftpexport.locator import locator as loc
service = loc.get_service('FtpExportService')
tipo_export = 'CONSUMATRICE'
exporter = service.get_exporter(tipo_export, False, False)
date_job_l = service.get_date_exports(tipo_export)
-- oppure
date_job_l = []
date = '20230208'
date_job_l.append((None, datetime.strptime(date, '%Y%m%d'), ''))
-- oppure
print(date_job_l)
cod_negozio = '0801237'
for date_job in date_job_l:
    data = exporter.get_data_consumatrice(date_job[1], cod_negozio)

from datetime import datetime
from poswsbe.ftpexport.locator import locator as loc
service = loc.get_service('FtpExportService')
tipo_export = 'VENDUTO'
exporter = service.get_exporter(tipo_export)
date_job_l = service.get_date_exports(tipo_export, False, False)
-- oppure
date_job_l = []
date = '20230208'
date_job_l.append((None, datetime.strptime(date, '%Y%m%d'), ''))
data = exporter.get_data(date_job_l[0][1])
-- oppure
for date_job in date_job_l:\
    data = exporter.get_data(date_job[1])

from datetime import datetime
from posws.bin.poswsbe.ftpexport.locator import locator as loc
service = loc.get_service('FtpExportService')
tipo_export = 'FIDELITY'
exporter = service.get_exporter(tipo_export, False, False)
date_job_l = service.get_date_exports(tipo_export)
-- oppure
date_job_l = []
date = '20230208'
date_job_l.append((None, datetime.strptime(date, '%Y%m%d'), ''))
data = exporter.get_data(date_job_l[0][1])
-- oppure
for date_job in date_job_l:\
  data = exporter.get_data(date_job[1])

from datetime import datetime
from posws.bin.poswsbe.ftpexport.locator import locator as loc
service = loc.get_service('FtpExportService')
tipo_export = 'CHIUSURE'
exporter = service.get_exporter(tipo_export, False, False)
date_job_l = service.get_date_exports(tipo_export)
-- oppure
date_job_l = []
date = '20230208'
date_job_l.append((None, datetime.strptime(date, '%Y%m%d'), ''))
data = exporter.get_data(date_job_l[0][1])
-- oppure
for date_job in date_job_l:\
  data = exporter.get_data(date_job[1])

from datetime import datetime
from posws.bin.poswsbe.ftpexport.locator import locator as loc
service = loc.get_service('FtpExportService')
tipo_export = 'PAGAMENTI'
exporter = service.get_exporter(tipo_export, False, False)
date_job_l = service.get_date_exports(tipo_export)
-- oppure
date_job_l = []
date = '20230208'
date_job_l.append((None, datetime.strptime(date, '%Y%m%d'), ''))
data = exporter.get_data(date_job_l[0][1])
-- oppure
for date_job in date_job_l:\
  data = exporter.get_data(date_job[1])

# AVVIO JOB
LANDSCAPE=TESTING docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/ftp_exporter_manager.py  -o -d 20240515 -t VENDUTO,PAGAMENTI,CONSUMATRICE,FIDELITY,CHIUSURE

exporter.do_export('data', 1, '20200323', '')
exporter.do_export('data', 2, '20200323', '')
exporter.do_export('data', 3, '20200324', '')
exporter.do_export('data', None, '20200324', '')

# BMS
from poswsbe.ftpexport.locator import locator as loc
serv = loc.get_service('ExportVendutoService')
from datetime import datetime
date_job_l = []
date = "20210930"
date_job_l.append((None, datetime.strptime(date, '%Y%m%d'), ''))
serv.do_export(date_job_l[0][0], date_job_l[0][1], date_job_l[0][2], True, False, True)
serv = loc.get_service('ExportPagamentiService')
serv.do_export(date_job_l[0][0], date_job_l[0][1], date_job_l[0][2], True, False, True)
