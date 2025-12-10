in annulla_transazione il parametro SKIP_SALE_DELETE è a 0 su US/CA (posweblite)
e quindi effettuerà la rimozione delle transazioni (al contrario di ES/PT,
dove il parametro sarà valorizzato a 1 e quindi non le rimuove, ma le riporta in stato SUSPENDED)
in US/CA viene rimossa la transazione anche in testata (parametro del_complete)

in questo punto dopo la rimozione avviene una chiamata alla sede con
un record su data_queue di posweb per settare in stato REFUSED le vendite in sede
che sono state cancellate su posweb. (per ripristinarle in caso di errore)
program - ws_set_status_sale

le tasse saranno settate a mano (o in altro modo calcolate ma non su posweb)
il parametro SHOW_TAX_ENABLED è di default a 0 su US/CA (posweblite) 1 per gli altri (USEIT, MMJ e JP)
i posweblite avranno il parametro settato a 0 e non mostreranno
il calcolo tasse (le tasse sono visibili per giappone e us/ca negozi diretti)
(evitano anche il controllo_transazione sulle tasse)
quindi i poswbelite di US/CA non usano VERTEX per il calcolo delle tasse
metodo - common_utils.show_tax_enabled(pard)


sui negozi ECI/EDI ci sono vendite di tipologia ECI/EDI e difficilmente
di altro genere (tipo_applicazione_apertura valorizzato con ECI)
se RIPRESA_LISTA_ENABLED è a 1 in lista_vendite si valorizza
sia la tendina di ricerca filtro per stato e anche la colonna sulle vendite
