come generare gpg
emanuele.bergonzini@MacBook-Pro-24-22 ~ % gpg2 --list-secret-keys
[keyboxd]
---------
sec   ed25519 2024-12-16 [SC] [expires: 2027-12-16]
      77FFD3202C35F2E53D11FB8552ED3E6BB9D49C75
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   cv25519 2024-12-16 [E] [expires: 2027-12-16]

emanuelebergonzini@MBP-di-Emanuele ~ % gpg2 --gen-key
gpg (GnuPG/MacGPG2) 2.2.20; Copyright (C) 2020 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

GnuPG needs to construct a user ID to identify your key.

Real name: Emanuele Bergonzini
Email address: emanuele.bergonzini@quix.it
You selected this USER-ID:
    "Emanuele Bergonzini <emanuele.bergonzini@quix.it>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.

--- decidere una nuova pwd: ein%59q12

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key AC254809F53F638B marked as ultimately trusted
gpg: revocation certificate stored as '/Users/emanuelebergonzini/.gnupg/openpgp-revocs.d/A0EDFD28C251701B57FDD516AC254809F53F638B.rev'
public and secret key created and signed.

sec   rsa3072 2024-08-16 [SC] [expires: 2026-08-16]
      E9E146ECE74532EB48AD6364C87C0A9A6E827113
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   rsa3072 2024-08-16 [E] [expires: 2026-08-16]

emanuelebergonzini@MBP-di-Emanuele ~ % gpg2 --armor --export E9E146ECE74532EB48AD6364C87C0A9A6E827113
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=L598
-----END PGP PUBLIC KEY BLOCK-----

QUESTA CHIAVE BISOGNA COPIARLA DA ---BEGIN A BLOCK--- e poi andare su 
git.mmfg.it (bitbucket) - manage account - GPG keys - add new e incollare nel box


emanuelebergonzini@MBP-di-Emanuele ~ % gpg2 --list-secret-keys
/Users/emanuelebergonzini/.gnupg/pubring.gpg
--------------------------------------------
sec   rsa2048 2021-03-04 [SC] [expired: 2023-03-04]
      A0EDFD28C251701B57FDD516AC254809F53F638B
uid           [ expired] Emanuele Bergonzini <emanuele.bergonzini@quix.it>

sec   rsa3072 2023-02-08 [SC] [expires: 2025-02-07]
      11EE95112343FFBEBD7842FEBE0E77FC826CB6F1
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   rsa3072 2023-02-08 [E] [expires: 2025-02-07]

sec   rsa3072 2024-08-16 [SC] [expires: 2026-08-16]
      E9E146ECE74532EB48AD6364C87C0A9A6E827113
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   rsa3072 2024-08-16 [E] [expires: 2026-08-16]





Ciao, vi lascio questa cosa da segnarvi che potrebbe essere utile prima o poi.
Ieri sera alle 17 mi è scaduta la chiave GPG ... GigaMadonne perchè non potevo più committare.
La procedura per il rinnovo è questa

OTTENERE LISTA DELLE CHIAVI da cui pesco l'ID:
gpg2 --list-secret-keys       
sec   rsa2048/BDEA3E534FBD4996 2020-05-28 [SC] [scaduto: 2024-05-29]
      C94BECDC286B20DDC8E8CB31BDEA3E534FBD4996
uid                 [ scaduto] Massimo Carmagnola <massimo.carmagnola@quix.it>


DUE COMANDI PER IL RINNOVO UNO PER LA CHIAVE E UNO PER LE SOTTOCHIAVI (10y aggiunge 10 anni):
gpg2 --quick-set-expire C94BECDC286B20DDC8E8CB31BDEA3E534FBD4996 10y
gpg2 --quick-set-expire C94BECDC286B20DDC8E8CB31BDEA3E534FBD4996 10y '*'




---------
Git Commit Freeze Due to GPG Lock Issues
If you encounter a problem where you cannot commit changes in Git – neither through the terminal nor via the GitHub Desktop application – the issue might be a freeze during the Git commit process. This is often caused by GPG lock issues. Below is a concise and step-by-step guide to resolve this problem.

Solution Steps
1. Check for GPG Lock Messages
Open your terminal and try to perform a GPG operation (like signing a test message). If you see repeated messages like gpg: waiting for lock (held by [process_id]) ..., it indicates a lock issue.

For example:

❯ echo "test" | gpg --clearsign

gpg: waiting for lock (held by 3571) ...
gpg: waiting for lock (held by 3571) ...
gpg: waiting for lock (held by 3571) ...
2. Locate and Remove Stale Lock Files
List Lock Files:

For Linux:

ls -l ~/.gnupg/*.lock
For MacOS (Darwin):

ls -l ~/.gnupg/**/*.lock
This command lists all lockfiles in ~/.gnupg and its subdirectories without manual exploration.

Remove the Identified Stale Lock Files:

For general lock files:

rm ~/.gnupg/[name-of-the-stale-lock-file].lock
For Linux systems, if the above doesn't work, try removing the public keys database lock:

rm -f ~/.gnupg/public-keys.d/pubring.db.lock
image

3. Restart GPG-Agent
After removing any stale lock files, it's important to reset the state of the GPG agent.

Command to Restart GPG-Agent:

gpgconf --reload gpg-agent
4. Test GPG Operations
To confirm if the issue is with GPG itself, try signing a simple test message:

Run:

echo "test" | gpg --clearsign
5. Retry Committing in Git
With the GPG lock issue resolved, try committing your changes again in Git.