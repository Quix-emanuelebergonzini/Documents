su linmara concession una vendita con promozione applicata (v1) è arrivata in sede
senza il capo incluso. cosa sia successo non si sa..
per recuperare la vendita si può ovviare in questo modo

sul negozio ricreo la situazione aggiungendo il capo e applicando la promo
(con l'aiuto o meno della promozione applicata...tipo se è uno sconto e so di quanto
posso aggiungerlo a manina...)

dopo di che a db lo recupero e poi gli cambio id_transazione con quello della mia issue

non è finita. bisogna ricreare l'aliquota_d

avvio sulla macchina in python questo script

vedi anche https://jira.mmfg.it/browse/REX-14109?focusedCommentId=1283448&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-1283448



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from future.builtins import *
import sys
import logging

for lib_dir in [
   'site/bin',
   'site/bin/lib',
]:
   if lib_dir not in sys.path:
      sys.path.insert(0, lib_dir)

import config_store
import movim_db_access
import json
pard = config_store.application_parameters(use_ws=True)

pard['POS_CONFIG']['IVA_ITEM_DETAIL_ENABLED'] = "1"
pard['ws_country_code'] = "CN"
pard["ws_decimal_places_currency"] = 2
pard["POS_CONFIG"]['COD_NEGOZIO'] = '4401135'
movim_db_access.salva_dettaglio_iva(pard, "4401135", 3581755)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

dopo di che controllo che si sia salvata aliquota sulla movimentazione giusta
con i dati corretti

poi posso rigenerare xml con xml_recovery

python bin/xml_recovery.py 3581755 --save 4401135

così deve salire in sede un nuovo xml e poi spaccarsi per chiave duplicata.

quindi elimino da dentro le tabelle pos_movim*** tutti i riferimenti e poi reimporto e controllo
che la vendita sia tutta perfettamente entrata

INSERT INTO `pos_movimentazioni` (`anno_transazione`, `id_transazione`, `cod_negozio`, `id_carrello`, `origine`, `numero_documento`, `numero_documento_orig`, `data_documento`, `ora_documento`, `codice_stato`, `codice_movimento`, `cod_mitt_dest`, `pk_consumer`, `id_utente`, `cod_cassiera`, `cod_cassa`, `sid`, `nota`, `divisa`, `importo_iniziale`, `importo_finale_capi`, `importo_finale`, `importo_pagato`, `esenzione_iva`, `capi`, `cod_documento`, `dati_documenti`, `numero_stampa_documento`, `flag_stampa_documento`, `data_creazione`, `file_name`, `codice_proprietario`, `upd_datetime`, `stato`, `cod_vettore`, `tipo_applicazione_apertura`, `id_postazione_apertura`, `tipo_applicazione_chiusura`, `id_postazione_chiusura`, `dati_aggiuntivi`, `dettaglio_iva`, `data_modifica`, `canale`, `nazione_oss`)
VALUES
	('2021', 3583489, '4401019', 'PW214401019000000655', 'POS_OFFLINE', 3227, '3227', '20211030', '192056', 'CLOSED', 'VENDITA', 'LIN_1106778', 'LIN_1106778', '4401019', 'E450924', '01', 'bd0sdqn0vhmm1q', '\æ?°å®¢ \ç»?\å?¸æ¬¾\è¢?\æ??\ä¸?\å¥? æ»¡2.2\ä¸?èµ 47160115', 'CNY', 0.00, 0.00, 27090.00, 0.00, '0', 0, 'SALE_TICKET', '{\"numero_scontrino\": \"3227\", \"dati_documento\": {\"currency\": \"CNY\", \"tax_total_amount\": \"0.00\", \"total_amount\": \"0.00\", \"taxable_total_amount\": \"0.00\"}}', '3227', 1, '2021-10-30 11:20:57', '4401019_20211030_112145_pos_000792_sale.xml', 'GDM', '2021-10-30 13:30:07', '', '', 'POSWEB', '01', 'POSWEB', '01', '', '{\"aliquote_d\": {}, \"totali_vendita\": {\"ven_abbuono\": 0.0, \"tot_costi_extra_detailed\": 0.0, \"lordo_tessuto\": 0.0, \"vendita_sconto\": 0.0, \"tot_shopping_bags\": 0.0, \"tot_sartoria\": 0.0, \"ven_coupon\": 0.0, \"ven_costi_extra\": 0.0, \"tot_netto\": 0.0, \"tot_lordo\": 0.0, \"lordo_capi\": 0.0, \"tot_sconti_abbuoni\": 0.0, \"tot_gift_card\": 0.0, \"tot_rettifiche_maggiorazioni\": 0.0}}', '2021-10-30 11:20:57', 'NEGOZIO', '');

INSERT INTO `pos_movimentazioni_custom_multi` (`id`, `cod_negozio`, `anno_transazione`, `id_transazione`, `tipo`, `progressivo`, `categoria`, `nome`, `valore`, `modificato`)
VALUES
	(437266, '4401019', '2021', 3583489, 'CAPI', 1, 'PROMO_ENGINE', 'effect_token', '1-V1-2020-MM-000002A', '2021-10-30 13:30:07'),
	(437267, '4401019', '2021', 3583489, 'CAPI', 1, 'PROMO_ENGINE', 'effect', '36', '2021-10-30 13:30:07'),
	(437268, '4401019', '2021', 3583489, 'TESTATA', NULL, 'PROMO_ENGINE', 'effect_token', '1-V1-2020-MM-000002A', '2021-10-30 13:30:07'),
	(437269, '4401019', '2021', 3583489, 'TESTATA', NULL, 'PROMO_ENGINE', 'effect', '36', '2021-10-30 13:30:07');

INSERT INTO `pos_movimenti_contabilita` (`anno_transazione`, `id_transazione`, `progressivo`, `cod_negozio`, `tipo_applicazione`, `codice_proprietario`, `id_postazione`, `codice_stato`, `progressivo_capo`, `codice_movimento`, `cod_operazione`, `dati_operazione`, `importo_iniziale`, `importo_finale`, `divisa`, `importo_divisa_pagamento`, `divisa_pagamento`, `nota`, `barcode`, `reso`, `data_creazione`, `data_modifica`, `file_name`, `upd_datetime`)
VALUES
	('2021', 3583489, 1, '4401019', 'POSWEB', 'GDM', '01', 'CLOSED', 0, 'CONTABILITA_PAGAMENTO', 'WEPAY', '{\"payment_date\": \"20211030\", \"payment_time\": \"132131\"}', 27090.00, 27090.00, 'CNY', NULL, NULL, '', '', 0, '2021-10-30 11:21:31', '2021-10-30 11:20:57', '4401019_20211030_112145_pos_000792_sale.xml', '2021-10-30 13:30:07');
