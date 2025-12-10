Aggiornare POSWSBE versione 1.XX
Aggiornare POSWSFE versione 1.XX
Aggiornare BOSS versione 1.XX

Aggiungere parametro XXX per tutti
SELECT @cod_pr := codice_proprietario FROM pos_config_store LIMIT 1;
SET @chiave = 'XXX';
SET @val_default = '0';
REPLACE INTO `pos_config_store_default` (`codice_proprietario`, `chiave`, `valore`, `tipo`, `sync`, `descrizione`, `modificato`)
VALUES (@cod_pr, @chiave, @val_default, 'I', 2, 'Attivazione buono gift a fronte reso', now());
SELECT concat(""INSERT IGNORE INTO pos_config_store values('"",@cod_pr,""','"",valore,""','"",@chiave,""','"",@val_default,""', '', now());"") FROM pos_config_bundle;

Aggiornamento parametro XXX per tutti i negozi sugli ambienti definiti
UPDATE pos_config_store_default set valore=""1"" where chiave=""SHOPPING_BAGS_NON_RISCOSSO"";
UPDATE pos_config_store set valore=""1"" where chiave=""SHOPPING_BAGS_NON_RISCOSSO"";

Aggiornamento parametro XXX per tutti i negozi di un determinato COUNTRY_CODE
UPDATE pos_config_store c
inner join pos_config_store c1 on c.negozio=c1.negozio and c1.chiave='COUNTRY_CODE' and c1.valore='COUNTRY_CODE_CUSTOM'
SET c.valore='1'
WHERE c.chiave='XXX';


esempio aggiunta crontab su CRM
20 */2 * * * /home/crm/virtualenv/bin/python ~/httpd-chroot/bin/scripts/anonimizzazione.py -a -t LINMARA_CB >> ~/httpd-chroot/log/check_anonimizzazione.log 2>&1
30 1 * * 1 /home/crm/virtualenv/bin/python ~/httpd-chroot/guest/posws/bin/poswsbe/pos_import_privacy.py -i
