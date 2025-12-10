Su posweb le promozioni di hk
sono abilitate sia per le vendite tradizionali che per il B2E


Se utilizzo il CeC e aggiungo a dati_documenti

dati_documenti.update({
	"promo_engine" : ""
})

la chiave promo_engine, c'è un controllo che se applico alla vendita delle contabilità (sartoria, gift,....) mi blocca la vendita b2e

Altro caso.

Se effettuo una vendita B2E con capi IN_STORE e OUT_STORE e la sospendo, riprendendola da posweb
posso applicare delle promozioni sospenderla e riprendendola mi ritrovo già le promozioni applicate

Quando si applicano delle promozioni viene passato in post una chiave promo_engine che viene salvata (solo in sospensione)
sulla dati_documenti nella tabella movimentazioni

Inoltre sulla tabella movimentazioni_custommulti
si salvano le seguenti informazioni:

In base a id_transazione, si salvano con tipo TESTATA records doppio al numero di promo applicate
una per ID: (PROMO_ENGINE,effect,19) e
una per TOKEN: (PROMO_ENGINE,effect_token,B2-9306091)

Poi per ogni CAPI in base al progressivo si salva ID e TOKEN

esempio
id,cod_negozio,id_transazione,tipo,progressivo,categoria,nome,valore,modificato
1135,1101013,287922,CAPI,1,PROMO_ENGINE,effect,19,2020-02-19 09:59:41
1136,1101013,287922,CAPI,3,PROMO_ENGINE,effect,19,2020-02-19 09:59:41
1138,1101013,287922,CAPI,1,PROMO_ENGINE,effect_token,B2-9306091,2020-02-19 09:59:41
1139,1101013,287922,CAPI,3,PROMO_ENGINE,effect_token,B2-9306091,2020-02-19 09:59:41
1134,1101013,287922,TESTATA,,PROMO_ENGINE,effect,19,2020-02-19 09:59:41
1137,1101013,287922,TESTATA,,PROMO_ENGINE,effect_token,B2-9306091,2020-02-19 09:59:41



Esempio di promozione VOUCHER sul negozio
{ "exclusivity": "CUMULABLE",  "effect": { "value_type": "PERCENTAGE",  "type": "VOUCHER",  "template_text": "TOKEN {var}",  "value": -20 },  "applicability": { "max": 1,  "step": 1,  "type": "AMOUNT",  "min": 1 }}


In caso di vendita con valuta. Si creano
due moviementazioni (quindi 2 id) e anche i pagamenti vengono splittati (in maniera tale che venga colmata la spesa di uno e il resto dello split nell'altro)
dipende dai casi
seguire pos.py

if info_transazione['num_articoli_fuori_negozio'] > 0: --> questo identifica che è un b2e
	# Split della vendita tra in e out store
	b2e_split_res = movim_utils.split_capi_e_movimenti_per_b2e(
		pard, shared['id_transazione'], pagamenti, mov_contabili, float(pard['subtotaleSartoriaNoModello']),
		dati['solo_fuori_negozio'], float(pard['vendita_totale']), common_record_data.get("promo_engine")
	)
