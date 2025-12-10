echo "Elimino i logs main.log.* di Posweb (lascio solo il main.log corrente)"
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_downloader/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_installer/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_keepalive/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_peoplecnt/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_printer/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_scheduler/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_terminal/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/pos_uploader/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/manager/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/web/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/query/main.log.*
rm /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/log/mmfg/main.log.*

echo "Elimino i backups di Posweb"

ls -l /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/backups/ | grep "^d" | grep "[^\.]$" | awk '{print $9}' | sed -e '$ d' | sed -e '$ d' | while IFS= read -r line ; do rm -rf /Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/var/backups/$line; done

# docker image prune -f
#if [ $# -eq 0 ] && [ "$1" == "--full" ]
#then
#	docker image prune -a --filter "until=168h" -f
#fi