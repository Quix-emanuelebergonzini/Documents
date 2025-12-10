--SUL NEGOZIO
select tipo_prezzo, data_inizio_validita, data_fine_validita
from listino_prezzi;

select c.sku, p.modello
from prezzi p
inner join catalogo_b2e c on c.modello = p.modello
where tipo_prezzo = S limit 5; -- e S deve essere valido ad oggi

SELECT concat('fid_punti.', COLUMN_NAME)
FROM information_schema.columns
WHERE  table_name = 'consumer_fidelity_calcolo_punti';
