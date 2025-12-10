# coding=utf-8

import json
import operator
import datetime
import itertools
import math


class FidelityPointOperationType():
	# B2C SOLO CONSTANTE
	# operazione di quotazione punti per quotazione carrello
	QUOTATION = "QUOTATION"
	# B2C
	# operazione di calcolo punti per checkout carrello
	CHECKOUT = "CHECKOUT"
	# operazione di calcolo punti quando tutte le spedizioni del carrello sono state assegnate ad un mittente
	ASSIGNMENT = "ASSIGNMENT"
	# stato previsto per le operazioni di reso con conseguente decurtazione dei punti
	RETURN = "RETURN"
	# POSWEB
	SALE = "SALE"


class Contabilita():
	GIFT_CARD = "CONTABILITA_GIFT"
	SCONTO = "CONTABILITA_SCONTO"
	ABBUONO = "CONTABILITA_ABBUONO"
	PROMOZIONE = "CONTABILITA_PROMOZIONE"
	SARTORIA = "CONTABILITA_SARTORIA"


class Pagamenti():
	CONTANTI = "CONTANTI"
	GIFT_CARD = "GIFT_CARD_CORPORATE"


fidelity_cache = { }
LISTINI_VENDITA = ("V",)
LISTINI_SALDO = ("S", "P", "C")
TIPOLOGIA_MERCE_TESSUTO = "TEXTILE"
tipo = LOYALTY_CARD_NEW


def partenza():
	data =     {
	      "pagamenti": [
	        {
	          "importo_finale": 244.0,
	           "cod_operazione": "CONTANTI"
	        }
	      ],
	       "contabilita": [
	        {
	          "codice_movimento": "CONTABILITA_GIFT",
	           "importo_finale": 200.0,
	           "progressivo": 1
	        },
	         {
	          "codice_movimento": "CONTABILITA_SCONTO",
	           "importo_finale": -4.0,
	           "progressivo": 3
	        },
	         {
	          "codice_movimento": "CONTABILITA_ABBUONO",
	           "importo_finale": -30.0,
	           "progressivo": 4
	        }
	      ],
	       "importo": 244.0,
	       "id_operazione": "1377",
	       "data_ora_operazione": "2019-04-05 09:33:03",
	       "cod_negozio": "0100514",
	       "divisa": "EUR",
	       "extra_data": {
	        "numero_documento": "18",
	         "data_documento": "20190405"
	      },
	       "operazione": "ASSIGNMENT",
	       "pk_consumer": "9042519",
	       "handle_duplicates": 0,
	       "capi": [
	        {
	          "tipo_prezzo": "S",
	           "variante": "001",
	           "taglia": "1",
	           "importo_finale": 39.0,
	           "modello": "1021015406",
	           "importo_iniziale": 39.0,
	           "sku": "10210154060011",
	           "nome": "ELLADE",
	           "classe": "02",
	           "progressivo": 1,
	           "annostag": "20151",
	           "tipologia_merce": "GARMENTS"
	        },
	         {
	          "tipo_prezzo": "S",
	           "variante": "001",
	           "taglia": "2",
	           "importo_finale": 39.0,
	           "modello": "1021015406",
	           "importo_iniziale": 39.0,
	           "sku": "10210154060012",
	           "nome": "ELLADE",
	           "classe": "02",
	           "progressivo": 2,
	           "annostag": "20151",
	           "tipologia_merce": "GARMENTS"
	        }
	      ]
	}
	sale_data = {
		"capi"       : data["capi"],
		"contabilita": data["contabilita"],
		"pagamenti"  : data["pagamenti"]
	}

	dati_ref = { }


	print json.dumps(calculate_amount(
		data["operazione"],
		data["cod_negozio"],
		data["importo"],
		data["divisa"],
		data[pk_consumer],
		data[id_operazione],
		data.get("data_ora_operazione"),
		sale_data,
		dati_ref,
		data.get("extra_data"),
		int(data.get("debug", 0)) == 1,
		data.get("handle_duplicates", 1) == 1
	), indent=4)


def _splama_importo(importo, totale_da_spalmare, totale_riferimento):
	segno = 1 if totale_da_spalmare >= 0 else -1
	return round((abs(importo) * abs(totale_da_spalmare) / abs(totale_riferimento)) * segno, 2)


