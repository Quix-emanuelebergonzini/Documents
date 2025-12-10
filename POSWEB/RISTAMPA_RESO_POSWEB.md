buono su MAXIMA20, negozio = 0100011, vanno sia il reso che lista reso da b2c

in (bms) /main/bin/config_common.py aggiungere a pard[TRUSTED_PROGRAMS] le righe con il programma da chiamare (se lerrore è NOT_AUTHORIZED)

--> ALTER TABLE `pos_resi_b2c` ADD `dati_reso_ristampa` TEXT NOT NULL  AFTER `dati_corriere`;

in main.store_config deve esistere la key_name RESI_B2C_CAUSALI_ENABLED che poi verrà utilizzata sotto params[CAUSALI_ENABLED]
il valore di questa chiave è 0 (ricerca per numero ordine e selezione semplice. niente altro)
il valore di questa chiave è 1 (ricerca per diversi campi e altre info per il reso, ma non da opportunità di rendere il campo con cambio di sku)
il valore di questa chieva è 2 (reso di sku)

COMUNICAZIONE TRA POSWEB E IFRAME (posweb e boss ad esempio)

su BOSS:        
                {
                    field: TabellaRicercaResiB2C.N_TRACKING,
                    title: traduci_label(ricerca_resi_b2c, stampa_reso, Stampa Reso),
                    template: """
                        <img class=etichettaIcon print_reso_button data-rma=#=rma# src=/static/storebackoffice/resi_b2c/css/etichetta.png />
                    """,
                    width: 5%
                },
                dove... su .js
                $(".print_reso_button").on("click", function() {
                    window.parent.postMessage({"type": "stampa_reso", "rma": $(this).attr("data-rma")}, "\*");
                });

su POSWEB:
                iframe-view.js

                var init = function () {
		                  window.addEventListener("message", onIframeMessage, false);
                };
                var onIframeMessage = function (e) {
        			if (e.data.type === "stampa_reso") {
        				stampaReso(e.data.rma);
        			}
		        };
                var stampaReso = function (reso_rma) {
        			// Recupero i parametri dallurl delliframe
        			try {
        				Y.io(YUI.mmfg.storeConfig.cgiBaseDir, {
        					method: POST,
        					data: {
        						module: resi_b2c,
        						program: resi_b2c,
        						function: stampa_reso_by_rma,
        						sid: YUI.mmfg.template.getLocalSID(),
        						rma: reso_rma
        					}
        				});
        			} catch (e) {
        				// do nothing
        				Y.log(handle_error: fallito invio notifiche per errore javascript, info, pos);
        			}
        		};

e...
                @ajax_handler
                def stampa_reso_by_rma(self, request, config):
                    logger.debug("reso rma da js a python " + request[rma])
