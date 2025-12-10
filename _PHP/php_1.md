==> php
To enable PHP in Apache add the following to httpd.conf and restart Apache:
    LoadModule php_module /usr/local/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Finally, check DirectoryIndex includes index.php
    DirectoryIndex index.php index.html

The php.ini and php-fpm.ini file can be found in:
    /usr/local/etc/php/8.1/

To restart php after an upgrade:
  brew services restart php
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/php/sbin/php-fpm --nodaemonize

I files di apache sono...
cd /etc/apache2

tail -f /var/log/apache2/access_log  /var/log/apache2/error_log

sudo apachectl -t ==> check

sudo apachectl -k start

wwww/...
cd /Library/WebServer/Documents


test di configurazione di apache
sudo apachectl configtest --> utile per non far partire il server e controllare che sia tutto ok


da testare:
https://www.simplified.guide/macos/apache-php-homebrew-codesign

su mac i moduli php vogliono un certificatore

seguire questa guida per creare l'autorità e il certificato
https://www.simplified.guide/macos/keychain-cert-code-signing-create

bisogna che il nome sia php (come scritto nel conf del httpd)

e poi fare come dice
https://developer.apple.com/forums/thread/694124

dove per certificare
codesign -s "php" --keychain ~/Library/Keychains/login.keychain-db /usr/local/opt/php@8.2/lib/httpd/modules/libphp.so

per controllare
codesign -dv --verbose=4 "/usr/local/opt/php@8.2/lib/httpd/modules/libphp.so"


... estratto httpd.conf .....
#PHP was deprecated in macOS 11 and removed from macOS 12
#LoadModule perl_module libexec/apache2/mod_perl.so
LoadModule hfs_apple_module libexec/apache2/mod_hfs_apple.so
LoadModule php_module /usr/local/opt/php@8.2/lib/httpd/modules/libphp.so "php"


esempio GO ok:
emanuelebergonzini@MacBook-Pro-4 apache2 % sudo apachectl -k start  
[Wed Apr 03 13:03:15.652560 2024] [so:notice] [pid 17241] AH06662: Allowing module loading process to continue for module at /usr/local/opt/php@8.2/lib/httpd/modules/libphp.so because module signature matches authority "php" specified in LoadModule directive
AH00557: httpd: apr_sockaddr_info_get() failed for MacBook-Pro-4.local
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1. Set the 'ServerName' directive globally to suppress this message
httpd (pid 14386) already running

dopo i pocci con mysql5 e brew
/usr/local/Cellar/mysql@8.4/8.4.2.reinstall/bin/mysqld ==> avvia il service

/usr/local/Cellar/mysql@8.4/8.4.2.reinstall/bin/mysql -u root ==> accedo alla console

cat /usr/local/etc/my.cnf
# Default Homebrew MySQL server config
[mysqld]
# Only allow connections from localhost
bind-address = 127.0.0.1

per killare il service mysqld
ps aux|grep mysql

/usr/local/Cellar/mysql@8.4/8.4.2.reinstall/bin/mysqladmin -u root status
Where command is a one or more of: (Commands may be shortened)
create databasename	Create a new database
debug			Instruct server to write debug information to log
drop databasename	Delete a database and all its tables
extended-status       Gives an extended status message from the server
flush-hosts           Flush all cached hosts
flush-logs            Flush all logs
flush-status		Clear status variables
flush-tables          Flush all tables
flush-privileges      Reload grant tables (same as reload)
kill id,id,...	Kill mysql threads
password [new-password] Change old password to new-password in current format
ping			Check if mysqld is alive
processlist		Show list of active threads in server
reload		Reload grant tables
refresh		Flush all tables and close and open logfiles
shutdown		Take server down
status		Gives a short status message from the server
start-replica		Start replication
start-slave		Deprecated: use start-replica instead
stop-replica		Stop replication
stop-slave		Deprecated: use stop-replica instead
variables             Prints variables available
version		Get version info from server