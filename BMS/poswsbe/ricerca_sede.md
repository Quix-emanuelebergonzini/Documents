POSWEB
quando digito sull'autocomplete della ricerca di vendita posso immettere:

- nome
- numero di telefono (con o senza il +)
- barcode fidelity
- pk-<numero> oppure pk-MMJ_<numero> (e simili con prefisso)

nota bene: ricerca per fidelity / telefono sempre attiva ( non solo asia )
viene invocato pos.consumatrici_json

da pagina della vendita
Consumer.get_consumatrice_privilegiata - ricerca per fidelity
Consumer.get_consumatrice_numero_list - ricerca per numero di telefono
Consumer.get_consumatrice_per_email - ricerca per email

da pagina delle consumatrici
common_db_access.get_lista_consumatrici_ricerca

poi c'è la ricerca consumatrice di gruppo
pos.ricerca_consumatrice_gruppo
Consumer.get_consumatrici_sede
ws_ricerca_consumatrici (su BMS vedi sotto)

per la chiave telefono_fullwidth
from validation import locale
locale.transliterate_latin(dati_d["telefono"])


-- BMS ---
>> aprire python console
from poswsbe.consumer.locator import locator as loc
serv = loc.get_service("PosWsBeConsumerService")

>> alcuni esempio poi si possono fare molte combinazioni di ricerca:
filtro = {
  "cognome":"MARCOM",
  "nome":"TESTTEST",
  "telefono_fullwidth": "\uff10\uff15\uff19\uff13\uff16\uff11\uff12\uff11\uff14",
}
oppure
filtro = {
  "promotions": "SYNC",
  "search_BMS_only": True,
  "brand_consensi": "MM",
  "alfabeti_indirizzi": ["JAPA"],
  "enabled_search_decoded": True,
  "codice_proprietario": "MMJ",
  "telefono": "059121212",
  "alfabeti_nomi": ["KANJI", "KANA"]
}
oppure
filtro = {
  "promotions": "SYNC",
  "search_BMS_only": False,
  "brand_consensi": "MM",
  "alfabeti_indirizzi": ["JAPA"],
  "enabled_search_decoded": True,
  "codice_proprietario": "MMJ",
  "email": "uncompleted@uncompleted.com",
  "alfabeti_nomi": ["KANJI", "KANA"]
}
oppure
filtro = { 
  "cod_negozio": "0100400",
  "promotions": "SYNC",
  "search_BMS_only": True,
  "brand_consensi": "MM",
  "alfabeti_indirizzi": ["JAPA"],
  "enabled_search_decoded": True,
  "codice_proprietario": "MMJ",
  "telefono": "+810353986946",
  "telefono_fullwidth": "\uff0b\uff18\uff11\uff10\uff13\uff15\uff13\uff19\uff18\uff16\uff19\uff14\uff16",
  "alfabeti_nomi": ["KANJI", "KANA"],
  "search_extended_insegna": "MM"
}
serv.ricerca_consumatrici_BMS(filtro, negozi_l=['0801234',])

n.b: se c'è la email non ci sono altri campi (nome, cognome, telefono, fidelity, consumer_id)
  se c'è il telefono non ci sono altri campi (nome, cognome, fidelity, email, consumer_id)
  se c'è il consumer_id non ci sono altri campi (nome, cognome, telefono, email, fidelity)
  se c'è la fidelity non ci sono altri campi (nome, cognome, telefono, email, consumer_id)
quindi ad esempio inutile cercare in AND su telefono ed email allo stesso tempo

il parametro "search_BMS_only" se impostato a False chiama il crm
vedi posfe/ws_interface_store.py --> ws_ricerca_consumatrici

su qualsiasi ambiente (es, MMJ) si può imbrogliare e mettere a False così
che chiami crm anche se il giappone non ha questa modalità


-- CRM --
initiative.service
CRMBackOffice.ricerca_consumatrici_da_pos()

from initiative.locator import locator as loc
serv = loc.get_service("CRMBackOffice")
filtro = { "telefono": "059121212", "enabled_search_decoded": True, "cod_negozio": "0801234"}
serv.ricerca_consumatrici_da_pos(filtro)
