o2o (offine to online) e b2c --> si parla di ordini online

Per gli ordini B2C Marella ha la funzionalità attiva. Acquisto online, ritiro in negozio

esempio
COD_INSTALLAZIONE = 9000100404
LISTA_COD_NEGOZIO = 0100404

in Vendita/Avanzamento Ordni si vede una pagina di boss con gli ordini b2c/b2e da ricercare
    - qui cè la stampa della bollettina (ritiro presso il negozio)
in Vendita/Resi Ordini online si vede la pagina di posweb con la ricerca dei resi b2c (simulate = true per i test)
in Vendita/Lista Resi Ordini online si vede una pagina di boss con i resi possibili degli ordini b2c

--------
durante il processo di vendita da website (b2c) viene chiamato
il crm per avere il calcolo dei punti (quotation)
però noi non logghiamo questa chiamata, ma sappiamo che viene invocato
fidelityRest.update in particolare calculate_amount

le quotation non vengono loggate ma non abbiamo controlli per validare
se la consumatrice ha punti sufficienti per aver lo sconto da punti
vedi issue https://jira.mmfg.it/browse/CRM-1666 (risposta di MarcoM)

-------

tabelle da guardare sono info_ordine_b2c e b2c_contatori

select *
from info_ordine_b2c
where id_ordine in ('36355891', '35949682'); --> json data della vendita

select *
from b2c_contatori
where num_ordine in ('36355891', '35949682'); --> altre info



IMPORTANTE:
quando viene effettuato un ordine b2c loro ci chiamano per avere i punti
chiamano il crm il servizio fidelityRest.update (calculate_amount)


------------------------
noi non facciamo per b2c una chiamata al corriere
e boss chiama bms (software di OT) ma anche loro non lo fanno

si consiglia di utilizzare il servizo simulate = True per studiare
bene il comportamento

------------------------------------------------------------------------
------------------------------------------------------------------------
------------------------------------------------------------------------
------------------------------------------------------------------------
(01/12/2022)
Nuovo OM Staging (dos-ma-it-staging macchina di test)

(Guglielmo Bertoli di Intrend)
Con questo nuovo progetto stargate viene tagliato fuori completamente
la gestione degli ordini è solo su OM
E parliamo di OM Staging

A differenza rispetto ad OM che invece recupera le vendita da Stargate (o viceversa)

La pagina di Posweb Resi Ordini Online chiama om per avere brand/region e poi chiama
(MuleSoft) Stargate per avere i dettaglio degli ordini.