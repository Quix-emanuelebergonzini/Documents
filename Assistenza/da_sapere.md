https://maxmarafashiongroup.atlassian.net/browse/REX-26020 - problema abilitazioni portale per visione iframe su poslite

se iniziativa e problema portale → team fgres-tec
se NON iniziativa e problema portale → team fgres-operations

in ogni caso se il problema è la singola abilitazione,
in entrambi i casi (iniziativa o no) il primo passaggio deve essere fatto a FGCED,
cioè il 1 livello che risponde a Subiaco.


tutto cio che aprivate nel progetto FGNOC va aperto IOT
ICT da usare per problemi su bitbucket e mondo Atlassian



Se durante il download dei sottorepos vi si rompe qualcosa (o erroneamente chiudete sourcetree...) potete invocare questa procedura per risolvere il problema:
git clean -xfd
git submodule foreach --recursive git clean -xfd
git reset --hard
git submodule foreach --recursive git reset --hard
git submodule update --init --recursive
(istruzioni in sequenza attendendo la fine di ogni operazione)