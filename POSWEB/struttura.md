per includere un view (es, SectionDematerializzazione) in una vecchia pagina di posweb (es, pagina_sospesi)
basta includere il locator del frontend dove si trova la view in questione e usare il render 

in pagina_sospesi.py

from frontend.pos.locator import locator as pos_locator
...
dematerializzazione = pos_locator.get_view("SectionDematerializzazione").render({})


e poi includere la variabile nel html
