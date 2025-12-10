Quando si attiva quel tab dovrebbero essere cambiati anche i parametri

Query di aggiornamento

update pos_config_store_default set valore = '1' where chiave = 'STOCK_CHECK_ENABLED';
update pos_config_store set valore = '1' where chiave = 'STOCK_CHECK_ENABLED';

update pos_config_store_default set valore = '1' where chiave = 'CHECK_VENDITE_NON_ACCOLTE';
update pos_config_store set valore = '1' where chiave = 'CHECK_VENDITE_NON_ACCOLTE';

update pos_config_store_default set valore = '0' where chiave = 'MISSING_ITEMS_SALE_ENABLED';
update pos_config_store set valore = '0' where chiave = 'MISSING_ITEMS_SALE_ENABLED';

Attenzione a informare gli utenti quando si fa in prod, dato che che oltre al tab si attiveranno le seguenti
1) sarà attivo il controllo di giacenza quando si vende un capo (evidenziando in colore diverso i capi non in giacenza)
2) sarà attivo sulla home page un link per mostrare i non accolti
3) non si potrà più vendere capi non presenti a catalogo
