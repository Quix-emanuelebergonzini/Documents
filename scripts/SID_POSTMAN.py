#!/usr/bin/python
import sys
import os.path
from os import path

print("Per il crm utilizzare possede")
print("Gli utente targati _bis sono una seconda possibiltà per l'utente (senza _bis)")

MAPPING_USER_PWD = {
    'possede': 'JustF0rD3bug',
    'ws_mm': 'd1PPyd1PPy',
    'ws_mm_bis': 'password1',
    'ws_om_bis': 'a09as7d7as96da6s9d6a',
    'pos_ws_be': 'fipDecr53vFjh7s22',
    'ws_om': 'a166c0d011def85f2e',
    'boh': 'Aiw267Xnp0',
    'store': 'oey;:ydh290ue.', # buono per poswsfe
    'om': 'fweC.sdjht-cC2adasdf',
    'pos': '25CC.sdc4t-cx#zcb15p',
    'pos-sede-be': 'fipDecr53vFjh7s22',
    'maxima': 'gdtey36d73trgc.',
    'ws_om_pos': 'a166c0d011def85f2e',
}

args = sys.argv

i = 1
if len(args) < 2:
    print("Inserire il nome dell'utente, uno tra i seguenti")
    for item in MAPPING_USER_PWD.items():
        print("{}) {}".format(i, item))
        i += 1
    raise Exception()

names_users = [users for users in MAPPING_USER_PWD.keys()]
if not args[1] in names_users:
    raise Exception("User non trovato!")

client_password = MAPPING_USER_PWD[args[1]]
import time
import hashlib
t = str(int(time.time()))
t = t[:-2]
client_password = t + client_password + t
client_password = hashlib.sha1(client_password.encode("utf-8")).hexdigest()
print(client_password)
