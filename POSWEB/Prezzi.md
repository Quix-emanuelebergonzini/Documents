OD - negozio outlet diretto i prezzi arrivano dalla pos_prezzi_negozi_<anno_stag>,
        però controllare bene e seguire il codice

per gli outlet si considera anno_stag_start = year - 6 (stag 1) e anno_stag_stop = year + 1 (stag 2)
quindi dalla stagione 1 di 6 anni fa alla stagione 2 fra un anno in avanti

ND - negozio diretto arrivano sia dalla pos_prezzi_negozi_ e anche dalla catalogo_prezzi

---------------------------------------------------------------------------------------------------
'STORE_CHANNEL': (
    'ND', -- diretti
    'NF', -- frh
    'OD' -- outlet diretti
),

Prezzi(TableExport)
--- Esportazione prezzi
-- raggruppiamo i negozi per parametri omogenei

-- il negozio è ITALIANO NON FRANCHISING MA CODICE_PROPRIETARIO E' DT --> prezzi_get_annostag_pos
"""
    SELECT p.negozio as cod_negozio, p.modello, {select_variante}, p.unita_vendibile as pezzo, p.tipo_prezzo,
            0 AS id_listino, p.data_inizio_validita, p.data_fine_validita, p.prezzo, p.divisa, p.perc,
            {importo_sconto} AS importo_sconto, p.annostag, p.modificato as data_modifica
    FROM mx_prezzi_negozi_{annostag} as p
    WHERE p.negozio in ({lista_negozi})
    AND tipo_prezzo in ({tipi_prezzo}) -- V,S,P,C
    AND NOT (tipo_prezzo in ({prezzi_abbattuti}) and perc = 0 and importo_sconto = 0) -- S,P,C
"""
altrimenti (tutt gli altri negozio, ad esempio, qui ci vanno a finire i DT stranieri
oppure gli italiani franchising....):
-- prezzi_get_annostag_bms
e ci sono tre vie:
    - il parametro PREZZI_FROM_DBG su quel negozio è a 1 e annostag è >= 20201

"""
    SELECT distinct m.codice_gruppo AS cod_negozio, cat.modello_retail AS modello, '' AS variante, pezzo, p.tipo_prezzo,
    0 AS id_listino, REPLACE(p.data_inizio, "-", "") as data_inizio_validita, REPLACE(p.data_fine, "-", "") as data_fine_validita, p.prezzo, p.valuta as divisa, p.perc_sconto as perc,
    '0.00' AS importo_sconto, CONCAT(p.anno, p.stagione) as annostag, p.upd_datetime as data_modifica
    FROM catalogo_dbg_prezzi p
    JOIN catalogo_dbg cat on p.anno=cat.anno and cat.stagione=p.stagione and p.modello=cat.modello_dt
    JOIN ana_soggetti_transcodifiche tr on tr.societa = p.societa and p.cliente = tr.codice and tr.data_fine is null
    JOIN ana_soggetti_master m on tr.id_soggetto = m.id_soggetto and m.codice_gruppo IN ({lista_negozi}) and p.tipo_prezzo in ({tipi_prezzo})
    WHERE p.anno = '{anno}' AND p.stagione = '{stagione}'
    {where_modello_retail}
    {ts_cond_min} {ts_cond_max}
"""


    - il negozio è OUTLET NON STATI UNITI O CANADA
    - tutti gli altri negozi...

PREZZI_FROM_DBG - se attivo il recupero avvine da catalogo_dbg_prezzi e ci sono solo dati >= 20201 non prima

da febbraio 2023 - export ai negozi va indietro fino a 6 anni (12 annistagione) per gli outlet.
Se però si va più indietro della 2020-1 (data inizio popolamento DBG),
prendiamo il catalogo/prezzi alla "vecchia maniera" (quella pre-DBG),
anche se il negozio lavora già "alla nuova" (PREZZI_FROM_DBG=1)
 