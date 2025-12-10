TEST: ws_rule_engine / u2DcvtzVv7s+6=3JFEQL
oppure
TEST: ws_posweb / jn6Gzx8cQkX?3z3R%SNT


sostanza è che c'è una prescelta da parte dell'utente
delle promo che possono essere applicate sui
capi.
alcune non applicabili verranno nascoste e visibili
solo su richiesta (aiutano le cassiere a consigliare).
la scelta è di promo sicuramente applicabili quindi
anche la risposta deve essere sicuramente adatta alla 
richiesta.
dopo la scelta della cassiera la/le promo sono applicate
direttamente non c'è la preview di anteprima.

simuate dobbiamo riempirlo con i token 
NEW, EXISTING, GIFT poi per l'applicazione ci penserà
automaticamente il py a generare la simulazione,
che si rifà ai token DISCOUNT, GIFT e DISCOUNT_SALE.

durante l'applicazione togliamo i capi current
dal db perché poi ci ripensa il promo engine a ridarci
i dati per riaggiungerlo. altra cosa prima
dell'applicazione lo scorporo iva non ha i capi aggiunti
quindi è bene ricalcolare il tutto ma avviene in modo
automatico.

