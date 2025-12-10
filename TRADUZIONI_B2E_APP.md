AGGIORNAMENTO FEBBRAIO 2023
da web funziona

1)
da google drive scaricare il file xls che ci passano e tradurlo in csv
con la virgola come separatore (passiamo l'intero file)
https://docs.google.com/spreadsheets/d/1c4YsJz0C9VoEh-KAYmiejXCDEx_FsE6YtYYx4M-NlMI/edit?usp=drive_web&ouid=104451566435703679640

2) apro firebase per controllare lo stato attuale e prepararmi a vedere i cambiamenti
https://console.firebase.google.com/project/mmfg-appb2e-stores-prod/firestore/data/~2Ftranslates-test~2Fen
- translates --> prod
- translates-test --> test

3) apro https://itmm-dev.bms.maxmara.com/?module=boss.traduzioni_b2e.action&program=traduzioni_b2e
invoco la procedura caricando il csv

4) controllo su firebase se le voci sono aggiornate

5) invitare gli utenti a fare logout e login perché...

"""
qualdo l'app fa login apre una websocket su firebase
e legge le traduzioni poi le mette in cache
prima che si vedano, gli utenti devono fare logout/login
(se parliamo di label), per le trad posweb il discorso è differente
...
si non sono sicuro al 100% ma direi che firebase utilizzi una cache
le traduzioni sono quasi statiche, non avrebbe senso fare polling via websocket
"""

!!!!
solo in cina, la traduzioni lato app è gestito da un altro servizio chiamato linmara. 
c'e un campo url linmara nel settings dell'app che va valorizzato

Su linmara bisogna andare sulla stessa pagina che su maxima serve per caricare le traduzioni b2e 
ma mentre in maxima aggiorna pos_b2e_traduzioni e firestore, su linmara i dati vengono presi solo dalla tabella 
su bms

------------------------------------------------------------------------------------------------------------------------

A WEB NON FUNZIONA

step 1)
su maxima20-prod fare btk tabella pos_b2e_traduzioni (export csv)
che viene usata solo per CHINA ma in generale lo usiamo come controllo
per tutte le app b2e. non posso ad oggi controllare su firestore
(vedi https://jira.mmfg.it/browse/REX-11190 fatto da me)

step 2)
da google drive scaricare il file xls che ci passano e tradurlo in csv
con la virgola come separatore (passiamo l'intero file)

step 3)
in un altro terminale invocare
scp "MAXIMA20 - FG1362 - Traduzioni B2E - label.csv" maxima20@posweb-be-01.mmfg.it:/home/maxima20/httpd-chroot/data/trad_20220314.csv
oppure
scp "LINMARA - FG1362 - Traduzioni B2E - label.csv" linmara@linmarabt-be-02.mmfg.it:/home/linmara/httpd-chroot/data/trad_20220314.csv

step 4)
collegarsi a maxima20@posweb-be-01.mmfg.it in un terminale
>>> python bin/console.py

e invocare in due step (VEDI https://jira.mmfg.it/browse/REX-11190)
step 4a)
import csv
from boss.traduzioni_b2e.locator import locator as loc
s = loc.get_service('TraduzioniB2EService')

with open('/home/linmara/httpd-chroot/data/trad_20220314.csv') as f:\
  content = f.read()
 >> [invio]
csv_data = list(csv.reader(content.splitlines(), delimiter=','))
s.load_trads(csv_data)

se tutto va bene si vedono dei log e la procedura deve terminare senza errori
su linmara di log non ne vedo ma poi se controllo sulla pos_b2e_traduzioni
la data di aggiornamento deve cambiare in oggi

su maxima20 (a meno che non mi venga detto il contrario)
è consigliato di aggiornare solo la colonna zh e non tutte le lingue
quindi dal xls si prende solo la colonna zh (cancellando le altre...)
