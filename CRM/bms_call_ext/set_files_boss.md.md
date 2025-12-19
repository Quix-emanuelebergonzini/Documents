se su boss l errore è ('OperationalError(2003, "Can\'t connect to MySQL server on \'vserverbox-01.mmfg.it:3308\' (110)")',
OperationalError(2003, "Can't connect to MySQL server on 'vserverbox-01.mmfg.it:3308' (110)"))

si può rimediare in questo modo:

in base al BMS docker avviato esempio maxima20 prendere da main il mysql.maxima20 sia da configmaps che da secret
e copiarli in guest/storebackoffice/bin/config/configmaps e guest/storebackoffice/bin/config/secrets

idem per mysql.web (sia configmaps che secrets da copiare
in guest/web/bin/config/configmaps e guest/web/bin/config/secrets)


riavviare il docker