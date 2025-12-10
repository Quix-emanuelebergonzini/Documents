gunzip <nome_file_gz_da_scompattare>

vi <nome_file_sql_scompattato_dal_gz>

REPLACE ALL SU VI:

%s/Search-Word/Replace-Word/gc

gc - tutto il file
g - solo su quella riga

quindi può essere utile

%s/INSERT INTO/REPLACE INTO/gc

ottimo in caso di errori di duplicate keys  nei files sql di posweb

alla domanda premere a
