
durante l'anno 01/02 al 31/12 le vendite vengono registrate
nella pos_vp_tiers_history e aggiorna il livello vip nella pos_vip_tiers

dal 01/01/<anno+1> al 31/01/<anno+1> tutte le vendite finisco nella tabella pos_vip_tiers_next_period_sales
e quindi queste vendite non servono per aumentare il punteggio

01/02 partono due job: ROTATE (guest/posws/bin/poswsbe/vip_tiers/controller.py)
    ==> prende la pos_vip_tiers ne fa una copia e la chiamata pos_vip_tiers_<anno-1> e crea una nuova pos_vip_tiers
    quindi pos_vip_tiers vuol dire "anno in corso"
    
    poi parte con il calcolo della nuova pos_vip_tiers. si basa sul livello_actual e livello_progressive
    (vedi il sorgente per capire il calcolo)
    
    se livello_actual > livello_progressive >>> nuovo livello è livello_last_year - 1
    se livello_last_year < livello_progressive >>> nuovo livello è livello_progressive

secondo job: process_next_period_sales prende le righe pos_vip_tiers_next_period_sales e calcola le vendite e calcola il nuovo livello