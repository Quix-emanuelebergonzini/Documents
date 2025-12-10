il caso vuole che il capo si trovi ma non venga esposto il prezzo saldo
alla vendita. il servizio api/models restituisce il prezzo S e V
correttamente.

si può provare sulla macchina di produzione (con opzione -i !!!!) a generare
una vendita e vedere effettivamente che prezzo espone

attenzione alla chiave price_type_applied che applica il prezzo in base al listino!!!!
vedasi...
SELECT *
FROM listino_prezzi
WHERE tipo_prezzo in ('S', 'V') and data_inizio_validita <= '20210127' and data_fine_validita >= '20210127';

sulla tabella in sede deve esserci un riga per tale negozio e listino da applicare



FGNEG-0801100-1:posweb posweb$ ./bin/python ./bin/CeC.py -l 73648200030051 73648200030052 73648200030053 7364820003005004 73648200030055 -u assistenza -p kojak -i
Pk consumer: MCJ_166121
Capi in store:
Capi out store: 5
Spedizione (1 consumer, 0 store): 0
Stato (1 chiusa, 0 sospesa): 0
Login
Consumatrice: MCJ_166121 MICHIKO F
Richiesta tasse
{'data': {'attributes': {'cod_documento': '', 'codice_movimento': 'VENDITA', 'data_documento': '2021126', 'cod_vettore': '', 'data_modifica': '2021-01-26 22:05:37', 'dati_aggiuntivi': '', 'importo_finale': 99000.0, 'codice_stato': 'SUSPENDED', 'dati_documenti': '{"shipping_destination": "STORE"}', 'id_utente': 'assistenza', 'ora_documento': '22537', 'data_creazione': '2021-01-26 22:05:37', 'nota': '', 'tipo_applicazione_chiusura': 'DSMOBILE', 'sid': u'0z8kfltqnjlpdg', 'divisa': 'EUR', 'importo_pagato': 0, 'pk_consumer': 'MCJ_166121', 'id_postazione_apertura': '01', 'tipo_applicazione_apertura': 'DSMOBILE', 'numero_documento': 113, 'pagamenti': [], 'numero_stampa_documento': '', 'capi': [{'codice_movimento': 'VENDITA', 'data_modifica': '2021-01-26 22:05:37', 'iva': 10.0, 'ean': u'8033731800221', 'id_transazione': 0, 'flag_divisa': 0, 'sku_splitted': 0, 'cod_commessa': u'E284', 'tipo_importo': u'S', 'correzione_importo': 0, 'sku_created': 0, 'importo_finale': 19800, 'codice_stato': 'SUSPENDED', 'importo_iniziale': 19800, 'sku': u'73648200030051', 'nome': u'CESENA', 'cod_negozio': '0801100', 'classe': u'36', 'progressivo': 1, 'data_creazione': '2021-01-26 22:05:37', 'flag_promo': 0, 'sconto': 0, 'composizione': u'F:100WV', 'nota': '', 'sku_read': u'73648200030051', 'importo_custom': 19800, 'custom_data': '{"stock_type": "OUT_STORE", "desc_classe": "", "desc_taglia": "M2JM1", "variante": "005", "annostag": "20202"}', 'tipologia_merce': 'GARMENTS'}, {'codice_movimento': 'VENDITA', 'data_modifica': '2021-01-26 22:05:37', 'iva': 10.0, 'ean': u'8033731800221', 'id_transazione': 0, 'flag_divisa': 0, 'sku_splitted': 0, 'cod_commessa': u'E284', 'tipo_importo': u'S', 'correzione_importo': 0, 'sku_created': 0, 'importo_finale': 19800, 'codice_stato': 'SUSPENDED', 'importo_iniziale': 19800, 'sku': u'73648200030051', 'nome': u'CESENA', 'cod_negozio': '0801100', 'classe': u'36', 'progressivo': 2, 'data_creazione': '2021-01-26 22:05:37', 'flag_promo': 0, 'sconto': 0, 'composizione': u'F:100WV', 'nota': '', 'sku_read': u'73648200030051', 'importo_custom': 19800, 'custom_data': '{"stock_type": "OUT_STORE", "desc_classe": "", "desc_taglia": "M2JM1", "variante": "005", "annostag": "20202"}', 'tipologia_merce': 'GARMENTS'}, {'codice_movimento': 'VENDITA', 'data_modifica': '2021-01-26 22:05:37', 'iva': 10.0, 'ean': u'8033731800221', 'id_transazione': 0, 'flag_divisa': 0, 'sku_splitted': 0, 'cod_commessa': u'E284', 'tipo_importo': u'S', 'correzione_importo': 0, 'sku_created': 0, 'importo_finale': 19800, 'codice_stato': 'SUSPENDED', 'importo_iniziale': 19800, 'sku': u'73648200030051', 'nome': u'CESENA', 'cod_negozio': '0801100', 'classe': u'36', 'progressivo': 3, 'data_creazione': '2021-01-26 22:05:37', 'flag_promo': 0, 'sconto': 0, 'composizione': u'F:100WV', 'nota': '', 'sku_read': u'73648200030051', 'importo_custom': 19800, 'custom_data': '{"stock_type": "OUT_STORE", "desc_classe": "", "desc_taglia": "M2JM1", "variante": "005", "annostag": "20202"}', 'tipologia_merce': 'GARMENTS'}, {'codice_movimento': 'VENDITA', 'data_modifica': '2021-01-26 22:05:37', 'iva': 10.0, 'ean': u'8033731800221', 'id_transazione': 0, 'flag_divisa': 0, 'sku_splitted': 0, 'cod_commessa': u'E284', 'tipo_importo': u'S', 'correzione_importo': 0, 'sku_created': 0, 'importo_finale': 19800, 'codice_stato': 'SUSPENDED', 'importo_iniziale': 19800, 'sku': u'73648200030051', 'nome': u'CESENA', 'cod_negozio': '0801100', 'classe': u'36', 'progressivo': 4, 'data_creazione': '2021-01-26 22:05:37', 'flag_promo': 0, 'sconto': 0, 'composizione': u'F:100WV', 'nota': '', 'sku_read': u'73648200030051', 'importo_custom': 19800, 'custom_data': '{"stock_type": "OUT_STORE", "desc_classe": "", "desc_taglia": "M2JM1", "variante": "005", "annostag": "20202"}', 'tipologia_merce': 'GARMENTS'}, {'codice_movimento': 'VENDITA', 'data_modifica': '2021-01-26 22:05:37', 'iva': 10.0, 'ean': u'8033731800221', 'id_transazione': 0, 'flag_divisa': 0, 'sku_splitted': 0, 'cod_commessa': u'E284', 'tipo_importo': u'S', 'correzione_importo': 0, 'sku_created': 0, 'importo_finale': 19800, 'codice_stato': 'SUSPENDED', 'importo_iniziale': 19800, 'sku': u'73648200030051', 'nome': u'CESENA', 'cod_negozio': '0801100', 'classe': u'36', 'progressivo': 5, 'data_creazione': '2021-01-26 22:05:37', 'flag_promo': 0, 'sconto': 0, 'composizione': u'F:100WV', 'nota': '', 'sku_read': u'73648200030051', 'importo_custom': 19800, 'custom_data': '{"stock_type": "OUT_STORE", "desc_classe": "", "desc_taglia": "M2JM1", "variante": "005", "annostag": "20202"}', 'tipologia_merce': 'GARMENTS'}], 'flag_stampa_documento': 0, 'importo_iniziale': 99000.0, 'id_postazione_chiusura': '01', 'cod_cassiera': u'E284', 'cod_negozio': '0801100', 'cod_cassa': '01'}, 'type': 'sales'}}
Capo out store (73648200030051)               19800
Capo out store (73648200030051)               19800
Capo out store (73648200030051)               19800
Capo out store (73648200030051)               19800
Capo out store (73648200030051)               19800
Tassa STANDARD_ITEM                          9900.0
Totale                                     108900.0
==================================================================================================== KEY ====================================================================================================
WyJNQ0pfMTY2MTIxIiwgIiIsICI1IiwgIjAiLCAiMCJd
==================================================================================================== INPUT ====================================================================================================
{
    "data": {
        "attributes": {
            "cod_documento": "",
            "codice_movimento": "VENDITA",
            "data_documento": "2021126",
            "cod_vettore": "",
            "data_modifica": "2021-01-26 22:05:37",
            "dati_aggiuntivi": "",
            "importo_finale": 108900.0,
            "codice_stato": "SUSPENDED",
            "dati_documenti": "{\"shipping_destination\": \"STORE\"}",
            "id_utente": "assistenza",
            "ora_documento": "22537",
            "data_creazione": "2021-01-26 22:05:37",
            "nota": "",
            "tipo_applicazione_chiusura": "DSMOBILE",
            "sid": "0z8kfltqnjlpdg",
            "divisa": "EUR",
            "importo_pagato": 0,
            "pk_consumer": "MCJ_166121",
            "id_postazione_apertura": "01",
            "tipo_applicazione_apertura": "DSMOBILE",
            "numero_documento": 113,
            "pagamenti": [
                {
                    "codice_movimento": "CONTABILITA_TASSA",
                    "valuta": "JPY",
                    "data_modifica": "2021-01-26 13:05:37",
                    "data_creazione": "2021-01-26 13:05:37",
                    "progressivo": 1,
                    "dati_operazione": "{\"percentuale\": 10}",
                    "cod_negozio": "0801100",
                    "importo_finale": 9900.0,
                    "cod_operazione": "STANDARD_ITEM",
                    "importo_iniziale": 9900.0
                }
            ],
            "numero_stampa_documento": "",
            "capi": [
                {
                    "codice_movimento": "VENDITA",
                    "data_modifica": "2021-01-26 22:05:37",
                    "iva": 10.0,
                    "ean": "8033731800221",
                    "id_transazione": 0,
                    "flag_divisa": 0,
                    "sku_splitted": 0,
                    "cod_commessa": "E284",
                    "tipo_importo": "S",
                    "correzione_importo": 0,
                    "sku_created": 0,
                    "importo_finale": 19800,
                    "codice_stato": "SUSPENDED",
                    "importo_iniziale": 19800,
                    "sku": "73648200030051",
                    "nome": "CESENA",
                    "cod_negozio": "0801100",
                    "classe": "36",
                    "progressivo": 1,
                    "data_creazione": "2021-01-26 22:05:37",
                    "flag_promo": 0,
                    "sconto": 0,
                    "composizione": "F:100WV",
                    "nota": "",
                    "sku_read": "73648200030051",
                    "importo_custom": 19800,
                    "custom_data": "{\"stock_type\": \"OUT_STORE\", \"desc_classe\": \"\", \"desc_taglia\": \"M2JM1\", \"variante\": \"005\", \"annostag\": \"20202\"}",
                    "tipologia_merce": "GARMENTS"
                },
                {
                    "codice_movimento": "VENDITA",
                    "data_modifica": "2021-01-26 22:05:37",
                    "iva": 10.0,
                    "ean": "8033731800221",
                    "id_transazione": 0,
                    "flag_divisa": 0,
                    "sku_splitted": 0,
                    "cod_commessa": "E284",
                    "tipo_importo": "S",
                    "correzione_importo": 0,
                    "sku_created": 0,
                    "importo_finale": 19800,
                    "codice_stato": "SUSPENDED",
                    "importo_iniziale": 19800,
                    "sku": "73648200030051",
                    "nome": "CESENA",
                    "cod_negozio": "0801100",
                    "classe": "36",
                    "progressivo": 2,
                    "data_creazione": "2021-01-26 22:05:37",
                    "flag_promo": 0,
                    "sconto": 0,
                    "composizione": "F:100WV",
                    "nota": "",
                    "sku_read": "73648200030051",
                    "importo_custom": 19800,
                    "custom_data": "{\"stock_type\": \"OUT_STORE\", \"desc_classe\": \"\", \"desc_taglia\": \"M2JM1\", \"variante\": \"005\", \"annostag\": \"20202\"}",
                    "tipologia_merce": "GARMENTS"
                },
                {
                    "codice_movimento": "VENDITA",
                    "data_modifica": "2021-01-26 22:05:37",
                    "iva": 10.0,
                    "ean": "8033731800221",
                    "id_transazione": 0,
                    "flag_divisa": 0,
                    "sku_splitted": 0,
                    "cod_commessa": "E284",
                    "tipo_importo": "S",
                    "correzione_importo": 0,
                    "sku_created": 0,
                    "importo_finale": 19800,
                    "codice_stato": "SUSPENDED",
                    "importo_iniziale": 19800,
                    "sku": "73648200030051",
                    "nome": "CESENA",
                    "cod_negozio": "0801100",
                    "classe": "36",
                    "progressivo": 3,
                    "data_creazione": "2021-01-26 22:05:37",
                    "flag_promo": 0,
                    "sconto": 0,
                    "composizione": "F:100WV",
                    "nota": "",
                    "sku_read": "73648200030051",
                    "importo_custom": 19800,
                    "custom_data": "{\"stock_type\": \"OUT_STORE\", \"desc_classe\": \"\", \"desc_taglia\": \"M2JM1\", \"variante\": \"005\", \"annostag\": \"20202\"}",
                    "tipologia_merce": "GARMENTS"
                },
                {
                    "codice_movimento": "VENDITA",
                    "data_modifica": "2021-01-26 22:05:37",
                    "iva": 10.0,
                    "ean": "8033731800221",
                    "id_transazione": 0,
                    "flag_divisa": 0,
                    "sku_splitted": 0,
                    "cod_commessa": "E284",
                    "tipo_importo": "S",
                    "correzione_importo": 0,
                    "sku_created": 0,
                    "importo_finale": 19800,
                    "codice_stato": "SUSPENDED",
                    "importo_iniziale": 19800,
                    "sku": "73648200030051",
                    "nome": "CESENA",
                    "cod_negozio": "0801100",
                    "classe": "36",
                    "progressivo": 4,
                    "data_creazione": "2021-01-26 22:05:37",
                    "flag_promo": 0,
                    "sconto": 0,
                    "composizione": "F:100WV",
                    "nota": "",
                    "sku_read": "73648200030051",
                    "importo_custom": 19800,
                    "custom_data": "{\"stock_type\": \"OUT_STORE\", \"desc_classe\": \"\", \"desc_taglia\": \"M2JM1\", \"variante\": \"005\", \"annostag\": \"20202\"}",
                    "tipologia_merce": "GARMENTS"
                },
                {
                    "codice_movimento": "VENDITA",
                    "data_modifica": "2021-01-26 22:05:37",
                    "iva": 10.0,
                    "ean": "8033731800221",
                    "id_transazione": 0,
                    "flag_divisa": 0,
                    "sku_splitted": 0,
                    "cod_commessa": "E284",
                    "tipo_importo": "S",
                    "correzione_importo": 0,
                    "sku_created": 0,
                    "importo_finale": 19800,
                    "codice_stato": "SUSPENDED",
                    "importo_iniziale": 19800,
                    "sku": "73648200030051",
                    "nome": "CESENA",
                    "cod_negozio": "0801100",
                    "classe": "36",
                    "progressivo": 5,
                    "data_creazione": "2021-01-26 22:05:37",
                    "flag_promo": 0,
                    "sconto": 0,
                    "composizione": "F:100WV",
                    "nota": "",
                    "sku_read": "73648200030051",
                    "importo_custom": 19800,
                    "custom_data": "{\"stock_type\": \"OUT_STORE\", \"desc_classe\": \"\", \"desc_taglia\": \"M2JM1\", \"variante\": \"005\", \"annostag\": \"20202\"}",
                    "tipologia_merce": "GARMENTS"
                }
            ],
            "flag_stampa_documento": 0,
            "importo_iniziale": 108900.0,
            "id_postazione_chiusura": "01",
            "cod_cassiera": "E284",
            "cod_negozio": "0801100",
            "cod_cassa": "01"
        },
        "type": "sales"
    }
}

