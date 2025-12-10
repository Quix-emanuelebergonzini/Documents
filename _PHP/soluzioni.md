Per esportare i dati da WordPress come un file CSV tramite il frontend, puoi utilizzare una combinazione di PHP e una funzione personalizzata. Qui ti mostro un esempio di come potresti farlo:

1. **Crea una funzione per generare il CSV**: Questa funzione raccoglie i dati che vuoi esportare (come post, utenti, o altro) e li restituisce in formato CSV.

2. **Aggiungi il codice nel tema o in un plugin personalizzato**: Inserisci la logica di esportazione in modo che venga eseguita quando un utente interagisce con una pagina o un link.

### Ecco un esempio di come fare:

#### 1. Aggiungi la funzione PHP per generare il CSV

Nel tuo `functions.php` (o in un plugin personalizzato), aggiungi questa funzione per generare il file CSV:

```php
function esporta_csv_frontend() {
    // Verifica che l'utente sia autenticato, se necessario
    if ( ! is_user_logged_in() ) {
        wp_die( 'Devi essere loggato per esportare i dati.' );
    }

    // Imposta l'header per il download del file CSV
    header('Content-Type: text/csv');
    header('Content-Disposition: attachment; filename="esportazione.csv"');

    // Apri un file CSV in modalità di scrittura
    $output = fopen('php://output', 'w');

    // Aggiungi le intestazioni del CSV (modifica in base ai dati che vuoi esportare)
    fputcsv($output, array('ID', 'Titolo', 'Data Pubblicazione'));

    // Ottieni i dati (ad esempio, i post pubblicati)
    $args = array(
        'post_type' => 'post',
        'posts_per_page' => -1, // Esporta tutti i post
        'post_status' => 'publish',
    );
    $query = new WP_Query( $args );

    // Cicla sui post e aggiungi una riga per ogni post nel CSV
    if ( $query->have_posts() ) {
        while ( $query->have_posts() ) {
            $query->the_post();
            fputcsv($output, array(
                get_the_ID(),
                get_the_title(),
                get_the_date('Y-m-d H:i:s'),
            ));
        }
    }

    // Chiudi il file CSV
    fclose($output);

    // Ferma l'esecuzione per evitare altri output
    exit();
}
```

#### 2. Crea un link per attivare l'esportazione

Puoi aggiungere un link nella tua pagina frontend (ad esempio in un template o in un shortcode) per attivare l'esportazione del CSV. Ecco come farlo:

```php
function crea_link_esportazione() {
    // Link per scaricare il CSV
    $url = add_query_arg( 'esporta_csv', 'true', home_url() );
    return '<a href="' . esc_url( $url ) . '">Esporta dati in CSV</a>';
}

// Usa il codice sopra dove vuoi visualizzare il link
echo crea_link_esportazione();
```

#### 3. Gestire il parametro `esporta_csv`

Nel file `functions.php`, aggiungi questo codice per verificare se il parametro `esporta_csv` è presente nell'URL e, in tal caso, eseguire la funzione di esportazione:

```php
function controlla_esportazione_csv() {
    if ( isset( $_GET['esporta_csv'] ) && $_GET['esporta_csv'] === 'true' ) {
        esporta_csv_frontend(); // Chiama la funzione per generare il CSV
    }
}
add_action( 'template_redirect', 'controlla_esportazione_csv' );
```

#### Cosa fa questo codice:

1. Crea una funzione `esporta_csv_frontend()` che raccoglie i dati (ad esempio, i post pubblicati) e li esporta come file CSV.
2. Fornisce un link nel frontend che, quando cliccato, avvia il processo di esportazione.
3. Verifica, tramite l'azione `template_redirect`, se il parametro `esporta_csv=true` è presente nell'URL. Se lo è, invoca la funzione di esportazione CSV.

### Testa il codice

1. Aggiungi il codice al tuo `functions.php` o in un plugin personalizzato.
2. Crea una pagina dove visualizzi il link per l'esportazione.
3. Quando un utente clicca sul link, il file CSV verrà scaricato automaticamente con i dati che hai specificato.

### Personalizzazione

- Puoi personalizzare la query per ottenere altri dati (come utenti, commenti, prodotti, ecc.).
- Modifica le intestazioni del CSV (`fputcsv`) per includere più o meno informazioni, a seconda di cosa ti serve esportare.

=== 

Hai ragione a essere preoccupato per la performance quando esporti tutti gli ordini senza limiti temporali, specialmente se il tuo negozio ha molti ordini. Una query che recupera tutti gli ordini senza filtri può causare un notevole impatto sulle prestazioni, quindi è importante gestire correttamente la situazione.

### Strategie per gestire l'esportazione degli ordini in modo efficiente:

1. **Utilizzare la paginazione**: Invece di cercare tutti gli ordini in un'unica query, puoi utilizzare la paginazione per eseguire più query più piccole,
2. recuperando un numero limitato di ordini alla volta. Questo riduce l'overhead di memoria e migliora la performance.

