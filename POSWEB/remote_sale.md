in posweb l'etichetta se la consumer ha o meno remote sale
appare da questa query

SELECT movimentazioni.*,
	(select count(*) from movimenti_capi cap where cap.id_transazione = movimentazioni.id_transazione) as nr_cap
FROM movimentazioni
WHERE cod_mitt_dest	 = '6015140'
	AND codice_movimento = 'SALE_ON_APPROVAL'
	AND codice_stato = 'OPEN'
	ORDER BY data_documento DESC


se è in stato ANNULLATO la remote sale dalla lista visibile sul negozio
significa che è già stata chiusa precedentemente.

Dopo che si recupera una remote_sale dalla etichetta per una data consumatrice
il servizio deve chiamare OM e farsi dare lo stato della vendita, dei capi
e capire chi sono rifiutati o accettati

dopo la cassiera chiude la vendita e viene staccato un xml

si creano due movimentazioni una che diventa OPEN --> REPLACED
e un altra che diventa se ANNULLATO in stato VOID
altrimenti in stato FINALIZED

le remote_sale seguono buona parte di quello che accade con le sale_on_approval

cmq pos.recupera_transazione

poi nel pos.chiudi_vendita
e in particolare movim_utils.salva_sale_on_approval


-------------
log non presenti per REMOTE_SALE con problema in fase di pagamento...

SELECT *
FROM pos_movimentazioni
WHERE id_transazione = '92954' AND anno_transazione = '2022' AND cod_negozio = '0100023';

SELECT *
FROM pos_movimenti_capi
WHERE id_transazione = '92954' AND anno_transazione = '2022' AND cod_negozio = '0100023';
