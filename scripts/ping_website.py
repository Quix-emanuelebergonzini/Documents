import time
import requests

# URL della pagina da chiamare
url = "https://dos-mr-fr-mmfg-01.posweb.mmfg.it/"

while True:
    try:
        response = requests.get(url, verify=False)
        print(f"Chiamata effettuata. Stato: {response.status_code}")
    except Exception as e:
        print(f"Errore nella chiamata: {e}")
    
    # Attende 5 minuti (300 secondi)
    time.sleep(300)

