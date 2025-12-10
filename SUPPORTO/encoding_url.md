attenzione ad esempio è capitato questo

su postman mandavao un parametro così

filter[telefono] --> +81091542

però su python arrivata ' 81091542' però non va bene come attendibilità
quindi bisogna ricordarsi
che i carattteri speciali deveno essere encodati

quindi andare sulla console js di chrome e usare

encodeUrlComponent('+081091542') e usare il risultato come parametro
così fa arrivare i caratteri speciali al python
