per cercare i login utilizzare

cat var/log/web/* | grep "NUOVO LOGIN"

però potrebbe essere falso (tipo assistenza fa NUOVO LOGIN ma non apre la cassa)

quindi incrociare questo con date e ore....

e poi qui
site/bin/frontend/auth/controller.py

@route_handler("/v1/sessions", methods=('POST', ))
def login(self, request, config):
    pass
