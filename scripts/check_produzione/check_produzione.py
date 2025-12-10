# https://jamf-pro.mmfg.it:8443/api/doc
# https://jamf-pro.mmfg.it:8443/classicapi/doc/#/computers/findComputersByName

# !/usr/bin/python
import os
import argparse
import sys
import requests
import json
from base64 import b64encode

sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/scripts'])
sys.path.extend(['/Users/emanuele.bergonzini/Documents/Documents/CREDENZIALI'])

from credenziali_cloud import user_ext, pwd_ext, print_password, FIX_INDIRIZZI_JAMF

def base_auth(username, password):
	base_auth = "{username}:{password}".format(username=username, password=password)
	return b64encode(base_auth.encode('utf-8')).decode("ascii")

def gen_token():
	url = "https://jamf-pro.mmfg.it:8443/api/v1/auth/token"
	basic_token = base_auth(user_ext, pwd_ext)
	headers = {
		"Authorization": "Basic {basic_token}".format(basic_token=basic_token)
	}
	res = requests.request("POST", url, headers=headers, data={})
	return json.loads(res.text)["token"]

def search_on_jamf(search_name):
	token = gen_token()
	print("Token: {}".format(token))
	url = "https://jamf-pro.mmfg.it:8443/JSSResource/computers/match/{search_name}".format(search_name=search_name)
	headers = {
		"accept": "application/json",
		"Authorization": "Bearer {token}".format(token=token)
	}
	res = requests.request("GET", url, headers=headers, data={})

	keys_ids = []
	computers = json.loads(res.text)["computers"]
	if len(computers) > 1:
		keys_ids = [{res_id["id"]: res_id["name"]} for res_id in computers]

	key_id = computers[0]["id"]
	print("Id: {}".format(key_id))
	url = "https://jamf-pro.mmfg.it:8443/JSSResource/computers/id/{key_id}".format(key_id=key_id)
	res = requests.request("GET", url, headers=headers, data={})
	return keys_ids, json.loads(res.text)["computer"]["general"]["ip_address"]


parser = argparse.ArgumentParser(description="Ricerca IP negozi di Produzione Posweb", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--info", action="store_true", help="print solo le credenziali più tipiche")
parser.add_argument("-n", "--negozio", help="codice negozio a cui collegarsi", default="")
parser.add_argument("-p", "--port", help="porta da usare")
parser.add_argument("-o", "--output", action="store_true", help="stampa comando ssh")
parser.add_argument("-m", "--mapping", action="store_true", help="mapping posweb on localhost")
parser.add_argument("-hk", "--hongkong", action="store_true", help="is hong konk")
args = parser.parse_args()
config = vars(args)

print(config)

print_password()

if config.get("info"):
	exit(0)

if not config["negozio"]:
	print("Inserire codice negozio")
	exit(1)

if config["hongkong"] and not config["port"]:
	print("Inserire porta 2022 per collegarsi ad hongkong")
	exit(1)

negozio = config["negozio"]
ip = ""
ids = []

if negozio in FIX_INDIRIZZI_JAMF:
	ip = FIX_INDIRIZZI_JAMF[negozio]

if not ip:
	print("Recupero delle informazioni da https://jamf-pro.mmfg.it:8443")
	try:
		ids, ip = search_on_jamf("FGNEG-{negozio}*".format(negozio=negozio))
		print("IP from JAMF: {ip}".format(ip=ip))
	except:
		print("Recupero fallito per {negozio}".format(negozio=negozio))
	print("Fine recupero delle informazioni.....")

INDIRIZZI_INTROVABILI_JAMF = {
	"0122050": "37.116.73.136",
	"3201052": "182.161.65.149",
	"3201323": "182.161.65.163" # australia
}

if negozio in INDIRIZZI_INTROVABILI_JAMF:
	ip = INDIRIZZI_INTROVABILI_JAMF[negozio]
	print("IP update on INDIRIZZI_INTROVABILI_JAMF")

if ids:
	print("Altri ip trovati su Jamf:")
	for data in ids[1:]:
		print(data)

if ip:
		print("sudo - u posweb -i")
		print("cd /rnd/pos/mmfg/posweb")

		ssh_cmd = "ssh posweb@{ip_store}{add_port}{add_mapping}".format(
			ip_store=ip,
			add_port=" -p {}".format(config["port"]) if config.get("port") else "",
			add_mapping=" -L 9000:pos:8000 " if config.get("mapping") else ""
		)
		print(ssh_cmd)
		if not config['output']:
			os.system("{ssh_cmd}".format(ssh_cmd=ssh_cmd))
else:
	print("Negozio non trovato da nessuna parte")
