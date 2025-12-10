https://pos-co-uat.linmara.com/

cod_installazione 9000000007

foglio delle Attività di migrazione
vedi colonna CINA 2 UAT

- il db per la nuova installazione è già in essere su alibaba

- il bms è già in essere su alibaba (e relativo db)

(CN - CO) posweblitecnco-kube

prendi il foglio EVO_FG1750 | Posweb On Container - note tecniche e di sviluppo
https://docs.google.com/document/d/1d1Ayd6TpAyc7RBOntVUjTm7mmck6TdTutpCPdL_5fBA

paragrafo Config nuova postazione

MYSQL_HOST si recupera nel magnifico mondo di alibaba
    switch linmara-test-dev
    cercare ApsaraDb rds
        i nomi rm-XXX nel dettaglio riportano il Nome. prendiamo quello di riferimento
        cliccandoci sopra passo alla schermata da cui posso fare LOG ON DATABASE

wsclient.ws_mmfg
    url te lo danno loro

i bucket per vederli si deve entrare con il ruolo da bms (linmara-test-dev)
    cercare oss ==> object storage service
    voce buckets
    li fanno loro e in base al nome si prende quello di riferimento (es, bucket-posco-XXXX-test)

(+ commit sul kube del configmaps)

i cronjob sono spenti momentaneamente per via di non concorrenziare con l'altra macchina ancora accesa

link provvisorio (ce lo danno loro)
https://pos-co-uat-cloud.linmara.com

se il db non è vergine copiare dentro global_status della macchina nuova
il due valori oggi presenti nella macchina vecchia presenti in conf/version
'DB_DOWNLOADED_VERSION'
'DB_INSTALLED_VERSION'

configurare il cronjob (prendere da macchina già in essere) + commit su kube


fare buil + deploy
Poswebonline BUILD
Push to Alicloud
PoswebOnlineConcessionCN Deploy

mandare un full db