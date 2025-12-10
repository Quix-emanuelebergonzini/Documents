SELECT c.id_transazione, c.importo_finale, c.cod_operazione, c.divisa_pagamento, c.importo_divisa_pagamento, c.importo_iniziale
FROM movimentazioni AS t
LEFT JOIN movimenti_contabilita AS c ON t.cod_negozio = c.cod_negozio AND t.id_transazione = c.id_transazione
WHERE t.cod_negozio = '5601005'
AND t.cod_cassa = '01'
AND t.codice_movimento not in ('LAYBY', 'SALE_ON_APPROVAL') AND t.codice_stato = 'CLOSED'
AND c.codice_movimento = 'CONTABILITA_PAGAMENTO'
AND c.divisa_pagamento = 'HKD';

REX-2344  si rompeva la pagina perché c'era un movimento in valuta
senza un importo che doveva esserci
