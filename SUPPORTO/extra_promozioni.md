REX-22939 - per l’attività Loyalty Pennyblack PB PEOPLE
periodo: 21-24 settembre INCLUSI
tipo di promozione: Raddoppio punti -->  raddoppia i punti di qualsiasi tipo di acquisto, su qualsiasi canale, fatta in tutti i negozi aderenti al programma, senza distinzione sul tipo di prodotto 
tipi di acquisto: TUTTI (in store, b2e, remote sale, b2c)
negozi aderenti:
DOS: tutti
FRH:  solo alcuni 0103010, 0125025, 0126011, 0169040, 0174009, 0180022, 0183040, 0184034, 0185048, 0188007, 0188013, 0189017, 0196858, 0199059
ECOM: si

considerare tutte le azioni che devono subire la promozione: ASSIGMENT, CHECKOUT (chiamabili solo dal B2C)

insert into in consumer_fidelity_extra_promozione con utente_modifica pari a REX-22939

RADOPPIA è una shortcut che indica cosa fa la query

QUOTATION (chiamabile in comune B2C e negozi) e SALE (chiamabile solo da negozi)

quali negozi? vedi issue

DOS -> diretti --> quali sono di manifatture perché la loyalty è la PB_IT
ECOM -> ecommerce --> consumer_fidelity_history o calcolo_punti --> tipo PB_IT, stato PENDING (sono operazioni da B2C non da altri) e prendo il negozio

faccio
select * 
from consumer_fidelity_tipi_negozi where negozi in (...) and tipo = 'LOYALTY_PB_IT' perché hanno la promo attiva su questi negozi


ora per i negozi trovati dalla query bisogna fare una riga di consumer_fidelity_extra_promozione

INSERT INTO `consumer_fidelity_extra_promozione` (`id_promo`, `tipo`, `cod_negozio`, `pk_consumer_group`, `tipo_operazione`, `data_inizio`, `data_fine`, `extra_promo`, `conditions`, `descrizione_promo`, `async`, `single`, `use_force`, `max_count`, `timestamp_modifica`, `utente_modifica`)
VALUES
	# B2C ASSIGNMENT, CHECKOUT
	(218, 'LOYALTY_PB_IT', '*', NULL, 'ASSIGNMENT', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(219, 'LOYALTY_PB_IT', '*', NULL, 'CHECKOUT', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),

	# QUOTATION E SALE PER OGNI NEGOZIO DOS ED ECOM e FRH (richiesto in issue)
	(220, 'LOYALTY_PB_IT', '0100700', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(245, 'LOYALTY_PB_IT', '0100700', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(221, 'LOYALTY_PB_IT', '0100704', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(246, 'LOYALTY_PB_IT', '0100704', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(222, 'LOYALTY_PB_IT', '0100707', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(247, 'LOYALTY_PB_IT', '0100707', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(223, 'LOYALTY_PB_IT', '0100709', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(248, 'LOYALTY_PB_IT', '0100709', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(224, 'LOYALTY_PB_IT', '0100711', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(249, 'LOYALTY_PB_IT', '0100711', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(225, 'LOYALTY_PB_IT', '0100716', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(250, 'LOYALTY_PB_IT', '0100716', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(226, 'LOYALTY_PB_IT', '0100717', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(251, 'LOYALTY_PB_IT', '0100717', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(227, 'LOYALTY_PB_IT', '0100718', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(252, 'LOYALTY_PB_IT', '0100718', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(228, 'LOYALTY_PB_IT', '0100720', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(253, 'LOYALTY_PB_IT', '0100720', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(229, 'LOYALTY_PB_IT', '0100721', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(254, 'LOYALTY_PB_IT', '0100721', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(230, 'LOYALTY_PB_IT', '0103010', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(255, 'LOYALTY_PB_IT', '0103010', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(231, 'LOYALTY_PB_IT', '0125025', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(256, 'LOYALTY_PB_IT', '0125025', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(232, 'LOYALTY_PB_IT', '0126011', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(257, 'LOYALTY_PB_IT', '0126011', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(244, 'LOYALTY_PB_IT', '0133010', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(269, 'LOYALTY_PB_IT', '0133010', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(233, 'LOYALTY_PB_IT', '0169040', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(258, 'LOYALTY_PB_IT', '0169040', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(234, 'LOYALTY_PB_IT', '0174009', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(259, 'LOYALTY_PB_IT', '0174009', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(235, 'LOYALTY_PB_IT', '0180022', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(260, 'LOYALTY_PB_IT', '0180022', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(236, 'LOYALTY_PB_IT', '0183040', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(261, 'LOYALTY_PB_IT', '0183040', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(237, 'LOYALTY_PB_IT', '0184034', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(262, 'LOYALTY_PB_IT', '0184034', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(238, 'LOYALTY_PB_IT', '0185048', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(263, 'LOYALTY_PB_IT', '0185048', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(239, 'LOYALTY_PB_IT', '0188007', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(264, 'LOYALTY_PB_IT', '0188007', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(240, 'LOYALTY_PB_IT', '0188013', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(265, 'LOYALTY_PB_IT', '0188013', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(241, 'LOYALTY_PB_IT', '0189017', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(266, 'LOYALTY_PB_IT', '0189017', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(242, 'LOYALTY_PB_IT', '0196858', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(267, 'LOYALTY_PB_IT', '0196858', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(243, 'LOYALTY_PB_IT', '0199059', NULL, 'QUOTATION', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939'),
	(268, 'LOYALTY_PB_IT', '0199059', NULL, 'SALE', '20230921', '20230924', 'RADDOPPIA', NULL, 'Pennyblack PB PEOPLE', 0, 0, 0, NULL, '2023-09-15 13:41:59', 'REX-22939');


per fare un test prendo un negozio dos-pb-it prendo MIODINI che ha una fidelity
inserisco solo quotation e sale per il negozio di test. faccio una prova prima e dopo aver tirato le query in crm-test
(quotation da posweb è chiamato dalle doppie frecce prima dei totali)