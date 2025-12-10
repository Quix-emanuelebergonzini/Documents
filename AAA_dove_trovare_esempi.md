# filtro log cloud ricerca per nome job ##
resource.type="k8s_container"
resource.labels.cluster_name="gke-stghislain"
resource.labels.namespace_name="bmsau-prod"
resource.labels.container_name="runtime"
labels."k8s-pod/job-name"="bergonzini.e-20200407135621-l2vudi9iaw4vchl0ag9uic9zb3vy-job"

# BMS - query diretta in runtime 
from poswsbe.ftpexport.locator import locator as loc
service = loc.get_service('ExportVendutoService')
conn = service.get_connection()
query = ""
conn.query(query)

## APPUNTI #
se devo su bms lavorare con popup posso utilizzare promo_negozio
se devo su bms lavorare con download posso utilizzare export_xml

se devo su posweb lavorare con popup posso utizzare
qui le popup sono fatte o sulla view o su js direttamente

su bms cè kendo (preferire usare il kendo puro ed evitare struttura)
su posweb cè YUI su bms no

su posweb per visualizzare una pagina di boss su iframe guardare export_xml

su posweb per un nuovo servizio rest guardare discount_reason


---- recupero in js dei parametri della query ----
var params = YUI.mmfg.utils.getUrlQueryParams(url);

---------------------------------------------------

aprire un iframe da dentro posweb

vedi resi.js

var enable_ricerca_consumer_reso = function(consumer, pk_consumer){
    var imgTag = "";
    if (YUI.mmfg.resi.enableSearchConsumer) {
        var imgPath = [
            YUI.mmfg.storeConfig.iconsPath, "/silk/zoom.png",
        ].join("");
        imgTag = " <img class='searchRicercaConsumerReso' data-nome='" + consumer.nome + "' data-cognome='" + consumer.cognome + "' " +
            "data-id='" + pk_consumer + "' alt='' src='" + imgPath + "' style='cursor: pointer;' />";
    }
    return imgTag;
};

...grid
dataBound: function() {
    $(".searchRicercaConsumerReso").on("click", function () {
        Y.io(YUI.mmfg.storeConfig.cgiBaseDir, {
            method: 'POST',
            data: {
                module: 'gestione_consumatrici', --> vedi gestione_consumatrici.py
                program: 'search_and_add_consumer',
                consumatrice: $(this).attr("data-id"),
                nome: $(this).attr("data-nome"),
                cognome: $(this).attr("data-cognome"),
                sid: YUI.mmfg.template.getLocalSID()
            },
            on: {
                complete: function (tID, resp) {
                    var res = {};
                    try {
                        res = Y.JSON.parse(resp.responseText);
                    } catch (e) {
                        res = {
                            status: YUI.mmfg.storeConfig.jsonErrorCode,
                            payload: {html: resp.responseText}
                        };
                        YUI.mmfg.utils.notifyJavascriptError({
                            'client_source': 'searchRicercaConsumerResoComplete',
                            'message': 'ERROR: ' + e + ' ||| RESPONSE: ' + resp + ' ||| responseText: ' + resp.responseText
                        });
                    }
                    if (res.status && res.status === YUI.mmfg.storeConfig.jsonNormalCode) {
                        var payload = res.payload;
                        var urlPopup = "?module=gestione_consumatrici&program=consumatrici&sid=" + YUI.mmfg.template.getLocalSID() +
                        "&pk_consumer=" + payload.pk_consumer + "&nome=" + payload.nome +"&cognome=" + payload.cognome;
                        var gestione_consumatrici_popup = new Y.mmfg.Popup({
                            title: strings.DETTAGLIO_CONSUMATRICE,
                            width: 1000,
                            height: 1000,
                            target: 'gestione_consumatrici_popup'
                        }).iframe(urlPopup);
                    } else {
                        YUI.mmfg.template.fancyDialogOpen(res, "error", true);
                    }
                }
            }
        });
    })
}

----- aggiungere in dashboard posweb un avviso -------
home.py
# 9. consumer card da caricare
if common_utils.use_new_consumer_datamodel(pard):
    stato = 1
    cards = common_utils.check_consumer_card_to_upload(pard, stato)
    if cards and cards > 0:
        messages.append(compose_dashboard_message(
            'gestione_consumatrici',
            'consumatrici',
            u"""<trad group="pos_dashboard" id='consumer_card_to_upload_check'> <b>{cards}</b> schededa caricare delle consumatrice</trad>""".format(cards=cards),
            feature_set,
            user_role,
            extra_params_link='scheda_card_stato={}'.format(stato)
        ))


-- AGGIUNTA SERVIZIO IN SEDE CHE RISPONDE AD UN PROGRAM PRESENTE IN DATAQUEUE SU POSWEB --
cerca su posweb e poi su poswsbe --> ws_set_status_sale


-- PROBLEMI CON FONT CARATTERI SPECIALI IN STAMPE PDF (e forse altro...) ---
andare in stampe_pdf e cercare il pdf degli OSS (nazione_oss)
html se notiamo è contornato dal tag <font> questo fa si che tutto
venga basato su un font.
poi controllare che venga usato un font che supporta più caratteri
