- prendere il quanto più possibile tracciati di produzione.
  - pensare a dove potrebbe accadere quel caso e carcare di ottenerlo per analizzare
- fidarsi poco o nulla di codice simulato in quanto potrebbe discostare dalla realtà (tipo promo engine)

Per far vedere i negozi poslite serve:
  - controllare sul configmaps se la postazione punta a secure-t
  - dire di configurare su Portale l'utente nw
  - dire di controllare che ci sia su Portale tabella negozi il negozio

- per una macchina di test:
  - scrivere alla referente quale postazione sul ticket e quali feature ci sono sopra
  - cercare di avere la branch allineata a produzione ma non troppo avanti a meno che non sia innocuo
  - alcuni esempi di test si potrebbero (se non creano confusione...) prendendole da negozi di produzione
  - e portandoseli in locale....
    - resettare il SID anche se non neccesario
    - catalogo presente (guardare le regole del poswsbe in onda)
    - fidelity card se c'è e in che tipologia (SYNC o ASYNC con xml)
    - consumatrici come si creano se SYNC o ASYNC (con xml)
    - controllare le consumatrici (anonime e non)
    - controllare se voglio le fatture o i taxfree
    - controllare i layby
    - controllare il reso che venga recuperato e chiuso
    - controllare se il menù è generato correttamente
    - tipo di stampante da configurare (se si tratta di un posweblite italiano, per cui è per forza KUBEUSBPDFK3 vedi FGPOS-1321)
    - se posweblite, il POS deve lavorare SCOLLEGATO (POS_CONNECTED = 0)
    - controllare UTC_OFFSET (a 1 sui poslite)
    - controllare se funziona il reperimento da remoto delle consumatrici
    - presenza delle commesse sul negozio
    - controllare MMFG_WS_HOST che punti al corretto ws affinché si vedano gli iframe
    - connessione crm (se ha le fidelity che vengano scaricate oppure una creazione della consumatrice)
    - gift card se abilitati
    - resi (controllare carta di credito principalmente)
      - controllare POS_TERMINAL_TYPE=ingienico e HIDE_RIMBORSO_CC per manifestare le scelte di reso con storno e/o abbuono
    - resi liberi
      - controllare RETURNS_ENABLED
    - capi omaggio
      - controllare GIFT_USAGE
    - prezzi presenti (vedi catalogo)
    - om (connessione)
    - promo engine (oauth connessione)
    - b2e (chiedere se possibile degli sku) - altrimenti rigenerare con lo scripts a negozio
      - fare se possibile un test con b2e in locale
    - giacenza per b2e (test con sku e connessione om)
    - se USACA controllare vertex di test (fare una domanda se è possibile usarlo)

La KUBE è usata anche all'estero con INVIO_TELEMATICO_ENABLED a 0.

Su DT è meglio usare la KUBE reale. Si deve stare attenti al discorso dell'arrotondamento (trae in inganno tra test e prod)

Arrotondamento al decimo significa DECIMAL_PLACES_ROUNDING = 1 (da confermare vedi itma-pos negozio 0130040)

Gaudioso sul promo engine (lato infra):
tutte le  chiamate vengono indirizzate verso l'istanza di Europa,
indipendentemente dalla zona del chiamante invece in test è gia attivo il loadbalancing tra regioni diverse
ma dopo il golive anche prod avrà il loadbalancing attivo.