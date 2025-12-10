se alla url di bms aggiungiamo alla fine /healthz vediamo il tag rilasciato sull'ambiente

### configmaps ##

cat main/bin/config/configmaps/mysql.XXX

 - storebackoffice hai i suoi configmaps e possono non essere uguali a quelli presenti in main
 - quando si effettua un rilascio (deploy) dentro al kubemeters del bms<XX> il file configmaps.yml viene suddiviso in enne files quante
 sono le configurazioni descritte

 Noi possiamo aggiungere le configurazioni ma non i segrets (pwd)

 es di configurazione:
 configmaps_base:
     mounts:
        ...
         wsclient.crm-rest-boss:
          json:
            connection_timeout: 60
            enable_compression: 0
            http_proxy: ""
            params: "{module: crm_ws_server,	program: boss_interface}"
            req_type: BASIC
            url: https://gw.ws.mmfg.it/crmws-t/api
            req_content_type: application/json
            client_cert: main/bin/config/configmaps/gw_cert.crt
            client_key: main/bin/config/secrets/gw_cert.key
            server_ca_cert: main/bin/config/configmaps/rootcert.pem
        ...
        guest/storebackoffice/bin/config/configmaps:
            wsclient.crm-rest: "\*wsclient.crm-rest-boss"

senza ciò è possibile che il sistema risponda con messaggi tipo
crm--rest response_content

## pos_export_to_store.py ##
Negozio:
    for cod_negozio in self.negozi_l:
        ...
        result = self.pard[DB].query_d(mysql_query, retail)
		d = dict((rec[cod_negozio_anag], rec) for rec in result)
        if self.codice_proprietario == "USEIT" or self.codice_proprietario == "MMHK":
        **significa che viene prima invocato retail per avere tutte le informazioni anagrafiche
        **sul negozio e poi se sono USA o HK sostituisco le informazioni con la query che effettuo sul BMS
        **per il resto del mondo le informazioni rimangono quelle di retail e vengono usate nello scontrino subito dopo il logo
        **Nel BMS se lutente modifica le anagrafiche se sono USA o HK allora va bene altrimenti le informazioni non le considera
        ***

## BMS ##
    /main/bin/config_common.py aggiungere a pard[TRUSTED_PROGRAMS] le righe con il programma da chiamare (se lerrore è NOT_AUTHORIZED)

## min_timestamp ##
min_timestamp di un incr è il risultato di questa query
SET @cod_installazione = '';
SELECT available_version FROM pos_install_info WHERE cod_installazione=@cod_installazione AND update_type='db';

quando si effettua un incr su un determinato negozio (es, 0801237 (JP)) su BMS (es, JP)

------------------------ NOTA BENE ---------------------------
sulla pos_install_info la colonna modificato
è il valore minimo al prossimo incrementale (era il valore massimo all'incr precedente)

------------------------ NOTA BENE PER JP ---------------------------
su BMS il valore degli timestamp_modificato sono all'UTC invece su CRM all'UTC+2
quindi incr su BMS è in anticipo di 2 ore sul CRM quindi i dati di aggiornamento da CRM ai negozio
hanno una latenza di 2 ore in avanti

quindi per fare i test quando su CRM arriva il dato aggiornato si
deve aggiornare con una data poco più futura del min_timestamp che esce dal codice qui sotto:

su BMS (es,JP)
python main/bin/console.py

## GET MAX MIN TIMESTAMP INCR ##
import poswsbe.pos_utils as pos_utils
pard = {}
pos_utils.init_db(pard, config={})
from poswsbe import pos_install_db_access
from poswsbe import pos_utils
cod_installazione = '0000001007'
pard['DEFAULT_DB_VERSION'] = '001002'
pard['CURRENT_TIMESTAMP'] = pos_utils.get_extended_timestamp(pard, ts=None)
update_type = 'db'
old_version = pos_install_db_access.pos_install_get_version(pard, cod_installazione, update_type, 'available')
new_version = ':'.join((pard['DEFAULT_DB_VERSION'], pos_utils.get_compact_timestamp(pard, pard['CURRENT_TIMESTAMP'])))
export_info = {'old_version': old_version, 'new_version': new_version}
min_timestamp = pos_utils.get_extended_timestamp(pard, export_info['old_version'].split(':')[-1])
max_timestamp = pos_utils.get_extended_timestamp(pard, export_info['new_version'].split(':')[-1])
min_timestamp
