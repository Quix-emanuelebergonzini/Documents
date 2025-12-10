in posweb alla chiusua della cassa si controlla che la cassa
abbia FEATURE_SET != ONLINE quindi non è ECI altirmenti è un ECI

gli ECI sono dentro i centri commerciali e hanno un solo cod_installazione comune (tipicamente 9000000001)
e sono i cosidetti (posweb online) POS_ONLINE a differenza di POS_OFFLINE (chiamati pos online)

per gli ECI se si fa da lista_vendite la chiamata di chiusura vendita
a se stesso bisogna in locale dentro a pos.service.\_call_rest_service

impostare localhost come macchina perché l'indirizzo della macchina locale non va

impostare il proxy http://proxy.mmfg.it:8080 sulla connection_parameter per il negozio in uso
altirmenti da timeout



usare come interprete python questo quindi
/rnd/pos/mmfg/posweb/bin/python
