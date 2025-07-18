# Crack The hash

## Recursos útiles
- https://hashcat.net/wiki/doku.php?id=example_hashes
- https://www.tunnelsup.com/hash-analyzer/
- https://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats
- https://countuponsecurity.files.wordpress.com/2016/09/jtr-cheat-sheet.pdf


## Comandos usados

### John the Ripper

**Para MD5:**
> `john -w=/usr/share/wordlists/rockyou.txt hash.txt --format=raw-MD5`

**Para SHA1:**
> `john -w=/usr/share/wordlists/rockyou.txt hash.txt --format=raw-SHA1`

**Para SHA256:**
> `john -w=/usr/share/wordlists/rockyou.txt hash.txt --format=raw-sha256`

**Para Blowfish:**
> `john -w=/usr/share/wordlists/rockyou.txt hash.txt --format=bf`

**Establecer reglas:**
> `john -w=/usr/share/wordlists/rockyou.txt hash.txt --rules:<NOMBRE-REGLA> --format=raw-md4`

**Sin reglas:**
> `john -w=/usr/share/wordlists/rockyou.txt hash.txt --rules:: --format=raw-md4`

**Ver Hashes Previamente Procesoados:**
> `sudo cat /root/.john/john.pot`

### Hashcat

**Ejemplo con SALT:**

SALT: tryhackme

HASH: e5d8870e5bdd26602cab8dbe07a942c8669e56d6

Guardar el hash con el siguiente formato:
> `e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme`

**Comando:**
> `hashcat -m 160 hash.txt /usr/share/wordlists/rockyou.txt`





