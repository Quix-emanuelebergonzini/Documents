
gcloud compute --project "mmfg-bms-gruppo-multi" ssh --zone europe-west1-c  --internal-ip "poswebonlinees-test"
dopo fare
sudo -u posweb -i

poi fare cd /rnd/pos/mmfg/posweb


https://es-dev.pos.maxmara.com/
per il db ti colleghi al server e poi dai
mysql --login-path=posweb main