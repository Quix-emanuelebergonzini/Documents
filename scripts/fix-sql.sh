#!/bin/bash

# Configura la directory di lavoro e la regex per filtrare i file
DIR="db"
REGEX="^db_[0-9]{6}:[0-9]{14}_[0-9]{1}\.sql\.gz$"
SED_COMMAND="s/INSERT INTO/REPLACE INTO/g"

# Controlla se la directory esiste
if [[ ! -d "$DIR" ]]; then
    echo "Errore: la directory $DIR non esiste."
    exit 1
fi

cd "$DIR"

# Itera sui file .sql.gz che corrispondono alla regex
for FILE in *.sql.gz; do
    BASENAME=$(basename "$FILE")
    # Verifica se il file corrisponde alla regex
    if [[ "$BASENAME" =~ $REGEX ]]; then
        echo "Elaborazione del file: $FILE"

        # Decomprime il file
        cp "$FILE" "${FILE}.backup"
        gzip -d "$FILE" || { echo "Errore durante la decompressione di $FILE"; exit 1; }

        # Nome del file senza .gz
        SQL_FILE="${FILE%.gz}"

        # Modifica il file con sed
        sed -i".old" "$SED_COMMAND" "$SQL_FILE" || { echo "Errore durante la modifica di $SQL_FILE"; exit 1; }

        # Ricomprime il file
        gzip "$SQL_FILE" || { echo "Errore durante la ricompressione di $SQL_FILE"; exit 1; }
        rm "${FILE}.backup"
        rm "${SQL_FILE}.old"

        echo "Modifica completata per: $FILE"
    fi
done

echo "Operazione completata!"
