il portale abilita le pagine.

per controllare quello che arriva come abilitazione ci si può collegare
al BMS di riferimento e provare con il python:

import config 
from poswsbe.pos_generate_custom_values import ws_get_menu_programs, ws_get_menu_structure
 -- sono i programs che arrivano giù
list_menu = ws_get_menu_programs()
 -- struttura del menù qui si può capire se viene messo a menù e sotto quale
list_struct = ws_get_menu_structure()

se io apro la tablla pos_custom_values

name è così composto MENU_<TIPOLOGIA>_<GRUPPO_UTENTE>_<ON/OFF>_<|FE>

TIPOLOGIA = {
    'CASH': 'cassa_posweb'
}

GRUPPO_UTENTE = {
    'SUPER': 'assistenza'
}

<ON_OFF> --> ON se il negozio è online in quel momento, OFF se offline


esempio,
se io entro in un POSWEB_OFFLINE con assitenza devo cercare la voce
MENU_CASH_SUPER_ON

<|FE> - se presente FE sono i permessi per le macchine abstract


-----

NUOVO MENU' SU POSWEB CHE APRE UN IFRAME SU BMS

https://maxmarafashiongroup.atlassian.net/browse/FGPOS-465

c'è la procedura per fare una nuova pagina e aprire una segnalazione anche alle ops di mmfg
ricordati di chattare ad erika la loro issue che aprirai