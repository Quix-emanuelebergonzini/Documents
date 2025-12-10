UPDATE_TYPE_LIST = "db" # db,sw,python,sqlite,httpd

#######################################################################################################################
# PARAMETRIZZATE
#######################################################################################################################
# COD_INSTALLAZIONE = "PARAM_COD_INSTALLAZIONE"
# LISTA_COD_NEGOZIO = "PARAM_LISTA_COD_NEGOZIO"
# CASH_ID = "01" # "02" per la SLAVE
# CASH_ROLE = "MASTER" # ONLINE, SLAVE
FEATURE_SET = "CASH"
# MASTER_IP = "192.168.140.86" # per la SLAVE (es, dos-mm-de.posweb.mmfg.it) indirizzo negozio cloud
# MASTER_PORT = "8000" # per la SLAVE imporre porta 80
LOCAL_IP = "192.168.1.107"
# MMFG_WS_HOST = "PARAM_MMFG_WS_HOST"
MMFG_WS_PROXY = ""

#######################################################################################################################
# ALTRE
#######################################################################################################################
BACKUP_IP = ""
# GUI_LANGUAGE = "ITAL" # ITAL SPAG INGL JAPA TEDE CHIN
GUI_THEME = "RICH"
DEPLOY_ENV = "development" # environment: live, demo, development
DEBUG = 1

# daemon options
POS_WEBSERVER =     1				# all
POS_PRINTER =       0				# all
POS_KEEPALIVE =     1  				# all
POS_DOWNLOADER =    1				# all
POS_UPLOADER =      0				# all
POS_INSTALLER =     1				# all
POS_TERMINAL =      0				# all
POS_SCHEDULER =     0				# all
POS_SYNCHRONIZER =  0			    # solo backup

# KUBE - ITAL
# KUBEUSBPDF
# KUBEUSBJP - JP
# EPSONUSBPDF
# KUBEUSBPDFK3 - EU
CASH_REGISTER_TYPE = "KUBEUSBPDFK3"
CASH_REGISTER_ENABLED = "1"	# abilitazione registratore di cassa

OVERRIDE_DEV = "1"

MAX_SAVED_BACKUPS = 2

PORTAL_LOGIN = 0