REVERT CODICE AL PACCHETTO ANTECEDENTE

# Andare nella cartella dell'ultimo backup
cd var/backups/20251024103502/
# Scompattarlo
tar -zxvf sw.tar.gz
# Andare nella root di Posweb
cd /rnd/pos/mmfg/posweb/
# Impostare i permessi in modo che sia possibile rinominare e cancellare i file
./bin/configure.sh relax
# Creo i backup della cartelle
mv bin _bin
mv daemons _daemons
mv site _site
# Rimetto le cartelle precedenti all'aggiornamento
mv var/backups/20251024103502/sw/bin bin
mv var/backups/20251024103502/sw/daemons daemons
mv var/backups/20251024103502/sw/site site
# resetto tutte le versioni a 5000 a parte il db che lo sbianco del tutto
# riavvio i demoni
./bin/manager.sh
