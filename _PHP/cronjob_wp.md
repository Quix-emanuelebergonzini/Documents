Creare un job schedulato (cron job) in WordPress è una funzionalità utile per eseguire azioni a intervalli regolari
senza dover fare affidamento su cron job a livello di server. WordPress ha un sistema di **WP-Cron** integrato, che permette di pianificare l'esecuzione di funzioni personalizzate a intervalli specifici.

### Passi per creare un job schedulato in WordPress:

#### 1. Registrare un evento personalizzato

Per prima cosa, devi registrare un evento che WordPress eseguirà in base a una pianificazione. Puoi farlo con la funzione `wp_schedule_event()`, che si occupa di registrare l'evento cron.

#### 2. Creare la funzione che verrà eseguita

Devi anche definire la funzione che sarà eseguita dal job schedulato. Questa funzione può fare qualsiasi cosa, come inviare email, eseguire un'operazione su database, generare report, ecc.

#### 3. Gestire la cancellazione dell'evento (opzionale)

In alcuni casi, potresti voler cancellare il job quando non è più necessario, ad esempio se il job è legato a una condizione o evento specifico.

### Esempio di codice:

Aggiungi il seguente codice al file `functions.php` del tuo tema o in un plugin personalizzato:

#### 1. Registrazione dell'evento

In questo esempio, registreremo un evento che verrà eseguito ogni ora.

```php
// Funzione per registrare il cron job all'attivazione del tema o plugin
function attiva_job_schedulato() {
    // Verifica se l'evento è già stato pianificato
    if ( ! wp_next_scheduled( 'esegui_job_ogni_ora' ) ) {
        wp_schedule_event( time(), 'hourly', 'esegui_job_ogni_ora' );
    }
}
add_action( 'wp', 'attiva_job_schedulato' );
```

- `wp_schedule_event( time(), 'hourly', 'esegui_job_ogni_ora' );`
  - `time()` è il momento in cui il job sarà avviato per la prima volta.
  - `'hourly'` è l'intervallo per l'esecuzione (ci sono anche altre opzioni, come `'daily'`, `'twicedaily'`, e puoi anche definire intervalli personalizzati).
  - `'esegui_job_ogni_ora'` è il nome del nostro evento personalizzato.

#### 2. Definizione della funzione da eseguire

La funzione che vuoi eseguire quando il job cron viene attivato deve essere registrata. Aggiungiamo una funzione che esegue un'operazione, come ad esempio inviare una notifica o eseguire un'azione.

```php
// Funzione da eseguire quando il cron job viene attivato
function esegui_job_ogni_ora() {
    // Qui inserisci il codice che vuoi eseguire
    // Ad esempio, puoi generare un report o inviare un'email

    // Esempio di scrittura di un log
    error_log( 'Il cron job è stato eseguito alle ' . date( 'Y-m-d H:i:s' ) );
}

// Collega la funzione all'evento personalizzato
add_action( 'esegui_job_ogni_ora', 'esegui_job_ogni_ora' );
```

#### 3. Cancellazione dell'evento (opzionale)

Se non hai più bisogno del cron job, puoi cancellarlo usando `wp_clear_scheduled_hook()`. Ad esempio, se desideri fermare il job quando un utente disattiva un plugin o un tema, puoi usare il seguente codice:

```php
// Funzione per annullare il cron job alla disattivazione del plugin o tema
function disattiva_job_schedulato() {
    $timestamp = wp_next_scheduled( 'esegui_job_ogni_ora' );
    if ( $timestamp ) {
        wp_unschedule_event( $timestamp, 'esegui_job_ogni_ora' );
    }
}
add_action( 'switch_theme', 'disattiva_job_schedulato' ); // per temi
// Oppure usa add_action( 'deactivate_plugin', 'disattiva_job_schedulato' ); per plugin
```

### Personalizzare l'intervallo di tempo:

Se desideri definire un intervallo personalizzato, puoi farlo utilizzando il filtro `cron_schedules` per aggiungere un intervallo di tempo personalizzato. Ecco come aggiungere un intervallo di 15 minuti:

```php
function intervallo_personalizzato( $schedules ) {
    $schedules['every_fifteen_minutes'] = array(
        'interval' => 15 * 60, // 15 minuti in secondi
        'display'  => 'Ogni 15 minuti'
    );
    return $schedules;
}
add_filter( 'cron_schedules', 'intervallo_personalizzato' );

// Poi, usa questo intervallo nella pianificazione dell'evento
function attiva_job_schedulato() {
    if ( ! wp_next_scheduled( 'esegui_job_ogni_15_minuti' ) ) {
        wp_schedule_event( time(), 'every_fifteen_minutes', 'esegui_job_ogni_15_minuti' );
    }
}
add_action( 'wp', 'attiva_job_schedulato' );
```

