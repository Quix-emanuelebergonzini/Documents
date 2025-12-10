"scompattare il backup python creato oggi

cd /Users/posweb/pos/mmfg/posweb/var/backups/20250722
tar -zxvf python.tar.gz

cd python

../../../../bin/configure.sh relax

mv ../../../../../../interpreters/python-3.9.1_intel ../../../../../../interpreters/python-3.9.1_intel_BAK
NB: se questo comando non va, controllare con  ls -lartf ../../../../../../interpreters 
(se manca la cartella del 3.9, passare al punto successivo)

cp -Rf python-3.9.1_intel ../../../../../../interpreters/.



# modifica versione python nel config/version.py mettendo nella PYTHON_INSTALLED_VERSION=""009372:3.12.8"" PYTHON_INSTALLED_VERSION=""009372:3.9.1""
vi ../../../../conf/version.py

../../../../bin/configure.sh



# far partire il manager
../../../../bin/manager.sh
#NB: se all'avvio dei demoni si vede solo una schermata nera, usare il comando ""a"" per l'autoconfig, poi ripartono da soli"