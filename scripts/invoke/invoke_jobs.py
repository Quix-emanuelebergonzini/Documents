#!/usr/bin/env python3
import sys, argparse
import subprocess
from os import system

def ensure_docker_running():
    try:
        result = subprocess.run("pgrep -x Docker", shell=True, capture_output=True)
        if result.returncode != 0:
            print("Docker non è avviato. Avvio Docker...")
            subprocess.Popen(["open", "-a", "Docker"])
        else:
            print("Docker è già avviato.")
    except Exception as e:
        print("Errore nel controllo di Docker:", e)

ensure_docker_running()

sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/scripts'])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

from credenziali_cloud import MAPPING_CLOUD, MAPPING_INDEX_JOB, TEMPLATE_JOB

parser = argparse.ArgumentParser(description="Scrittura facilitata per invocare un job su bms o crm",
         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-a", "--env", help="name of project", required=True)
# parser.add_argument("-j", "--job", help="name of job to load without .py extension")
parser.add_argument("-ld", "--landscape", help="environment to deploy, default TESTING", default="TESTING")
parser.add_argument("-m", "--memory", help="memory to allocate, default 2000", default="2000")
parser.add_argument("-p", "--parameters", action="store_true", help="parameters to pass to job", default=True)
parser.add_argument("-c", "--custom_path", default="posws/bin/poswsbe", help="custom path")
args = parser.parse_args()
config = vars(args)
print(config)

job = {}
parameters = ""

mmfg_command = f"/Users/emanuele.bergonzini/Documents/Documents/scripts/mmfgcloud.sh {config['env']}"
print(mmfg_command)
system(mmfg_command)

# if not config["job"]:
#     for i, job in enumerate(MAPPING_INDEX_JOB.values()):
#         print(f"{i}) {job}")
#
#     index = input("Selezionare la propria scelta: ")
#     if not index:
#         print("Nessuna scelta selezionata")
#         exit(1)
#
#     job = MAPPING_INDEX_JOB[index]

job = MAPPING_INDEX_JOB['2']

# if not config["job"]:
#     script_name = f"{job.lower()}.py"
# else:
#     script_name = f"{config['job'].lower()}.py"

script_name = f"{job.lower()}.py"

if config["landscape"] not in ("prod", "PROD", "production", "PRODUCTION", "test", "TEST", "testing", "TESTING", "uat", "UAT", "staging", "STAGING"):
    raise Exception("Landscape non riconosciuto")

if config["landscape"] in ("prod", "PROD", "production"):
	config["landscape"] = "PRODUCTION"

if config["landscape"] in ("test", "TEST", "testing"):
	config["landscape"] = "TESTING"

if config["landscape"] in ("uat", "UAT", "staging"):
	config["landscape"] = "STAGING"

if config["env"] not in MAPPING_CLOUD.keys():
    raise Exception("Ambiente non riconosciuto")

project = MAPPING_CLOUD.get(config["env"])

path = config["custom_path"] if config.get("custom_path") else job.get("custom_path", "posws/bin/poswsbe")

if config["parameters"]:
    parameters = "-h"
    if script_name in ("pos_export_to_store_sw.py", "pos_export_to_store_db.py"):
        list_negozi = input("Inserire la lista negozi separati da spazio: ")
        if script_name == "pos_export_to_store_sw.py":
            parameters = f"full -p10 {list_negozi} -f"

        if script_name == "pos_export_to_store_db.py":
            action = input("Inserire l'azione: ")
            if action not in ("incr", "full", "part", ""):
                raise Exception("Azione non riconosciuta")
            if not action:
                action = "incr"
            parameters = f"{action} -p10 {list_negozi} -f"
            if action in ("part",):
                partitions = input("Tabella da esportare: ")
                parameters = f"{action} -p10 {list_negozi} -t {partitions} -f"

template = TEMPLATE_JOB.format(
    mmfg_provider="MMFG_PROVIDER=ALICLOUD" if project in ("linmara", "cn", "cina") else "",
    landscape=config["landscape"].upper(),
    project=project,
    path=path,
    memory=config["memory"],
    script_name=script_name,
    parameters=parameters
)
print(template)

# Esecuzione del comando generato
# exec_cmd = input("Premere Invio per eseguire il comando...")
# if exec_cmd in ("", "y", "Y", "yes", "YES", "si", "SI", "s", "S"):
# 	try:
# 		result = subprocess.run(template, shell=True, check=True, capture_output=True, text=True)
# 		print("Output comando:\n", result.stdout)
# 		if result.stderr:
# 			print("Errori:\n", result.stderr)
# 	except subprocess.CalledProcessError as e:
# 		print("Errore durante l'esecuzione del comando:")
# 		print(e)
# 		print("Output:\n", e.output)
