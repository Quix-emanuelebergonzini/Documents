curr_num_scontrino --> ultimo scontrino inviato correttamente, ma non è lo
scontrino che è inviato in questo momento
after_num_scontrino --> scontrino inviato correttamente in questo momento

quindi after_num_scontrino deve essere quello staccato in questo momento
e se uguale al curr_num_scontrino vuol dire che l'invio fiscale non è andato
e posweb permette la stampa da lista vendite

invece se è diverso after_num_scontrino da curr_num_scontrino invio fiscale
è andato a buon fine e da liste vendite si stamperà solo la bollettina interna


REX-23361 - dal log delle query si è trovato risposta. in pratica il nuovo fe permetteva
la ristampa della bollettina con flag_fiscale = 1