2. **Esegui l'esportazione in background**: Un'altra opzione è spostare il processo di esportazione su un sistema asincrono (ad esempio, un job in background)
3. per evitare di sovraccaricare il server con una lunga operazione di esportazione in tempo reale.

3. **Ridurre il numero di dati**: Limita i dati esportati a solo quelli strettamente necessari, per esempio includendo solo le informazioni essenziali sugli ordini,
4. come l'ID dell'ordine, lo stato, il totale e la data di creazione.

### Ecco un esempio di come implementare l'esportazione con **paginazione** per evitare carichi pesanti:

#### 1. Modifica della funzione per gestire la paginazione:

Puoi suddividere il processo di esportazione in più "lotti" recuperando un numero limitato di ordini per volta, ad esempio 100 ordini per query.

```php
function esporta_ordini_csv() {
    // Verifica che l'utente sia autenticato, se necessario
    if ( ! is_user_logged_in() ) {
        wp_die( 'Devi essere loggato per esportare i dati.' );
    }

    // Imposta l'header per il download del file CSV
    header('Content-Type: text/csv');
    header('Content-Disposition: attachment; filename="ordini.csv"');

    // Apri un file CSV in modalità di scrittura
    $output = fopen('php://output', 'w');

    // Aggiungi le intestazioni del CSV
    fputcsv($output, array('ID Ordine', 'Cliente', 'Totale', 'Data Ordine', 'Stato'));

    // Imposta il numero di ordini per "pagina"
    $per_page = 100;
    $paged = 1; // Iniziamo dalla prima pagina

    // Iniziamo a recuperare gli ordini a partire dal primo "lotto"
    while ( true ) {
        // Ottieni gli ordini con la paginazione
        $args = array(
            'post_type' => 'shop_order',
            'posts_per_page' => $per_page,
            'paged' => $paged,
            'post_status' => 'any', // Ottieni tutti gli ordini (puoi specificare uno stato particolare se necessario)
        );

        $query = new WP_Query( $args );

        // Se non ci sono più ordini, termina il ciclo
        if ( ! $query->have_posts() ) {
            break;
        }

        // Cicla attraverso gli ordini e aggiungi le righe nel CSV
        while ( $query->have_posts() ) {
            $query->the_post();
            $order_id = get_the_ID();
            $order = wc_get_order( $order_id );

            fputcsv($output, array(
                $order_id,
                $order->get_billing_first_name() . ' ' . $order->get_billing_last_name(),
                $order->get_total(),
                $order->get_date_created()->date('Y-m-d H:i:s'),
                $order->get_status(),
            ));
        }

        // Aumenta la pagina per la successiva iterazione
        $paged++;
    }

    // Chiudi il file CSV
    fclose($output);

    // Ferma l'esecuzione per evitare altri output
    exit();
}
```

#### 2. Gestione del link per attivare l'esportazione

Il link per attivare l'esportazione rimane invariato, ma il processo di esportazione ora è gestito tramite la paginazione, quindi l'utente otterrà il CSV in più passaggi, se necessario.

```php
function crea_link_esportazione_ordini() {
    $url = add_query_arg( 'esporta_ordini', 'true', home_url() );
    return '<a href="' . esc_url( $url ) . '">Esporta Ordini in CSV</a>';
}

echo crea_link_esportazione_ordini();
```

#### 3. Gestione del parametro `esporta_ordini`

Nel file `functions.php`, aggiungi un codice simile per gestire la richiesta di esportazione tramite URL:

```php
function controlla_esportazione_ordini() {
    if ( isset( $_GET['esporta_ordini'] ) && $_GET['esporta_ordini'] === 'true' ) {
        esporta_ordini_csv(); // Chiama la funzione per generare il CSV
    }
}
add_action( 'template_redirect', 'controlla_esportazione_ordini' );
```

### Spiegazione:

1. **Paginazione**: La query viene eseguita su "lotti" di ordini limitati (`$per_page`), e si prosegue con il caricamento dei successivi ordini finché non ce ne sono più da recuperare.
2. **Impatto sulle prestazioni**: Poiché ogni query recupera solo una parte degli ordini, l'impatto sulle prestazioni è ridotto.
3. **Dati essenziali**: Per evitare di esportare troppi dati, vengono inclusi solo gli elementi più importanti (ID ordine, cliente, totale, stato, e data di creazione).
4. **Controllo di accesso**: Puoi aggiungere controlli di accesso (ad esempio, solo per amministratori o utenti specifici) se necessario.

### Opzione 2: Esecuzione in Background

Se hai una grande quantità di ordini, un'altra opzione è spostare il processo di esportazione in un sistema asincrono, come una coda di lavoro. In questo caso, potresti voler utilizzare un plugin come [WP Crontrol](https://wordpress.org/plugins/wp-crontrol/) o [WP Queue](https://github.com/michaeluno/wp-queue) per gestire i lavori in background.

Con questa soluzione, puoi evitare che l'utente debba aspettare a lungo per il completamento del processo di esportazione, migliorando l'esperienza dell'utente.

=== 