#!/usr/bin/python
import sys, argparse
import subprocess
from os import system

sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/scripts'])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

from credenziali_cloud import MAPPING_CLOUD

parser = argparse.ArgumentParser(description="Cambio del negozio in locale configurato su Posweb",
								 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-l", "--list", action="store_true", help="print lista ambienti")
args = parser.parse_args()
config = vars(args)
# print(config)

if config['list']:
	print(MAPPING_CLOUD.keys())
	exit()

landscape = "test"
dove = input("Inserire ambiente di riferimento (default, test): ")
dove = dove.lower()
if dove in ("uat", "staging",):
	landscape = "staging"

if dove not in (landscape, ''):
	landscape = dove

ambiente = input("Scegliere ambiente tramite nome (es, jp): ")
if not ambiente in MAPPING_CLOUD.keys():
	raise Exception("Ambiente non riconosciuto")

mmfg_command = f"/Users/emanuele.bergonzini/Documents/Documents/scripts/mmfgcloud.sh {ambiente}"
print(mmfg_command)
system(mmfg_command)

print("Avvio comando")

ambiente = MAPPING_CLOUD[ambiente]
#if ambiente == "bmsbenelux":
	#ambiente = "benelux"

command = "kubectl -n {ambiente}-{landscape} get pods".format(ambiente=ambiente, landscape=landscape)
print(command)
kubectl_process = subprocess.run(
	["kubectl", "-n", "{ambiente}-{landscape}".format(ambiente=ambiente, landscape=landscape), "get", "pods"],
	capture_output=True, text=True
)
error = kubectl_process.stderr.splitlines()
output = kubectl_process.stdout.splitlines()
# print(kubectl_process)
if output and not error:
	runtime_l = [out for out in output if "runtime" in out]
	# print(runtime_l[0][:24])
	print("Accesso ssh")
	command = "kubectl exec {runtime} -n {ambiente}-{landscape} -it -- bash".format(ambiente=ambiente, landscape=landscape, runtime=runtime_l[0][:24])
	print(command)
	system(command)
if error:
	print(error[0])
