UPDATE pos_config_store pcs
JOIN pos_config_store pcs2 USING(negozio)
SET pcs.valore = CASE pcs.chiave
                   WHEN 'CARD_ENABLED' THEN '1'
                   WHEN 'FIDELITY_MODE' THEN 'SYNC'
                   	  ELSE pcs.valore
                   END
WHERE pcs2.chiave = 'AVAILABLE_BRANDS' AND pcs2.valore = 'MC';
