
 * questo job importa da tabella o file xls e scrive o meno sulla consumer_crm (vedi Linmara o Uat). Scrive sulla pos_dati_negozi xml generato
~~~
python httpd-chroot/guest/posws/script/consumer_bulk_import.py -t _import_LIN_MA -v -d -l 100 -c
python httpd-chroot/guest/posws/script/consumer_bulk_import.py -f "/Users/emanuelebergonzini/Downloads/FG1054_ Salmple upload Consumers Data - HK.xlsx" -v -d -l 100 -c
~~~

consumer_code deve essere (per i record nuovi) un "XX_numero di telefono senza prefisso", ovviamente tutto attaccato
altrimenti se ci metto già un pk_consumer sul bms aggiorno il dato

 * query è il tipico job che importa i dati dalla pos_dati_negozi e scrive sulla pos_import_spool
~~~
/env/bin/python /source/guest/posws/bin/poswsbe/pos_import_from_store.py
~~~

* CRM job per avviare lo scongelamento dei punti dopo i 30gg
~~~
/home/crm/virtualenv/bin/python ~/httpd-chroot/bin/runalone.py ~/httpd-chroot/bin/scripts/pos_promozioni.py -t LOYALTY_CARD_NEW -a process -j finalize_points
~~~
in particolare esegue:
SELECT codice, tipo, custom_data, id_operazione, id_ref, importo_utilizzato, timestamp_operazione, stato, importo,
cod_negozio, tipo_operazione, anno_operazione, timestamp_modifica, id, utente_modifica
FROM consumer_fidelity_calcolo_punti WHERE (stato = PENDING AND tipo_operazione = ASSIGNMENT
AND timestamp_operazione < 20191110103350 AND tipo = LOYALTY_CARD_NEW)

*  CRM job per avviare il force dei punti  dato un csv (separato da ;)
~~~
/home/crm/virtualenv/bin/python ~/httpd-chroot/bin/runalone.py ~/httpd-chroot/bin/scripts/pos_promozioni.py -a process -j force_amount_csv
~~~
il file può esssere inviato alla cartella tramite scp

* Linmara importazione dei Consumers
~~~
python httpd-chroot/guest/posws/script/consumer_bulk_import.py -t _import_LIN -v -d -c
~~~
dove \_import_LIN è una tabella che contiene i consumers importati da un xls tramite SequelPro
-c significa chiama il crm e scrivi il consumer sulla consumer_crm (del bms) così da avere la corrispondenza brm <--> crm
