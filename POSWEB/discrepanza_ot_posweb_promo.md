INPUT
"shop" --|> "shop_country" presente nella api condivise con il nome "state_shop". Possiamo inviare
entrambi le chiavi con la nazione del negozio

"shop_sign" --|> nella api condivisa non era presente questo campo fuori dal pacchetto "shop"
In questo momento se viene passato un valore diverso da "MM" da errore. Se possibile,
terrei quello dentro il pacchetto "shop" chiamato uguale

"legal_entity" --|> nella api condivisa non era presente questo campo e non possiamo
riempirlo su posweb perchè non abbiamo il dato. Si può togliere?

"sale_channel": "Retail" --|> non presente nelle api, non è un problema aggiungerlo teniamo fisso Retail

"items" --|> "style_code" --|> nella api condivisa questo campo si chiama "model_code"
            "style_name" --|> nella api condivisa questo campo si chiama "model_name"
            "style_variant" --|> nella api condivisa questo campo si chiama "variante"
            "tailor_expenses" --|> nella api condivisa questo campo si chiama "spese_sartoria"
            "pricelist_type" --|> nella api condivisa questo campo non c'era ma possiamo aggiungerlo
            "product_category" --|> nella api condivisa questo campo non c'era e non capiamo a cosa si mappa

OUTPUT
la chiave "promo_engine" viene aggiunta al pacchetto "input" --|> "items"
invece che "output" --|> "items"

"output" --|> "items" --|> "#id#" da api condivisa era "id". Possiamo mantenere questa nomenclatura?
