# python main/bin/console.py

# COMMENTARE TUTTI I self.process_template !!!!
# METTERE DEI PRINT
from poswsbe import pos_utils
import config

pard = config.application_parameters()
pos_utils.init_logger(pard, config={
	"logger_name": "mmfg",
})
pos_utils.init_db(pard, config={
	"logger"   : pard["LOGGER"],
	"log_level": 10,
})
pos_utils.init_db(pard)

from poswsbe.pos_export_to_store_db import Movimenti, Catalogo, Prezzi, CatalogoTessuto

table = Catalogo(pard, '0000000006', ['0811496'], None, None)
table.populate()

#table = Prezzi(pard, '0000000006', ['0811496'], None, None)
#table.populate()

#table = Movimenti(pard, '9000000008', ['0201024'], None, None)
#table.populate()

#table = CatalogoTessuto(pard, '9000100050', ['0100050'], None, None)
#table.populate()

# o più semplicemente:
pos_utils.init_db(pard)
from poswsbe.locator import locator
crm_service = locator.get_service(CRMBackOffice)
result = crm_service.get_consumer_from_clifi(cliente_finale=NW00009028454)
mysql_query = """SELECT DISTINCT pk_consumer, IFNULL(c.cognome, ) AS cognome, IFNULL(c.nome, ) AS nome, grado_anonimato
				FROM crm.consumer_cliente_finale AS ccf
				LEFT JOIN crm.consumer AS c USING (pk_consumer)
				WHERE cliente_finale=010200300446 AND timestamp_fine IS NULL
"""
#
# mysql_query = """
# 		SELECT negozio, num_bolla, data_bolla, importo, nominativo, cod_cli AS valore_codice, CODICE AS tipo_codice
# 		FROM mx_bolle_clienti
# 		UNION ALL
# 		SELECT negozio, num_bolla, data_bolla, importo, nominativo, ,
# 		FROM mx_sospesi
# 		ORDER BY negozio, num_bolla, data_bolla
# """

result = pos_utils.send_query_d(pard, mysql_query)

if type(result_d) == dict:
	consumer_data = result_d
else:
	if len(result_l) > 1:
		pos_utils.log_warning(pard, "pk_consumer multiplo per")
		consumer_data = None
	else:
		consumer_data = result_l[0]
