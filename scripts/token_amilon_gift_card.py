import sys

for lib_dir in [
    "/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/site/bin",
    "/Users/emanuele.bergonzini/pos/posweb/mmfg/posweb/site/bin/lib",
    "/Users/emanuele.bergonzini/pos/posweb/mmfg/posweb/daemons",
    "/Users/emanuele.bergonzini/pos/posweb/mmfg/posweb",
]:
    sys.path.insert(0, lib_dir)

from mmfg.webservice import client

connections = {
    "login_amilon_rest": {
        "url": "https://b2bstg-sso.amilon.eu",
        "req_type": "URL",
        "trust_all_server_cert": True
    }
}
params = {"barcode": "3501701731528859"}
access_token = ""

connections["login_amilon_rest"]["additional_headers"] = (('Authorization', 'Bearer ' + access_token), ('Accept', '*/*'),)

resp = client.request("login_amilon_rest", {},
                      url="{{url}}/v1/card/checkPhisical?cardCodex={barcode}&returnInactiveCards=true".format(
                      barcode=params["barcode"]),
                      config=connections,
                      request_method="GET"
                      )
