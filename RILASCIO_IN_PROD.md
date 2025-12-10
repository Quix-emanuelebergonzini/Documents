Sono su una branch di posweb
    1. mi metto su master e mergio il mio branch (occhio al terzo flag)
    2. mi metto su production e mergio master
    3. stacco un tag di produzione (il più alto tra i numerici e i numerici con \_test). E un numero senza \_test come postfisso (es, 5786)
Sono su una branch di poswsbe
    1. mi metto su master e mergio il mio branch (occhio al terzo flag)
    2. stacco un tag di produzione numerico (es, 1.51.00) --> chiedere se scatta il numero o meno

Apro il foglio dei rilasci
    1. se avevo un foglio con un mio rilascio lo trasformo nella forma 1.50 > 1.51 (dove 1.51 è il mio tag di produzione)
    2. compilo in Aggiornare poswsbe versione 1.51.00 sul foglio del mio rilascio e delle versioni precendenti (es, 1.49 > 1.50)
    3. compilo in Fare la build di posweb dalla branch che si intende rilasciare sul foglio del mio rilascio e delle versioni precendenti con la versione di poswsbe 5786 (dove 5786 è il mio tag di produzione)
    4. aggiungere in confluence/versioni di poswsbe dopo la tabella, se scatta il numero, il nuovo tag 1.51 con descrizione


-p0: nella notte si installa (il pacchetto viene subito creato e mandato al negozio) e il giorno dopo la modifica
    si trova sul negozio (il negozio sa del pacchetto, ma dice "installazione non consentita" fino all'ora X)
-p10: parte subito appena ricepito


ATTENZIONE:
in caso di -p0 tutto quello che antecedente (poswsbe e query sul db) deve essere fatto il giorno prima.
non inviare un -p0 senza domandarsi cosa fare prima!!!!!

in caso di bisogna
python ~/httpd-chroot/guest/posws/bin/poswsbe/pos_export_to_store_db.py part
-t <tabelle_coinvolte>
-p10 -r "<001002:20210127110553>" all -f

<001002:20210127110553> - cos'è? è l'incrementale o il part che si è rotto
come si deduce? si apre un negozio coinvolto e si va in var/update/db
il pacchetto dovrebbe essere db_001002:20210127110553_... la parte in messo
è identificativo in questo caso.
