-- report catalogo scontato
SELECT
  p.modello,
  p.variante,
  p.pezzo,
  listino.data_inizio_validita AS data_validita,
  p.prezzo,
  --prezzo                        scontato
p.perc,
p.importo_sconto AS importo_sconto,
p2.prezzo AS prezzo_listino, --prezzo di vendita
p2.data_inizio_validita AS data_inizio_validita_listino,
c.nome, c.annostag, c.societa, c.collezione, c.desc_collezione, c.classe, c.desc_classe,
p.divisa AS currency,
p.tot AS giacenza,
listino.id_listino,
p.data_modifica
FROM prezzi p
INNER JOIN prezzi p2 ON ( p.cod_negozio = p2.cod_negozio AND p.modello = p2.modello AND p.pezzo = p2.pezzo )
INNER JOIN listino_prezzi listino ON listino.id_listino= p.id_listino AND listino.tipo_prezzo = p.tipo_prezzo
INNER JOIN catalogo AS c ON (p.modello = c.modello AND p.pezzo = c.pezzo)
WHERE 1=1
AND p.cod_negozio = 0100617
AND p.tipo_prezzo = S
AND p2.tipo_prezzo = V
AND listino.data_inizio_validita = 20190320
AND p2.data_inizio_validita <= 20190320
GROUP BY p.modello, p.pezzo, p.variante, p2.data_inizio_validita

-- report validita listino prezzi variante
SELECT data_inizio_validita
FROM listino_prezzi
WHERE 1=1
	AND cod_negozio = 0100617
	AND data_inizio_validita != 
	AND data_fine_validita != 
	AND data_inizio_validita <= 20190320
	AND data_fine_validita >= 20190320
	AND tipo_prezzo = S
ORDER BY data_inizio_validita DESC

-- inserimento prezzi per brand
INSERT INTO prezzi (cod_negozio, modello, variante, pezzo, tipo_prezzo, id_listino, data_inizio_validita, data_fine_validita, prezzo, divisa, perc, importo_sconto, tot, annostag, data_modifica)
VALUES (0100617, 1021018004, 059, 0, V, null, , , 900.00, EUR, 0.00, 0.00, 0, 20191, 2019-03-18 00:00:00);
INSERT INTO prezzi (cod_negozio, modello, variante, pezzo, tipo_prezzo, id_listino, data_inizio_validita, data_fine_validita, prezzo, divisa, perc, importo_sconto, tot, annostag, data_modifica)
VALUES (0100617, 1021018004, 059, 0, S, 801, , , 630.00, EUR, 0.00, 30.00, 0, 20191, 2019-03-18 00:00:00);
INSERT INTO prezzi (cod_negozio, modello, variante, pezzo, tipo_prezzo, id_listino, data_inizio_validita, data_fine_validita, prezzo, divisa, perc, importo_sconto, tot, annostag, data_modifica)
VALUES (0100617, 1021018004, 828, 0, V, null, , , 250.00, EUR, 0.00, 0.00, 0, 20191, 2019-03-18 00:00:00);
INSERT INTO prezzi (cod_negozio, modello, variante, pezzo, tipo_prezzo, id_listino, data_inizio_validita, data_fine_validita, prezzo, divisa, perc, importo_sconto, tot, annostag, data_modifica)
VALUES (0100617, 1021018004, 828, 0, C, 803, , , 200.00, EUR, 0.00, 20.00, 0, 20191, 2019-03-18 00:00:00);
