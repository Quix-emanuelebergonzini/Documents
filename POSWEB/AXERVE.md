pagamenti_carte c'è tutto
pos_terminal se axerve va in stopped

le tabelle in uso sono uguali a quelle pos_terminal (ingenico, pax )

pos_terminal (demone) o axerve fanno
si salva un record dentro local.db/pos_transaction
dopo polling fino a completato

quando premo paga si stacca il tran_id e dopo lo passa al polling e richiede lo stato del pagamento

CREATED -> FINALIZED o ERROR
