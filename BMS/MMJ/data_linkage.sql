SELECT *
FROM pos_movimenti_contabilita
WHERE anno_transazione = '2022'
  AND cod_negozio IN (SELECT valore FROM pos_config_bundle WHERE tipologia_istanza = 'POSWEB_OFFLINE');


SELECT *
FROM pos_chiusura
WHERE cod_negozio IN (SELECT valore FROM pos_config_bundle WHERE tipologia_istanza = 'POSWEB_OFFLINE');

SELECT *
FROM pos_consumer
         JOIN pos_consumer_negozio USING (pk_consumer)
WHERE negozio IN (SELECT valore FROM pos_config_bundle WHERE tipologia_istanza = 'POSWEB_OFFLINE');

-- chiusure --
SELECT 0                                                                                                                                              AS 'seq_no',
       0                                                                                                                                              AS 'vdate_create',
       0                                                                                                                                              AS 'vdate_update',
       IFNULL(ast.codice, '')                                                                                                                         AS 'shop',
       pc.data_chiusura                                                                                                                               AS 'invoice_date',
       SUM(CASE WHEN IFNULL(consumatrici.qty, 0) = 0 THEN 0 WHEN IFNULL(consumatrici.qty, 0) < 0 THEN -1 ELSE 1 END)                                  AS 'quantity01',
       SUBSTRING_INDEX(substr(pc.dati, locate('\"', pc.dati, locate('\"customer_traffic\"', pc.dati) + length('\"customer_traffic\"')) + 1), '\"', 1) AS 'quantity02',
       0                                                                                                                                              AS 'quantity03',
       0                                                                                                                                              AS 'quantity04',
       0                                                                                                                                              AS 'quantity05',
       0                                                                                                                                              AS 'quantity06',
       0                                                                                                                                              AS 'quantity07',
       0                                                                                                                                              AS 'quantity08',
       0                                                                                                                                              AS 'quantity09',
       0                                                                                                                                              AS 'quantity10',
       0                                                                                                                                              AS 'quantity11',
       0                                                                                                                                              AS 'quantity12',
       0                                                                                                                                              AS 'quantity13',
       0                                                                                                                                              AS 'quantity14',
       0                                                                                                                                              AS 'quantity15',
       0                                                                                                                                              AS 'quantity16',
       0                                                                                                                                              AS 'quantity17',
       0                                                                                                                                              AS 'quantity18',
       0                                                                                                                                              AS 'quantity19',
       0                                                                                                                                              AS 'quantity20',
       0                                                                                                                                              AS 'quantity21',
       0                                                                                                                                              AS 'quantity22',
       0                                                                                                                                              AS 'quantity23',
       0                                                                                                                                              AS 'quantity24',
       0                                                                                                                                              AS 'quantity25',
       0                                                                                                                                              AS 'quantity26',
       0                                                                                                                                              AS 'quantity27',
       0                                                                                                                                              AS 'quantity28',
       0                                                                                                                                              AS 'quantity29',
       0                                                                                                                                              AS 'quantity30',
       IFNULL(contabilita.price01, 0)                                                                                                                 AS 'price01',
       IFNULL(contabilita.price02, 0)                                                                                                                 AS 'price02',
       0                                                                                                                                              AS 'price03',
       IFNULL(contabilita.price04, 0)                                                                                                                 AS 'price04',
       0                                                                                                                                              AS 'price05',
       0                                                                                                                                              AS 'price06',
       IFNULL(contabilita.price07, 0)                                                                                                                 AS 'price07',
       0                                                                                                                                              AS 'price08',
       0                                                                                                                                              AS 'price09',
       0                                                                                                                                              AS 'price10',
       0                                                                                                                                              AS 'price11',
       0                                                                                                                                              AS 'price12',
       SUBSTRING_INDEX(substr(pc.dati, locate('\"', pc.dati, locate('\"store_balance\"', pc.dati) + length('\"store_balance\"')) + 1), '\"', 1)       AS 'price13',
       0                                                                                                                                              AS 'price14',
       0                                                                                                                                              AS 'price15',
       0                                                                                                                                              AS 'price16',
       0                                                                                                                                              AS 'price17',
       0                                                                                                                                              AS 'price18',
       0                                                                                                                                              AS 'price19',
       0                                                                                                                                              AS 'price20',
       0                                                                                                                                              AS 'price21',
       0                                                                                                                                              AS 'price22',
       0                                                                                                                                              AS 'price23',
       0                                                                                                                                              AS 'price24',
       0                                                                                                                                              AS 'price25',
       IFNULL(contabilita.price26 * -1, 0)                                                                                                            AS 'price26',
       0                                                                                                                                              AS 'price27',
       0                                                                                                                                              AS 'price28',
       0                                                                                                                                              AS 'price29',
       0                                                                                                                                              AS 'price30',
       0                                                                                                                                              AS 'price31',
       0                                                                                                                                              AS 'price32',
       0                                                                                                                                              AS 'sysflg',
       '0'                                                                                                                                            AS 'register_noa'
