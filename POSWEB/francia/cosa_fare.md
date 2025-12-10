soluzione se ws_master va in forbidden
http_proxy= https_proxy= HTTP_PROXY= HTTPS_PROXY= /rnd/pos/mmfg/posweb/bin/python bin/fiscal_archive_recovery.py -t -f

/rnd/pos/mmfg/posweb/bin/python bin/fiscal_archive_recovery.py -t -f

https://maxmarafashiongroup.atlassian.net/browse/REX-29384

modificare fiscal_archive.py la seguente istruzione

# Se richiesto aggiungo un giorno in modo che sia inclusa anche la giornata odierna
    if self.include_today:
        date_limit = date_limit + timedelta(days=1)

e portare timedelta(days=1) da 1 a quanti giorni servono per arrivare a fine mese (esatti!) e poi lanciare il job

