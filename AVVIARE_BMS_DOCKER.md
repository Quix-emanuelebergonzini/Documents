avviare sempre con (per bmsde) LANDSCAPE=TESTING ./docker/compose_up

--- tutto questo senza toccare compose_up.sh e non riavviare ---
* avviare la prima volta con il LANDSCAPE

*aggancio al crm test*
* dopo andare in storebackoffice/bin/config/configmaps e storebackoffice/bin/config/secrets
    e prendere il wsclient.crm e copiarlo
    in /main/bin/config/configmaps e in /main/bin/config/secrets

*aggancio al db di test per boss*
* viceversa da /main a storebackoffice copiare il contenuto di mysql.bmsde

* e andare a mettere
    *se non va*
    env_name = "TESTING" o "DEVELOPMENT" (anche perché LANDSCAPE sembra in questo punto non essere ascoltato
    cmq guardare poco sopra che ci sono i settings)

    -- TUTTO QUELLO PRESENTE DENTROA bms../main non si committa o altro perché non è un nostro sotto-modulo --

    in storebackoffice/bin/config/env.py (circa riga 369)

    e invocare una pagina di boss
    (es, https://localhost:4443/?module=boss.order.action&program=search_order&sid=)
    così che....scopri che sei in TESTING o DEVELOPMENT


potrebbe servire
in guest/storebackoffice/bin/boss/config_boss/env.py
riga 423 prima di
project_conf = projects[env_name][project_name]
aggiungere prima
projects[env_name]['bmsde'] = {'title': 'BMS [dev]', 'fe_url': 'http://bmsde.5d945181a6de/bin/driver', 'codice_proprietario': 'MMDE'}

serve anche per avviare i servizi da poswsbe


=====

1. aprire un terminale

2. posizionarsi nel codice del bms in questione
    * cd /Users/emanuele.bergonzini/bms/bmshk/

3. eseguire i gcloud di posizionamento al progetto cloud per il bms in questione
    * gcloud config set project mmfg-bms-gruppo-multi
    * gcloud container clusters get-credentials gke-tokyo --zone asia-northeast1-a

VEDI MyDocuments/tunnel_cloud.sh

4. avviare
    * LANDSCAPE=TESTING docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py part -t Consumer -f -p10 all

ALTERNATIVAMENTE:
1. aprire browser
2. collegarsi allinterfaccia web del bms in questione
3. aprire il link
    * https://hk-dev.bms.maxmara.com/?module=boss.aggiornamenti_negozi.action&program=search&sid=540vpo5yij50kh
