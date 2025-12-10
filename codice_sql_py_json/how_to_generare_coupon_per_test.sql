vedi https://maxmarafashiongroup.atlassian.net/browse/AMSB2C-60530
commento di Giulia

>>> "hai scoperto come si configura Posweb per accettare una serie di coupon che hanno quel "prefisso""
>>> "ma i coupon stanno su Hybris, cosa per la quale dipendiamo da digital"


SET @token := 'AMSB2C60530';
SET @descr := 'test LOY MC 24'; -- <nome campagna>
SET @inizio := '20240201';
SET @fine := '20240630';


-- cosi la promo vale sempre
INSERT INTO `pos_promozioni` (`nome`, `descrizione`, `giorni_validita`, `regole_promo`, `attivo`, `tipologia`, `modificato`)
VALUES
    (@token, @descr, '1234567','{\n \"effect\": {\n \"item_condition\": [\n \"VAL\", \n true\n ]\n }\n}', 1, 'COUPON', now());

-- prendere l'id asegnato autoincrement
SELECT @id_coup := id FROM pos_promozioni WHERE nome= @token;


-- decommentare l'insert dopo una prova
-- INSERT INTO `pos_promozioni_negozi` (`id_promo`, `cod_negozio`, `giorni_validita`, `data_inizio`, `data_fine`, `attivo`, `modificato`)
SELECT @id_coup, b.valore, '1234567', @inizio, @fine, 1, now()
FROM pos_config_bundle b
LEFT JOIN pos_config_store cs ON (b.valore=cs.negozio)
LEFT JOIN pos_config_cash cc ON (b.valore=cc.negozio)
LEFT JOIN pos_config_store cs2 ON (cs2.negozio=b.valore AND cs2.chiave='UNINSTALL_DATE')
LEFT JOIN ana_soggetti_master asm ON (b.valore=asm.codice_gruppo)
WHERE cs.chiave='STORE_CLOSING_TIME'
AND cs2.valore=''
AND LEFT(asm.catena_retail,2) IN ('MC') -- inserire i brand coinvolti
GROUP BY b.valore
;

-- verifica
SELECT * FROM pos_promozioni_negozi WHERE id_promo= @id_coup;

-- inviare un incr