def calcola_punti_fidelity(capi, contabilita, pagamenti, totale_vendita,
						   collect_details=False):
	dettaglio_punti = []
	# tipo = fidelity.tipo

	capi = sorted(capi, key=operator.itemgetter("progressivo"))  # in base ad una chiave ordina il dizionario

	# Calcolo il totale delle contabilità divise per tipo
	group_key = operator.itemgetter("codice_movimento")

	tot_contabilita = {
		cont_type: sum(float(c["importo_finale"]) for c in conts)
		for cont_type, conts in itertools.groupby(sorted(contabilita, key=group_key), key=group_key)
		}

	print tot_contabilita, tot_contabilita

	if tipo in ("LOYALTY_CARD_NEW", "FIDELITY_CARD"):

		is_promo_old = tipo != "LOYALTY_CARD_NEW"
		tessuti = filter(lambda c: c.get("tipologia_merce") == TIPOLOGIA_MERCE_TESSUTO, capi)

		capi = filter(lambda c: c.get("tipologia_merce") != TIPOLOGIA_MERCE_TESSUTO, capi)

		# prende tutti i capi che rispondono alla espressione c.get() != TIPO...
		# lambda è una mini funzione con un parametro (c) e una espressione (c.get() != TIPO...appunto)
		# dove c è un oggetto di capi...vedi filter per definizione è una funzione e un iterabile
		# filter(function, iterable)

		# Calcoli preliminari per lo spalmaggio degli punti
		totale_capi = last_prog = 0
		for capo in capi:
			importo_finale = float(capo[importo_finale])
			totale_capi += importo_finale
			last_prog = capo["progressivo"]

		last_prog_capi_o_tessuti = last_prog

		last_prog_tessuti = 0
		if tessuti:
			for tessuto in tessuti:
				last_prog_tessuti = tessuto["progressivo"]
			last_prog_capi_o_tessuti = last_prog_tessuti

		gift_cards = [c for c in contabilita if c["codice_movimento"] == Contabilita.GIFT_CARD]

		# Arrotondamenti per evitare errori di approssimazione
		has_promo_or_sconti = Contabilita.SCONTO in tot_contabilita or Contabilita.PROMOZIONE in tot_contabilita
		tot_sartorie = tot_contabilita.get(Contabilita.SARTORIA, 0)
		print tot_sartorie

		tot_gift_card = tot_contabilita.get(Contabilita.GIFT_CARD, 0)
		totale_capi = round(totale_capi, 2)
		totale_tessuti = sum(float(t["importo_finale"]) for t in tessuti)
		tot_pagamenti_gift = sum(
			float(p["importo_finale"]) for p in pagamenti if p["cod_operazione"] == Pagamenti.GIFT_CARD)
		tot_punti_promo = sum(float(c["punti"]) for c in contabilita if c["codice_movimento"] == Contabilita.PROMOZIONE)
		all_pagato_gift = len(pagamenti) and all(p["cod_operazione"] == Pagamenti.GIFT_CARD for p in pagamenti)

		# La lista spalmaggio_contabilità contiene le regole per spalmare le contabilità della vendita. Le chiavi sono:
		# - "rule": descrizione della regola ai fini di debug
		# - "tot": totale da spalmare, è il totale della contabilità
		# - "tot_ref": totale da prendere come riferimento per spalmare la vendita, è il totale complessivo su cui
		#   spalmare la contabilità
		# - "calc": funzione a cui vanno passati i dati di capo o gift per controllare se la contabilità può essere
		# 	spalmata
		# - "is_last": funzione a cui vanno passati i dati di capo o gift per controllare se si tratta dellultimo
		# 	su cui spalmare la contabilità, infatti sullultimo verrà fatto un calcolo per differenza per assorbire
		# 	eventuali arrotondamenti
		# - "used": se True i punti derivanti da questo scorporo rappresenteranno punti utilizzati e non guadagnati
		# - "promo": se True questo totale verrà valutato per calcolare lo sconto totale da promozione
		# - "calc_netto": se True come importo su cui calcolare lo spalmaggio verrà usato limporto al netto dei
		# 	calcoli fatti fino a quel punto (al netto dei calcoli effettuati nelle regole precedenti), invece che
		# 	limporto del capo prima di ogni calcolo (comportamento di default)
		tot_spalmati = { }
		if is_promo_old:
			spalmaggio_contabilita = [
				{
					"rule"   : "ABBUONO da spalmare su tutti i capi in base al peso sul totale dei capi",
					"tot"    : tot_contabilita.get(Contabilita.ABBUONO, 0),
					"tot_ref": totale_capi,
					"calc"   : lambda item_d, gr: gr == "capi",
					"is_last": lambda item_d, gr: item_d["progressivo"] == last_prog
				}, {
					"rule"   : "PUNTI PROMOZIONE da spalmare sui capi in base al peso sul totale dei capi",
					"tot"    : tot_punti_promo,
					"tot_ref": totale_capi,
					"calc"   : lambda item_d, gr: gr == "capi",
					"is_last": lambda item_d, gr: item_d["progressivo"] == last_prog,
					"used"   : True
				}
			]
		else:
			contabilita_gestite = (Contabilita.SCONTO, Contabilita.ABBUONO, Contabilita.PROMOZIONE, Pagamenti.GIFT_CARD)
			all_contabilita_gestite = all(k in contabilita_gestite for k in tot_contabilita.iterkeys())
			spalmaggio_contabilita = [
				{
					"rule"   : "SCONTO da spalmare su tutti i capi in base al peso sul totale di capi e sartorie",
					"tot"    : tot_contabilita.get(Contabilita.SCONTO, 0),
					"tot_ref": round(totale_capi + tot_sartorie, 2),
					"calc"   : lambda item_d, gr: gr == "capi",
					"is_last": lambda item_d, gr: item_d["progressivo"] == last_prog and not tot_sartorie
				}, {
					"rule"   : "ABBUONO da spalmare su tutti i capi in base al peso sul totale di capi e sartorie",
					"tot"    : tot_contabilita.get(Contabilita.ABBUONO, 0),
					"tot_ref": round(totale_capi + tot_sartorie, 2),
					"calc"   : lambda item_d, gr: gr == "capi",
					"is_last": lambda item_d, gr: item_d["progressivo"] == last_prog and not tot_sartorie
				}, {
					"rule"   : "PROMOZIONE da spalmare su tutti i capi in base al peso sul totale di capi e sartorie",
					"tot"    : tot_contabilita.get(Contabilita.PROMOZIONE, 0),
					"tot_ref": round(totale_capi + tot_sartorie, 2),
					"calc"   : lambda item_d, gr: gr == "capi",
					"is_last": lambda item_d, gr: item_d["progressivo"] == last_prog and not tot_sartorie,
					"promo"  : True
				}, {
					"rule"      : "PAGAMENTI GIFT CARD da spalmare sui capi in base al peso sul totale vendita",
					"tot"       : round(tot_pagamenti_gift * -1, 2),
					"tot_ref"   : totale_vendita - tot_gift_card,
					"calc"      : lambda item_d, gr: gr in ("capi", "tessuti"),
					# Il calcolo per differenza in questo caso può essere fatto solo se non ci sono altre
					# contabilità non spalmabili tipo sartorie
					"is_last"   : lambda item_d, gr: all_contabilita_gestite and item_d[
																					 "progressivo"] == last_prog_capi_o_tessuti,
					"calc_netto": True
				}, {
					"rule"   : "PUNTI PROMOZIONE da spalmare su tutti i capi in base al peso sul totale dei capi",
					"tot"    : tot_punti_promo,
					"tot_ref": totale_capi,
					"calc"   : lambda item_d, gr: gr == "capi",
					"is_last": lambda item_d, gr: item_d["progressivo"] == last_prog,
					"used"   : True
				}
			]

		groups = (("capi", capi), ("tessuti", tessuti), ("gift_cards", gift_cards))

		# Calcolo dei punti su capi e gift card
		for group_def in groups:
			group_name, group = group_def
			for item in group:  # per ogni capo nel mio esempio
				details = []

				# Come importo base uso limporto finale
				importo_base = float(item[importo_finale])
				importo = importo_base
				punti_utilizzati = 0
				sconto_promo = 0

				listino = ""
				if group_name == "capi":
					listino = item["tipo_prezzo"]
					progressivo = item["progressivo"]
					# Per la vecchia promo il calcolo è sempre 1 euro 1 punto
					if is_promo_old:
						punti_per_euro = 1.0
					# Per i capi le regole sul tipo prezzo sono:
					# V: 1 euro 1 punto
					# S: 2 euro 1 punto
					elif listino in LISTINI_VENDITA:
						punti_per_euro = 1.0
					elif listino in LISTINI_SALDO:
						punti_per_euro = 2.0
					else:
						punti_per_euro = 1.0
				else:
					# Per le gift card vale la regola 1 euro 1 punto
					punti_per_euro = 1.0
					progressivo = item.get("progressivo", 0)

				regola_text = str(punti_per_euro) + " euro 1 punto"
				print regola_text

				# is_promo_old nasce da if tipo != LOYAL_CARD_NEW
				# Controllo se questo elemento deve accumulare punti
				if is_promo_old:
					accumula_punti = False
					# Nella vecchia promozione le gift card accumulano sempre
					if group_name == "gift_cards":
						accumula_punti = True
					# I capi accumulano solo se non sono presenti sconti o sconti da promozione in vendita e se:
					# - è un capo con listino V su cui non sono state fatti sconti
					# - è un capo in storno con listino S su cui sono state fatte maggiorazioni
					elif not has_promo_or_sconti and (
								(listino in LISTINI_VENDITA and abs(importo_base) >= abs(item["importo_iniziale"])) or
								(importo_base < 0 and listino in LISTINI_SALDO and abs(importo_base) > abs(
									item["importo_iniziale"]))
					):
						accumula_punti = True

					if not accumula_punti and collect_details:
						if has_promo_or_sconti:
							details.append("Non accumula perchè presenti sconti o sconti da promozione")
						elif listino in LISTINI_VENDITA:
							details.append("Non accumula perchè listino V scontato")
						elif importo_base < 0 and listino in LISTINI_SALDO:
							details.append("Non accumula perchè listino S non maggiorato")

				else:
					# Nella nuova promozione si accumula sempre a meno che la vendita non sia pagata interamente
					# con gift
					accumula_punti = not all_pagato_gift
					if not accumula_punti and collect_details:
						details.append("Non accumula perchè vendita pagata interamente con gift card")

				# Calcolo il punteggio iniziale in base allimporto
				punti_guadagnati_old = int(importo_base / punti_per_euro) if accumula_punti else 0
				punti_guadagnati = math.ceil(importo_base / punti_per_euro) if accumula_punti else 0

				if collect_details:
					details.append("Prezzo {listino} {importo} ({regola}) -> {punti} punti".format(
						listino=listino, importo=importo_base, regola=regola_text, punti=punti_guadagnati
					))
					details.append("Prezzo OLD {listino} {importo} ({regola}) -> {punti} punti".format(
						listino=listino, importo=importo_base, regola=regola_text, punti=punti_guadagnati_old
					))

				# Scorro la lista delle contabilità da spalmare
				for idx_cont, sc in enumerate(spalmaggio_contabilita):

					# Controllo se questa contabilità ha un totale spalmabile e può essere spalmata sul capo
					if sc["tot"] and sc["tot_ref"] and sc["calc"](item, group_name):

						# Controllo se il capo o la gift card è lultimo su cui poter spalmare la contabilità
						sconto_diff = sc["is_last"](item, group_name)
						tot_gia_spalmato = tot_spalmati.get(idx_cont, 0)
						if sconto_diff:
							# Se è lultimo faccio il calcolo per differenza tra limporto da spalmare e quello già
							# spalmato
							importo_pesato_raw = sc["tot"] - tot_gia_spalmato
						else:
							# Altrimenti devo calcolare limporto in base al peso sul totale di riferimento
							importo_calc_spalmaggio = importo if sc.get("calc_netto") else importo_base
							importo_pesato_raw = _splama_importo(importo_calc_spalmaggio, sc["tot"], sc["tot_ref"])

						# Arrotondo sempre allintero
						importo_pesato = round(importo_pesato_raw, 0)
						importo += importo_pesato_raw

						# Aggiungo i punti ad uno dei punteggi a seconda che rappresentino punti usati o guadagnati
						if sc.get("used"):
							# Per i punti pesati non ci sono regole da applicare, 1 punto è sempre 1 punto
							punti_pesati = int(importo_pesato)
							punti_utilizzati += punti_pesati
						else:
							# A seconda della regola da applicare converto limporto spalmato in punti
							punti_pesati = int(importo_pesato / punti_per_euro)
							punti_guadagnati += punti_pesati
							punti_guadagnati_old += punti_pesati

						# Uso limporto pesato della contabilità per calcolare lo sconto da promo se richiesto
						if sc.get("promo"):
							sconto_promo += importo_pesato

						if collect_details:
							details_text = u"{} ".format(sc["rule"])
							if sconto_diff:
								details_text += u"(ultimo capo calcolato per differenza): " \
												u"(totale da spalmare) {tot_spal} - " \
												u"(totale già spalmato) {splamato}".format(
									tot_spal=sc["tot"], splamato=tot_gia_spalmato
								)
							else:
								details_text += u"(importo) {importo} * (totale da spalmare) {tot_spal} " \
												u"/ (totale di riferimento) {tot_ref}".format(
									importo=importo_calc_spalmaggio, tot_spal=sc["tot"],
									tot_ref=sc["tot_ref"]
								)
							details_text += u" = (quota parte calcolata) {quota_raw} -> (arrotondata) {quota} ".format(
								quota_raw=importo_pesato_raw, quota=importo_pesato
							)
							if sc.get("used"):
								details_text += u"-> (punti utilizzati)"
							else:
								details_text += u"-> (punti guadagnati applicando {regola_text})".format(
									regola_text=regola_text, punti=punti_pesati
								)
							details_text += " {punti}".format(punti=punti_pesati)
							details.append(details_text)

						# Segno limporto calcolato come già spalmato
						tot_spalmati[idx_cont] = tot_gia_spalmato + importo_pesato

				if not accumula_punti:
					punti_guadagnati = 0

				# Calcolo il totale dei punti (i punti utilizzati sono sempre negativi quindi bisogna sommarli per
				# fare la differenza)
				punti = int(punti_guadagnati + punti_utilizzati)
				punti_old = int(punti_guadagnati_old + punti_utilizzati)

				# Aggiungo il capo al dettaglio della distribuzione dei punti
				dettaglio_capo = {
					"tipo"              : Contabilita.GIFT_CARD if group_name == "gift_cards" else "CAPO",
					"progressivo"       : progressivo,
					"punti"             : float(punti),
					"punti_old"         : float(punti_old),
					"guadagnati"        : float(punti_guadagnati),
					"guadagnati_old"    : float(punti_guadagnati_old),
					"utilizzati"        : float(punti_utilizzati),
					"importo_promozione": sconto_promo
				}

				if collect_details:
					dettaglio_capo["dettaglio"] = details

				dettaglio_punti.append(dettaglio_capo)

		print json.dumps(dettaglio_punti)

		# Per la vecchia promo se sono presenti pagamenti con gift card devo fare unelaborazione finale per spalmarli
		if is_promo_old and tot_pagamenti_gift and dettaglio_punti:
			# Se il totale dei punti guadagnati finora supera la parte di vendita non pagata con gift card,
			# devono essere ricalcolati i punteggi sui capi
			if sum(i["guadagnati"] for i in dettaglio_punti) > totale_vendita - tot_pagamenti_gift:
				# Devo spalmare su tutti tra
				tot_da_spalmare = round(totale_vendita - tot_pagamenti_gift - tot_gift_card, 2)
				tot_capi_tessuti = round(totale_tessuti + totale_capi, 2)
				new_punti = { }
				last_progressivo = 0
				for group in (tessuti, capi):
					for item in group:
						new_punti[item["progressivo"]] = round(_splama_importo(
							item["importo_finale"], tot_da_spalmare, tot_capi_tessuti
						), 0)
						last_progressivo = item["progressivo"]
				# Aggiungo leventuale rimanenza dovuta agli arrotondamenti
				new_punti[last_progressivo] += round(tot_da_spalmare - sum(new_punti.values()), 2)
				for i in dettaglio_punti:
					if i["tipo"] == "CAPO" and i["progressivo"] in new_punti:
						i["guadagnati"] = new_punti[i["progressivo"]]
						i["punti"] = float(int(i["guadagnati"] + i["utilizzati"]))
						if collect_details:
							i["dettaglio"].append("Ricalcolo per pagamento con gift card: {}".format(i["guadagnati"]))

	return dettaglio_punti


