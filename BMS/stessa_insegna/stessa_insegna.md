## BMSMMJ - stessa_insegna ##
# consumatrici che appartengono appunto alla stessa insegna (STORE_SIGN), quindi se non si trova nella ricerca
# in autocomplete
# la si può trovare con la ricerca globale (es, https://jira.mmfg.it/browse/REX-22944)
SELECT c.pk_consumer, c.nome, c.cognome, cn.negozio, cs.valore, GROUP_CONCAT(DISTINCT substring(cs.valore, 1, 2)),
IF(GROUP_CONCAT(DISTINCT substring(cs.valore, 1, 2)) REGEXP "MM|WE|SP", "1", "0") AS stessa_insegna
FROM pos_consumer c
JOIN pos_consumer_negozio cn USING (pk_consumer)
JOIN pos_config_store cs ON (cn.negozio=cs.negozio AND cs.chiave='BRANDS_CATALOGO')
-- WHERE cn.negozio = '0801204'
GROUP BY pk_consumer
-- LIMIT 100
;

SELECT c.* , IF(GROUP_CONCAT(DISTINCT substring(cs.valore, 1, 2)) REGEXP "MM|WE|SP", "1", "0") AS stessa_insegna FROM pos_consumer c JOIN pos_consumer_negozio cn USING (pk_consumer) LEFT JOIN pos_consumer_nome_alfabeto n USING(pk_consumer) LEFT JOIN pos_consumer_indirizzo_alfabeto i USING(pk_consumer) INNER JOIN pos_config_store cs ON (cs.negozio=cn.negozio AND cs.chiave='BRANDS_CATALOGO') WHERE 1=1 AND ((c.cognome = "TAKIZAWA" AND c.nome = "MITHUYO") OR (n.cognome = "TAKIZAWA" AND n.nome = "MITHUYO")) AND cn.timestamp_fine IS NULL GROUP BY pk_consumer LIMIT 100;

## BMS ##
SELECT c.pk_consumer, c.nome, c.cognome, cn.negozio, am.catena_retail, GROUP_CONCAT(DISTINCT substring(am.catena_retail, 1, 2)),
IF(GROUP_CONCAT(DISTINCT substring(am.catena_retail, 1, 2)) REGEXP "MM|WE|SP", "1", "0") AS stessa_insegna
FROM pos_consumer c
JOIN pos_consumer_negozio cn USING (pk_consumer)
JOIN ana_soggetti_master am ON (am.`codice_gruppo`=cn.negozio)
WHERE cn.negozio = '0801204'
GROUP BY pk_consumer
-- LIMIT 100
;

PER SAPERE CHE TIPO DI NEGOZIO (SU BMS): SU ana_soggetti_master VEDI catena_retail
SU CRM DA consumer_negozio JOIN negozi USANDO IL CAMPO tipo_negozio


## CRM ##
from initiative.locator import locator as loc
serv = loc.get_service("CRMBackOffice")
filtro = {
    "cognome": "ZUNTINI",
    "nome": "MARTA", # OPPURE "LUCA"
    "enabled_search_decoded": True,
    "cod_negozio": "0100400",
    "search_extended_insegna": "MA",
}
serv.ricerca_consumatrici_da_pos(filtro, limit=100)


tipi_consenso = ['Profiling', 'Direct Marketing']
pk_consumer_list = ['11133478', '11133484']
filtro = {
	'pk_consumer': pk_consumer_list
}
brand_consensi = 'MC'
cod_negozio = '1001189'
from initiative.locator import locator as loc
service = loc.get_service('CRMBackOffice')
consumer_crm = service.ricerca_consumatrici_complete(filtro, brand_consensi=brand_consensi, tipi_consenso=tipi_consenso)
