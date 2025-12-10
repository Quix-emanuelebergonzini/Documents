SELECT codice_proprietario, negozio, chiave, valore, utente, modificato
FROM (
SELECT codice_proprietario, negozio, chiave, valore, utente, modificato FROM pos_config_store where negozio = '0801424'
UNION ALL
SELECT codice_proprietario, negozio, chiave, valore, utente, modificato FROM pos_config_store where negozio = '0801038'
) tbl
GROUP BY codice_proprietario, negozio, chiave, valore, utente, modificato
HAVING count(*) = 1
ORDER BY chiave;


dove i fields della select vengono tutti sostituiti in
tutte le SELECT, GROUP BY

così si comparano (più o meno) i valori presi in questo caso da due negozi
dalla pos_config_store e si vedono le differenze

esempio...
MMJ	0801424	AVAILABLE_BRANDS	MM	davolii	2020-09-22 09:47:57
MMJ	0801038	AVAILABLE_BRANDS			2021-01-26 13:30:07
MMJ	0801424	B2E_ENABLED	1		2020-09-22 09:47:17
MMJ	0801038	B2E_ENABLED	1		2021-01-26 13:30:07

non il massimo ma si può fare di meglio....