FROM pos_chiusura pc
         LEFT JOIN ana_soggetti_master am ON (pc.cod_negozio = am.codice_gruppo AND am.tipo_soggetto = 'Negozio')
         LEFT JOIN ana_soggetti_transcodifiche ast ON (ast.id_soggetto = am.id_soggetto AND ast.data_fine IS NULL AND ast.sistema = 'MMJ')
         LEFT JOIN (SELECT IFNULL(sum(IF(pmc.codice_movimento = 'CONTABILITA_PAGAMENTO', pmc.importo_finale, 0)), 0)                                            AS 'price01',
                           IFNULL(sum(IF(pmc.codice_movimento = 'CONTABILITA_PAGAMENTO' AND pmc.cod_operazione = 'CONTANTI', pmc.importo_finale, 0)), 0)        AS 'price02',
                           IFNULL(sum(IF(pmc.codice_movimento = 'CONTABILITA_PAGAMENTO' AND pmc.cod_operazione = 'CARTA' AND SUBSTRING_INDEX(substr(pmc.dati_operazione,
                                                                                                                                                    locate('\"',
                                                                                                                                                           pmc.dati_operazione,
                                                                                                                                                           locate('\"card_utilization_type\"', pmc.dati_operazione) +
                                                                                                                                                           length('\"card_utilization_type\"')) +
                                                                                                                                                    1), '\"', 1) = 'CREDIT' OR
                                         (pmc.codice_movimento = 'CONTABILITA_PAGAMENTO' AND pmc.cod_operazione = 'ECOLLECT') OR
                                         (pmc.codice_movimento = 'CONTABILITA_PAGAMENTO' AND pmc.cod_operazione = 'GIFT_CARD_MMJ'), pmc.importo_finale, 0)), 0) AS 'price04',
                           IFNULL(sum(IF(pmc.codice_movimento = 'CONTABILITA_TASSA', FLOOR(pmc.importo_finale), 0)), 0)                                         AS 'price07',
                           IFNULL(sum(IF(pmc.codice_movimento = 'CONTABILITA_PROMOZIONE', pmc.importo_finale, 0)), 0)                                           AS 'price26',
                           pm.cod_negozio
                    FROM pos_movimentazioni pm
                             INNER JOIN pos_movimenti_contabilita pmc USING (cod_negozio, id_transazione, anno_transazione)
                    WHERE pm.data_documento = '20210524'
                      AND pm.anno_transazione = '2021'
                    GROUP BY pm.cod_negozio) AS contabilita ON (contabilita.cod_negozio = pc.cod_negozio)
         LEFT JOIN (SELECT SUM(IF(pm.codice_movimento = 'SCARICO_OMAGGIO', 0, IF(pm.codice_movimento = 'STORNO', -1, 1))) AS qty, pm.cod_negozio
                    FROM pos_movimentazioni pm
                             INNER JOIN pos_consumer pc USING (pk_consumer)
                    WHERE pc.grado_anonimato NOT IN (40, 50)
                      AND pm.data_documento = '20210524'
                      AND pm.anno_transazione = '2021'
                    GROUP BY pm.cod_negozio, pm.pk_consumer
                    UNION ALL
                    SELECT SUM(IF(pm.codice_movimento = 'SCARICO_OMAGGIO', 0, IF(pm.codice_movimento = 'STORNO', -1, 1))) AS qty, pm.cod_negozio
                    FROM pos_movimentazioni pm
                             INNER JOIN pos_consumer pc USING (pk_consumer)
                    WHERE pc.grado_anonimato IN (40, 50)
                      AND pm.data_documento = '20210524'
                      AND pm.anno_transazione = '2021'
                    GROUP BY pm.cod_negozio) AS consumatrici ON (consumatrici.cod_negozio = pc.cod_negozio)
