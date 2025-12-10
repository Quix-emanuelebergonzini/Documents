store_config INVIO_TELEMATICO_ENABLED a 1 per gli italiani

in stampe_custom invio telematico è sotto la variabile
is_corrispettivi_enabled

la riga di scontrino (comando_riga_fiscale) è "speciale" e si chiama RIGA_FISCALE_REP_IVA

PER DEBUG SU STAMPA CARTACEA UTILIZZARE DENTRO
custom.py in print_all (metodo chiamato da tutte le stampe da stampe_custom.py)
tipo questa istruzione self.logger.info(self.row_list) --|> stampa tutto il
dizionario di righe (e così controllo i suoi valori)

su log/cash_register/main.log e mettere CASH_ENABLED a 0
e CASH_REGISTER_TYPE a KUBE