def calculate_amount(tipo_operazione, cod_negozio, totale_vendita, divisa, pk_consumer, id_operazione,
					 data_ora_operazione,
					 sale_data, dati_ref, extra_data=None, collect_details=False, handle_duplicates=True):
	capi = sale_data.get("capi", [])
	contabilita = sale_data.get("contabilita", [])
	print contabilita , contabilita
	pagamenti = sale_data.get("pagamenti", [])
	fidelity_consumer = []

	# fidelity_consumer = get_fidelities_for_consumer_store(pk_consumer, cod_negozio)

	validate_sale_data(tipo_operazione, fidelity_consumer, capi, contabilita, pagamenti, totale_vendita)

	dettaglio_aggregato = { }
	processed_types = []
	try:
		# Se ho già processato una fidelity di questo tipo la ignoro
		processed_types.append(LOYALTY_CARD_NEW)
		# Ricavo la entity con la definizione del tipo della fidelity
		# Calcolo i punti accumulati sulla base dei dati di vendita
		dettaglio = calcola_punti_fidelity(capi, contabilita, pagamenti, totale_vendita, collect_details)

		# Non serve continuare se non ho accumulato punti su nessun capi
		if not dettaglio:
			pass
		raddoppia_punti = False

		if tipo == "LOYALTY_CARD_NEW" and tipo_operazione == FidelityPointOperationType.SALE and \
				cod_negozio and (extra_data or data_ora_operazione):
			date_start = 20190314
			date_end = 20190324
			cod_negozio_ulteriore_promozione = 0100518

			if extra_data and extra_data.get(data_documento):
				data_operazione = extra_data.get(data_documento)
			else:
				data_operazione = datetime.datetime.strptime(data_ora_operazione, %Y-%m-%d %H:%M:%S).strftime(
					"%Y%m%d")
			# verifico se rientro nella condizione di raddoppiare il punteggio:
			raddoppia_punti = cod_negozio == cod_negozio_ulteriore_promozione and date_start <= data_operazione <= date_end

			if raddoppia_punti:
				print ("""** punteggio da raddoppiare: data inizio {} / data fine {}
					e codice negozio {} a cui viene applicata questa condizione
					(data operazione: {}).""".format(
					date_start, date_end, cod_negozio_ulteriore_promozione, data_operazione))
		punteggio = calcola_totali_punti_fidelity(dettaglio, 2130022454821, raddoppia_punti=raddoppia_punti)

		# Gestisco le operazioni sui punti se il tipo operazione non è quotation
		if tipo_operazione != FidelityPointOperationType.QUOTATION:
			update_amount(tipo_operazione, cod_negozio, , punteggio["guadagnati"], punteggio["utilizzati"],
				punteggio["dettaglio"], id_operazione, data_ora_operazione, dati_ref, extra_data)

		dettaglio_aggregato[tipo] = punteggio
	except Exception as exc:
		print Eccezione, exc
	# Rilancio leccezione se è uneccezione diversa dallerrore di integrità oppure se non devo gestire i
	# duplicati
	# In caso di errore di integrità, se devo gestire i duplicati, recupero tutte le operazioni già registrate
	# con gli stessi riferimenti e ricreo il dettaglio nel momento in cui è stata salvata loperazione
	return dettaglio_aggregato


