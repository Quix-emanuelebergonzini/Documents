from itertools import groupby
from operator import itemgetter

import sqlite_access
import config_store
import json

pard = config_store.application_parameters()

brand = 'MC'
nome_principale = 'ARAK'
modello_principale = '6101044402'
cod_negozio = '3201008'  # dos-dt-au
lingua = 'INGL'

query = """
SELECT distinct nome as c, nome_principale as p
FROM catalogo
WHERE nome = '{nome_principale}' OR nome_principale = '{nome_principale}'
""".format(nome_principale=nome_principale)

query = """
SELECT cat.modello_principale
FROM catalogo_b2e cat
JOIN catalogo_b2e_prezzi catprezzi on (
    cat.modello_principale = catprezzi.modello_principale 
    and catprezzi.cod_negozio = '{cod_negozio}'
)
WHERE 1=1  AND cat.cod_marchio = '{brand}' AND cat.nome_principale IN ('{nome_principale}')  
ORDER BY cat.nome_principale
LIMIT 0,10
""".format(cod_negozio=cod_negozio, brand=brand, nome_principale=nome_principale)

('7101014606', '', 'MAGENTA', '7101024606', '6', 'MR', 'MR', 'MM', '', '001', '4', '71010246060014', '28', '', 'Skirt', '10', '20241', 12, None, None, None,
 None, None, None,
 '[["71010146060011","1","",1,""],["71010146060012","2","",2,""],["71010146060013","3","",3,""],["71010146060014","4","",4,""],["71010146060015","5","",5,""],["71010146060016","6","",6,""],["71010146060017","7","",7,""],["71010146060018","8","",8,""],["71010246060011","1","25",9,""],["71010246060012","2","26",10,""],["71010246060013","3","27",11,""],["71010246060014","4","28",12,""]]',
 'STAGIONALE', 0)
query = """
SELECT cat.modello_principale                                                  code,
		cat.colore,
       cat.nome_principale                                                     name,
       cat.modello,
       cat.cod_sottocategoria_b2c,
       cat.cod_marchio                                                         brand,
       cat.cod_marchio_originale                                               brand_originale,
       cat.societa                                                             societa,
       cat.composizione                                                        composition,
       cat.variante,
       cat.taglia,
       cat.sku,
       IFNULL(IFNULL(cd_taglia.descrizione, cd_taglia_def.descrizione), '') as desc_taglia,
       IFNULL(cd_colore.descrizione, '')                                    as desc_colore,
       IFNULL(cd_classe.descrizione, '')                                    as desc_classe,
       cat.classe,
       cat.annostag,
       cat.indice_tg,
       NULL                                                                    washing_description,
       NULL                                                                    technical_description,
       NULL                                                                    emotional_description,
       cda.listing,
       cda.swatch
        ,
       cda.details,
       cat.campi_aggregati,
       cat.stagionale
        ,
       CASE WHEN 1 = 0 THEN 1 ELSE 0 END                                    AS priority
FROM catalogo_b2e_varianti cat
         LEFT JOIN catalogo_digital_asset cda ON cat.modello_principale = cda.modello AND cat.variante = cda.variante

         LEFT JOIN catalogo_descrizione cd_taglia
                   ON (cd_taglia.chiave = cat.societa || '.' || cat.codice_taglia || '.' || cat.taglia || '.AU' AND cd_taglia.tipo_descrizione = 'taglia')

         LEFT JOIN catalogo_descrizione cd_taglia_def ON (cd_taglia_def.chiave = cat.societa || '.' || cat.codice_taglia || '.' || cat.taglia ||
                                                          '.IT' AND cd_taglia_def.tipo_descrizione = 'taglia_default')
         LEFT JOIN catalogo_descrizione cd_classe
                   ON (cd_classe.chiave = cat.societa || '.' || cat.classe AND cd_classe.tipo_descrizione = 'classe' AND cd_classe.lingua = '{lingua}')
         LEFT JOIN catalogo_descrizione cd_colore
                   ON (cd_colore.chiave = cat.societa || '.' || cat.colore AND cd_colore.tipo_descrizione = 'colore' AND cd_colore.lingua = '{lingua}')

WHERE 1 = 1
  AND cat.cod_marchio = '{brand}'  AND cat.nome_principale IN ('{nome_principale}')   AND cat.modello_principale IN ('{modello_principale}')
ORDER BY cat.modello_principale
""".format(brand=brand, nome_principale=nome_principale, modello_principale=modello_principale, lingua=lingua)

pard["mysql_query"] = query
rows = sqlite_access.sqlite_dict(pard, dbname=pard['CATALOG_DB_FILE'])

item_mod = {'variants': []}
variants_order = itemgetter('variante', 'desc_colore')
size_order = lambda c: c["indice_tg"] if c["indice_tg"] is not None else 0

for key, group in groupby(rows, itemgetter("code")):
	g = []
	for variant_group in group:
		vg = dict(variant_group)
		for grouped_attrs in json.loads(vg.pop("campi_aggregati")):
			item_sku = vg.copy()
			if len(grouped_attrs) == 4:
				# Una volta aggiunto il campo ean su tutti gli ambienti questo ramo di codice
				# può essere rimosso
				item_sku["sku"], item_sku["taglia"], item_sku["desc_taglia"], item_sku["indice_tg"] = grouped_attrs
				item_sku["ean"] = ""
			else:
				item_sku["sku"], item_sku["taglia"], item_sku["desc_taglia"], item_sku["indice_tg"], item_sku["ean"] = grouped_attrs
			g.append(item_sku)

for key_var, group_var in groupby(sorted(g, key=variants_order), variants_order):
	gr = list(group_var)
	item_mod['variants'].append(
		{
			'code': key_var[0],
			'description': key_var[1],
			'priority': gr[0]["priority"],
			'listing_img': gr[0]["listing"],
			'swatch_img': gr[0]["swatch"],
			'details_img': gr[0]["details"] if not gr[0]["details"] else json.loads(
				gr[0]["details"]),
			'sizes': [
				{
					'code': item['taglia'],
					'description': item['desc_taglia'],
					'sku': item['sku'],
					'ean': item['ean'],
				}
				for item in sorted(gr, key=size_order)
			]
		}
	)
