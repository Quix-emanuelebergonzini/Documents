# coding=utf-8
from decimal import Decimal

from connection_sqlite import select_posweb
from db_config import DB_CONFIG_CONTAINER
import datetime
import json

import scripts.pymysql as pymysql

from sshtunnel import SSHTunnelForwarder

AMBIENTE = 0 # bms
# AMBIENTE = 1 # posweb

amb = 'crm' # se BMS viene utilizzata questa variabile per ottenere la connessione

# Funzione per eseguire una query
def exec_query(sql, db_conn):
	with db_conn.cursor() as cursor:
		cursor.execute(sql)
		result = cursor.fetchall()
	return result

def fix_resultset(resultset):
	return [fix_result(result) for result in resultset]

def fix_result(result):
	return {fix_field(field_name): fix_field(field_val) for field_name, field_val in result.items()}

def fix_field(field):
	if isinstance(field, datetime.datetime):
		return field.strftime('%Y-%m-%d %H:%M:%S')
	elif isinstance(field, datetime.date):
		return field.strftime('%Y-%m-%d')
	elif isinstance(field, int) or isinstance(field, float) or isinstance(field, Decimal):
		return "{}".format(field)
	elif isinstance(field, datetime.timedelta):
		return (datetime.datetime.min + field).time().strftime("%H:%M:%S")
	return field

if not AMBIENTE:
	DATABASE_BMS = DB_CONFIG_CONTAINER["TESTING"][amb]
	tunnel = None

	if DATABASE_BMS.get('sshHost'):
		tunnel = SSHTunnelForwarder(
			(DATABASE_BMS['sshHost'], 22),
			ssh_password='',
			ssh_username=DATABASE_BMS['sshUser'],
			remote_bind_address=('127.0.0.1', DATABASE_BMS['port'])
		)
		tunnel.start()

	try:
		print("Waiting to open db...")
		connection = pymysql.connect(host='127.0.0.1' if tunnel else DATABASE_BMS["host"],
							 user=DATABASE_BMS["user"],
							 passwd=DATABASE_BMS["password"],
							 db=DATABASE_BMS["db"],
							 port=tunnel.local_bind_port if tunnel else DATABASE_BMS["port"],
							 cursorclass=pymysql.cursors.DictCursor)
		# connection.begin()

		cont = 0
		limit_from = 0
		for i in range(2000, 60000, 2000):
			limit_to = i
			QUERY = """
				SELECT group_concat(pk_consumer) FROM (
				SELECT DISTINCT pk_consumer AS pk_consumer
				FROM consumer
				INNER JOIN consumer_negozio USING(pk_consumer)
				WHERE negozio IN ('0801154', '0801404', '0801021', '0801099', '0801442', '0801536', '0801097', '0801130', '0801577', '0801105', '0801334', '0801424', '0801048', '0801011', '0801060', '0801116', '0801371', '0801042', '0801448', '0801033', '0801544', '0801411', '0801159', '0801040', '0801574', '0801343', '0801061', '0801003', '0801370', '0801344', '0801403', '0801385', '0801009', '0801981', '0801096', '0801559', '0801366', '0801537', '0801517', '0801286', '0801378', '0801126', '0801206', '0801092', '0801067', '0801288', '0801443', '0801471', '0801017', '0801575', '0801958', '0801032', '0801138', '0801356', '0801235', '0801355', '0801482', '0801181', '0801127', '0801992', '0801053', '0801534', '0801141', '0801546', '0801572', '0801279', '0801381', '0801298', '0801013', '0801016', '0801429', '0801993', '0801483', '0801557', '0801418', '0801036', '0801586', '0801072', '0801054', '0801039', '0801234', '0801289', '0801074', '0801018', '0801545', '0801062', '0801243', '0801045', '0801076', '0801217', '0801582', '0801037', '0801568', '0801415', '0801107', '0801367', '0801204', '0801585', '0801237', '0801449', '0801565', '0801400', '0801331', '0801086', '0801038', '0801441', '0801049', '0801026', '0801058', '0801118', '0801398', '0801564', '0801213', '0801085', '0801055', '0801144', '0801558', '0801020', '0801567', '0801335', '0801991', '0801433', '0801139', '0801551', '0801555')
				AND grado_anonimato NOT IN (25, 40, 50, 100)
				LIMIT {limit_from},{limit_to}
				) AS pk_consumer;
			""".format(limit_from=limit_from, limit_to=limit_to)
			limit_from = limit_to
			res = exec_query(QUERY, connection)
			res = fix_resultset(res)

			cont += 1

			print(json.dumps(res, indent=4 if options.pretty_print else None) if options.json else res)


		connection.close()
		tunnel.stop()
		print("Db close")
	except Exception as error:
		print("Error while connecting to MySql", error)

else:
	QUERY = """
		select * from consumer limit 1
	"""
	result = select_posweb("main", QUERY)
	print(result)