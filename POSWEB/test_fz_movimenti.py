from movim_utils import calcola_scorporo_iva, get_testa_e_righe

import config_store
pard = config_store.application_parameters()

id_transazione = "44355"
testa, righe, mov_contabili = get_testa_e_righe(pard, id_transazione)

calcola_scorporo_iva(pard, testa, righe, mov_contabili)