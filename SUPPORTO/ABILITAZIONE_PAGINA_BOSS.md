quando sviluppo una pagina boss
per far vedere una pagina nuova aggiungo nel progetto main/bin
in config_common.py in pard["TRUSTED_PROGRAM"]
la mia pagina boss

però è anche vero che non tutti gli utenti vedono e fanno tutto
le abilitazioni arrivano da portale

e tramite il database web (si accede come solito ma con nome db web)
ci sono i sid_XXX relativi agli utenti che vi accedono
quindi non entriamo con il loro user/pwd ma utilizziamo
il XXX per richiamare quella pagina e per vedere gli errori

possiamo o andare in LANDSCAPE=PRODUCION in locale e richiamare
con quello sid_XXX

altrimenti...

bisogna andare in profondità del codice...

un buon modo è usare il debugger di cloud console
che funziona con le chiamate da gui da ambiente online (non in locale)
