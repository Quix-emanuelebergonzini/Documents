per abilitare funzionalità già presenti guardare il file condiviso
https://docs.google.com/spreadsheets/d/1sFPpzttcVgR5XGNRL4pvLi8TyL4_cp0G7GqcTjyDRYY/edit#gid=1661782208

*attenzione* PER RESO SI INTENDE ANCHE RESO DURANTE LA VENDITA (STORNO)
con il seguente comando io spengo lo storno sul negozio
~~~
UPDATE pos_config_store SET valore = 0 WHERE chiave = RETURNS_ENABLED and negozio = 0100051;
~~~
dopo devo inviare giù un pos_generate_custom_values e poi un part di Negozi,CustomVAlues


ESEMPIO: ABILITARE RESI ORDINI ONLINE (O2O --> OFFINE TO ONLINE) PER MA (Marella)
-- i clienti restituiscono in negozio gli acquisti online (o cambio taglia) --

nel file convidiso vedere pagina "Resi B2C 020"

* aprire da master una branch (o2o_marella) su poswsbe per abilitare la nuova voce di menù
modificando il file pos_generate_custom_values.py

~~~~
# Resi
if codice_proprietario not in ("USEIT", "DT"):
	func_permissions.pop(POS:::resi, )

# Resi b2c
if codice_proprietario not in ("DT", "MX", "USEIT"):
	func_permissions.pop(POS:::resi_b2c, )

# Resi b2c list
	if codice_proprietario not in ("MX", "USEIT"):
		func_permissions.pop(POS:::resi_b2c_list, )
~~~~

* aggiungo MA perché qui vige la logica della doppia negazione. quindi se aggiungo un brand il menù viene aggiunto

~~~~
# Resi
if codice_proprietario not in ("USEIT", "DT", "MA", "MMDE"): <<<--- fare solo questo per attivare la pagina reso (non b2c)
	func_permissions.pop(POS:::resi, )

# Resi b2c
if codice_proprietario not in ("DT", "MX", "USEIT", "MA"):
	func_permissions.pop(POS:::resi_b2c, )

# Resi b2c list
if codice_proprietario not in ("MX", "USEIT", "MA"):
	func_permissions.pop(POS:::resi_b2c_list, )
~~~~

* aprire la pagina https://confluence.mmfg.it/display/POS/Branches e aggiungere la branch
* aggiungere una nuova riga prendendo spunto dalle precendenti...

* eseguire insert_testMx_to_testMa_o2o_connect_to_mule.sql sul db interessato, cambiando cod_negozio e brand

* aggiornare gli update descritti nel foglio, specializzato per negozio (vedi se o meno cambiare il valore di default)

* vedi https://confluence.mmfg.it/display/POS/Versioni+software+BOSS per sapere che versione
di BOSS è presente sul BMS ma controllare:
    * aprire in ssh il BMS di MA (possedema)
    * cd httpd-chroot/deployer_files/
    * cat deployment.storebackoffice.status
    * guardo la prima riga in alto e lì cè il nome del tag

* per controllare se un tag COD_NEGOZIO_ORDERS_1 è più recente o meno di un tag 1.15.2 (numerico) posso andare su https://git.mmfg.it e usare la funzione compare
    * apro il repo bms/storebackoffice
    * apro il compare (vedi bottone ...)
    * in alto metto il tag 1.15.02 e in basso metto il tag COD_NEGOZIO_ORDERS_1
    * se non cè nulla vuol dire che COD_NEGOZIO_ORDERS_1 è più recente e non devo aggiornare BOSS

* avviare python ~/httpd-chroot/guest/posws/bin/poswsbe/pos_generate_custom_values.py -v sul bms
