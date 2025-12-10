- login alibaba
- cambio utente, tipo linmara-prod-dev
- menù a sinistra > Log service > Audit Logging

__time__ ==> orario cinese (UTC+8)
Time ==> orario ITALIA (UTC+2)
_pod_name_ ==> keepalive-XXX oppure runtime-XXX

il filtro di ricerca in alto a destra sul log di linmara è orario ITALIANO

SPECCHIO DI STUDIO:
Su Xml <datetime_begin>2025-08-24 14:09:52</datetime_begin> ==> orario UK (UTC+0)
==> cercare per "2025-08-24 16:09:53"
==> orario cinese "2025-08-24 22:09:53" contando dalle 14:09:52 + 8 ore


nel box di un risultato c'è context view (una lente d'ingrandimento)
e fa vedere tutti i logs prima e dopo quello selezionato

________


* and runtime => senza virgolette o altro, nella query di ricerca così da filtrare per il log runtime (alternativamente cronjob)

* and runtime and "<id_transazione>" => si riesce più o meno a risalire a tutto il processo della transazione
poi è necessario proseguire con la lente di ingrandimento dopo l'ultima occorrenza