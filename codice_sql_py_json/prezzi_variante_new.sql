### PREZZI VARIANTE ATTIVAZIONE ###
-- sul negozio
1) decidere alcuni modelli su cui attivare per ogni variante un prezzo diverso
select p.modello, p.variante, p.id_listino, p.annostag, p.prezzo
from prezzi as p inner join listino_prezzi using(id_listino)
where p.modello in (5481129204,5481129004,5481119004,5481069204) and p.annostag = 20191
order by p.variante;

2) controllo lo stato dei listini prezzi
select id_listino, cod_listino, tipo_prezzo, annostag, data_inizio_validita, data_fine_validita from listino_prezzi as lp;

-- sul bms guardo pos_listino_negozi e pos_prezzi_negozi_<annostag>
1)
select p.modello, p.variante, p.id_listino, p.annostag, p.prezzo
from pos_prezzi_negozi_20191 as p inner join pos_listino_negozi using(id_listino)
where p.modello in (5481129204,5481129004,5481119004,5481069204) and p.annostag = 20191 and p.negozio = 0100600
order by p.variante;

2)
select id_listino, cod_listino, tipo_listino, annostag, data_inizio_validita, data_fine_validita
from pos_listino_negozi as lp
where negozio = 0100600;
