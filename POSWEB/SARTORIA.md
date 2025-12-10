la classe non è il riferimento al capo

la classe è la classe del prodotto su cui viene fatta la sartoria

il fatto che la sartoria sia agganciata al capo o no
è stabilito da un campo che su db è pogressivo_capo

ma la classe non c'entra con il fatto che sia su capo o extra vendita


cod_operazione è il tipo di operazione che viene effettuata
su mmj la 99 è il campo libero da non confondere con classe 99 (oggettistica)!!!!

mmj usano la classe 99 per definire cose che non sono veramente sartorie
(credo i costi di spedizione)


metodo recupero delle sartorie che si vedono nel dettaglio del capo:
get_lavorazioni (dentro al capo)
get_lavorazioni_extra (sartoria extra fuori vendita nel cruscotto in basso a sinistra
nella schermata di vendita)


modifica_movimento va a modificare il movimento di VENDITA
(vedi causale_reso salvato come dato in tabella)

invece se si vuole modificare il movimento di STORNO
(vedi causale_reso salvato dentro al custom_data)
bisogna andare in Resi.set_progressivi_resi() che chiama il
servizio su sede ws_segna_capi_resi
e poco sotto c'è un ciclo che salva le infomazioni sui capi o contabilità
