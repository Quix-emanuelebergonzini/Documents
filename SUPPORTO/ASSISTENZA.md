## RICERCA ALL'INTERNO DEI LOGS DI UN JOBS ##

se devo lanciare un incr su molti negozio
ricordarsi MEMORY=3000

poi non cancellare mai il log della console perché appena parte scrive il nome del job sul CLOUD

esempio
MEMORY=3000 LANDSCAPE=PRODUCTION docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py incr -p10 0001401735 0001402135 0001402136 0001402398 0001499005 0001499007 -f
Flag --export has been deprecated, This flag is deprecated and will be removed in future.
job.batch/bergonzini.e-20200207163421-l2vudi9iaw4vchl0ag9uic9zb3vy-job created <<<<<---------- ** qui c'è il nome del JOB!!! ****
Recuperare yaml: kubectl_run_job_rBU7o1/runtime-job.yml kubectl_run_job_rBU7o1/job_cmd.yml
MEMORY=3000 LANDSCAPE=PRODU{"asctime": "2020-02-07 15:35:18,025", "message": "Esportazione di tipo DB con priorita' 10 per:\n0001401735\n0001402135\n0001402136\n0001402398\n0001499005\n0001499007\n", "severity": "WARNING"}
Esportazione di tipo DB con priorita' 10 per:
...


con il nome
bergonzini.e-20200207163421-l2vudi9iaw4vchl0ag9uic9zb3vy-job
andare in console CLOUD
Kubermeters Engine - Carichi di Lavoro

Impostare il progetto giusto

Mettere nel filtro
Nome: bergonzini.e-20200207163421-l2vudi9iaw4vchl0ag9uic9zb3vy-job

entrarvi e poi cliccare su Container Logs

da li può partire la mia ricerca....


labels."k8s-pod/job-name"="bergonzini.e-20210211103501-l2vudi9iaw4vchl0ag9uic9zb3vy-job"


# proxy.pac per Tunnelblink da immettere nelle config del wifi
http://pacg.mmfg.it:8888/proxy.pac