WHERE pc.tipo_totale = 'ALGEBRAIC'
  AND pc.data_chiusura = '20210524'
GROUP BY pc.cod_negozio, pc.data_chiusura, pc.ora_chiusura
ORDER BY pc.data_chiusura, pc.ora_chiusura DESC;

-- consumer --
SELECT cn.negozio,
       pc.timestamp_modifica,
       pcs.valore                                                                                                                                              AS 'insegna',
       pc.pk_consumer,
       ''                                                                                                                                                      AS 'customer_CD',
       IFNULL(CONCAT(IF(pcnb.pk_consumer IS NULL, pc.cognome, pcnb.cognome), ' ', IF(pcnb.pk_consumer IS NULL, pc.nome, pcnb.nome)), '')                       AS 'customer_name',
       IFNULL(CONCAT(pcna.cognome, ' ', pcna.nome), '')                                                                                                        AS 'customer_kana',
       IFNULL(IF(pc.cap IS NOT NULL AND pc.cap != '', pc.cap, pcia.cap), '')                                                                                   AS 'zip_code',
       IFNULL(concat(IF(pcia.pk_consumer IS NULL, pc.provincia, pcia.provincia), ' ', IF(pcia.pk_consumer IS NULL, pc.localita, pcia.localita)), '')           AS 'address_1',
       IFNULL(concat(IF(pcia.pk_consumer IS NULL, pc.indirizzo, pcia.indirizzo), ' ', IF(pcia.pk_consumer IS NULL, pc.numero_civico, pcia.numero_civico)), '') AS 'address_2',
       IFNULL(concat(IF(pcia.pk_consumer IS NULL, pc.edificio, pcia.edificio), ' ', IF(pcia.pk_consumer IS NULL, pc.note_indirizzo, pcia.note_indirizzo)), '') AS 'address_3',
       IFNULL(pc.telefono1, '')                                                                                                                                AS 'phone_1',
       IFNULL(pc.cellulare1, '')                                                                                                                               AS 'phone_2',
       pc.email                                                                                                                                                AS 'email',
       '.'                                                                                                                                                     AS 'customer_ranking',
       ''                                                                                                                                                      AS 'customer_loyalty_ranking',
       IFNULL(ast.codice, '')                                                                                                                                  AS 'shop_CD',
       IF(pc.anno_nascita IS NOT NULL AND pc.anno_nascita != '', concat(pc.anno_nascita, pc.mese_nascita, pc.giorno_nascita), '')                              AS 'birthday',
       CASE WHEN IFNULL(pc.sesso, '') = 'F' THEN '1' WHEN IFNULL(pc.sesso, '') = 'M' THEN '2' ELSE '0' END                                                     AS 'sex',
       IFNULL(aspp.matricola, '')                                                                                                                              AS 'sales_person_CD',
       0                                                                                                                                                       AS 'cumulative_visits',
       0                                                                                                                                                       AS 'cumulative_quantity_of_purchases',
       0                                                                                                                                                       AS 'cumulative_amount_of_purchase',
       '8'                                                                                                                                                     AS 'customer_category',
       IF(pc.anno_nascita IS NOT NULL OR pc.anno_nascita_presunto IS NOT NULL, cast(YEAR(curdate()) AS SIGNED) - cast(IFNULL(pc.anno_nascita, pc.anno_nascita_presunto) AS SIGNED),
          '.')                                                                                                                                                 AS 'name_CD01',
       '.'                                                                                                                                                     AS 'name_CD02',
       '.'                                                                                                                                                     AS 'name_CD03',
       '.'                                                                                                                                                     AS 'name_CD04',
       '.'                                                                                                                                                     AS 'name_CD05',
       IFNULL(pc.wechat, '.')                                                                                                                                  AS 'name_CD06',
       '.'                                                                                                                                                     AS 'name_CD07',
       '.'                                                                                                                                                     AS 'name_CD08',
       '.'                                                                                                                                                     AS 'name_CD09',
       '.'                                                                                                                                                     AS 'name_CD10',
       IFNULL(REPLACE(REPLACE(pc.note, ' ', ''), ' ', ' '), '.')                                                                                               AS 'remarks',
       REPLACE(pc.data_prima_registrazione, '-', '')                                                                                                           AS 'membership_creation_date',
       '19010101'                                                                                                                                              AS 'last_visit_date',
       '19010101'                                                                                                                                              AS 'last_updated_date',
       '.'                                                                                                                                                     AS 'old_customer_CD1',
       '.'                                                                                                                                                     AS 'parental_customer_CD',
       IFNULL(REPLACE(REPLACE(pc.note, ' ', ''), ' ', ' '), '.')                                                                                               AS 'DM_remarks',
       REPLACE(pc.data_prima_registrazione, '-', '')                                                                                                           AS 'enrollment_date'
