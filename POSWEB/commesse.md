1) PROVARE DA INTERFACCIA A CREARE UN Dipendente
2) valuare Commesse nella pos_export_to_db
3) SELECT DISTINCT m.id_soggetto AS id_soggetto
FROM ana_soggetti_master m
JOIN ana_soggetti_master n ON (
	m.tipo_soggetto=Dipendente
	AND n.tipo_soggetto=Negozio
	AND n.codice_gruppo={codice_gruppo_negozio}
	AND m.id_soggetto_appartenenza=n.id_soggetto)
WHERE m.status="Attivo"

in questo caso, dove basta prendere da ana_soggetti_master un tipo_soggetto = Dipendente
e mettergli come id_soggetto_appartenenza = id_soggetto del negozio (negozio lo trovo con codice_gruppo)
però controllare ana_soggetti_contratti che non ci siano record riferiti a quel Dipendente


---------------------------------------------------------------------------------------------------------

-- estrazione full dipendenti standard
SELECT  m.*
FROM ana_soggetti_master m
JOIN ana_soggetti_master n ON (
	m.tipo_soggetto='Dipendente'
	AND n.tipo_soggetto='Negozio'
	AND m.id_soggetto_appartenenza=n.id_soggetto
)
WHERE m.status = 'Attivo' AND n.codice_gruppo='0801237';

-- controllo anagrafica fisica
SELECT id_soggetto_spedizione AS `soggetto_spedizione_SoggettoAnagrafico__id_soggetto`, divisione, id_soggetto_appartenenza AS `soggetto_appartenenza_SoggettoAnagrafico__id_soggetto`, utente_modifica, nome_localizzato, id_soggetto, nome, status, id_soggetto_responsabile AS `soggetto_responsabile_SoggettoAnagraficoBase__id_soggetto`, codice_gruppo, id_soggetto_fatturazione AS `soggetto_fatturazione_SoggettoAnagrafico__id_soggetto`, dataora_modifica, dataora_inserimento, utente_inserimento, ragione_sociale, nazione, categoria, tipo_soggetto FROM ana_soggetti_master WHERE (id_soggetto = '430460') AND tipo_soggetto = 'Dipendente';

-- controllo anagrafica professionale
 SELECT matricola, lingua, mercato, id_soggetto, id_lingua_correlata, id_ruolo_corporate, id_origine, mansione, data_inizio, dataora_inserimento, id_soggetto_profilo_professionale, id_ruolo, utente_inserimento, data_fine, reparto FROM ana_soggetti_profilo_professionale WHERE (id_soggetto = '430460' AND data_fine IS NULL AND id_lingua_correlata IS NULL) ORDER BY data_inizio DESC;
