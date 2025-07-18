# Instalación Nessus

Instalar paquete de nessus:
> `sudo dpkg -i package_file.deb`

Iniciar Servicio de Nessus:
> `sudo systemctl start nessusd`

Abrir el navegador para dirigirse al siguiente URL
> `https://localhost:8834/`

> `Usuario: gabriel`
> `PW: kali123`

# Reconocimiento Activo
El reconocimiento activo requiere que hagas algún tipo de contacto con tu objetivo. Este contacto puede ser una llamada telefónica o una visita a la empresa objetivo con el pretexto de recopilar más información, generalmente como parte de la ingeniería social. Alternativamente, puede ser una conexión directa al sistema de destino, ya sea visitando su sitio web o verificando si su firewall tiene un puerto SSH abierto.

Es esencial recordar no participar en trabajos de reconocimiento activo antes de obtener la autorización legal firmada por el cliente.

También es importante mencionar que no todas las conexiones son sospechosas. Es posible dejar que su reconocimiento activo aparezca como actividad regular del cliente. Considere la navegación web; nadie sospecharía que un navegador está conectado a un servidor web de destino entre cientos de otros usuarios legítimos.

## Herramientas útiles

### Navegador Web
Algunas extensiones que pueden ser usadas son las siguientes:

- **FoxyProxy:** permite cambiar rápidamente el servidor proxy que está utilizando para acceder al sitio web de destino.
- **User-Agent Switcher and Manager:** da la posibilidad de fingir que está accediendo a la página web desde un sistema operativo diferente o un navegador web diferente
- **Wappalyzer:** proporciona información sobre las tecnologías utilizadas en los sitios web visitados

### Ping 
Ping es un comando que envía un paquete ICMP Echo a un sistema remoto. Si el sistema remoto está en línea y el paquete de ping se enrutó correctamente y no lo bloqueó ningún firewall, el sistema remoto debe enviar una respuesta de echo ICMP. Del mismo modo, la respuesta al ping debería llegar al primer sistema si se enruta correctamente y no está bloqueada por ningún firewall.

**Algunos Parámetros**
> **-c:** cantidad de paquetes enviados

> **-s:** definir tamaño del paquete

### Traceroute
- El comando traceroute rastrea la ruta tomada por los paquetes desde su sistema a otro host.

- No existe una forma directa de descubrir la ruta desde su sistema hasta un sistema de destino. Confiamos en ICMP para "engañar" a los enrutadores para que revelen sus direcciones IP. Podemos lograr esto mediante el uso de un pequeño tiempo de vida (TTL) en el campo de encabezado de IP.

- TTL indica la cantidad máxima de enrutadores/saltos por los que puede pasar un paquete antes de descartarse.

**comando**
En linux:
> `traceroute <HOST>`

En windows:
> `tracert <HOST>`

### Telnet 
El cliente telnet, con su sencillez, puede utilizarse para otros fines. Sabiendo que el cliente telnet se basa en el protocolo TCP, puede usar Telnet para conectarse a cualquier servicio y obtener su banner.

**comando**
> `telnet <HOST> <PORT>`

En un servicio web se puede usar de la siguiente forma
`telnet <HOST> 80`
`GET / HTTP/1.1`

### Netcat
Netcat o simplemente `nc` tiene diferentes aplicaciones que pueden ser de gran valor para un pentester. Netcat es compatible con los protocolos TCP y UDP. Puede funcionar como un cliente que se conecta a un puerto de escucha; alternativamente, puede actuar como un servidor que escucha en un puerto de su elección.

**Parámetros útiles**
- **-l** : Modo de escucha
- **-p** : Especifique el número de puerto
- **-n** : Solo numérico; sin resolución de nombres de host a través de DNS
- **-v** : Activar Verbose
- **-vv** : Activar Very Verbose 
- **-k** : Seguir escuchando después de que el cliente se desconecte

**Comandos**
Netcat como cliente: `nc <HOST> PORT_NUMBER`
Netcat en server: `nc -lvnp PORT_NUMBER`


