RICALCOLO SCORPOPO IVA
REX-14109. OCCHIO AL COD_NEGOZIO ED ID_TRANSAZIONE E VIA DICENDO...

1) Collegandosi a BMS Linmara si guarda a che istanza appartiene il negozio :

select cod_installazione from pos_config_bundle where valore="4401840";

2) Ci si collega via browser alla macchina giusta e si seleziona il negozio a cui manca la vendita,
3) si apre anche il db della macchina e ci si collega in ssh da console

3) Si va in lista vendite cercando per il numero documento e si controlla che manchino davvero i capi,
4) dalla popup si tiene da parte l'id transazione

4) Si fa una nuova vendita con il capo o i capi che mancano (se non scrivono gli sku sulla issue vanno chiesti)
5) e si applicano le promozioni.
Se si ha dubbi su che promozioni aggiungere, basta cercare su BMS LINMARA per codice negozio, anno transazione e l'id_transazione preso da lista vendite:

select * from pos_movimentazioni_custom_multi where anno_transazione="2022" and cod_negozio="4401840" and id_transazione=3470683 and nome="effect_token";
A questo punto il totale della vendita dovrebbe essere uguale al totale della vendita i cui capi sono spariti, lasciare la vendita ferma senza cliccare bottoni. Deve inoltre essere usato lo stesso pk consumer che può essere trovato con questa query:

select * from pos_movimentazioni where anno_transazione="2022" and cod_negozio="4401840" and id_transazione=3470683;

5) Si cercano sul db di negozio i capi che sono stati aggiunti alla vendita,
6) basta trovare quelli in stato CURRENT e in caso tornino più transazioni filtrare per la più recente:

select * from movimenti_capi where cod_negozio="4401840" and codice_stato="CURRENT";

6) Per tutti i capi trovati si modifica il codice_stato in CLOSED e l'id_transazione con quello preso da lista vendite

7) A questo punto da browser si abbandona la vendita senza cliccare alcun bottone,
8) si entra nella pagina di lista vendite e si cerca di nuovo la vendita incriminata, ora si dovrebbero vedere i capi

8) Collegandosi in ssh sulla macchina, per ricalcolare lo scorporo iva, si apre il python di Posweb
con ./bin/python e si incolla questo codice, mettendo il cod_negozio e l'id_transazione corretti
(meglio incollare il codice poco alla volta):

cod_negozio = "4401840"
id_transazione = 3470683

import sys

for lib_dir in ['site/bin', 'site/bin/lib', 'daemons']:
 if not lib_dir in sys.path:
  sys.path.insert(0, lib_dir)

import config_store
import movim_db_access

pard = config_store.application_parameters(use_ws=True)
pard["POS_CONFIG"]["COD_NEGOZIO"] = cod_negozio
config_store.load_config_from_ws(pard)
movim_db_access.salva_dettaglio_iva(pard, pard["POS_CONFIG"]["COD_NEGOZIO"], id_transazione)

13) In sede va eliminata la vendita attuale (modificare i dati nella where):

DELETE
    m,
    pos_movimenti_capi,
    pos_movimenti_contabilita,
    pos_store_credits,
    pos_store_credits_contabilita,
    pos_store_sospesi,
    pos_store_sospesi_contabilita
    FROM pos_movimentazioni m
    LEFT JOIN pos_movimenti_capi USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimenti_contabilita USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimentazioni_custom USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimentazioni_custom_multi USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimentazioni_info_stampa USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimentazioni_relazioni USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimentazioni_split USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimenti_capi_split USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_movimenti_contabilita_split USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_store_credits USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_store_credits_contabilita USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_store_sospesi USING (cod_negozio, anno_transazione, id_transazione)
    LEFT JOIN pos_store_sospesi_contabilita USING (cod_negozio, anno_transazione, id_transazione)
WHERE m.cod_negozio={cod_negozio} AND m.anno_transazione={anno_transazione} AND m.id_transazione={id_transazione}

10) In ssh da negozio si reinvia l'xml (sostituire id_transazione e cod_negozio):

./bin/python bin/xml_recovery.py 3470683 --save 4401840
A questo punto quando l'xml verrà importato si può chiudere la issue