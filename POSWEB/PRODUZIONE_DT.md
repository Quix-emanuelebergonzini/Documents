https://docs.google.com/spreadsheets/d/1yDnrMl5Fd0t_hU-SoVRZUigE7f35PMvJyNBaMVzfIRU/edit?ts=5d6f5a6a#gid=1263246775
foglio condiviso con gli IP di Produzione.

Nella scheda "diretti Diffusione Tessile"
    - codice: sono le ultime tre cifre del codice di negozio
    - lan backoffice: sono gli ip raggiungibili dalla rete per collegarsi al negozio
    (es, 10.128.186.1)

*Per collegarsi da web:*
    10.128.186.1:8000
con:
    Utente (sempre e comunque, MAI cassiera): assistenza
    Pwd: kojak

**PER DT se la pagina della vendita non si apre, andare a 10.128.186.2:800 (uguale utente/pwd)**

*Per collegarsi ssh:*
    ssh posweb@10.128.186.1
    pwd: dtneg2011
