gli EDI arrivano su tutti i posweblite tranne CN.
nessuna logica. chiude solo vendite già fatte.

arrivano da EDI (sistema esterno) e li scrivono sui posweblite

... where codice_status = SUSPEND and tipo_applicazione_apertura = EDI ...

Vengono esportate al negozio in incrementale a differenza del normale flusso (che non mandano le vendite in incr...)
Quindi su ES,MX c'è un ulteriore incr che gira durante il giorno solo per il cod_installazione POSWEB_ONLINE

gli incr sulla sede esporta sui negozi con codice_stato SUSPENDED. si riprendono da posweb e si chiudono

Quindi se qualcuno non vede le vendite sul negozio, magari è passato prima gli incrs e poi l'utente è
andato a vederle (su lista vendite) quindi non sono ancora arrivate al negozio.


cosa succede nella realtà (EDI, BMS, EDW, BOARD):
- EDI esporta in venduto alle 8:30 verso BMS (maxima20)
- tali file vengono inviati da BMS a EDW (non sono però a conoscenza delle tempistiche e schedulazioni sul primo)
- EDW importa il venduto tre volte al giorno, mattina, pomeriggio e sera
- BOARD importa i dati una volta in mattinata


Da lista vendita si può recuperare la vendita e farci portare nella pagina vendita per poterla chiudere

Cosa succcede se recuparata una vendita EDI e si preme il tasto ANNULLA:
se sul negozio il parametro SKIP_SALE_DELETE è a 1:
- sbianca la pagina di vendita, ma la vendita è ancora SUSPEND.
- la pagina si sbianca e si genera un nuovo id_transazione per la vendita successiva

Il paramtro SKIP_SALE_DELETE è a 0
Se la vogliono proprio RIFIUTARE:
- il bottone ANNULLA esegue un annullo di vendita (vendita eliminata da negozio)
- viene scritto in data_queue un record json con data_content
  {"program": "ws_set_status_sale", "ws_id_transazione": "676132", "ws_cod_negozio": "0100216", "ws_anno_transazione": 2022} a WS_SEDE
- su sede la vendita cambia stato in REFUSED
- la pagina si sbianca e si genera un nuovo id_transazione per la vendita successiva

Se la vogliamo (ri)sospendere, premendo il tasto INTERROMPI:
- sbianca la pagina di vendita, ma la vendita è ancora SUSPEND.
- la pagina si sbianca e si genera un nuovo id_transazione per la vendita successiva