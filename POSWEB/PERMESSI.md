su bms vedi pos_generate_custom_values dove cè il mapping 1 a 1 tra utente e ruolo

USER_ROLE = {
	GERENTE		: POS:::Gerente,
	SUPER			: POS:::Super, (assistenza)
	CASSIERA		: POS:::Cassiera, (cassiera)
	MAGAZZINIERE	: POS:::Magazziniere,
	RDV			: POS:::RDV,
	FISCALAUTHORITY: POS:::FiscalAuthority,
}

ogni pagina del menù di posweb, esempio:
POS:::ImpExp:	{user_role: [SUPER, GERENTE, CASSIERA], machine_env: [CASH, WAREHOUSE, OFFICE]},

la può vedere chi ha il determinato ruolo descritto nel dizionario

poi su posweb nella pagina specifica ci può essere una parte di pagina visibile solo chi ha quel determinato ruolo, esempio:
if contents[role] in (POS:::Gerente, POS:::Super)

---------------------------------------
import config
from poswsbe.pos_generate_custom_values import ws_get_menu_programs
list = ws_get_menu_programs()