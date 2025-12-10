# select c.num_spedizione, count(c.num_spedizione)
# from (
    select c.sku,
           c.num_ordine,
           c.num_spedizione,
           c.brand,
           c.prezzo_totale,
           c.nome_modello,
           c.desc_variante,
           c.desc_taglia,
           o.tipo_destinatario_spedizione,
           o.negozio_stacco_vendita,
           ifnull(s.is_piazza, )     as is_piazza,
           h.upd_datetime              as data_ora_assegnazione,
           ifnull(s.load_datetime, ) as data_ora_evasione,
           h.stato
    from capo c
             inner join ordine o on c.brand = o.brand and c.num_ordine = o.num_ordine
             left join spedizione s
                       on c.brand = s.brand and c.num_ordine = s.num_ordine and
                          c.num_spedizione = s.num_spedizione
             left join ordine_spedizione_history h
                       on s.num_ordine = h.num_ordine and s.num_spedizione = h.num_spedizione
    where 1 = 1
      and h.stato = ASSEGNATO
      and o.negozio_stacco_vendita in (0100026, 0100200, 0100076, 0100119, 0100100, 0100038, 0100195)
      and o.data_ordine between (2019-06-24) and (2019-07-08)
    order by c.num_ordine desc, c.num_spedizione desc
#      ) c
# where 1 = 1
# group by c.num_spedizione
# having count(c.num_spedizione) > 1;
