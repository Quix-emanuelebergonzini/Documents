# PASSAGGIO DEI DEMONI A PYTHON 3
	- spegnere i demoni (sudo launchctl unload /Library/LaunchDaemons/it.mmfg.pos.plist)
	- ./bin/configure.sh
	- ./bin/python (controllare che esegua una versione > 3.0)
	- accendere i demoni (sudo launchctl load /Library/LaunchDaemons/it.mmfg.pos.plist)
	- ./bin/configure.sh relax
	- provare a scaricare il db di un negozio

HTTP_VERSION_INSTALLED in version.py
005000:2.4.20.pf --> python2
005000:2.4.46.pf --> python3
