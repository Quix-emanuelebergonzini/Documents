aprire il db di un negozio online di test

!!! USARE ./bin/sqlite3 PERCHE ALTRIMENTI CE IL RISCHIO DI ROMPERE IL DB !!!


>> cd /rnd/pos/mmfg/posweb/
>> ./bin/sqlite3 ./var/database/catalogo.db
>> .mode column
>> .quit (uscire)

PRENDO IL FILE SU DRIVE Postazioni TEST POSWEB, colonna H e trovo IP
sulle colonne di destra ci sono per i vari brand i negozi
configurati e quello con descrizione ha in "test" qualche funzionalità

########################################################################################

SQLITE (https://www.sqlite.org/cli.html)

>>> .help
>>> ./bin/sqlite3 var/database/catalogo.db
>>> sqlite3// .mode list
>>> sqlite3// .mode column (in alternative)
>>> sqlite3// .mode line (in alternative)

>>> .mode insert new_table
>>> select * from catalog limit 5;
sputa fuori un output in formato INSERT delle prime 5 righe (ma ho eseguito una SELECT)

>>> .schema catalogo
sputa fuori un output con la CREATE TABLE e gli INDEX

>>> .headers ON
abilita visualizzazione dei nomi colonna in testata

################################################################################
########                      comandi da utilizzare                     ########
################################################################################
>>> .shema columns list
>>> .headers ON
su query con poche colonne va bene

################################################################################

.quit                  Exit this program
.databases             List names and files of attached databases
.changes on|off        Show number of rows changed by SQL
.schema ?TABLE?        Show the CREATE statements
                         If TABLE specified, only show tables matching
                         LIKE pattern TABLE.
================================================================================
.clone NEWDB           Clone data into NEWDB from the existing database
.backup ?DB? FILE      Backup DB (default "main") to FILE
.dbinfo ?DB?           Show status information about the database
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
.echo on|off           Turn command echo on or off
.eqp on|off            Enable or disable automatic EXPLAIN QUERY PLAN
.explain ?on|off|auto? Turn EXPLAIN output mode on or off or to automatic
.fullschema            Show schema and the content of sqlite_stat tables
.headers on|off        Turn display of headers on or off
.import FILE TABLE     Import data from FILE into TABLE
.indexes ?TABLE?       Show names of all indexes
                         If TABLE specified, only show indexes for tables
                         matching LIKE pattern TABLE.
.limit ?LIMIT? ?VAL?   Display or change the value of an SQLITE_LIMIT
.load FILE ?ENTRY?     Load an extension library
.log FILE|off          Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         ascii    Columns/rows delimited by 0x1F and 0x1E
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator strings
                         tabs     Tab-separated values
                         tcl      TCL list elements
.nullvalue STRING      Use STRING in place of NULL values
.once FILENAME         Output for the next SQL command only to FILENAME
.open ?FILENAME?       Close existing database and reopen FILENAME
.output ?FILENAME?     Send output to FILENAME or stdout
.print STRING...       Print literal STRING
.prompt MAIN CONTINUE  Replace the standard prompts

.read FILENAME         Execute SQL in FILENAME
.restore ?DB? FILE     Restore content of DB (default "main") from FILE
.save FILE             Write in-memory database into FILE
.scanstats on|off      Turn sqlite3_stmt_scanstatus() metrics on or off
.separator COL ?ROW?   Change the column separator and optionally the row
                         separator for both the output mode and .import
.shell CMD ARGS...     Run CMD ARGS... in a system shell
.show                  Show the current values for various settings
.stats ?on|off?        Show stats or turn stats on or off
.system CMD ARGS...    Run CMD ARGS... in a system shell
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         LIKE pattern TABLE.
.timeout MS            Try opening locked tables for MS milliseconds
.timer on|off          Turn SQL timer on or off
.trace FILE|off        Output each SQL statement as it is run
.vfsinfo ?AUX?         Information about the top-level VFS
.width NUM1 NUM2 ...   Set column widths for "column" mode
                         Negative values right-justify
