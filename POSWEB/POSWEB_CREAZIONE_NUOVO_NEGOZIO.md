Master e bisogna controllare da quale negozio bisogna staccare la vendita.

*se non so quale sw devo inviare al negozio di test*
--> guardare versionamento poswsbe sul bms di riferimento
--> guardo quale numero è tra () colonna di test --> guardo che versione cè nella colonan di prod e prendo quella che più si allinea anche con gli altri bms
--> a questo punto prendo il bms che ho valutato ok
--> vado poi su versionamento posweb di produzione in base al bms che ho scelto e guardo il tag di riferimento
*~~~--> GUARDA PUNTO 14 per invio a bms del sw oppure guarda jenkins!!! ~~~*

Creazione passo passo:
1. codice negozio (0100437)
3. apro il db del bms (es, MA )
4. apro chrome sulla web page del bms ( http://pos-sede-ma-dev.mmfg.it )
5. controllo sul db che non esista in pos_config_bundle il codice negozio
        1. nella tendita se lo trova è perché recensito in ana_soggetti_master
        1. se non cè
        bottone: creo nuovo negozio (codice, lingua, paese, numero casse 1 [master] )

6. valorizzare le chiavi (B2E_ENABLED = 1) ... chiedere o viene scritto nella issue
7. lancio la query sul BMSTEST (di MA/IB) per aggiunta dei brand a catalogo

PER ANNO / STAGIONE occhio!!!
~~~
INSERT INTO `pos_regole_catalogo` (`brand`, `nazione`, `anno`, `stagione`, `collezione`, `attivo`, `data_modifica`) VALUES
(IB, IT, 2019, 1, , 1, now()),
(IB, IT, 2019, 2, , 1, now());
~~~

CONTROLLARE BENE LE REGOLE CATALOGO E I PREZZI DA PROD PER PASSARLI IN TEST!!!!

8. aggiungo al negozio i brand collegati (es, IB ) sulla chiave AVAILABLE_BRANDS
9. controllo BRANDS_CATALOGO
10. apro web url per macchina cloud ( https://dos-ib-it.posweb.mmfg.it/ )

vedi: https://confluence.mmfg.it/display/POS/Configurazione+nuovo+negozio+in+Cloud

**DA SAPERE:**
- Su POSWeb ci sono due livelli di configurazioni:
    BRANDS_CATALOGO: serve per esportare gli SKU al negozio e filtrare solo i brand che effettivamente vende sia per B2E che per vendite normali, per i negozi DT Italia, solitamente cè il valore DT, perchè viene matchato sulla societa della tabella catalogo, ma sulla quale non avremmo questi dati.
    AVAILABLE_BRANDS: serve per pubblicare i capi allapp b2e. Per i negozi DTND Italia, solitamente cè il valore IN, perchè verrebbe matchato sul campo cod_marchio della tabella catalogo.

- CONTROLLO SUL BMS LE SEGUENTI TABELLE CHE SIANO VALORIZZATI:
    catalogo|catalogo_dbg|catalogo_descrizioni|catalogo_dbg_descrizioni|catalogo_prezzi|catalogo_dbg_prezzi

- Per un negozio DT non ITALIA:
    AVAILABLE_BRANDS --> IN
    BRANDS_CATALOGO --> DT,WE,MC,SP,MM,MA,PB,TS,AM,IB
    STORE_CHANNEL --> OD
    STORE_TYPE --> DTOD
    STORE_CHANNEL_DESC --> Outlet Diretti
    STORE_SIGN --> DT
    OWNER --> MMAU
    Sul BMS cè una forzatura del campo cod_marchio a IN anche per i negozi OD si per DT italia che non. Quando si provano i ws REST di POSWeb bisogna sempre usare IN come filtro di brand e aspettarsi dei risultati

11. ./bin/run_python.sh bin/catalog_b2e_generator.py -f

12. controprova https://frh-mr-de.posweb.mmfg.it/api/v1/posweb/models
e https://frh-mr-de.posweb.mmfg.it/api/v1/posweb/categories

########################################## POSWEB se il catalogo è vuoto... #################################################
    * controllare sul bms la chiave AVAILABLE_BRANDS in pos_config_store
    * controllare sul bms la chiave BRANDS_CATALOGO in pos_config_store
    * controllare la tabella pos_regole_catalogo se per brand/annostag è attivo

eseguire sul negozio questa query in main.catalogo:

~~~
-- , GROUP_CONCAT(DISTINCT c.variante), GROUP_CONCAT(DISTINCT c.raggruppamento_colore), GROUP_CONCAT(DISTINCT c.sku), GROUP_CONCAT(DISTINCT(c.societa || '.' || c.codice_taglia || '.' || IFNULL(c.indice_tg, 'null')))
SELECT DISTINCT c.*
FROM catalogo c
INNER JOIN prezzi p  ON p.modello=c.modello AND p.pezzo=c.pezzo AND p.tipo_prezzo="V" AND p.data_inizio_validita <= "20220308"
WHERE c.sku_padre = "" AND c.validita_variante IN ("V", "B") AND c.versione_modello = "V" AND
    c.data_consegna IS NOT NULL AND c.data_consegna <> "00000000" AND c.data_consegna <= '20220308'
    AND c.cod_marchio in ('MR')

    AND ((c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20181')OR(
    c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20182')OR(
    c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20191')OR(
    c.cod_marchio_originale IN('IN','MC','MM','WE','SP') AND c.annostag='20192')OR(
    c.cod_marchio_originale IN('IN','MC') AND c.annostag='20201')OR(
    c.cod_marchio_originale IN('PB') AND c.annostag='20202')OR(
    c.cod_marchio_originale IN('IB','MC','MM','WE','PB','MR','SP','MA') AND c.annostag='20211')OR(
    c.cod_marchio_originale IN('PE','IN','MC','IB','MM','WE','PB','SP','MR','MA') AND c.annostag='20212')OR(
    c.cod_marchio_originale IN('SP','WE','MM') AND c.annostag='20202' AND c.stagionale='PERMANENTE')OR(
    c.cod_marchio_originale='MR' AND c.annostag='20192' AND c.collezione IN('89')))

    AND p.cod_negozio in ('1101012')
GROUP BY c.modello_principale

SELECT DISTINCT c.modello_principale, p.cod_negozio , REPLACE(MAX(p.data_inizio_validita || "|" || p.prezzo), MAX(p.data_inizio_validita || "|"), "")
FROM catalogo c
INNER JOIN prezzi p  ON p.modello=c.modello AND p.pezzo=c.pezzo AND p.tipo_prezzo="V" AND p.data_inizio_validita <= "20220308"
WHERE c.sku_padre = "" AND c.validita_variante IN ("V", "B") AND c.versione_modello = "V" AND
    c.data_consegna IS NOT NULL AND c.data_consegna <> "00000000" AND c.data_consegna <= '20220308'
    AND c.cod_marchio in ('MR') AND ((c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20181')OR(c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20182')OR(c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20191')OR(c.cod_marchio_originale IN('IN','MC','MM','WE','SP') AND c.annostag='20192')OR(c.cod_marchio_originale IN('IN','MC') AND c.annostag='20201')OR(c.cod_marchio_originale IN('PB') AND c.annostag='20202')OR(c.cod_marchio_originale IN('IB','MC','MM','WE','PB','MR','SP','MA') AND c.annostag='20211')OR(c.cod_marchio_originale IN('PE','IN','MC','IB','MM','WE','PB','SP','MR','MA') AND c.annostag='20212')OR(c.cod_marchio_originale IN('SP','WE','MM') AND c.annostag='20202' AND c.stagionale='PERMANENTE')OR(c.cod_marchio_originale='MR' AND c.annostag='20192' AND c.collezione IN('89'))) AND p.cod_negozio in ('1101012')
GROUP BY c.modello_principale, p.cod_negozio

SELECT DISTINCT c.* , '[' || GROUP_CONCAT(DISTINCT('["' || c.sku || '","' || c.taglia || '","' || c.desc_taglia || '",' || IFNULL(c.indice_tg, 'null') || ',"' || c.ean || '"' || ']')) || ']'
FROM catalogo c
INNER JOIN prezzi p  ON p.modello=c.modello AND p.pezzo=c.pezzo AND p.tipo_prezzo="V" AND p.data_inizio_validita <= "20220308"
WHERE c.sku_padre = "" AND c.validita_variante IN ("V", "B") AND c.versione_modello = "V" AND
    c.data_consegna IS NOT NULL AND c.data_consegna <> "00000000" AND c.data_consegna <= '20220308'
    AND c.cod_marchio in ('MR') AND ((c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20181')OR(c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20182')OR(c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20191')OR(c.cod_marchio_originale IN('IN','MC','MM','WE','SP') AND c.annostag='20192')OR(c.cod_marchio_originale IN('IN','MC') AND c.annostag='20201')OR(c.cod_marchio_originale IN('PB') AND c.annostag='20202')OR(c.cod_marchio_originale IN('IB','MC','MM','WE','PB','MR','SP','MA') AND c.annostag='20211')OR(c.cod_marchio_originale IN('PE','IN','MC','IB','MM','WE','PB','SP','MR','MA') AND c.annostag='20212')OR(c.cod_marchio_originale IN('SP','WE','MM') AND c.annostag='20202' AND c.stagionale='PERMANENTE')OR(c.cod_marchio_originale='MR' AND c.annostag='20192' AND c.collezione IN('89'))) AND p.cod_negozio in ('1101012')
GROUP BY c.modello_principale, c.variante

SELECT DISTINCT c.modello_principale, c.variante, p.cod_negozio , NULL, NULL, NULL
FROM catalogo c
INNER JOIN prezzi p ON p.modello = c.modello AND p.pezzo = c.pezzo AND p.tipo_prezzo = "V" AND p.data_inizio_validita <= "{oggi}"
WHERE 1=1
AND c.sku_padre = "" AND c.validita_variante IN ("V", "B") AND c.versione_modello = "V"
AND c.data_consegna IS NOT NULL AND c.data_consegna <= "{oggi}"
AND c.cod_marchio in ('MR') AND ((c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20181')OR(c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20182')OR(c.cod_marchio_originale IN('MC','IN','MM') AND c.annostag='20191')OR(c.cod_marchio_originale IN('IN','MC','MM','WE','SP') AND c.annostag='20192')OR(c.cod_marchio_originale IN('IN','MC') AND c.annostag='20201')OR(c.cod_marchio_originale IN('PB') AND c.annostag='20202')OR(c.cod_marchio_originale IN('IB','MC','MM','WE','PB','MR','SP','MA') AND c.annostag='20211')OR(c.cod_marchio_originale IN('PE','IN','MC','IB','MM','WE','PB','SP','MR','MA') AND c.annostag='20212')OR(c.cod_marchio_originale IN('SP','WE','MM') AND c.annostag='20202' AND c.stagionale='PERMANENTE')OR(c.cod_marchio_originale='MR' AND c.annostag='20192' AND c.collezione IN('89'))) AND p.cod_negozio in ('1101012')
GROUP BY c.modello_principale, c.variante;
~~~
--> deve tornare valorizzata (cambiare marchio e annostag nel caso e anche data_inizio_validita). LA DATA DI VALIDITA è buona da dopo il 2018

questa query nasce da (da lanciare sulla macchina in cloud con il negozio installato così da avere marchio, data, annostag valorizzati bene):
cd /rnd/pos/mmfg/posweb
./bin/run_python.sh bin/catalog_b2e_generator.py -f
è dentro una create_table
##############################################################################################################################

11. apro il terminale sulla macchina in gcloud
```sh
gcloud beta compute --project "mmfg-testnw-gruppo-test" ssh --internal-ip "dos-ib-it"
sudo -u posweb -i
cd /rnd/pos/mmfg/posweb/
./bin/manager
x (spengo i servers)
cd conf/
vi config.py
vi version.py
```
12. configuro il config.py e version.py se non già correttamente configurati
    * attenzione!!! se non è italiano ci va il proxy adatto alla nazione
        * montecarlo --> francia
    * ESEGUO --> https_proxy='' curl https://pos-ws-fr-dev.bms.maxmara.com/bin/driver_ws OPPURE
    https_proxy="http://proxy.mmfg.it:8080" curl https://pos-ws-fr-dev.bms.maxmara.com/bin/driver_ws in base a quello che restituisce MISSING_MODULE_PROGRAM capisco se o meno mettere il proxy


13. mando al negozio un full del db
se non funziona il bms restituisce il messaggio grafico
> [/rnd/apps/interpreters/python/bin/python, /home/possedema/guest/posws/bin/poswsbe/pos_export_to_store_db.py, full, 9000100437, -p10, -f, -u, bergonzinie, -i, 3c75977c-6996-417d-b673-3366cee95fab]

che tradotto diventa
```sh
/rnd/apps/interpreters/python/bin/python /home/possedema/guest/posws/bin/poswsbe/pos_export_to_store_db.py full 9000100437 -p10 -f -u bergonzinie

/rnd/apps/interpreters/python/bin/python /home/possedema/guest/posws/bin/poswsbe/pos_export_to_store_sw.py full 9000100437 -p10 -f -u bergonzinie
```

14. apro in un altro tab il terminale sul BMS
    ```
    ssh possedema@pos-sede-ma-dev.mmfg.it
    ```
    ed eseguo il comando al punto precedente (13)

14. build su jenkins
15. mando al negozio un full del swf

                    OGNI ALTRA OPERAZIONE E DESCRITTA IN CONFLUENCES
                    OGNI ALTRA OPERAZIONE E DESCRITTA IN CONFLUENCES
                    OGNI ALTRA OPERAZIONE E DESCRITTA IN CONFLUENCES

vedi: https://confluence.mmfg.it/display/POS/Configurazione+nuovo+negozio+in+Cloud

16. aggiorno il file delle postazioni di test di posweb

<h5>Pagina Aggiornamento Negozi su BMS</h5>
> ?module=boss.aggiornamenti_negozi.action&program=search&sid=


!!! ATTENZIONE !!!!
################################################################################################
*SE POS_DOWNLOAD restituisce errore*
700 - Exception(cod_installazione non ammesso: 9002001007,):
devo
on cloud deve il cod_installazione della config.py matchare con la config pos_config_bundle
OPPURE
*controllare sul bms se installazione non sia locked. guardare pos_install_info*
SELECT locked FROM pos_install_info WHERE cod_installazione='9000108030' -- and update_type={update_type}
*e controllare che abbia dei pacchetti da inviare...*
select p.id, p.cod_installazione, p.update_type, p.version, p.requirements, p.properties, p.creation_mode, p.tot_files,
		f.progressivo, f.file_name, f.file_format, f.file_size, f.checksum, f.url, f.file_info
		from pos_install_packages p join pos_install_files f using (cod_installazione, update_type, version)
		where cod_installazione='9000108030'
OPPURE
controllare i logs del BMS perché potrebbe esserci un errore di connessione db....
################################################################################################


16. se contesto b2e deve arrivare ordine su test.om ed essere validato e passare da creato a delivery (o annullato se non cè giacenza ma va bene lo stesso)ù
17. cerco un capo su regione = del bms e brand=di riferimento e lo cerco con giacenza
17. se tutto ok devo aprire il bms di riferimento e guardare la tabella request_log_<annomese> e vedere che arrivino delle chiamate da ws_om per la giacenza
    questo per dire che ho configurato bene la chiamata di giacenza sul bms giusto e devo trovarmi in catena (della giacenza) un negozio del pool
