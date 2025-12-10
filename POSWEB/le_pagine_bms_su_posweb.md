le pagine di bms su posweb viste con iframe devono avere nell'url (nascosto..f12 per vederlo)
con un sid che non è quello di posweb che viene passato al bms.
è staccato dal keepalive che chiama poswsbe che chiama il portale e ce lo restituisce.
poi viene validato dal bms dove posweb chiama frontend (vedi INIT_SID) il quale ha url da chiamare di media (o media-test)

nel frontend nella pagina ws_interface_store_config ci sono tre if per PRODUCTION else TESTING else STAGING
con le stesse variabili riscritte

però da portale deve esistere un utente che ha come username questa forma

nw + cod_negozio
user: nw1601113
pwd: bf969pp6

questo utente lo creano le ops quindi se le pagine su posweb non fanno vedere quelle di bms fare:
- se dai tool di posweb faccio reset sid e poi dai dati_installazione cerco remote_sid e lo vedo rigenerato
  (aspettare che il keepalive giri di nuovo per staccare un nuovo sid)
- se iframe ha il nuovo sid staccato noi siamo a posto e chiediamo alle ops di controllare
