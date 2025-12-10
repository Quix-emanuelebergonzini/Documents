git show stash list
git checkout stash@{0} -- site/html/js/mmfg/rich/vendita/1.5/vendita.js
------------------------------------------------------------------------
git fetch origin master:master --> update master  without switching branch???
------------------------------------------------------------------------
git revert -m 1 <merge commit hash>
devo immetter un commit di merge che poi lui rollbackkerà
invocato da terminare apre una specie di file di test che poi bisognare fare :q
poi da sourcetree si committa il rollback

!!! se non ho pushato !!!
- spostarmi su altra branch
- eliminare la branch "errata"
- riscaricare la branch "(ex errata)"

!!!!! se mi accorgo dell'errore !!!!
- creare nuova branch dal commit antecedente del merge errato
- aggiornare foglio branches
- mandare mail segnalando il fatto
------------------------------------------------------------------------
git clone ....
cd benelux
git checkout release
git submodule init
git submodule update -f --recursive

vi docker/docker-compose.yml
sudo ./docker/compose_build.sh
------------------------------------------------------------------------

per forzare il download di un sottoresos corrotto....una operazione alla volta...

git clean -xfd
git submodule foreach --recursive git clean -xfd
git reset --hard
git submodule foreach --recursive git reset --hard
git submodule update --init --recursive