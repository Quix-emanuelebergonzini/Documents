quando la b2e fa una vendita arriva un payload che viene intercettato da posweb
SaleRest (controller) _set_vendita


su app nella configurazione:

cassa 01 (non scrivere 1)

url è ad esempio https://dos-dt-it.posweb.mmfg.it/api/v1
oppure https://pos-co.linmara.com/api/v1

Use test portal ==> attivare per test
Ledwall         ==> roba di diffusione tessile (schermi/monitor grandi)... non da usare ...

Da usare queste qua sotto anche nella configurazione app su tablet
https://bms.linmara.com/api/data/v1/b2e/traduzioni?filter[lingua]=zh
https://bms-uat.linmara.com ==> basic auth gbmax / Au8sZ4CNpZ0nGBW1 per test/uat
https://bms.linmara.com ==> basic auth gbmax / Z91arb0Mxq9oTj3S per prod


Picking URL http://192.168.1.110:8080/ui/api ==> roba vecchi di diffusione tessile
Username dtrfid
Password dtRF!d

da leggere ? https://developer.chrome.com/blog/devtools-tips-34?hl=it

vedi anche https://maxmarafashiongroup.atlassian.net/browse/REX-53328

se ho bisogno di giacenza su macchina di test imbroglio modificando il file
site/bin/backend/stock/service.py il dizionario mettendo valori fissi....