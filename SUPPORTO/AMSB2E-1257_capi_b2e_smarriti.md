hk-PROD

1101062 - MA STORE
1101062|COUNTRY_CODE|HK|2019-11-22 15:50:57
1101062|AVAILABLE_BRANDS|MA,DT|2019-12-17 13:53:46
SELECT DISTINCT c.cod_marchio, c.nome, c.annostag
from catalogo c
INNER JOIN prezzi p ON p.modello=c.modello AND p.pezzo=c.pezzo AND p.tipo_prezzo="V" AND p.data_inizio_validita <= "20210119"
where 1 and c.modello = '7041011102' and c.sku_padre = "" AND c.validita_variante IN ("V", "B") AND c.versione_modello = "V"
and c.data_consegna IS NOT NULL AND c.data_consegna <> "00000000" AND c.data_consegna <= '20210119'
and p.cod_negozio in ('1101118') and c.cod_marchio in ('MA', 'DT', 'IB');

1101024 - IB STORE
1101024|COUNTRY_CODE|HK|2019-11-22 16:22:42
1101024|AVAILABLE_BRANDS|IB,DT,MA|2021-01-08 16:33:17
SELECT DISTINCT c.cod_marchio, c.nome, c.annostag
from catalogo c
INNER JOIN prezzi p ON p.modello=c.modello AND p.pezzo=c.pezzo AND p.tipo_prezzo="V" AND p.data_inizio_validita <= "20210119"
where 1 and c.modello = '3021071102' and c.sku_padre = "" AND c.validita_variante IN ("V", "B") AND c.versione_modello = "V"
and c.data_consegna IS NOT NULL AND c.data_consegna <> "00000000" AND c.data_consegna <= '20210119'
and p.cod_negozio in ('1101065');


se non trovo un capo nel catalogo_b2e e c'è nel catalogo a negozio
probabilmente sono i brands (AVAILABLE_BRANDS)
posso aggiungere tranquillamente il brands mancante alla configurazione di negozio

se non scende a catalogo sul negozio bisogna guardare BRANDS_CATALOGO su sede

controllo che il capo si veda su b2e con il servizio
/api/v1/posweb/models?debug=1&filter[brand]=IB&filter[model]=7041011102&filter[name]=WALES
Query che avvengono:

SELECT distinct nome as c, nome_principale as p FROM catalogo WHERE nome = 'ILONGDISCO'OR nome_principale = 'ILONGDISCO';

SELECT cat.modello_principale
FROM catalogo_b2e cat
JOIN catalogo_b2e_prezzi catprezzi on (
	cat.modello_principale = catprezzi.modello_principale 
	and catprezzi.cod_negozio = '0100107'
)
WHERE 1=1  AND cat.nome_principale IN ('ILONGDISCO')  
ORDER BY cat.nome_principale
LIMIT 0,10;