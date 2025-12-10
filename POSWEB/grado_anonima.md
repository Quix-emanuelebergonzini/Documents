Riepilogo regole gradi anonimato:

101: consumatrice anonimizzata per GDPR
100: pk_consumer creati da posweb in attesa di arrivo dati da flusso (questo grado anonimato è prettamente tecnico)
50: consumatrici senza nome o senza cognome, con cognome diverso da "UNKNOW" e "UNKNOWN" (queste sono le consumatrici prospect da Salesforce)
e senza nazione_iso
40: consumatrici senza nome o senza cognome, con cognome diverso da "UNKNOW" e "UNKNOWN" (queste sono le consumatrici prospect da Salesforce) 
e con nazione_iso
30: consumatrici con nome e con cognome, senza dati di contatto (indirizzo o email o telefono primario o cellulare primario) e senza acquisti (o solo omaggi) negli ultimi 3 anni
20: consumatrici con nome e con cognome, senza dati di contatto (indirizzo o email o telefono primario o cellulare primario) e con almeno un acquisto (non omaggio) negli ultimi 3 anni
10/0: consumatrici con nome e cognome e almeno un dato di contatto (indirizzo o email o telefono primario o cellulare primario).
Il flag non_trattare discrimina tra grado anonimato 10 (non_trattare = 1) e 0 (non_trattare = 0) ma visto che ad oggi non è più usato i due gradi anonimato sono da considerarsi equivalenti e
rappresentano il grado di anonimato "meno anonimo"


https://maxmarafashiongroup.atlassian.net/wiki/spaces/CRM/pages/3884744800/Documentazione+tecnica+per+fusione+consumatrici