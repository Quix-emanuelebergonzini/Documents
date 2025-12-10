import poswsbe.pos_utils as pos_utils

import logging

from itertools import groupby
from operator import itemgetter


def init_pard(pard=None, verbose=False):
	pos_utils.init_logger(pard, config={
		'logger_name': 'mmfg',
	})
	pos_utils.init_db(pard, config={
		'logger'   : pard['LOGGER'],
		'log_level': verbose and logging.DEBUG or 0,
	})
	return pard


pard = { }

init_pard(pard, True)


def get_dematerialization_data(pard):
	mysql_query = """ 
		SELECT cod_negozio, gruppo, ref, path, email
		FROM pos_stampe_dematerializzate
		WHERE email_to_send = 1
		ORDER BY gruppo, email
	"""
	return pos_utils.send_query_d(pard, mysql_query)


def update_dematerialization_data(pard, cod_negozio, group):
	mysql_query = """
		UPDATE pos_stampe_dematerializzate
		SET email_to_send = 0
		WHERE gruppo = '{group}' and cod_negozio = '{cod_negozio}'
	""".format(group=group, cod_negozio=cod_negozio)
	return pos_utils.send_query_d(pard, mysql_query)


result = get_dematerialization_data(pard)

for group, prints in groupby(result, key=itemgetter("gruppo", "email")):
	print("Invio mail dello scontrino riferito al gruppo {gruppo}".format(gruppo=group))
	for ps in prints:
		print("Staccato dal negozio {cod_negozio} con invio a {email} dal path {path}".format(
			cod_negozio=ps["cod_negozio"],
			email=ps["email"],
			path=ps["path"]
		))
		update_dematerialization_data(pard, ps["cod_negozio"], group[0])