### Esecuzione del Cron Job:

- **WP-Cron non è come un cron tradizionale**: WordPress esegue i cron job quando un utente visita il sito,
- quindi non verranno eseguiti se nessuno visita il sito. Se il sito ha poca attività,
- potresti voler configurare un cron job esterno a livello di server che richiama periodicamente l'URL `wp-cron.php`.
  
  Puoi configurare un cron job a livello di server per chiamare questo URL ogni pochi minuti per garantire che i cron job vengano eseguiti anche senza traffico sul sito:

  ```bash
  wget -q -O /dev/null http://tuosito.com/wp-cron.php?doing_wp_cron
  ```

  Questo invierà una richiesta al file `wp-cron.php` per eseguire i cron job pianificati.

### Conclusione:

- `wp_schedule_event()` è la funzione principale per registrare eventi cron in WordPress.
- Puoi personalizzare l'intervallo, definire funzioni da eseguire, e anche rimuovere i cron job quando non sono più necessari.
- WordPress cron non è un vero cron job di sistema, quindi assicurati che ci sia abbastanza traffico sul sito o usa un cron job esterno per garantirne l'esecuzione regolare.

=== 

Per eseguire un cron in WordPress senza dover visitare il sito, puoi utilizzare il **WP-Cron** di WordPress o configurare un cron job tramite il tuo server. Ecco come puoi farlo:

### 1. **Utilizzare WP-Cron di WordPress** (senza visitare manualmente il sito)
WordPress ha un sistema interno chiamato WP-Cron che simula l’esecuzione di cron jobs. Di solito, viene attivato quando una pagina del sito viene caricata, ma puoi configurarlo per eseguire cron job anche in modo regolare, senza visitare il sito.

#### Passaggi per attivare WP-Cron:
1. **Disabilita WP-Cron automatico (opzionale)**: Puoi disabilitare la funzionalità di WP-Cron che viene attivata ad ogni visita del sito aggiungendo una riga nel file `wp-config.php`. Questo ti permetterà di eseguire i cron job manualmente o tramite il cron del server.

   Aggiungi questa riga al file `wp-config.php` prima della riga `/* That's all, stop editing! Happy publishing. */`:

   ```php
   define('DISABLE_WP_CRON', true);
   ```

2. **Configura un cron job del server per WP-Cron**:
   Devi aggiungere un cron job al tuo server che esegua lo script WP-Cron a intervalli regolari. Per farlo, segui questi passaggi:

   - Accedi al tuo server (tramite SSH o tramite il pannello di controllo del tuo hosting).
   - Aggiungi un cron job con il comando `wget` o `curl` per eseguire WP-Cron regolarmente. Ecco un esempio di cron job che esegue WP-Cron ogni 15 minuti:

   ```bash
   */15 * * * * wget -q -O - https://www.tuosito.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
   ```

   Se usi `curl`, puoi fare così:

   ```bash
   */15 * * * * curl -s https://www.tuosito.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
   ```

   In questo esempio, il cron job viene eseguito ogni 15 minuti, ma puoi personalizzare l'intervallo come preferisci.

3. **Verifica il funzionamento**: Dopo aver configurato il cron job, WP-Cron verrà eseguito automaticamente senza la necessità di visitare il sito.

### 2. **Usare il cron job del server direttamente** (senza WP-Cron)
Se vuoi eseguire un cron job specifico e non vuoi che venga gestito da WordPress, puoi creare uno script PHP personalizzato per eseguire il cron senza passare attraverso WP-Cron. Questo richiede un po' più di configurazione manuale, ma ti dà maggiore controllo.

Ad esempio, puoi creare uno script PHP che esegue una funzione personalizzata e poi configurare un cron job sul server che esegue quello script.

```php
// esempio-script.php
<?php
require_once('/path/to/your/wordpress/wp-load.php');

// Esegui una funzione personalizzata o una query
do_action('my_custom_cron_function'); // Sostituisci con la tua funzione
?>
```

Poi aggiungi un cron job sul server per eseguire questo script PHP regolarmente.

Spero che queste informazioni ti siano utili! Se hai bisogno di ulteriori chiarimenti o aiuto con la configurazione, fammi sapere!