per testing

collegare om al docker

collegare posweb a om cambiando i parametri di connessione (senza proxy)

piantare la giacenza su om (vedi la cartella /path/om_remote_sale.diff)

fare una remote sale

quando arriva su om aprire il runtime di docker

python bin/console.py

from ordine.locator import locator as loc
ord = loc.get_service("OrdineService")
ord.crea_spedizioni_da_ordini_b2e()

la spedizione deve essere PRENOTATA

from ordine.locator import locator as loc
ord = loc.get_service("OrdineService")
ord.processa_remote_sales()

si crea un pagamento con stato INVIATO

sul pagamento metto CONFERMATO

sui capi nel campo remote_sale_status metto o TRATTENUTO o RIFIUTATO


R00000000452317
R00000000452316
TERZI AMABILIA


su posweb c'è movim_utils.salva_sale_on_approval() --> rende da OPEN a REPLACED il record SOA o RS