def calcola_totali_punti_fidelity(dettaglio_punti, codice, raddoppia_punti=False):
	# Calcolo i totali
	tot_punti = tot_punti_guadagnati = tot_punti_utilizzati = tot_importo_promo = 0
	for i in dettaglio_punti:

		if raddoppia_punti:
			i["guadagnati"] *= 2
			i["punti"] = i["guadagnati"] + i["utilizzati"]
		tot_punti += i["punti"]
		tot_punti_guadagnati += i["guadagnati"]
		tot_punti_utilizzati += i["utilizzati"]
		tot_importo_promo += i["importo_promozione"]

	return {
		"totale"            : tot_punti,
		"guadagnati"        : tot_punti_guadagnati,
		"utilizzati"        : tot_punti_utilizzati,
		"dettaglio"         : dettaglio_punti,
		"importo_promozione": tot_importo_promo,
		"codice"            : codice
	}


def validate_sale_data(tipo_operazione, fidelity_consumer, capi, contabilita, pagamenti, totale_vendita):
	# Se sono presenti degli sconti da promozione valido che i barcode siano tra quelli attivi per il consumer
	tot_used_fidelities = 0
	used_fidelities = [c for c in contabilita if c["codice_movimento"] == Contabilita.PROMOZIONE]
	if used_fidelities:
		active_pairs = [(f.tipo, f.codice) for f in fidelity_consumer]

		for used in used_fidelities:
			tot_used_fidelities += float(used["importo_finale"])
			if (used["tipo"], used["codice"]) not in active_pairs:
				print Errore FD010 con codice {} e tipo {}.format(used[codice], used[tipo])
			# raise Exception