query utilizzate per la ricerca:
SELECT DISTINCT c.modello_principale, p.cod_negozio, REPLACE(MAX(p.data_inizio_validita || '|' || p.prezzo), MAX(p.data_inizio_validita || '|'), '') as prezzo
FROM catalogo c
    INNER JOIN prezzi p
ON p.modello=c.modello AND p.pezzo=c.pezzo AND p.tipo_prezzo='V' AND p.data_inizio_validita <= '20210126'
WHERE c.sku_padre = ''
  AND c.validita_variante IN ('V', 'B')
  AND c.versione_modello = 'V' AND
    c.data_consegna IS NOT NULL
  AND c.data_consegna <> '00000000'
  AND c.data_consegna <= '20210126'
  AND c.cod_marchio in ('MC') AND ((c.cod_marchio_originale='MC' AND c.annostag='20201' AND c.stagionale='PERMANENTE')
      OR (c.cod_marchio_originale='MC' AND c.annostag='20202' AND c.stagionale='PERMANENTE')
      OR (c.cod_marchio_originale='MC' AND c.annostag='20211' AND c.stagionale='PERMANENTE'))
  AND p.cod_negozio IN ('0801100')

GROUP BY c.modello_principale, p.cod_negozio;

select *
from prezzi
where modello = '7364820003' and tipo_prezzo = 'V' AND data_inizio_validita <= '20210126';


