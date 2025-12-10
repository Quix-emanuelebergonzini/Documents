# Script Python che legge tutti i file .gz in una cartella, li estrae e sostituisce "INSERT INTO" con "REPLACE INTO" nei file .sql

import os
import gzip
import shutil
import glob
import subprocess
import argparse

def estrai_gzip_e_modifica_sql(cartella):
	print(f"Estrarre e modificare file in: {cartella}")
	for gz_file in glob.glob(os.path.join(cartella, "*.gz")):
		sql_file = gz_file[:-3]
		with gzip.open(gz_file, 'rb') as f_in, open(sql_file, 'wb') as f_out:
			shutil.copyfileobj(f_in, f_out)
		os.remove(gz_file)
		print(f"Estratto: {sql_file} ed eliminato {gz_file}")

	for sql_file in glob.glob(os.path.join(cartella, "*.sql")):
		subprocess.run(["sed", "-i.old", "s/INSERT INTO/REPLACE INTO/g", sql_file])
		print(f"Modificato: {sql_file}")
		# comprimi il file sql_file in gz_file
		gz_file = sql_file + ".gz"
		with open(sql_file, 'rb') as f_in, gzip.open(gz_file, 'wb') as f_out:
			shutil.copyfileobj(f_in, f_out)
		os.remove(sql_file)

	for old_file in glob.glob(os.path.join(cartella, "*.old")):
		os.remove(old_file)
		print(f"Rimosso file temporaneo: {old_file}")

def main():
	parser = argparse.ArgumentParser(description="Estrai e modifica file .gz/.sql")
	parser.add_argument("-p", "--path", type=str, help="Percorso della cartella",
						default="/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/updates/db",)
	args = parser.parse_args()
	estrai_gzip_e_modifica_sql(args.path)

if __name__ == "__main__":
	main()
