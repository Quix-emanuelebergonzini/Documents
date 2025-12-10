SOLITAMENTE DA FARE DOPO LE NOSTRE ORE 13

1) andare su db CRM PROD e ricreare la tabella __imp_fid
DROP TABLE __imp_fid;

CREATE TABLE `__imp_fid` (
  `cliente_finale` varchar(16) NOT NULL,
  `importo_corrente` decimal(13,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`cliente_finale`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

2) Si inseriscono tutti i pk e importi presi dall'excel
https://regexr.com
/(\w+)\s(\w+)/gm

MMJ_34956 6400 ---> deve esserci solo uno spazio tra pk_consumer e points
MMJ_35124 2850
MMJ_33565 6050
MMJ_5634 11200
...

tools: Replace
("$1","$2"),

INSERT INTO `__imp_fid`
VALUES
("MMJ_34956", 6400), ("MMJ_35124", 2850), ....

3) Eseguire questa query per trovare tutte le consumatrici che hanno un importo uguale a quello indicato.
Deve esserci corrispondenza (al 96%) di numero, tra quelli su db  e quelli del file xls

-- SHOW VARIABLES LIKE '%group_concat%';
-- SET SESSION group_concat_max_len = 10000000;
-- SELECT GROUP_CONCAT(concat("'", temp.pk_consumer, "'") ORDER BY temp.pk_consumer ASC SEPARATOR ',') from (
SELECT pk_consumer, i.importo_corrente AS imp_corrente, f.importo_corrente AS cons_fid_imp_corrente
FROM  __imp_fid i
INNER JOIN consumer_cliente_finale USING(cliente_finale)
INNER JOIN consumer_fidelity f USING(pk_consumer)
WHERE attivo=1 AND f.tipo="LOYALTY_CARD_JP"
HAVING i.importo_corrente=f.importo_corrente
-- ) AS temp;

4) Prendere il pk_consumer di tutte quelle che escono dalla query sopra (togliere i commenti alla query sopra)

5) Collegarsi in ssh su CRM prod

6) vi bin/fidelity/source.py e andare alla funzione /get_fidelity_non_utilizzate

7) prima del return inserire questa query
query = """select tipo, codice, timestamp_modifica as last_op_date from consumer_fidelity where tipo="LOYALTY_CARD_JP" and pk_consumer in ('11925519','11925952', .... );"""

8) esci salvando il file

8b) stm_hg

9) esegui:
/home/crm/virtualenv/bin/python ~/httpd-chroot/bin/runalone.py ~/httpd-chroot/bin/scripts/pos_promozioni.py -a process -j empty_unused -t LOYALTY_CARD_JP >> ~/httpd-chroot/log/pos_promozioni.log_`date +\%Y\%m` 2>&1

(copia/incolla tutta la stringa sopra)

10) torni dentro al source ed elimini la query aggiunta, salvi ed esci

10b) stm_hg

11) Se ci sono incongruenze parlarne con MARCO:
select pk_consumer, i.importo_corrente, f.importo_corrente, f.codice
from __imp_fid i
inner join consumer_cliente_finale using(cliente_finale)
inner join consumer_fidelity f using(pk_consumer)
where attivo=1 and f.tipo="LOYALTY_CARD_JP"
having i.importo_corrente<>f.importo_corrente;

se questa query ritorna 0 punti su f.importo_corrente siamo a posto
Se ci sono incongruenze parlarne con MARCO