FROM pos_consumer pc
         JOIN pos_consumer_negozio cn ON (cn.pk_consumer = pc.pk_consumer AND cn.timestamp_fine IS NULL)
         JOIN pos_config_store pcs ON (pcs.negozio = cn.negozio AND pcs.chiave = 'STORE_SIGN')
         LEFT JOIN ana_soggetti_master asm ON (cn.utente_modifica = asm.codice_gruppo AND asm.tipo_soggetto = 'Dipendente')
         LEFT JOIN ana_soggetti_master asmn ON (cn.negozio = asmn.codice_gruppo AND asmn.tipo_soggetto = 'Negozio')
         LEFT JOIN ana_soggetti_transcodifiche ast ON (ast.id_soggetto = asmn.id_soggetto AND ast.data_fine IS NULL AND ast.sistema = 'MMJ')
         LEFT JOIN ana_soggetti_profilo_professionale aspp ON (asm.id_soggetto = aspp.id_soggetto AND aspp.data_fine IS NULL)
         LEFT JOIN pos_consumer_nome_alfabeto pcna ON (pc.pk_consumer = pcna.pk_consumer AND pcna.alfabeto = 'KANA')
         LEFT JOIN pos_consumer_nome_alfabeto pcnb ON (pc.pk_consumer = pcnb.pk_consumer AND pcnb.alfabeto = 'KANJI')
         LEFT JOIN pos_consumer_indirizzo_alfabeto pcia ON (pc.pk_consumer = pcia.pk_consumer AND pcia.alfabeto = 'JAPA')
WHERE cn.negozio IN (SELECT valore FROM pos_config_bundle WHERE tipologia_istanza = 'POSWEB_OFFLINE')
ORDER BY cn.timestamp_modifica;


-- new in crm --
SELECT pc.pk_consumer,
       cn.negozio,
       IFNULL((SELECT clm.user FROM consumer_log_modifiche clm WHERE clm.pk_consumer = pc.pk_consumer AND clm.user LIKE concat('pos::%') ORDER BY id DESC LIMIT 1),
              "")                                                                                                                        AS 'utente_modifica',
       ''                                                                                                                                as 'customer_CD',
       IFNULL(CONCAT(IF(pcnb.pk_consumer IS NULL, pc.cognome, pcnb.cognome), ' ', IF(pcnb.pk_consumer IS NULL, pc.nome, pcnb.nome)), '') AS 'customer_name',
       IFNULL(CONCAT(pcna.cognome, ' ', pcna.nome), '')                                                                                  AS 'customer_kana',
       IFNULL(IF(pc.cap is not null and pc.cap != '', pc.cap, pcia.cap), '')                                                             AS 'zip_code',
       IFNULL(concat(pcia.provincia, ' ', pcia.localita), '')                                                                            AS 'address_1',
       IFNULL(concat(pcia.indirizzo, ' ', pcia.numero_civico), '')                                                                       AS 'address_2',
       IFNULL(concat(pcia.edificio, ' ', pcia.note_indirizzo), '')                                                                       AS 'address_3',
       IFNULL(pc.telefono1, '')                                                                                                          AS 'phone_1',
       IFNULL(pc.cellulare1, '')                                                                                                         AS 'phone_2',
       pc.email                                                                                                                          AS 'email',
       '.'                                                                                                                               AS 'customer_ranking',
       ''                                                                                                                                AS 'customer_loyalty_ranking',
       IF(pc.anno_nascita is not null and pc.anno_nascita != '', concat(pc.anno_nascita, pc.mese_nascita, pc.giorno_nascita), '')        AS 'birthday',
       CASE WHEN IFNULL(pc.sesso, '') = 'F' THEN '1' WHEN IFNULL(pc.sesso, '') = 'M' THEN '2' ELSE '0' END                               AS 'sex',
       0                                                                                                                                 AS 'cumulative_visits',
       0                                                                                                                                 AS 'cumulative_quantity_of_purchases',
       0                                                                                                                                 AS 'cumulative_amount_of_purchase',
       '8'                                                                                                                               AS 'customer_category',
       IF(pc.anno_nascita is not null or pc.anno_nascita_presunto is not null, cast(YEAR(curdate()) as signed) - cast(IFNULL(pc.anno_nascita, pc.anno_nascita_presunto) as signed),
          '.')                                                                                                                           AS 'name_CD01',
       '.'                                                                                                                               AS 'name_CD02',
       '.'                                                                                                                               AS 'name_CD03',
       '.'                                                                                                                               AS 'name_CD04',
       '.'                                                                                                                               AS 'name_CD05',
       IFNULL(cc.valore, '.')                                                                                                            AS 'name_CD06',
       '.'                                                                                                                               AS 'name_CD07',
       '.'                                                                                                                               AS 'name_CD08',
       '.'                                                                                                                               AS 'name_CD09',
       '.'                                                                                                                               AS 'name_CD10',
       IFNULL(REPLACE(REPLACE(pc.note, ' ', ''), ' ', ' '), '.')                                                                         AS 'remarks',
       REPLACE(pc.data_prima_registrazione, '-', '')                                                                                     AS 'membership_creation_date',
       '19010101'                                                                                                                        AS 'last_visit_date',
       '19010101'                                                                                                                        AS 'last_updated_date',
       '.'                                                                                                                               AS 'old_customer_CD1',
       '.'                                                                                                                               AS 'parental_customer_CD',
       IFNULL(REPLACE(REPLACE(pc.note, ' ', ''), ' ', ' '), '.')                                                                         AS 'DM_remarks',
       REPLACE(pc.data_prima_registrazione, '-', '')                                                                                     AS 'enrollment_date'
