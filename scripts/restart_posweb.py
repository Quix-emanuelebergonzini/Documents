#!/usr/bin/env python3
import sys, argparse
import json
import os.path
from time import sleep
import sqlite3
import shutil
import subprocess

sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/scripts'])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

def get_root_dir():
	check_string = 'mmfg'
	check_last_string = 'posweb'
	actdir = "/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb"
	last_dirname = ''
	outdir = ''
	while True:
		dirname = os.path.basename(os.path.abspath(actdir))
		if dirname == '/':
			break
		actdir = os.path.dirname(os.path.abspath(actdir))
		if dirname == check_string and last_dirname == check_last_string:
			outdir = actdir
			break
		last_dirname = dirname
	return outdir

daemons_path = os.path.join("/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/daemons")
if daemons_path not in sys.path:
	sys.path.append(daemons_path)
ROOT_DIR = get_root_dir()

from process_monitor import PosMonitor

# process_list = PosMonitor().send_command("status")
# print(process_list)
PosMonitor().send_command("restart pos_webserver")