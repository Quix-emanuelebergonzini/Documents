apro una issue a Erika chiedendo di abilitare il modulo e program (che saranno quelli che invoco su posweb e dargli il nome della funzione che è
    il nome della classe che invoco sul controller in posweb che poi apre iframe)

vado poswsbe dentro a pos_generate_custom_values.py

aggiungo nelle funzioni il POS:::<nome_nuovo> e aggiungo la condizione di attivazione

eseguo:
gcloud config set project mmfg-bms-gruppo-multi
gcloud container clusters get-credentials gke-stghislain --zone europe-west1-c
LANDSCAPE=TESTING docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_generate_custom_values.py

se non va richiedere le abilitazioni...

anche se basterebbe un incr, per direttiva noi mandiamo sempre un part al negozio
(se è un bms cloud basta andare da interfaccia)