FROM consumer pc
         JOIN consumer_negozio cn ON (cn.pk_consumer = pc.pk_consumer and cn.timestamp_fine is null)
         LEFT JOIN consumer_nome_alfabeto pcna ON (pc.pk_consumer = pcna.pk_consumer AND pcna.alfabeto = 'KANA')
         LEFT JOIN consumer_nome_alfabeto pcnb ON (pc.pk_consumer = pcnb.pk_consumer AND pcnb.alfabeto = 'KANJI')
         LEFT JOIN consumer_indirizzo pcia ON (pc.pk_consumer = pcia.pk_consumer and pcia.alfabeto in ('LATIN', 'JAPA') and pcia.tipo_indirizzo = 'Residence' and pcia.main = 1)
         LEFT JOIN consumer_contatto cc ON (cc.pk_consumer = pc.pk_consumer AND tipo_contatto = 'wechat')
WHERE pc.timestamp_modifica between '2020-03-02 00:00:00' and '2020-03-02 23:59:59'
  AND cn.negozio IN
      ('0801003', '0801009', '0801011', '0801013', '0801016', '0801017', '0801018', '0801020', '0801026', '0801032', '0801033', '0801036', '0801037', '0801038', '0801039',
       '0801040', '0801042', '0801045', '0801048', '0801049', '0801053', '0801054', '0801055', '0801058', '0801060', '0801061', '0801062', '0801067', '0801067', '0801072',
       '0801074', '0801076', '0801085', '0801086', '0801092', '0801096', '0801097', '0801099', '0801105', '0801107', '0801116', '0801118', '0801126', '0801130', '0801138',
       '0801139', '0801141', '0801144', '0801154', '0801159', '0801181', '0801206', '0801213', '0801217', '0801234', '0801235', '0801237', '0801243', '0801279', '0801286',
       '0801288', '0801289', '0801298', '0801331', '0801334', '0801335', '0801343', '0801344', '0801355', '0801356', '0801366', '0801367', '0801370', '0801371', '0801378',
       '0801381', '0801385', '0801398', '0801400', '0801403', '0801411', '0801415', '0801418', '0801424', '0801429', '0801433', '0801441', '0801442', '0801443', '0801448',
       '0801449', '0801471', '0801482', '0801483', '0801517', '0801534', '0801536', '0801537', '0801544', '0801545', '0801546', '0801551', '0801555', '0801557', '0801558',
       '0801559', '0801564', '0801565', '0801567', '0801568', '0801572', '0801574', '0801575', '0801577', '0801582', '0801585', '0801586', '0801958', '0801991', '0801992',
       '0801993')
ORDER BY cn.timestamp_modifica