SELECT cat.modello_principale, catprezzi.*
FROM catalogo_b2e cat
         JOIN catalogo_b2e_prezzi catprezzi on (
        cat.modello_principale = catprezzi.modello_principale
        and catprezzi.cod_negozio = '0801100'
    )
WHERE 1 = 1
  AND cat.modello_principale IN ('7364820003')
ORDER BY cat.nome_principale
LIMIT 0,10;


servizio api/models
http://localhost:9000/api/v1/posweb/models?filter[model]=7364820003
{
    "data": [
        {
            "attributes": {
                "technical_description": null,
                "code": "7364820003",
                "desc_classe": "Sweater",
                "name": "CESENA",
                "desc_classe_it": "Maglia-Canottiera-Top",
                "cod_sottocategoria": "7",
                "societa": "MN",
                "brand": "MC",
                "classe": "36",
                "emotional_description": null,
                "desc_sottocategoria": "Knitwear",
                "annostag": "20202",
                "price_type_applied": "V",
                "cod_categoria": "2",
                "prices": [
                    {
                        "price_type": "S",
                        "price": 19800
                    },
                    {
                        "price_type": "V",
                        "price": 33000
                    }
                ],
                "composition": "F: 100% Virgin Wool",
                "variants": [
                    {
                        "code": "001",
                        "description": "",
                        "sizes": [
                            {
                                "sku": "73648200030011",
                                "code": "1",
                                "description": "XS"
                            },
                            {
                                "sku": "73648200030012",
                                "code": "2",
                                "description": "S"
                            },
                            {
                                "sku": "73648200030013",
                                "code": "3",
                                "description": "M"
                            },
                            {
                                "sku": "73648200030014",
                                "code": "4",
                                "description": "L"
                            }
                        ],
                        "listing_img": "/MC/2020/2/7364820003/001/s3master/7364820003001-z-cesena-maglia-canottiera-top_thumbnail.jpg",
                        "priority": 0,
                        "swatch_img": "/MC/2020/2/7364820003/001/s3swatch/SW-7364820003001.jpg",
                        "details_img": [
                            "/MC/2020/2/7364820003/001/s3master/7364820003001-a-cesena-maglia-canottiera-top_normal.jpg",
                            "/MC/2020/2/7364820003/001/s3details/7364820003001-c-cesena-maglia-canottiera-top_normal.jpg"
                        ]
                    },
                    {
                        "code": "002",
                        "description": "",
                        "sizes": [
                            {
                                "sku": "73648200030021",
                                "code": "1",
                                "description": "XS"
                            },
                            {
                                "sku": "73648200030022",
                                "code": "2",
                                "description": "S"
                            },
                            {
                                "sku": "73648200030023",
                                "code": "3",
                                "description": "M"
                            },
                            {
                                "sku": "73648200030024",
                                "code": "4",
                                "description": "L"
                            }
                        ],
                        "listing_img": "/MC/2020/2/7364820003/002/s3master/7364820003002-z-cesena-maglia-canottiera-top_thumbnail.jpg",
                        "priority": 0,
                        "swatch_img": "/MC/2020/2/7364820003/002/s3swatch/SW-7364820003002.jpg",
                        "details_img": [
                            "/MC/2020/2/7364820003/002/s3details/7364820003002-c-cesena-maglia-canottiera-top_normal.jpg",
                            "/MC/2020/2/7364820003/002/s3master/7364820003002-a-cesena-maglia-canottiera-top_normal.jpg"
                        ]
                    },
                    {
                        "code": "003",
                        "description": "",
                        "sizes": [
                            {
                                "sku": "73648200030031",
                                "code": "1",
                                "description": "XS"
                            },
                            {
                                "sku": "73648200030032",
                                "code": "2",
                                "description": "S"
                            },
                            {
                                "sku": "73648200030033",
                                "code": "3",
                                "description": "M"
                            },
                            {
                                "sku": "73648200030034",
                                "code": "4",
                                "description": "L"
                            }
                        ],
                        "listing_img": "/MC/2020/2/7364820003/003/s3master/7364820003003-z-cesena-maglia-canottiera-top_thumbnail.jpg",
                        "priority": 0,
                        "swatch_img": "/MC/2020/2/7364820003/003/s3swatch/SW-7364820003003.jpg",
                        "details_img": [
                            "/MC/2020/2/7364820003/003/s3master/7364820003003-a-cesena-maglia-canottiera-top_normal.jpg",
                            "/MC/2020/2/7364820003/003/s3details/7364820003003-c-cesena-maglia-canottiera-top_normal.jpg"
                        ]
                    },
                    {
                        "code": "004",
                        "description": "",
                        "sizes": [
                            {
                                "sku": "73648200030041",
                                "code": "1",
                                "description": "XS"
                            },
                            {
                                "sku": "73648200030042",
                                "code": "2",
                                "description": "S"
                            },
                            {
                                "sku": "73648200030043",
                                "code": "3",
                                "description": "M"
                            },
                            {
                                "sku": "73648200030044",
                                "code": "4",
                                "description": "L"
                            }
                        ],
                        "listing_img": "/MC/2020/2/7364820003/004/s3master/7364820003004-z-cesena-maglia-canottiera-top_thumbnail.jpg",
                        "priority": 0,
                        "swatch_img": "/MC/2020/2/7364820003/004/s3swatch/SW-7364820003004.jpg",
                        "details_img": [
                            "/MC/2020/2/7364820003/004/s3master/7364820003004-a-cesena-maglia-canottiera-top_normal.jpg",
                            "/MC/2020/2/7364820003/004/s3details/7364820003004-c-cesena-maglia-canottiera-top_normal.jpg"
                        ]
                    },
                    {
                        "code": "005",
                        "description": "",
                        "sizes": [
                            {
                                "sku": "73648200030051",
                                "code": "1",
                                "description": "XS"
                            },
                            {
                                "sku": "73648200030052",
                                "code": "2",
                                "description": "S"
                            },
                            {
                                "sku": "73648200030053",
                                "code": "3",
                                "description": "M"
                            },
                            {
                                "sku": "73648200030054",
                                "code": "4",
                                "description": "L"
                            }
                        ],
                        "listing_img": "/MC/2020/2/7364820003/005/s3master/7364820003005-z-cesena-maglia-canottiera-top_thumbnail.jpg",
                        "priority": 0,
                        "swatch_img": "/MC/2020/2/7364820003/005/s3swatch/SW-7364820003005.jpg",
                        "details_img": [
                            "/MC/2020/2/7364820003/005/s3master/7364820003005-a-cesena-maglia-canottiera-top_normal.jpg",
                            "/MC/2020/2/7364820003/005/s3details/7364820003005-c-cesena-maglia-canottiera-top_normal.jpg"
                        ]
                    }
                ],
                "washing_description": null,
                "desc_categoria": "Clothing",
                "brand_originale": "MC"
            },
            "type": "models",
            "id": "7364820003"
        }
    ]
}
