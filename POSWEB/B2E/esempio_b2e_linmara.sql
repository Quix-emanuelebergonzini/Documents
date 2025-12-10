INSERT INTO `movimentazioni` (`id_transazione`, `cod_negozio`, `id_carrello`, `numero_documento`, `numero_documento_orig`, `data_documento`, `ora_documento`,
                              `codice_stato`, `codice_movimento`, `cod_mitt_dest`, `id_utente`, `cod_cassiera`, `cod_vettore`, `cod_cassa`,
                              `tipo_applicazione_apertura`, `id_postazione_apertura`, `tipo_applicazione_chiusura`, `id_postazione_chiusura`, `sid`, `nota`,
                              `divisa`, `importo_iniziale`, `importo_finale`, `importo_pagato`, `esenzione_iva`, `cod_documento`, `dati_documenti`,
                              `numero_stampa_documento`, `flag_stampa_documento`, `dati_aggiuntivi`, `dettaglio_iva`, `firma_posweb_input`,
                              `firma_posweb_output`, `firma_posweb_version`, `nazione_oss`, `data_creazione`, `data_modifica`)
VALUES (3650104, '4401002', 'PW244402047000013648', 0, '0', '', '', 'SUSPENDED', 'VENDITA', '1', 'bergonzinie', 'E557085', '', '01', 'B2EMOBILE',
        'iOS Simulator', 'POSWEB', '01', 'rjtyn5gwoh2heh', '', 'CNY', 8000.00, 8000.00, 0.00, '0', '', '{"promo_engine": {"payments": [], "vouchers": [], "promo": {}}, "shipping_destination": "STORE", "shipping_address": {"name": "", "surname": "", "address": "\u6d59\u6c5f\u7701\u676d\u5dde\u5e02", "city": "", "province": "", "county": "", "state": "", "zipcode": "", "country": "CN", "reference_name": "HANGZHOU OUTLET MM2", "contact_number": "", "consumer_info": {"surname": "12", "name": "123", "reference_name": "123 12", "contact_number": "+8613052182662", "contact_email": "347645845@qq.com"}}}', '', 0, '',
        '{"aliquote_d": {"13": {"capi": [{"id_transazione": 3650104, "progressivo": 1, "cod_negozio": "4401002", "codice_stato": "SUSPENDED", "codice_movimento": "VENDITA", "cod_commessa": "E557085", "sku": "93260113060052", "ean": "8050994094525", "rfid": "", "sku_gruppo": "", "flag_promo": 0, "flag_divisa": 0, "sku_created": 0, "sku_splitted": 0, "sku_read": "93260113060052", "nome": "CURSORE", "classe": "32", "iva": 13.0, "flag_tassabile": 0, "composizione": "F:080WO020WS", "custom_data": "{\\"annostag\\":\\"20212\\",\\"desc_taglia\\":\\"S\\",\\"desc_classe\\":\\"\\u9488\\u7ec7\\u88d9\\",\\"data_consegna_sartoria\\":\\"\\",\\"variante\\":\\"005\\",\\"nota_lavorazioni\\":\\"\\",\\"stock_type\\":\\"OUT_STORE\\"}", "nota": "", "prezzo_listino_vendita": 8000.0, "sconto_listino_vendita": 0.0, "importo_iniziale": 8000.0, "importo_custom": 0.0, "sconto": 0, "correzione_importo": 0.0, "importo_finale": 8000.0, "tipo_importo": "V", "tipologia_merce": "GARMENTS", "reso": 0, "causale_reso": "", "data_creazione": "0000-00-00 00:00:00", "data_modifica": "2024-07-25 10:00:23", "dettaglio_mov": [], "prezzo_ricalcolato": 8000.0, "imponibile": 7079.65, "imposta": 920.35}], "movimenti": [], "num_capi_ricalcolo_vendita": 1, "num_capi_ricalcolo_storno": 0, "costi_contabili_alq": 0, "totale_alq": 8000.0, "imponibile": 7079.65, "imposta": 920.35}}, "totali_vendita": {"ven_coupon": 0, "ven_abbuono": 0, "ven_costi_extra": 0, "lordo_tessuto": 0, "lordo_capi": 8000.0, "tot_costi_extra_detailed": 0, "vendita_sconto": 0, "tot_sartoria": 0, "tot_gift_card": 0, "tot_shopping_bags": 0, "tot_spedizioni": 0, "tot_netto": 8000.0, "tot_lordo": 8000.0, "tot_sconti_abbuoni": 0.0, "tot_rettifiche_maggiorazioni": 0}}',
        null, null, null, '', '2024-07-25 09:18:28', '2024-07-25 10:05:44');

INSERT INTO `movimenti_capi` (`id_transazione`, `progressivo`, `cod_negozio`, `codice_stato`, `codice_movimento`, `cod_commessa`, `sku`, `ean`, `rfid`,
                              `sku_gruppo`, `flag_promo`, `flag_divisa`, `sku_created`, `sku_splitted`, `sku_read`, `nome`, `classe`, `iva`, `flag_tassabile`,
                              `composizione`, `custom_data`, `nota`, `prezzo_listino_vendita`, `sconto_listino_vendita`, `importo_iniziale`, `importo_custom`,
                              `sconto`, `correzione_importo`, `importo_finale`, `tipo_importo`, `tipologia_merce`, `reso`, `causale_reso`, `data_creazione`,
                              `data_modifica`)
