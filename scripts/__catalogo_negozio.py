# SCRIPT che dato il codice negozio(... e il suo ambiente...o vedere che parametri dover utilizzare)
# restituisce se il catalogo e prezzi è correttamente riempito

# creare una struttura con i dati più frequenti che vengono utilizzati dai negozi
# per compilare più o meno verosimilmente le query da fare

import sys
sys.path.extend(['/Users/emanuelebergonzini/Documents/Documents/scripts'])

import argparse
from commons.constants import CONNECTIONS
from commons.utils import exec_query_accept, split_queries

usage = "usage: catalogo_negozio.py [args]"
parser = argparse.ArgumentParser(usage)

parser.add_argument(
	"-a", "--environment",
	help="Ambiente", default="test"
)

parser.add_argument(
	"-n", "--cod_negozio",
	help="Codice negozio", required=True
)

parser.add_argument(
	"-notran", "--no-transactions", action="store_true", dest="no_transactions",
	help="Di default le query vengono gestite in transazione, se questo flag viene passato invece non saranno usate"
)

parser.add_argument(
	"-y", "--year", dest="year", help="anno_transazione", default="2024"
)

args = parser.parse_args()
config = vars(args)

# chiamo il crm e mi faccio dare l'ambiente corrispondente

anno = config["year"]

cod_negozio = config["cod_negozio"]

query = f"""SELECT codice_proprietario from negozi where negozio = '{cod_negozio}';"""

args.query = ""  # compatibiltà

if config["environment"] == "test":
	accept = {"CRM": set(CONNECTIONS["CRM"].keys()) for k in CONNECTIONS["CRM"]["TEST"].keys()}
if config["environment"] == "prod":
	accept = {"CRM": set(CONNECTIONS["CRM"].keys()) for k in CONNECTIONS["CRM"]["PROD"].keys()}

print(config)

env = config["environment"].upper()

result = exec_query_accept(accept, args, split_queries(query))
codice_proprietario = result[0]["codice_proprietario"]

accept = {env: {codice_proprietario}}

# pos_export_to_store_db.py, table: Catalogo

query = f"""
	SELECT s.*
	FROM pos_config_bundle AS b
	INNER JOIN pos_config_store AS s ON s.negozio=b.valore
	WHERE s.chiave="STORE_CHANNEL" AND s.valore<>"IN" AND (b.cod_installazione = "{cod_negozio}" or b.valore = "{cod_negozio}");
"""
result = exec_query_accept(accept, args, split_queries(query))
store_channel = result[0]["valore"]
print(f"store_channel is {store_channel}")

query = f"""
	SELECT s.*
	FROM pos_config_bundle AS b
	INNER JOIN pos_config_store AS s ON s.negozio=b.valore
	WHERE s.chiave="BRANDS_CATALOGO" AND s.valore<>"IN" AND (b.cod_installazione="{cod_negozio}" or b.valore = "{cod_negozio}");
"""
result = exec_query_accept(accept, args, split_queries(query))
brands_catalogo = result[0]["valore"]
print(f"brands_catalogo is {brands_catalogo}")

# brands_catalogo serve il mapping preciso...

query = f"""
	SELECT c.*
	FROM catalogo AS c
	LEFT JOIN catalogo_descrizioni AS t_classe ON (t_classe.tipo="classe" AND t_classe.lingua="ITAL" AND t_classe.chiave=CONCAT(c.societa,'.',c.classe))
	LEFT JOIN catalogo_descrizioni AS t_colore ON (t_colore.tipo="colore" AND t_colore.lingua="ITAL" AND t_colore.chiave=CONCAT(c.societa,'.',c.colore))
	LEFT JOIN catalogo_descrizioni AS t_taglia ON (t_taglia.tipo="taglia" AND t_taglia.lingua="ITAL" AND t_taglia.chiave=CONCAT(c.societa,'.',c.codice_tg,'.',c.indice_tg,".HK"))
	LEFT JOIN catalogo_descrizioni AS t_taglia_default ON (t_taglia_default.tipo="taglia" AND t_taglia_default.lingua="ITAL" AND t_taglia_default.chiave=CONCAT(c.societa,".",c.codice_tg,".",c.indice_tg,".IT"))
	LEFT JOIN catalogo_dbg_b2c_category AS cdbc ON c.societa = cdbc.societa AND c.classe = cdbc.classe
	LEFT JOIN catalogo_dbg AS cdbg ON c.sku=cdbg.barcode_negozio
	LEFT JOIN catalogo_dbg_uscite_collezione ctu ON c.societa = ctu.societa AND c.anno = ctu.anno AND c.stagione = ctu.stagione AND c.uscita_collezione = ctu.uscita_collezione
	WHERE c.anno="{anno}" AND c.stagione="1" AND c.societa="{brands_catalogo}";
"""
result = exec_query_accept(accept, args, split_queries(query))
print(result)

