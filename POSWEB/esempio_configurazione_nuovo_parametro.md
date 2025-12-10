Aggiungere parametro SHOW_TAX_ENABLED

SELECT @cod_pr := codice_proprietario FROM pos_config_store LIMIT 1;
SET @chiave = 'SHOW_TAX_ENABLED';
SET @val_default = '0';
REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_pr, @chiave, @val_default, 'I', 2, 'Abilitazione calcolo tasse', now());
SELECT concat(""INSERT IGNORE INTO pos_config_store values('"",@cod_pr,""','"",valore,""','"",@chiave,""','"",@val_default,""', '', now());"") FROM pos_config_bundle;

Abilitare tax enabled per ambienti con tasse
update pos_config_store_default set valore="1" where chiave="SHOW_TAX_ENABLED";
update pos_config_store set valore="1" where chiave="SHOW_TAX_ENABLED";

Spegnere il parametro SHOW_TAX_ENABLED per concession USA/CA
update pos_config_store set valore="0" where chiave="SHOW_TAX_ENABLED"
and negozio IN (select valore from pos_config_bundle where tipologia_istanza="POSWEB_ONLINE");


Incrementale
python ~/httpd-chroot/guest/posws/bin/poswsbe/pos_export_to_store_db.py incr -p10 all -f

Dare la versione software ai negozi
python ~/httpd-chroot/guest/posws/bin/poswsbe/pos_export_to_store_sw.py full -p10 all -f
