Per forzare i negozi a rigenerare il sid si può fare questo accrocchio

update session_head set user_data = CONCAT("{", user_data) where user_data like '%nw%';

Mettendo un json corrotto si fa in modo che la chiamata di validazione del sid vada in errore,
costringendo poswsfe a ristaccare un nuovo sid e ad inviarlo al negozio.
