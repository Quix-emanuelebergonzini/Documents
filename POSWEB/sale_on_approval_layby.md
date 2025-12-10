nella tabella movimenti e movimenti_relazioni ci vanno le vendite, ma anche i sale on approvals e layby

il primo è la cliente prova il capo poi paga successivamente
il sencondo la cliente paga uan parte, poi un altra parte fino a raggiungimento della cifra finale


in pratica con il sale on approvals e layby si creano delle relazioni appunto e nella tabella movimenti_relazioni

layby
trovo id_transazione come id (id della seconda parte di acquisto) e id_transazione_rel (id della prima parte di acquisto)
quindi la prima volta non troverà relazioni, ma dalla seconda volta in avanti si.

guardare pos.py --> chiudi_vendita()

simile per pos_on_approval anche se qui cè una triplice relazione ovvero che la prima transazione viene registrata OPEN poi REPLACE poi FINALIZED e infine CLOSED
ovviamente i tre stati nella movimenti_relazioni sono tutti un record per ciascuno

atttenzione

id_transazione = 5 id_transazione_rel = 8
la volta dopo è
id_transazione = 14 e id_transazione_rel = 5 quindi ogni passo punta al passo antecedente
