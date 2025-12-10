# coding=utf-8
import sqlite3

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def select_posweb(database_posweb, query):
	sqliteConnection = None
	try:
		path_database = "/Users/emanuelebergonzini/projects/repos/posweb/mmfg/posweb/var/database/{db}.db".format(db=database_posweb)
		sqliteConnection = sqlite3.connect(path_database)
		sqliteConnection.row_factory = dict_factory
		cursor = sqliteConnection.cursor()
		# print(u"Successfully Connected to SQLite")
		cursor.execute(query)
		record = cursor.fetchall()
		cursor.close()
	except Exception as error:
		record = {}
		print("Error while connecting to sqlite", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
			print("The SQLite connection is closed")
	return record

def insert_posweb(database_posweb, query):
	sqliteConnection = None
	try:
		path_database = "/Users/emanuelebergonzini/projects/repos/posweb/mmfg/posweb/var/database/{db}.db".format(db=database_posweb)
		sqliteConnection = sqlite3.connect(path_database)
		sqliteConnection.row_factory = dict_factory
		cursor = sqliteConnection.cursor()
		cursor.execute(query)
		cursor.close()
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
