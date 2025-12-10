Gli aggiornamenti su test usare incr
I part solo in caso di nuova colonna (o quando si sviluppa per una nuova tabella)

StoreConfig aggiornare con incr per evitare che in part
si scombinino i contattori

è possibile fare incr su ALCUNI negozi (così è più veloce)
ma ahimè non su una determinata tabella

- mmfg_queue
- consumer_counter
- sale_number

sync 2 (ogni feature flag) perché dice: vince sempre il valore della sede
quindi incr lui genera le replace into

sync 1 sono oggetto di problemi!!! contattori per i quali il dato di negozio deve vincere su tutti

incr i contattori critici sono soggetti ma i sync == 1
metto una query di replace or into (e quindi non lo aggiorna)