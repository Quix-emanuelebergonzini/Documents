per rendere un reso di nuovo rendibile devo mettere il flag reso = 1 nella pos_movimentazioni
per trovare il mio reso devo prendere id_transazione (che in posweb nel pagina dei resi è presente nella response nella chiamata di ricerca delle vendite da rendere)
con id_transazione vado nella pos_movimentazioni poi con id della movimentazione pos_movimentazioni_capo e rendo il capo con flag reso = 0

==== HK ====
attivazione del reso tramite menù nella CustomValues. Aggiornare menù e mandare giu un part della CustomValues al negozio
riempire la tabella ana_soggetti_raggruppamenti che non è nostra ma possiamo utilizzarla dove il tipo_raggruppamento è RESI_POSWEB
id_soggetto lo prendo dalla ana_soggetti_master


CONSIGLIO:
dopo aver fatto le vendite in locale per testare se dalla sede arriva tutto ok ricordarsi di cancellare da
movimentazioni le vendite locali!!!!
segnarsi i dati delle vendite per saperle ritrovare su sede
ovviamente devono essere importate sul bms correttamente

get_vendite_rendibili su bms per la ricerca su sede

pos.crea_reso (tasto procedi)
pos.paga_reso (tasto paga che apre la popup dei documenti di vendita)
pos.chiudi_reso (tasto chiudi dalla schermata dei documenti di vendita)


PER NON FARE MILLE VENDITE E NON RENDERE SU POSWEB UNA VENDITA E PROVARLA
E RIPROVARLA MILLE VOLTE POSSO ANDARE SU
resi.service.py
set_progressivi_resi e mettere subito un return alla prima riga del metodo

@transaction
def set_progressivi_resi(self, cod_negozio, anno_transazione, id_transazione, progressivi, list_causali_reso):
  return
