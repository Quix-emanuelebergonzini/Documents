il colore deriva da questa tabella _k_20240612090917_740_catalogo_b2e_varianti (temporanea durante la generazione del catalogo).
il campo arriva da catalogo (campo colore) che deve esistere su BMS ed arrivare a negozio

INSERT INTO _k_20240612090917_740_catalogo_b2e_varianti
SELECT DISTINCT c.* , '[' || GROUP_CONCAT(DISTINCT('["' || c.sku || '","' || c.taglia || '","' || c.desc_taglia || '",' || IFNULL(c.indice_tg, 'null') || ',"' || c.ean || '"' || ']')) || ']'          
FROM catalogo c        
INNER JOIN prezzi p  ON p.modello=c.modello AND p.pezzo=c.pezzo AND p.tipo_prezzo="V" AND p.data_inizio_validita <= "20240612"        
WHERE 1  AND c.sku_padre = "" AND c.validita_variante IN ("V", "B") AND c.versione_modello = "V"                AND c.cod_marchio in ('MR') AND 
  ((c.cod_marchio_originale IN('SP','MM','WE') AND c.annostag='20192')OR(c.cod_marchio_originale IN('MC','WE','MM','SP') AND c.annostag='20211')OR(c.cod_marchio_originale IN('MC','WE','MM','SP') AND c.annostag='20212')OR(c.cod_marchio_originale IN('MC','WE','MM','SP') AND c.annostag='20221')OR(c.cod_marchio_originale IN('MC','WE','MM','SP') AND c.annostag='20222')OR(c.cod_marchio_originale IN('MR','MM','MC','SP','WE','IN') AND c.annostag='20232')OR(c.cod_marchio_originale IN('MR','MM','WE','SP','IN','MC') AND c.annostag='20241')OR(c.cod_marchio_originale IN('WE','MM','SP') AND c.annostag='20202' AND c.stagionale='PERMANENTE'))
==> devono essere attive le regole di catalogo per l'anno da considerare     
AND p.cod_negozio in ('3201003')           GROUP BY c.modello_principale, c.variante 

=============================================
=============================================
=============================================
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
## ==> dove codice_taglia è codice_tg sul BMS e taglia è indice_tg sul BMS

         LEFT JOIN catalogo_descrizione cd_taglia_def ON (cd_taglia_def.chiave = cat.societa || '.' || cat.codice_taglia || '.' || cat.taglia ||
                                                          '.IT' AND cd_taglia_def.tipo_descrizione = 'taglia_default')
         LEFT JOIN catalogo_descrizione cd_classe
                   ON (cd_classe.chiave = cat.societa || '.' || cat.classe AND cd_classe.tipo_descrizione = 'classe' AND cd_classe.lingua = 'INGL')
         LEFT JOIN catalogo_descrizione cd_colore
                   ON (cd_colore.chiave = cat.societa || '.' || cat.colore AND cd_colore.tipo_descrizione = 'colore' AND cd_colore.lingua = 'INGL')

WHERE 1 = 1
  AND cat.cod_marchio = 'MR'  AND cat.nome_principale IN ('MAGENTA')   AND cat.modello_principale IN ('MAGENTA')
ORDER BY cat.modello_principale
=============================================
=============================================
=============================================
{
    "data": [
        {
            "attributes": {
                "code": "7101014606",
                "name": "MAGENTA",
                "cod_categoria": "2",
                "desc_categoria": "Clothing",
                "cod_sottocategoria": "6",
                "desc_sottocategoria": "Skirts",
                "brand": "MR",
                "brand_originale": "MR",
                "societa": "MM",
                "classe": "10",
                "desc_classe": "Skirt",
                "annostag": "20241",
                "composition": "",
                "washing_description": null,
                "technical_description": null,
                "emotional_description": null,
                "variants": [
                    {
                        "code": "001", ==> fallback del colore se "description" è vuoto ==> (dal campo della query (catalogo_b2e_varianti) cat.variante [vedi catalogo su BMS])
                        "description": "", ==> colore (da catalogo_descizioni per tipo='colore' and chiave = 'societa.[cat.colore]' dove cat è catalogo.colore)
                        "priority": 0,
                        "listing_img": null,
                        "swatch_img": null,
                        "details_img": null,
                        "sizes": [
                            {
                                "code": "1",
                                "description": "", ==> deriva da desc_taglia che è un campo composto su catalogo_b2e_varianti
                                "sku": "71010146060011",
                                "ean": ""
                            },
                            {
                                "code": "2",
                                "description": "",
                                "sku": "71010146060012",
                                "ean": ""
                            },
                            {
                                "code": "3",
                                "description": "",
                                "sku": "71010146060013",
                                "ean": ""
                            },
                            {
                                "code": "4",
                                "description": "",
                                "sku": "71010146060014",
                                "ean": ""
                            },
                            {
                                "code": "5",
                                "description": "",
                                "sku": "71010146060015",
                                "ean": ""
                            },
                            {
                                "code": "6",
                                "description": "",
                                "sku": "71010146060016",
                                "ean": ""
                            },
                            {
                                "code": "7",
                                "description": "",
                                "sku": "71010146060017",
                                "ean": ""
                            },
                            {
                                "code": "8",
                                "description": "",
                                "sku": "71010146060018",
                                "ean": ""
                            },
                            {
                                "code": "1",
                                "description": "25",
                                "sku": "71010246060011",
                                "ean": ""
                            },
                            {
                                "code": "2",
                                "description": "26",
                                "sku": "71010246060012",
                                "ean": ""
                            },
                            {
                                "code": "3",
                                "description": "27",
                                "sku": "71010246060013",
                                "ean": ""
                            },
                            {
                                "code": "4",
                                "description": "28",
                                "sku": "71010246060014",
                                "ean": ""
                            }
                        ],
                        "color_img": "https://media.mmfg.it/bin/imageService?version=10&username=POSWEB&service=color&societa=MR&modello10=7101014606&variante=001&tts=1718180871&rnd=26653&dhashed=ud3DB3/UtXhfgCGCQF7Z7k9%2BXy4%3D"
                    }
                ],
                "stagionale": "STAGIONALE",
                "price_type_applied": "V",
                "desc_classe_it": "Gonna",
                "prices": [
                    {
                        "price_type": "V",
                        "price": 1435.0
                    }
                ],
                "iva": 10.0,
                "model_img": "https://media.mmfg.it/bin/imageService?version=10&username=POSWEB&service=model&societa=MR&modello10=7101014606&variante=&tts=1718180871&rnd=4850&dhashed=EuJvt7HvnJDaTj3PVyhOP8yb03c%3D"
            },
            "type": "models",
            "id": "7101014606"
        }
    ]
}