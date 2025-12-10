INSERT INTO `autorizzazioni_permesso` (`codice_ruolo`, `codice_azione`, `upd_datetime`, `upd_user`)
VALUES
	(ADMIN, CONSUMER_CONSENSI, 2018-07-05 16:16:35, pivam);

INSERT INTO `autorizzazioni_azione` (`codice`, `descrizione`, `gruppo`)
VALUES
	(CONSUMER_CONSENSI, Edit consensi delle consumatrici per tutti i brand, );



INSERT INTO `autorizzazioni_ruolo` (`codice`, `tipo_ruolo`, `descrizione`)
VALUES
	(Developer_Filiali, ADMIN, Tipo ruolo identificativo di un admin);


INSERT INTO `autorizzazioni_ruolo` (`codice`, `tipo_ruolo`, `descrizione`)
VALUES
	(LINMARA_B2CManager, SEDE, Ruolo identificativo di un impiegato dell\area B2C);

INSERT INTO `autorizzazioni_permesso` (`codice_ruolo`, `codice_azione`, `upd_datetime`, `upd_user`)
VALUES
	(Developer_Filiali, CONSUMER_CONSENSI, 2018-07-05 16:16:35, pivam);
