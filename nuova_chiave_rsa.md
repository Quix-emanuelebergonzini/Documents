MacBook-Pro-24-22:.ssh emanuele.bergonzini$ ls
known_hosts
MacBook-Pro-24-22:.ssh emanuele.bergonzini$ vi config
MacBook-Pro-24-22:.ssh emanuele.bergonzini$ cd ..
MacBook-Pro-24-22:~ emanuele.bergonzini$ vi .zsh_rc_emanuele.bergonzini
MacBook-Pro-24-22:~ emanuele.bergonzini$ vi .zshrc
MacBook-Pro-24-22:~ emanuele.bergonzini$ ssh-keygen -t rsa -f ~/.ssh/id_rsa
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/emanuele.bergonzini/.ssh/id_rsa
Your public key has been saved in /Users/emanuele.bergonzini/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:E+RQ4fF4sfVGHXmTDST9NMqtwl0NNr1NNCf90s/nS6E emanuele.bergonzini@MacBook-Pro-24-22.local
The key's randomart image is:
+---[RSA 3072]----+
|      ..=.. oo=OB|
....
+----[SHA256]-----+
MacBook-Pro-24-22:~ emanuele.bergonzini$ cat ~/.ssh/id_rsa.pub
stampa la chiave pubblica