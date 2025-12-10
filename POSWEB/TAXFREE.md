########################################## TEXFREE #############################################

*** MAGICO TAX FREE ***

# Job di poswsbe:
Job taxfree_init.py -> dismesso, era per la vecchia versione
Job taxfree_manager.py -g -> ora va eseguito sempre questo, con 4 modalità diverse (e sempre con -g)
-m GB_DESK -> parte dalle configurazioni di base di ana_negozi_tax_free per popolare le altre configurazioni dei negozi
-m GB_COUNTRIES -> popola i paesi gestiti da Global Blue nella tabella ana_negozi_tax_free_country
-m GB_BLOCKED -> spegne/accende i paesi nella tabella ana_negozi_tax_free_country (alcuni non possono fare tax free)
-m GB_DOCIDS -> popola pos_tax_free_offline con i doc_id da usare offline
forti limitazioni alle chiamate (anche in test!): una volta al giorno per negozio, richieste solo se sotto soglia

Se fate un setup iniziale, es. nuovo negozio in test, vanno eseguite nell'ordine esatto riportato qui sopra
Poi vi servirà un part di NazioniTaxfree,TaxFree,TaxFreeOffline (oppure un incr ovviamente)
Altri dettagli qui:
https://docs.google.com/spreadsheets/d/1sFPpzttcVgR5XGNRL4pvLi8TyL4_cp0G7GqcTjyDRYY/edit#gid=1656825011

# Taxfree da negozio:
Controllare che ci sia GRIPS_MX_ENABLED = 2 (1 era la vecchia versione dismessa, 0 spegne tutto)
Il tab del Taxfree in vendita appare solo se si supera una spesa minima configurabile (attualmente 154.95 EUR)
Finestra di ricerca per card/cellulare -> chiamata traveller che scarica i dati consumatrice da Global Blue
Chiudi vendita -> fa partire la chiamata di ISSUE che registra il Taxfree su Global Blue e lo stampa su negozio
Dalla pagina dei resi invece tutti i campi sono auto-fillati e parte una chiamata di VOID
Se il negozio è offline e c'è almeno un doc_id offline da usare parte una ISSUE_OFF (o VOID_OFF)
Questa non parla con Global Blue in tempo reale ma viene registrata su una queue di negozio da spedire appena online
Codice magico KO per stornare le Issue fallite male (che quindi non hanno un doc_id valido)

## fine appunti Demetrio ##


###############################################################################################
ATTIVAZIONE (non so cosa sia ma mi è stato detto così)
main/nazioni_taxfree nel db
    cercare per country_code = 643
    e mettere
    document_country_code = 643
    e phone_prefix = 7
main/store_config nel db
    cercare per key_name = GRIPS_MX_ENABLED
    e mettere
    key_value = 2

- il prezzo di vendita deve essere sopra 154 euro
- gli scontrini targati GlobalBlue non sono di nostra gestione (servizio esterno)
- poi fare una vendita con una consumatrice con tutti i dati e mettere pure che lei sia RUSSA anche se non lo è

####

attivi in tutta italia + diffusione tessile (no estero)
*come fare il test*
1. vado sulle vendite/reso di posweb ed effettuo una vendita con (invece del solito scontrino) selezione su TAX_FREE
la nuova modalità è per key_name=GRIPS_MX_ENABLED = 2
2. inserire i dati della consumatrice, una falsa data di nascita, passaporto, etc. e fare vendita.
3. viene chiamata la sede BMS che chiama GlobalBlue
    * i metodi (in sede) sono get_void_cheque (resi), get_issue_rendered_cheque (vendite)
    * in caso voglia il negozio offline devo disattivare il demone POS_KEEPALIVE e mettere nella global_status il CONN_STATUS = 0
    di conseguenza se faccio vendite/resi offline i metodi sono get_offline_issue_cheque (vendita), get_offline_void_cheque (resi)

(usare, forse, dos-mm-it)

*le tabelle da conoscere*
nella sede quando si fa un tax free si deve creare nella tabella log_tax_free_20191 un log ISSUE_OFF con codice 00 e un doc_id valorizzato
nella sede quando si fa un reso tax free si deve creare nella tabella log_tax_free_20191 un log VOID_OFF con codice 00 e un doc_id valorizzato uguale al ISSUE_OFF

*rompere la chiamata a global blue*
per rompere la chiamata di global blue devo inserire in negozio nella tabella tax_free_off un doc_id con data più vecchia di tutte le altre
così dopo facendo una vendita invierà a global blue ancora quel codice già registrato da global blue e quindi andrà in eccezione nei metodi sopra citati

########################################################################

attivi in tutta italia + diffusione tessile (no estero)

*come fare il test*
1. vado sulle vendite/reso di posweb ed effettuo una vendita con (invece del solito scontrino) selezione su TAX_FREE
la nuova modalità è per key_name=GRIPS_MX_ENABLED = 2
2. inserire i dati della consumatrice, una falsa data di nascita, passaporto, etc. e fare vendita.
3. viene chiamata la sede BMS che chiama GlobalBlue
    * i metodi (in sede) sono get_void_cheque (resi), get_issue_rendered_cheque (vendite)
    * in caso voglia il negozio offline devo disattivare il demone POS_KEEPALIVE e mettere nella global_status il CON_STATUS = 0
    di conseguenza se faccio vendite/resi offline i metodi sono get_offline_issue_cheque (vendita), get_offline_void_cheque (resi)

(usare, forse, dos-mm-it)

*le tabelle da conoscere*
nella sede quando si fa un tax free si deve creare nella tabella log_tax_free_20191 un log ISSUE_OFF con codice 00 e un doc_id valorizzato
nella sede quando si fa un reso tax free si deve creare nella tabella log_tax_free_20191 un log VOID_OFF con codice 00 e un doc_id valorizzato uguale al ISSUE_OFF

*rompere la chiamata a global blue*
per rompere la chiamata di global blue devo inserire in negozio nella tabella tax_free_off un doc_id con data più vecchia di tutte le altre
così dopo facendo una vendita invierà a global blue ancora quel codice già registrato da global blue e quindi andrà in eccezione nei metodi sopra citati

########################################################################
