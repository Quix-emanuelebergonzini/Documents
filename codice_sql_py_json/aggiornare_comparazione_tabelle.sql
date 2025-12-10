-- traduzioni prese da altro cluster
update mmfg_translations mmfg, (select id, (select group_concat(translated_text)
from mmfg_translations m
where m.language = 'en'
and m.cluster = 'common' and m.id = o.id) as 'new_translation'
from mmfg_translations o
where o.cluster = 'anagrafica_new' and o.language = 'en') appoggio
set mmfg.translated_text = appoggio.new_translation
where mmfg.id = appoggio.id;

-- aggiornare un mapping modificandolo all'occorenza, prendendo
-- il dato da altra tabella
update ana_soggetto ana, (select temp.codice_gruppo,
case
	when p_tipologia is null and temp.codice_gruppo not like '%PIATT_%' then 'NEGOZIO'
	when p_tipologia is null and temp.codice_gruppo like '%PIATT_%' then 'MAGAZZINO'
	when p_tipologia = 'NEGOZIO_MAGAZZINO' then 'NEGOZIO_MAGAZZINO'
	when p_tipologia <> 'NEGOZIO_MAGAZZINO' and (p_tipologia like '%MAGA%' or p_tipologia like '%BOX%') then 'MAGAZZINO'
END
as 'tipologia'
from (select codice_gruppo, (select group_concat(distinct tipologia)
from priorita where codice_gruppo = a.codice_gruppo
AND tipologia <> 'NEGOZIO') as 'p_tipologia'
from ana_soggetto a
order by p_tipologia) temp) appoggio
set ana.tipologia = appoggio.tipologia
where ana.codice_gruppo = appoggio.codice_gruppo;
