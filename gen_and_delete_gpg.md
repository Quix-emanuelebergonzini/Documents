MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg --full-generate-key
gpg (GnuPG) 2.4.7; Copyright (C) 2024 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
   (9) ECC (sign and encrypt) *default*
  (10) ECC (sign only)
  (14) Existing key from card
Your selection? 
Please select which elliptic curve you want:
   (1) Curve 25519 *default*
   (4) NIST P-384
   (6) Brainpool P-256
Your selection? 
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: Emanuele Bergonzini
Email address: emanuele.bergonzini@quix.it
Comment: 
You selected this USER-ID:
    "Emanuele Bergonzini <emanuele.bergonzini@quix.it>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
....
public and secret key created and signed.

pub   ed25519 2024-12-13 [SC]
      15695....
uid                      Emanuele Bergonzini <emanuele.bergonzini@quix.it>
sub   cv25519 2024-12-13 [E]

MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg --armor --export 15695....
-----BEGIN PGP PUBLIC KEY BLOCK-----
....
-----END PGP PUBLIC KEY BLOCK-----
MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg2 --gen-key gpg
gpg (GnuPG) 2.4.7; Copyright (C) 2024 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

usage: gpg [options] --generate-key
MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg2 --list-secret-keys
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   2  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 2u
[keyboxd]
---------
sec   ed25519 2024-12-13 [SC]
      15695....
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   cv25519 2024-12-13 [E]

sec   rsa3072 2024-12-13 [SC]
      DCDB171.....
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonznini@quix.it>
ssb   rsa3072 2024-12-13 [E]

MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg2 --gen-key
gpg (GnuPG) 2.4.7; Copyright (C) 2024 g10 Code GmbH
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
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: revocation certificate stored as '/Users/emanuele.bergonzini/.gnupg/openpgp-revocs.d/XXXX.rev'
public and secret key created and signed.

pub   ed25519 2024-12-13 [SC] [expires: 2027-12-13]
      0F3C53D....
uid                      Emanuele Bergonzini <emanuele.bergonzini@quix.it>
sub   cv25519 2024-12-13 [E] [expires: 2027-12-13]

MacBook-Pro-24-22:~ emanuele.bergonzini$ git config --global gpg.program gpg2
MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg2 --list-secret-keys
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   3  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 3u
gpg: next trustdb check due at 2027-12-13
[keyboxd]
---------
sec   ed25519 2024-12-13 [SC] [expires: 2027-12-13]
      0F3C53D...
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   cv25519 2024-12-13 [E] [expires: 2027-12-13]

sec   ed25519 2024-12-13 [SC]
      15695....
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   cv25519 2024-12-13 [E]

sec   rsa3072 2024-12-13 [SC]
      DCDB171....
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonznini@quix.it>
ssb   rsa3072 2024-12-13 [E]

MacBook-Pro-24-22:~ emanuele.bergonzini$ git config --global user.signingkey 0F3C53D...
MacBook-Pro-24-22:~ emanuele.bergonzini$ git config --global commit.gpgsign true
MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg2 --armor --export 0F3C53D....
-----BEGIN PGP PUBLIC KEY BLOCK-----
....
-----END PGP PUBLIC KEY BLOCK-----
MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg --delete-secret-key 15695....
gpg (GnuPG) 2.4.7; Copyright (C) 2024 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


sec  ed25519/358614.... 2024-12-13 Emanuele Bergonzini <emanuele.bergonzini@quix.it>

Delete this key from the keyring? (y/N) y
This is a secret key! - really delete? (y/N) y
MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg2 --list-secret-keys
[keyboxd]
---------
sec   ed25519 2024-12-13 [SC] [expires: 2027-12-13]
      0F3C53D....
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   cv25519 2024-12-13 [E] [expires: 2027-12-13]

sec   rsa3072 2024-12-13 [SC]
      DCDB171E.....
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonznini@quix.it>
ssb   rsa3072 2024-12-13 [E]

MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg --delete-secret-key DCDB171E....
gpg (GnuPG) 2.4.7; Copyright (C) 2024 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


sec  rsa3072/9B342..... 2024-12-13 Emanuele Bergonzini <emanuele.bergonznini@quix.it>

Delete this key from the keyring? (y/N) y
This is a secret key! - really delete? (y/N) y

MacBook-Pro-24-22:~ emanuele.bergonzini$ gpg2 --list-secret-keys
[keyboxd]
---------
sec   ed25519 2024-12-13 [SC] [expires: 2027-12-13]
      0F3C53D....
uid           [ultimate] Emanuele Bergonzini <emanuele.bergonzini@quix.it>
ssb   cv25519 2024-12-13 [E] [expires: 2027-12-13]
