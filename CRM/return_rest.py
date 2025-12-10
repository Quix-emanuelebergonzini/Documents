request = {'data': {'cod_negozio': '0133008', 'pk_consumer': '100234799', 'data_ora_operazione': '2024-04-12 12:50:07', 'id_operazione_ref': '15593047', 'cod_negozio_ref': '0133008', 'anno_operazione_ref': '2024', 'reso': {'LOYALTY_MC_IT_24': [{'tipo': 'LOYALTY_MC_IT_24', 'guadagnati': 135.0, 'utilizzati': 0.0, 'punti': 135.0, 'importo_promozione': 0.0, 'progressivo': 1}]}}}

from fidelity.locator import locator as loc
self = loc.get_service("Fidelity")

data = request["data"]

pk_consumer = data["pk_consumer"]

data_ora_operazione = request["data"]["data_ora_operazione"]
cod_negozio_ref = request["data"]["cod_negozio"]
cod_negozio = cod_negozio_ref
id_operazione_ref = request["data"]["id_operazione_ref"]
id_operazione = "{}_{}_{}".format(data_ora_operazione.replace("-", "").replace(":", "").replace(" ", "_"),cod_negozio_ref,id_operazione_ref)

dati_ref = {
	"id_operazione": data["id_operazione_ref"],
	"cod_negozio": data["cod_negozio_ref"],
	"anno_operazione": data["anno_operazione_ref"]
}

fidelity_consumer = self.get_fidelities_for_consumer_store(pk_consumer, cod_negozio)

processed_types = []
fidelity = fidelity_consumer[0]

tipo_fidelity = fidelity.tipo
processed_types.append(tipo_fidelity)
return_data = data["reso"]
fidelity_ret_data = return_data[tipo_fidelity]

punti_guadagnati = punti_utilizzati = 0

for item in fidelity_ret_data:
	punti_guadagnati += float(item["guadagnati"])
	punti_utilizzati += float(item["utilizzati"])

op_accumula_punti = True

anno_operazione = int(data_ora_operazione[0:4])

tipo_operazione = "RETURN"

import json
import datetime
dettaglio_punti = fidelity_ret_data
data = {
	"id_operazione": id_operazione,
	"tipo_operazione": tipo_operazione,
	"cod_negozio": cod_negozio,
	"anno_operazione": anno_operazione,
	"tipo": fidelity.tipo,
	"codice": fidelity.codice,
	"timestamp_operazione": datetime.datetime.strptime(data_ora_operazione, "%Y-%m-%d %H:%M:%S"),
	"stato": "PENDING",
	"importo": punti_guadagnati,
	"importo_utilizzato": punti_utilizzati,
	"custom_data": json.dumps(dettaglio_punti),
	"utente_modifica": self.user or ""
}


data_keys_to_history = ("id_operazione", "tipo_operazione", "cod_negozio", "anno_operazione")
history_custom_data = {k: data[k] for k in data_keys_to_history}

history_custom_data.update({"{}_ref".format(k): dati_ref[k] for k in data_keys_to_history if k in dati_ref})

punti_gift = sum(d['punti'] for d in dettaglio_punti if d['tipo'] == "CONTABILITA_GIFT")

op_root = self.get_root_op_calcolo_punti(tipo_operazione, dati_ref, cod_negozio, fidelity.tipo)
op_accumula_punti = self._op_accumula_punti(op_root)

data["id_ref"] = op_root.id

filtro_asign_root = (
	(e.id_ref == op_root.id) &
	(e.codice == fidelity.codice) &
	(e.tipo == fidelity.tipo) &
	(e.tipo_operazione == "ASSIGNMENT")
)

ents = self.get_some("FidelityCalcoloPunti", filtro_asign_root, limit=1)

freeze_points = self.must_freeze_points(fidelity.tipo, op_root.timestamp_operazione)
#True
fidelity.importo_congelato -= punti_guadagnati

fidelity.importo_corrente -= punti_utilizzati

data["importo"] *= -1
data["importo_utilizzato"] *= -1


replace_checkout_skipped = False
ent_calcolo_punti = self.new('FidelityCalcoloPunti', **data)

#self.set(ent_calcolo_punti)