def get_fidelity_types_for_store(cod_negozio, tipo=None, only_active=True):
	# Estraggo tutte le righe dei tipi-negozio con il codice negozio uguale a quello passato
	filtro = e.cod_negozio == cod_negozio

	# Se passato filtro anche per tipo
	if tipo:
		filtro &= e.tipo == tipo

	tipi_per_negozio = get_some(FidelityTipoNegozio, filtro)

	# Estraggo la riga del tipo
	if not tipi_per_negozio:
		defs = []
	else:
		filtro_tipi = e.tipo._in(set(t.tipo for t in tipi_per_negozio))

		# Se richiesto filtro solo i tipi attivi
		if only_active:
			oggi = datetime.datetime.now().strftime("%Y%m%d")
			filtro_tipi &= e.stato == "ENABLED"
			filtro_tipi &= (e.data_inizio == "") | (e.data_inizio <= oggi)
			filtro_tipi &= (e.data_fine == "") | (e.data_fine >= oggi)

		defs = get_some("FidelityTipo", filtro_tipi)

	return defs


def get_fidelities_for_consumer_store(self, pk_consumer, cod_negozio=None, only_active=True, only_active_types=True):
	pk_consumer = int(pk_consumer)

	if pk_consumer not in fidelity_cache:
		fidelity_cache[pk_consumer] = get_some("Fidelity", e.pk_consumer == pk_consumer)

	filtro = e.pk_consumer == int(pk_consumer)

	if only_active:
		oggi = datetime.datetime.now().strftime("%Y%m%d")
		filtro &= e.attivo == 1
		filtro &= (e.data_inizio == "") | (e.data_inizio <= oggi)
		filtro &= (e.data_fine == "") | (e.data_fine >= oggi)

	if cod_negozio:
		tipi_fidelity_negozio = get_fidelity_types_for_store(cod_negozio, only_active=only_active_types)
		filtro &= e.tipo._in([t.tipo for t in tipi_fidelity_negozio])

	return [i for i in fidelity_cache[pk_consumer] if filtro(i)]