VALUES (3650104, 1, '4401002', 'SUSPENDED', 'VENDITA', 'E557085', '93260113060052', '8050994094525', '', '', 0, 0, 0, 0, '93260113060052', 'CURSORE', '32',
        13.00, 0, 'F:080WO020WS',
        '{"annostag":"20212","desc_taglia":"S","desc_classe":"针织裙","data_consegna_sartoria":"","variante":"005","nota_lavorazioni":"","stock_type":"OUT_STORE"}',
        '', 8000.00, 0.00, 8000.00, 0.00, 0, 0.00, 8000.00, 'V', 'GARMENTS', 0, '', '0000-00-00 00:00:00', '2024-07-25 10:05:44');

esempio, http://dos-dt-it.posweb.mmfg.it/api/v1/posweb/models?debug=1&filter[name]=*BCOLLA
{
    "data": [
        {
            "attributes": {
                "code": "6016282306",
                "name": "*BCOLLA", #==> nome che si vede in app sotte le taglie
                "cod_categoria": "4",
                "desc_categoria": "Cappotti e Giacche",
                "cod_sottocategoria": "12",
                "desc_sottocategoria": "Cappotti",
                "brand": "IN",
                "brand_originale": "MM",
                "societa": "DT",
                "classe": "01",
                "desc_classe": "Cappotto",
                "annostag": "20222",
                "composition": "F: 100% Viscosa<br>F: 100% Lana Vergine",
                "washing_description": null,
                "technical_description": null,
                "emotional_description": null,
                "variants": [
                    {
                        "code": "006", #==> in app non si vede se c''è description
                        "description": "CAMMELLO", #==> si vede in app sotto il prezzo
                        "priority": 0,
                        "listing_img": null,
                        "swatch_img": null,
                        "details_img": null,
                        "sizes": [
                            {
                                "code": "1", #==> 6016282306006 + 1
                                "description": "34", #==> taglia che si vede sei quadratini
                                "sku": "60162823060061",
                                "ean": ""
                            },
                            {
                                "code": "2", #===> 6016282306006 + 2
                                "description": "36",
                                "sku": "60162823060062",
                                "ean": ""
                            },
                            {
                                "code": "3", #==> 6016282306006 + 3
                                "description": "38",
                                "sku": "60162823060063",
                                "ean": ""
                            },
                            {
                                "code": "4", #==> 6016282306006 + 4
                                "description": "40",
                                "sku": "60162823060064",
                                "ean": ""
                            },
                            {
                                "code": "5", #==> 6016282306006 + 5
                                "description": "42",
                                "sku": "60162823060065",
                                "ean": ""
                            },
                            {
                                "code": "6", #==> 6016282306006 + 6
                                "description": "44",
                                "sku": "60162823060066",
                                "ean": ""
                            },
                            {
                                "code": "7", #==> 6016282306006 + 7
                                "description": "46",
                                "sku": "60162823060067",
                                "ean": ""
                            },
                            {
                                "code": "8",  #==> 6016282306006 + 8
                                "description": "48",
                                "sku": "60162823060068",
                                "ean": ""
                            },
                            {
                                "code": "9", #==> 6016282306006 + 9
                                "description": "50",
                                "sku": "60162823060069",
                                "ean": ""
                            }
                        ],
                        "color_img": "https://media.mmfg.it/bin/imageService?version=10&username=POSWEB&service=color&societa=MM&modello10=6016282306&variante=006&tts=1722864984&rnd=22123&dhashed=AM269EhaSVZe08G28rwT3rb3KYA%3D"
                        #==> immagine con il colore che si vede in app nel quadratino
                    },
                    {
                        "code": "013",
                        "description": "NERO",
                        "priority": 0,
                        "listing_img": null,
                        "swatch_img": null,
                        "details_img": null,
                        "sizes": [
                            {
                                "code": "1",
                                "description": "34",
                                "sku": "60162823060131",
                                "ean": ""
                            },
                            {
                                "code": "2",
                                "description": "36",
                                "sku": "60162823060132",
                                "ean": ""
                            },
                            {
                                "code": "3",
                                "description": "38",
                                "sku": "60162823060133",
                                "ean": ""
                            },
                            {
                                "code": "4",
                                "description": "40",
                                "sku": "60162823060134",
                                "ean": ""
                            },
                            {
                                "code": "5",
                                "description": "42",
                                "sku": "60162823060135",
                                "ean": ""
                            },
                            {
                                "code": "6",
                                "description": "44",
                                "sku": "60162823060136",
                                "ean": ""
                            },
                            {
                                "code": "7",
                                "description": "46",
                                "sku": "60162823060137",
                                "ean": ""
                            },
                            {
                                "code": "8",
                                "description": "48",
                                "sku": "60162823060138",
                                "ean": ""
                            },
                            {
                                "code": "9",
                                "description": "50",
                                "sku": "60162823060139",
                                "ean": ""
                            }
                        ],
                        "color_img": "https://media.mmfg.it/bin/imageService?version=10&username=POSWEB&service=color&societa=MM&modello10=6016282306&variante=013&tts=1722864984&rnd=50381&dhashed=JVE7DwrScXDaZI4oSfOgKqetMdE%3D"
                    }
                ],
                "stagionale": "STAGIONALE",
                "price_type_applied": "V", ==> # occhio al fix eseguito in REX-54977
                "desc_classe_it": "Cappotto",
                "prices": [
                    {
                        "price_type": "V",
                        "price": 357.0 #==> prezzo che si vede in app sopra al colore
                    }
                ],
                "iva": 22.0,
                "model_img": "https://media.mmfg.it/bin/imageService?version=10&username=POSWEB&service=model&societa=MM&modello10=6016282306&variante=&tts=1722864984&rnd=8511&dhashed=jDsP3fe3gu3ZgmFqSQhYbKB/leQ%3D"
                #==> immagine che si vede app a sinistra
            },
            "type": "models",
            "id": "6016282306"
        }
    ]
}