UPDATE_TYPE_LIST = db  # ,sw,config,python,httpd  # lista di aggiorn.ti abilitati separati da ,:db,sw,python,sqlite,httpd,microlog,firefox

#
#COD_INSTALLAZIONE = 
#LISTA_COD_NEGOZIO = 

# Per tutti i negozi:
#MMFG_WS_HOST = http://pos-ws-dev.mmfg.it/bin/driver_ws
#MMFG_WS_PROXY = 

# FIXME: ATTENZIONE! NELLO SWITCH DA PREMISE A CLOUD RICORDATI DI SVUOTARE LA GLOBAL_STATUS!!!
# FIXME: ATTENZIONE! NELLO SWITCH DA PREMISE A CLOUD RICORDATI DI SVUOTARE LA GLOBAL_STATUS!!!
# FIXME: ATTENZIONE! NELLO SWITCH DA PREMISE A CLOUD RICORDATI DI SVUOTARE LA GLOBAL_STATUS!!!
# FIXME: ATTENZIONE! NELLO SWITCH DA PREMISE A CLOUD RICORDATI DI SVUOTARE LA GLOBAL_STATUS!!!
# FIXME: ATTENZIONE! NELLO SWITCH DA PREMISE A CLOUD RICORDATI DI SVUOTARE LA GLOBAL_STATUS!!!

# per i negozi FRH:
# MMFG_WS_HOST = https://pos-ws-franchising-dev.bms.maxmara.com/bin/driver_ws
# MMFG_WS_PROXY = http://proxys.mmfg.it:8080

# per i negozi MMAU:
# MMFG_WS_HOST = https://pos-ws-au-dev.bms.maxmara.com/bin/driver_ws
# MMFG_WS_PROXY = http://proxy.mmfg.it:8080

# per i negozi HK:
# MMFG_WS_HOST = https://pos-ws-hk-dev.bms.maxmara.com/bin/driver_ws
# MMFG_WS_PROXY = http://proxy.mmfg.it:8080

# per i negozi BENELUX:
# MMFG_WS_HOST = https://pos-ws-benelux-dev.bms.maxmara.com/bin/driver_ws
# MMFG_WS_PROXY = http://proxy.mmfg.it:8080

# per i negozi FR:
# MMFG_WS_HOST = https://pos-ws-fr-dev.bms.maxmara.com/bin/driver_ws
# MMFG_WS_PROXY = http://proxy.mmfg.it:8080

# per i negozi DE:
# MMFG_WS_HOST = https://pos-ws-de-dev.bms.maxmara.com/bin/driver_ws
# MMFG_WS_PROXY = http://proxy.mmfg.it:8080

# per i negozi USA:
# MMFG_WS_HOST = https://pos-ws-usa-dev.bms.maxmara.com/bin/driver_ws
# MMFG_WS_PROXY = http://proxys.mmfg.it:8080

# per i negozi in cloud:
# MMFG_WS_PROXY = http://proxy3.mmfg.it:9000

CASH_ID = 01
CASH_ROLE = MASTER                # ruolo cassa: MASTER, SLAVE, BACKUP
FEATURE_SET = CASH                # insieme di funzionalita permesse: CASH, WAREHOUSE, OFFICE, CONSULTATION
LOCAL_IP = 192.168.195.55
MASTER_IP = 192.168.195.55        # 192.168.201.164  # 192.168.195.55
BACKUP_IP = 
MASTER_PORT = 8000
GUI_LANGUAGE = ITAL               # ITAL SPAG PORT FRAN INGL JAPA TEDE DANE OLAN CHIN
GUI_THEME = RICH                  # global appearance of this webapp; values are: "RICH" (normal) or "BASIC" (touchscreen)
DEPLOY_ENV = development          # environment: live, demo, development
DEBUG = 1			                # debug: 0 (default), 1
# ENABLE_CNT = 0                    # abilitazione contapersone: 0 (default), 1
# MANAGE_BUNDLE_USERS = 0
# ALLOW_WEB_TRANSLATIONS = 1

# sales options
# GIFT_CARD_ENABLED = 1

# daemon options
# POS_WEBSERVER = 1		# all
# POS_PRINTER = 1		# all
# POS_KEEPALIVE = 1		# all
# POS_DOWNLOADER = 1	# all
# POS_UPLOADER = 1		# all1
# POS_INSTALLER = 1		# all
# POS_TERMINAL = 1		# all
# POS_SYNCHRONIZER = 0	# solo backup

# pos_installer
# POS_INSTALLER_MIN_TIME = 000000	# estremo inferiore dellintervallo di installazione in formato HHMMSS
# POS_INSTALLER_MAX_TIME = 080000	# estremo superiore dellintervallo di installazione in formato HHMMSS

# pos_controller
POS_CONTROLLER_HOST = localhost
POS_CONTROLLER_PORT = 13456
POS_CONTROLLER_PASS = zinc0st4

# pos_printer
POS_PRINTER_DEVICE = 
POS_PRINTER_COMMAND = "lpr -P %(printer_name)s -o sides=two-sided-long-edge -o media=A4 %(file_name)s"

# pos_terminal
POS_TERMINAL_ID_TERMINALE = 12345678
POS_TERMINAL_HOST = 192.168.1.25
POS_TERMINAL_PORT = 14520
POS_TERMINAL_TIMEOUT = 1
POS_TERMINAL_SCONTRINO = 1
POS_TERMINAL_DEBUG = 1
POS_TERMINAL_BACKUP = 1

# cash register
CASH_REGISTER_HOST = 192.168.195.39 # 39 senza invio fiscale - 40 invio fiscale
CASH_REGISTER_PORT = 9100
CASH_REGISTER_PROTOCOL = CUSTOMDLL
CASH_REGISTER_ENABLED = 0                     # abilitazione registratore di cassa

# CASH_REGISTER_TYPE puo avare i seguenti valori
# KUBE - OFFICE
# KUBEUSBPDF - ITAL
# KUBEUSBJP
# EPSONUSBPDF
# KUBEUSBPDFK3
CASH_REGISTER_TYPE = KUBEUSBPDF
