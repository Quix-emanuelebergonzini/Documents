export TERMINFO="/usr/share/terminfo"

export LANG="it_IT.UTF-8"
export LC_CTYPE="it_IT.UTF-8"
export LC_ALL="it_IT.UTF-8"

export PROJECTS=/Users/emanuele.bergonzini/repos
export SQLSCRIPTS=/Users/emanuele.bergonzini/Documents/Documents/scripts/sql
export SCRIPTS=/Users/emanuele.bergonzini/Documents/Documents/scripts

export NVM_DIR="$HOME/.nvm"
# This loads nvm
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
# This loads nvm bash_completion
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

export crm=$PROJECTS/backoffice
export maxima=$PROJECTS/maxima20
export maxima20=$PROJECTS/maxima20
export bmsmaxima=$PROJECTS/maxima20
export bmsmaxima20=$PROJECTS/maxima20
export bmsdt=$PROJECTS/possededt
export bmsma=$PROJECTS/possedema
export bmsmn=$PROJECTS/possedemn
export bmsdt=$PROJECTS/possededt
export bmsmr=$PROJECTS/possedemr
export bmsbenelux=$PROJECTS/benelux
export bmsau=$PROJECTS/bmsau
export bmsde=$PROJECTS/bmsde
export bmses=$PROJECTS/bmses
export bmsfr=$PROJECTS/bmsfr
export bmsfranchising=$PROJECTS/bmsfranchising
export bmsfrh=$PROJECTS/bmsfranchising
export bmshk=$PROJECTS/bmshk
export bmsjp=$PROJECTS/bmsjp
export bmsuk=$PROJECTS/bmsuk
export bmsusa=$PROJECTS/bmsusa
export bmscn=$PROJECTS/bmscn
export linmara=$PROJECTS/bmscn
export bmslinmara=$PROJECTS/bmscn
export bmscn=$PROJECTS/bmscn
export posweb=$PROJECTS/posweb/mmfg/posweb
export b2e=$PROJECTS/b2e-app-mobile
export poslite=$PROJECTS/poslite

alias pythonposweb=/Users/emanuele.bergonzini/repos/posweb/interpreters/python/bin/python
alias sid="python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/SID_POSTMAN.py"
alias change_store="python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/change_store/change_store.py"
alias check_produzione="python3.11 /Users/emanuele.bergonzini/Documents/Documents/scripts/check_produzione/check_produzione.py"
alias invoke_jobs="python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/invoke/invoke_jobs.py"
alias invoke_pods="python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/invoke/invoke_pods.py"
alias update_git="pythonposweb /Users/emanuele.bergonzini/Documents/Documents/scripts/cmd_git/git_operations.py"
alias gunzipfix="python3 /Users/emanuele.bergonzini/Documents/Documents/scripts/utility/replace_all_gzip.py"
alias docker_crm="pythonposweb /Users/emanuele.bergonzini/Documents/Documents/scripts/crm/docker/test_service.py"

alias sqliteposweb=/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/bin/sqlite3

alias import_from_store="LANDSCAPE=TESTING MEMORY=8000 docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_import_from_store.py"
alias testing="/Users/emanuele.bergonzini/Documents/Documents/scripts/printcredetial.sh & open -a docker &  LANDSCAPE=TESTING ./docker/compose_up.sh"
alias runtime="docker exec -it docker-runtime-1 bash"
alias incr_all_prod="LANDSCAPE=PRODUCTION MEMORY=8000 docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py incr -p10 all -f"
alias incr_all_test="LANDSCAPE=TESTING MEMORY=8000 docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py incr -p10 all -f"

alias clean_docker="docker image prune -a --filter "until=24h" -f"

alias weblog="tail -f $PROJECTS/posweb/mmfg/posweb/var/log/web/main.log"
alias mmfglog="tail -f $PROJECTS/posweb/mmfg/posweb/var/log/mmfg/main.log"
alias fullog="tail -f $PROJECTS/posweb/mmfg/posweb/var/log/web/main.log $PROJECTS/posweb/mmfg/posweb/var/log/mmfg/main.log"
alias querylog="tail -f $PROJECTS/posweb/mmfg/posweb/var/log/query/main.log"
alias httplog="tail -f $PROJECTS/posweb/mmfg/posweb/var/log/httpd/*"
alias cash_register="tail -f $PROJECTS/posweb/mmfg/posweb/var/log/cash_register/main.log"
alias poscloud="$SCRIPTS/mmfgcloud.sh poscloud"
alias mmfgcloud="$SCRIPTS/mmfgcloud.sh"
alias clearlog="$SCRIPTS/clean_posweb_logs.py"

alias daemons="/Users/emanuele.bergonzini/repos/posweb/interpreters/python/bin/python /Users/emanuelebergonzini/projects/repos/posweb/mmfg/posweb/daemons/daemon_controller.py"
alias cec="$PROJECTS/posweb/mmfg/posweb/bin/python $PROJECTS/posweb/mmfg/posweb/bin/CeC.py -u assistenza"
alias manager="$PROJECTS/posweb/mmfg/posweb/bin/manager.sh"
alias poswebpy="$PROJECTS/posweb/mmfg/posweb/bin/python $PROJECTS/posweb/mmfg/posweb/site/bin/console.py"

alias merge_mmj="python3 $SCRIPTS/merge_dati_mmj/script_merge_mmj/process.py"
alias unidb="python3 $SCRIPTS/utility/unidb.py"
alias translate="python3 $SCRIPTS/translator/translate.py"
alias querycustom="python3 $SCRIPTS/utility/query_custom.py"
alias catalogo_prezzi="pythonposweb $SCRIPTS/sql_posweb/catalogo_prezzi.py"
alias privacy="python3 $SCRIPTS/privacy.py"
alias svuota_posweb="pythonposweb $SCRIPTS/sql_posweb/svuota_posweb.py"