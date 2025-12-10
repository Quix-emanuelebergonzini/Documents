/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

brew install mysql-client
brew install mysql
brew install mysql-client

1) dvo'è il mio interprete python per posweb?
cat /Library/LaunchDaemons/it.mmfg.pos.plist

	<array>
----------> <string>/Users/emanuelebergonzini/projects/repos/posweb/interpreters/python/bin/python</string> <---------------
		<string>/Users/emanuelebergonzini/projects/repos/posweb/mmfg/posweb/daemons/daemon_controller.py</string>
	</array>

2) /Users/emanuelebergonzini/projects/repos/posweb/interpreters/python/bin/python -m pip list

3) /Users/emanuelebergonzini/projects/repos/posweb/interpreters/python/bin/python -m pip install mysqlclient==1.3.10
    in caso di errore uninstall e install nuovamente

4) /Users/emanuelebergonzini/projects/repos/posweb/interpreters/python/bin/python
    * 3b) import _mysql

se tutto ok bene

poi su posweb ho aggiunto

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 12345
MYSQL_USER = "poswebonline"
MYSQL_PASSWD = "jkg$repoj$ahng3"

ho messo

FEATURE_SET='ONLINE'

e

LISTA_COD_NEGOZIO = ''


vi /usr/local/etc/my.cnf

==> mysql
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To restart mysql after an upgrade:
  brew services restart mysql
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/mysql/bin/mysqld_safe --datadir=/usr/local/var/mysql
==> mysql-client
mysql-client is keg-only, which means it was not symlinked into /usr/local,
because it conflicts with mysql (which contains client libraries).

If you need to have mysql-client first in your PATH, run:
  echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.zshrc

For compilers to find mysql-client you may need to set:
  export LDFLAGS="-L/usr/local/opt/mysql-client/lib"
  export CPPFLAGS="-I/usr/local/opt/mysql-client/include"

For pkg-config to find mysql-client you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/mysql-client/lib/pkgconfig"
