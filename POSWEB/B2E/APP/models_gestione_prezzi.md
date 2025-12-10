come viene usata oggi la chiave price_type_applied ???

Matteo Malagoli:
L'app è di base ignorante, nel senso che non deve avere logiche particolari
il price_type_applied serve a indicarle quale listino applicare e quale deve recuperare tra quelli presenti sotto prices

in caso di mancanza(errore di configurazione di sede), fa fallback
ma dato che il tipo indicato è l'S, anche per fini statistici continua a indicare il tipo che le è stato detto
o almeno la logica stabilita ai tempi era questa

il fallback del prezzo(inteso come importo) è una gestione d'errore
ma il tipo indicato da posweb viene preso come legge
se posweb dice C è C
se posweb dice S, l'app usa quello


REX-54977:
ho sbrogliato la logica di override per tutti non solo per dt,hk,cn e chi avesse PRICE_LIST_MODE = 0
però il vero override avviene solo se LISTINO_ESTESO_ENABLED = 0 altrimenti
in caso di LISTINO_ESTESO_ENABLED = 1 prendo il tipo_prezzo dai prezzi in variante.

==
override_tipo_listino = {k: v[0]["tipo_prezzo"] for k, v in prezzi_per_modello.items()}
** Per chi ha LISTINO_ESTESO_ENABLED = 0 bisogna sapere che i prezzi (nella tabella prezzi)
non hanno il riferimento alla variante quindi prezzi_per_modello torna questa forma di dizionario

la chiave è il modello e il valore è una lista dove ci sono due prezzi V e S
si noti come override_tipo_listino viene preso il primo. Quale ordinamento? in base alla data di data_inizio_validita
che infatti essendo valorizzata viene considerata più recente. Se ci fosse la data_inizio_validita su S valorizzata
anche in questo caso il primo prezzo sarebbe il più recente (anche se data_fine_validita è vuoto)

{'1103053004': [
{'prezzo_listino': 10, 'prezzo_attuale': 10, 'perc_attuale': 0, 'divisa': 'EUR', 'tipo_prezzo': 'V',
'data_inizio_validita': '20230415', 'data_fine_validita': '', 'modello': '1103053004', 'variante': '',
'id_listino': 0}, {'V': {'prezzo_listino': 10, 'prezzo_attuale': 10, 'perc_attuale': 0, 'divisa': 'EUR',
'tipo_prezzo': 'V', 'data_inizio_validita': '20230415', 'data_fine_validita': '', 'modello': '1103053004',
'variante': '', 'id_listino': 0}, 
'S': {'prezzo_listino': 10, 'prezzo_attuale': 10, 'perc_attuale': 50, 'divisa': 'EUR', 'tipo_prezzo': 'S', 
'data_inizio_validita': '20230102', 'data_fine_validita': '', 'modello': '1103053004', 'variante': '', 'id_listino': 0}}]}

== dopo REX-54977
override_tipo_listino per chi ha LISTINO_ESTESO_ENABLED = 1 di fatto non c'entra ma price_type_applied viene
modificato se nei variants["price"] non si trova il prezzo del listino attivo sul negozio


pos.add_barcode => pos.get_info_capi => pos.get_modelli_by_sku (=> movim_utils.get_dati_capi)
=> movim_db_access.get_dati_capi => movim_db_access.get_dati_sku_from_catalogo
qui c'è il log
	pard['LOGGER'].debug("------------ anagrafica_d -------------")
	pard['LOGGER'].debug(anagrafica_d)
qui c'è la chiamata a sede per recuperare il catalogo da BMS
=> movim_db_access.verifica_dati_catalogo => movim_db_access.get_prezzo_from_modello_pezzo