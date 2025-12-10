test login negozio locale, da terminale

http_proxy = '' curl --location --max-time 60 --request POST 'http://localhost:8000/api/v1/sessions?cod_cassa=01&cod_negozio=0801234' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic YXNzaXN0ZW56YTptbWZn' \
--data-raw ''


python
cd $posweb
./bin/python site/bin/console.py

!!!! Authorization è con un Basic di assistenza/mmfg !!!!

import requests
import json
url = "http://localhost:8000/api/v1/sessions?cod_cassa=01&cod_negozio=0801234"
payload = ""
proxies = {
  "http": "",
  "https": "",
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic YXNzaXN0ZW56YTptbWZn',
}
response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
result = response.text
result = json.loads(result)
sid = result["data"]["id"]
print(sid)
