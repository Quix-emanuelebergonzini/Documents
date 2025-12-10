# api_request_log
sulla tabella api_request_log di crm
è obbligo apporre il filtro per pk_consumer altrimenti si pianta tutto...

è una tabella che logga tutte le chiamate a CRM derivanti da chiamate api

su ambiente di test pk_consumer 10248080 (rif. Bergonzini Emanuele)

Nella chiamata se si mette { "data": "debug": True,... } si possono vedere i dettagli dei calcoli dei punti

I punti, solo per il guadagno sul totale speso, non sullo spalamaggio calcolati allimporto successivo
(arrotondamento per eccesso). es, 13,1 --> 14!!!


################################### MULE #################################################
logging nella tabella api_request_log attraverso le v2, ma il controller è quello common
CRMConsumerNotify -> notify
nella chiamata dellapi
{
	"data": {
		"request_payload": {
		},
		"ext_name": "slf",
		"status": "SYNC",
		"error": "",
		"id": "8660206,", # i possibili valori sono:
		    pk_consumer singolo per un consumer
		    pk_consumer consumer_indirizzo , valore della colonna tipo_indirizzo (es, Residence)
		    pk_consumer consumer_contatto  , valore della colonna tipo_contatto (es, phone_primary)
		    pk_consumer consumer_privacy   , valore della colonna ????

		"requestid": "e3361c58-209e-49d3-ab86-166b37c7e304"
	},
	"type": "notify"
}