https://jira.mmfg.it/browse/REX-458
in questo caso ci si collega su ambiente di produzione
e si fanno le seguenti ipotesi

select *
from pos_import_spool
where file_name = '2401563_20210118_153559_pos_106457_sale.xml';

ricerco per file_name prima con like e mi accorgo se esiste uno solo xml
o più xml associati

ricerco per esatte informazioni descritte nell'xml e mi accorgo se c'è
qualche anomalia (controllare veridicità dei dati)

select file_name
from pos_movimentazioni
where id_transazione = '102777' and anno_transazione = '2021' and cod_negozio = '2401563' and numero_documento = '252';

in sostanza si può notare

a) file_name uguali cioè esiste già la movimentazione associata all'xml
xml è FAILED ma in realtà esistendo la movimentazione è già stata correttamente
importata ma per qualche ragione strana il cloud non aggiorna il dato e viene
riconsiderata. mettere in stato IMPORTED e dire che non ci sono problemi

b) i file_name sono diversi quindi comapare tra i due xml
può capitare che gli xml sono UGUALI (in tutto e per tutto) e in questo caso
mettere IGNORED
c ) se sono diversi gli xml (ma uguale file_name) ovviamente indagare perché hanno la terna
negozio-anno-id_transazione uguale i due xml con stesso file_name
