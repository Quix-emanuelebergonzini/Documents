in pratica dentro alle sartorie fuori vendita (quelle in basso a sinistra)

si decide la classe
si immette una descrizione e si flegga il checkbox e poi invece di mettere
il prezzo si clicca sull'immaginina a destra dei contanti

quando si clicca diventa una immagine con contanti con una X

dopo che si salva si ha in movimenti_contabilita un codice_movimento
CONTABILITA_SARTORIA_OMAGGIO

VEDI ANCHE vendita-sartoria.js (non vendita-editmodello.js)


select * from movimenti_contabilita where codice_movimento = 'CONTABILITA_SARTORIA_OMAGGIO' and codice_stato = 'CURRENT' limit 1;
id_transazione = 35258
   progressivo = 1
   cod_negozio = 0901042
tipo_applicazione = POSWEB
 id_postazione = 01
  codice_stato = CURRENT
progressivo_capo = 0
codice_movimento = CONTABILITA_SARTORIA_OMAGGIO
cod_operazione = 99
dati_operazione = {"rdv": "E1841", "desc_classe": "Pantalon court", "iva": 20.0, "tipo": "VENDITA", "gruppo": "1", "classe": "14", "data_consegna_sartoria": "", "descrizione": "sartoria", "nota_lavorazioni": ""}
importo_iniziale = 10
importo_finale = 0
        divisa = EUR
importo_divisa_pagamento =
divisa_pagamento =
          nota =
       barcode =
          reso = 0
data_creazione = 2021-04-22 11:54:54
 data_modifica = 2021-04-22 11:54:54