# chiamo il bms corrispondente ed esegue alcune query...

"""
-- CATALOGO --
SELECT s.*
FROM pos_config_bundle AS b
INNER JOIN pos_config_store AS s ON s.negozio=b.valore
WHERE s.chiave='STORE_CHANNEL' AND s.valore<>'IN' AND b.cod_installazione='9001101012'; -- NF

SELECT s.*
FROM pos_config_bundle AS b
INNER JOIN pos_config_store AS s ON s.negozio=b.valore
WHERE s.chiave='BRANDS_CATALOGO' AND s.valore<>'IN' AND b.cod_installazione='9001101012'; -- MR, DT --> MR

SELECT c.*
FROM catalogo AS c
LEFT JOIN catalogo_descrizioni AS t_classe ON (t_classe.tipo='classe' AND t_classe.lingua='ITAL' AND t_classe.chiave=CONCAT(c.societa,'.',c.classe))
LEFT JOIN catalogo_descrizioni AS t_colore ON (t_colore.tipo='colore' AND t_colore.lingua='ITAL' AND t_colore.chiave=CONCAT(c.societa,'.',c.colore))
LEFT JOIN catalogo_descrizioni AS t_taglia ON (t_taglia.tipo='taglia' AND t_taglia.lingua='ITAL' AND t_taglia.chiave=CONCAT(c.societa,'.',c.codice_tg,'.',c.indice_tg,'.HK'))
LEFT JOIN catalogo_descrizioni AS t_taglia_default ON (t_taglia_default.tipo='taglia' AND t_taglia_default.lingua='ITAL' AND t_taglia_default.chiave=CONCAT(c.societa,'.',c.codice_tg,'.',c.indice_tg,'.IT'))
LEFT JOIN catalogo_dbg_b2c_category AS cdbc ON c.societa = cdbc.societa AND c.classe = cdbc.classe
LEFT JOIN catalogo_dbg AS cdbg ON c.sku=cdbg.barcode_negozio
LEFT JOIN catalogo_dbg_uscite_collezione ctu ON c.societa = ctu.societa AND c.anno = ctu.anno AND c.stagione = ctu.stagione AND c.uscita_collezione = ctu.uscita_collezione
WHERE c.anno='2024' AND c.stagione='1' AND c.societa='MM'; -- > la società MR diventa MM

-- PREZZI --

SELECT s.*
FROM pos_config_bundle AS b
INNER JOIN pos_config_store AS s ON s.negozio=b.valore
WHERE s.chiave IN ('LISTINO_ESTESO_ENABLED', 'PREZZI_EVENTO_ENABLED', 'PREZZI_EMPLOYEE_ENABLED',
'PREZZI_PROMOTION_ENABLED', 'PREZZI_FROM_DBG', 'BOARDING_PASS_ENABLED') AND s.valore<>'IN' AND b.cod_installazione='9001101012'; -- tutto a 0
;

-- pos_prezzi_negozi_ perché false la condizione >> nazione == 'IT' and codice_proprietario != "FRH" and codice_proprietario not in ITA_EXPORT_DA_POS_PREZZI <<
;
SELECT '' AS cod_negozio, c.modello_retail AS modello, '' AS variante, p.pezzo,
				p.tipo_prezzo, 0 AS id_listino, '' AS data_inizio_validita, '' AS data_fine_validita, p.prezzo,
				p.valuta AS divisa, '0.00' AS perc, '20241' AS annostag, MAX(p.upd_datetime) as data_modifica
FROM catalogo_prezzi AS p
JOIN catalogo c USING (societa, anno, stagione, modello, pezzo)
WHERE tipo_prezzo IN ('V')
AND anno='2024' AND stagione='1'
AND nazione='HK'
AND modello_retail NOT LIKE '0000000%'
GROUP BY p.societa, p.anno, p.stagione, c.modello_retail, p.pezzo, p.nazione, p.valuta, p.tipo_prezzo;


SELECT p.negozio AS cod_negozio, p.modello, p.unita_vendibile AS pezzo, p.tipo_prezzo,
0 AS id_listino, p.data_inizio_validita, p.data_fine_validita, p.prezzo, p.divisa, p.perc, p.annostag, p.modificato AS data_modifica
FROM pos_prezzi_negozi_20241 p
WHERE p.negozio IN ('1101012')
AND tipo_prezzo IN ('V') AND data_inizio_validita != ''
"""