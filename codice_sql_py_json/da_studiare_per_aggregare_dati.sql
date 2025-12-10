insert into piazza
SELECT c.context_id, a2.codice_gruppo AS codice_negozio_spedente, a.codice_gruppo AS codice_negozio_mittente, 0 AS spedizione_manuale, CURRENT_TIMESTAMP AS upd_datetime, 'bergonzinie' AS upd_user
FROM context c
INNER JOIN priorita p USING(context_id)
INNER JOIN ana_soggetto a USING(context_id, codice_gruppo)
INNER JOIN priorita p2 USING(context_id)
INNER JOIN ana_soggetto a2 ON a2.codice_gruppo=p2.codice_gruppo AND a2.nazione="HK" AND a2.codice_gruppo NOT LIKE "PIATT%"
WHERE c.region="MO" AND a.nazione="MO"

tipica query per creare un mapping in poche parole

se voglio sapere tutti i negozi che devo aggiungere ad una data tabella (con certe caratteristiche)
abbinati ad un dato negozio o più negozi.

in questo caso voglio che tutti i negozi MACAO (MO) abbiano in piazza tutti i negozi HK
a parità di contesto (idem brand perché il contesto è quel brand)

196	1101024	5601006	0	2021-04-28 07:22:09	bergonzinie
196	1101029	5601006	0	2021-04-28 07:22:09	bergonzinie
196	1101062	5601006	0	2021-04-28 07:22:09	bergonzinie
196	1101065	5601006	0	2021-04-28 07:22:09	bergonzinie
196	1101118	5601006	0	2021-04-28 07:22:09	bergonzinie

i negozi nella prima colonna sono gli stessi sotto per un negozio diverso nella terza colonna

196	1101024	5601007	0	2021-04-28 07:22:09	bergonzinie
196	1101029	5601007	0	2021-04-28 07:22:09	bergonzinie
196	1101062	5601007	0	2021-04-28 07:22:09	bergonzinie
196	1101065	5601007	0	2021-04-28 07:22:09	bergonzinie
196	1101118	5601007	0	2021-04-28 07:22:09	bergonzinie
