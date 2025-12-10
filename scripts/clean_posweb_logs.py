#!/usr/bin/env python3
import glob
import os.path

ROOT_DIR = "/Users/emanuele.bergonzini/repos/posweb"
POSWEB_ROOT_DIR = os.path.join(ROOT_DIR, "mmfg", "posweb", "var", "log")

for dir in ["web", "mmfg", "pos_installer", "pos_downloader",
			"pos_printer", "pos_scheduler", "pos_synchronizer",
			"pos_terminal", "pos_uploader", "query"]:

	folder_path = f"{POSWEB_ROOT_DIR}/{dir}"
	# print(folder_path)
	for f in glob.glob(f"{folder_path}/main.log.*"):
		print(f"Eliminato {f}")
		os.remove(f)