def update_amount(tipo_operazione, cod_negozio, fidelity, punti_guadagnati, punti_utilizzati, dettaglio_punti, id_operazione,
		data_ora_operazione, dati_ref, extra_data=None):
		# Dati per il salvataggio sulla tabella del calcolo punti
		anno_operazione = int(data_ora_operazione[0:4])
		data = {
			"id_operazione": id_operazione,
			"tipo_operazione": tipo_operazione,
			"cod_negozio": cod_negozio,
			"anno_operazione": anno_operazione,
			"tipo": LOYALTY_CARD_NEW,
			"codice": 2130022454821,
			"timestamp_operazione": datetime.datetime.strptime(data_ora_operazione, "%Y-%m-%d %H:%M:%S"),
			"stato": PENDING,
			"importo": punti_guadagnati,
			"importo_utilizzato": punti_utilizzati,
			"custom_data": json.dumps(dettaglio_punti),
			"utente_modifica": "pycharm"
		}

		# Creo il dizionario che finirà nei custom data dello storico
		data_keys_to_history = ("id_operazione", "tipo_operazione", "cod_negozio", "anno_operazione")
		history_custom_data = {k: data[k] for k in data_keys_to_history}

		# Storicizzo i dati referenziati
		history_custom_data.update({"{}_ref".format(k): dati_ref[k] for k in data_keys_to_history if k in dati_ref})

		# Aggiungo eventuali dati
		if extra_data:
			history_custom_data.update(extra_data)

		# Dati per il salvataggio della riga di storico
		history_data = {
			tipo: LOYALTY_CARD_NEW,
			codice: 2130022454821,
			cod_negozio: cod_negozio,
			action: UPDATE,
			importo_orig_corrente: 0,
			importo_orig_congelato: 0,
			utente_modifica: "pycharm",
			custom_data: json.dumps(history_custom_data)
		}

		# ASSIGNMENT
		importo_corrente = 2942 # CHECKOUT -> 2742
		importo_congelato = 24 # CHECKOUT -> 0
		punti_gift = {}
		punti_gift[punti] = 0

		# Vendita Posweb: porta allaccumulo di punti reali
		if tipo_operazione == SALE:

			# Salvo la vendita nella tabella di calcolo punti direttamente in stato finalizzato dato che non dovrà
			# più essere processata
			data[stato] = FINALIZED

			# La somma dei punti guadagnati e utilizzati (che saranno negativi), vengono aggiunti direttamente
			# ai punti reali della fidelity
			importo_corrente += punti_guadagnati + punti_utilizzati

		# Checkout B2C: prima fase di conferma dellordine B2C, i punti salvati in questa fase verranno
		# sovrascritti dallassignment
		elif tipo_operazione == CHECKOUT:
			for dict in dettaglio_punti:
				punti_gift = {punti: dict.get(punti) for key, value in dict.iteritems() if value == Contabilita.GIFT_CARD}

			# Aumento i punti congelati sulla fidelity in base ai punti guadagnati
			importo_congelato += punti_guadagnati - punti_gift[punti]

			# I punti utilizzati invece vanno aggiunti ai punti reali perchè vanno scalati immediatamente
			importo_corrente += punti_utilizzati + punti_gift[punti]

		# Operazioni che richiedono il legame con il checkout
		else:

			# Per assignment e return trovo la riga di origine delloperazione
			# filtro_op_root = (
			# 	(e.id_operazione == dati_ref["id_operazione"]) &
			# 	(e.cod_negozio == dati_ref.get(cod_negozio, cod_negozio)) &
			# 	(e.anno_operazione == int(dati_ref["anno_operazione"])) &
			# 	(e.tipo == fidelity.tipo)
			# )

			# Per lassignment si tratta sicuramente di un checkout
			# if tipo_operazione == FidelityPointOperationType.ASSIGNMENT:
			# 	filtro_op_root &= e.tipo_operazione == FidelityPointOperationType.CHECKOUT
			# # Per il return può trattarsi di un checkout o una sale
			# else:
			# 	filtro_op_root &= e.tipo_operazione._in(
			# 		(FidelityPointOperationType.CHECKOUT, FidelityPointOperationType.SALE)
			# 	)
			# ents = self.get_some("FidelityCalcoloPunti", filtro_op_root, limit=1)
			# if not ents:
			# 	raise CRMApiError(FD012, id_operazione=dati_ref["id_operazione"])
			# op_root = ents[0]

			# Aggiungo il legame con loperazione iniziale
			# data["id_ref"] = op_root.id

			# Assignment B2C: fase in cui lordine viene confermato definitivamente, scartando i capi che non possono
			# essere spediti, dovrà sostituire interamente ciò che è stato calcolato dal checkout perchè è un dato più
			# preciso
			if tipo_operazione == FidelityPointOperationType.ASSIGNMENT:

				# # Controllo che non sia già stato creato un assignment per questo ordine
				# filtro_assigment = (e.id_ref == data["id_ref"]) & (e.tipo_operazione == FidelityPointOperationType.ASSIGNMENT)
				# if self.get_some("FidelityCalcoloPunti", filtro_assigment, limit=1):
				# 	# Disabilitata leccezione in modo che venga restituito il calcolo punti dellassignment precedente
				# 	# in caso di invii multipli della stessa operazione
				# 	# raise CRMApiError(FD021)
				# 	return
				# else:
				# 	# Devo segnare il relativo checkout come cancellato
				# 	op_root.stato = FidelityPointStatus.CANCELLED
				# 	self.set(op_root)

				# Rimuovo dallimporto congelato della fidelity ciò che avevo guadagnato con il CHECKOUT e aggiungo i
				# punti guadagnati con lASSIGNMENT
				importo_congelato = importo_congelato - importo_congelato + punti_guadagnati

				# Rimuovo dallimporto corrente della fidelity ciò che avevo utilizzato con il CHECKOUT e aggiungo i
				# punti utilizzati con lASSIGNMENT
				importo_corrente = importo_corrente - importo_corrente + punti_utilizzati

			# Return Posweb o B2C: reso di una vendita Posweb o B2C
			elif tipo_operazione == FidelityPointOperationType.RETURN:

				# Se loperazione di origine era di tipo SALE è un reso PosWeb
				if op_root.tipo_operazione == FidelityPointOperationType.SALE:

					# Sottraggo sia i punti guadagnati che i punti utilizzati direttamente dallimporto reale della fidelity
					fidelity.importo_corrente -= punti_guadagnati + punti_utilizzati

					# La riga delloperazione di reso deve essere registrata in FINALIZED per PosWeb
					data[stato] = FidelityPointStatus.FINALIZED

				# Altrimenti sarà un CHECKOUT, quindi un reso B2C
				else:

					# Sottraggo i punti guadagnati dallimporto congelato
					fidelity.importo_congelato -= punti_guadagnati

					# I punti utilizzati invece devo sottrarli dallimporto reale visto che in fase di CHECKOUT erano
					# stati applicati direttamente alla fidelity come punti reali
					fidelity.importo_corrente -= punti_utilizzati

				# La riga delloperazione deve essere registrata con importo negativo
				data["importo"] *= -1
				data["importo_utilizzato"] *= -1

		# Salvo la riga di calcolo dei punti
		# ent_calcolo_punti = self.new(FidelityCalcoloPunti, **data)
		# try:
		# 	self.set(ent_calcolo_punti)
		# except Exception as ex:
		# 	# Intercetto gli errori di integrità che si verificano se inserisco unoperazione già presente su db
		# 	if isinstance(ex, IntegrityError) or isinstance(getattr(ex, original_exception, None), IntegrityError):
		# 		# Se loperazione è un checkout gestisco il replace delloperazione salvata con la corrente
		# 		if tipo_operazione == FidelityPointOperationType.CHECKOUT:
		# 			fidelity, history_data = self.replace_checkout(
		# 				id_operazione, cod_negozio, anno_operazione, fidelity, ent_calcolo_punti, history_data
		# 			)
		# 		else:
		# 			# Per qualsiasi altro caso in cui si verifica lerrore di integrità lancio leccezione
		# 			raise CRMApiError(FD022, tipo_operazione=tipo_operazione, id_operazione=id_operazione)
		# 	else:
		# 		raise ex
		#
		# # Salvo la fidelity dopo le modifiche
		# self.set(fidelity)

		# Tengo traccia del cambiamento di punti sullo storico e salvo la riga
		history_data["importo_corrente"] = importo_corrente
		history_data["importo_congelato"] = importo_congelato

		print "punti congelati ",  history_data["importo_congelato"]
		print "punti_corrente ", history_data["importo_corrente"]

		# Salvo solo se cè stata una variazione di punti reali o congelati, dato che verrà salvata una riga di tipo
		# update non ha senso salvare una riga di storico se non è cambiato null
		# if (tipo_operazione != SALE or
		# 	history_data["importo_orig_corrente"] != history_data["importo_corrente"] or
		# 	history_data["importo_orig_congelato"] != history_data["importo_congelato"]):
		# 	# Salvo la history per le operazioni di CHECKOUT, ASSIGNMENT, RETURN e SALE
		# 	# solo se cè una variazione dei saldi (caso MR con punti a 0)
		# 	history_data["id_calcolo_punti"] = ent_calcolo_punti.id
		# 	self.set(self.new(FidelityHistory, **history_data))


partenza()
