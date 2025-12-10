Gestione dei listini (tipi prezzo)

S = SALDO
P = PRE_SALDO
C = SALDI PRIVATI
V = REGOLARE - PREZZO PIENO - VENDITA
questa è la priorità

Solitamente S e P non possono essere presenti contemporaneamente

Possono esiste più listini attivi contemporaneamente (per cui sopra è possibile avere più tipi prezzi vigenti per un capo)

Se LISTINO_ESTESO_ENABLED = 1 è attivo quindi i pressi sono per Modello/Variante esiste la (remota) possibilità di inserire
un prezzo differente per una variante rispetto alle altre


Cosa succederà: sulla B2E con LISTINO_ESTESO_ENABLED = 1 se price_type_applied è ad esempio P,
ma non c'è il prezzo P sul quella variante esso verrà sostituito con C. Se anche C non ci fosse allore prenderà V