SELECT *
FROM pos_consumer_indirizzo_alfabeto
WHERE length(cast(CONVERT(localita USING  latin1) AS BINARY)) <> length(CONVERT(cast(CONVERT(localita USING  latin1) AS BINARY) USING utf8));
