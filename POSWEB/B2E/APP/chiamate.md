la app chiama i servizi di posweb
quindi a esempio

<url>/api/v1/posweb/models?filter[brand]=MM&filter[categoria]=2&filter[stock]=1
/models il parametro stock=1  credo che serve per filtrare i capi con giacenza

<url>/api/v1/posweb/stock?filter[sku]=<lista di skus>
api/v1/stock è quello che restituisce la giacenza

<url>/api/v1/posweb/categories?filter[brand]=MM
b 

GIACENZA. COME CAPIRE UNA B2E NELLA REALTA'

NELLA REALTA' COME SI DECIDE UNA VENDITA B2E OPPURE NO??? DALLA GIACENZA !!!

Matteo Malagoli:
l'ordine di consumo della giacenza....se la giacenza dice
store : 1 , - outstore: 2
il primo capo che metti nel carrello è in_store  mentre il secondo è out_store

ed infatti.... (REX-28458)

https://pos-uat.linmara.com/api/v1/stock?filter[sku]=63660433060112&filter[details]=0
{
    "data": [
        {
            "type": "stock",
            "id": "63660433060112",
            "attributes": {
                "b2e": 23,
                "store": 100,
                "chain": 0,
                "b2e_zone": 0,
                "square_manual": 0,
                "square": 0,
                "store_showroom": 0
            }
        }
    ]
}

quindi la vendita seppura aperta da iOS e chiusa su Posweb, il capo immesso viene considerato IN_STOCK
ed infatti nel custom_data si troverà
{"annostag":"20232","desc_taglia":"36","desc_classe":"", "data_consegna_sartoria":"",
"variante":"011","nota_lavorazioni":"", "stock_type":"IN_STORE"}
