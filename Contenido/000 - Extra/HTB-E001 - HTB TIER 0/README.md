# MAQUINAS DE TIER0 

**Contendio**
- [Primer Maquina](#Primer-Maquina)
- [Segunda Máquina](#Segunda-Máquina)
- [Tercera Máquina](#Tercera-Máquina)
- [Cuarta Máquina](#Cuarta-Máquina)
- [Quinta Máquina](#Quinta-Máquina)
- [Sexta Máquina](#Sexta-Máquina)

## Primer Maquina
El objetivo de la maquina consiste en dar la introducción a la **dinámica de la plataforma**, donde primero se explicara como conectar con el equipo para luego poder vulnerarlo.

**Tareas realizadas**

- Conexión con la maquina mediante OpenVPN 
- Escaneo de puertos abiertos haciendo uso de Nmap
- Analizar el servicio encontrado y evaluar vectores de ataques
- Explotación simple del servicio de Telnet (Puerto 23) mediante credenciales por defecto.
- Completar las preguntas teóricas de las maquinas.

**Comandos usados**

Para la conexión con el vpn:
> `sudo openvpn <NombreArchivo>.ovpn`

Para el escaneo de puertos abiertos:
> `nmap -sV <IP>`

Para acceder al Telnet:
> `Telnet <IP>`

## Segunda Máquina
El objetivo de la maquina consiste en atacar la vulnerabilidad que contiene un equipo que hace uso de un **servicio FTP**. Muchas veces estos servicios son mal configurados provocando que los archivos del sistema sean fácilmente accesibles.

**Tareas realizadas**

- Escaneo de puertos abiertos haciendo uso de Nmap.
- Analizar el servicio encontrado y evaluar vectores de ataques, en este caso sera con el servicio de FTP (Puerto 21). 
- Explotar el servicio FTP gracias a las **Malas configuraciones**, los cuales permiten acceder con un usuario por defecto denominado *"anonymous"*.
- Capturar la Bandera
- Completar las preguntas teóricas de las maquinas.

**Comandos usados**

Para el escaneo de puertos abiertos:
> `nmap -sV <IP>`

Para acceder al servidor FTP:
> `ftp <IP>`

Para Acceder poner el siguiente usuario y dejar la contraseña en blanco:
> `anonymous`

Para obtener la bandera:
> `get <nombreArchivo>`

## Tercera Máquina
El objetivo de la maquina consiste en atacar la vulnerabilidad que contiene un equipo que hace uso de un **servicio de SMB** (Server Message Block). De la misma forma que la anterior maquina, los servicios SMB suelen ser mal configurados provocando que los archivos sean fácilmente accesibles para su modificación, lectura o incluso eliminación.

**Mas información del Protocolo**

Este protocolo de comunicación proporciona acceso compartido a archivos, impresoras y puertos serie entre puntos finales de una red. En su mayoría, vemos servicios SMB que se ejecutan en máquinas con Windows.


**Tareas realizadas**

- Escaneo de puertos abiertos haciendo uso de Nmap.
- Analizar el servicio encontrado y evaluar vectores de ataques, en este caso sera con el servicio de SMB (Puerto 445). 
- Identificar los distintos Shares que existen en el servicio.
- Explotar el servicio SMB gracias a las **Malas configuraciones**, El cual permite llevar a cabo autenticación en shares donde la contraseña no se encuentre configurada.
- Capturar información de seguridad de la maquina.
- Capturar la Bandera.
- Completar las preguntas teóricas de las maquinas.

**Comandos usados**

Para obtener los shares disponibles:

> `smbclient -L=<HOST>`

Para proceder a la autenticación de un determinado Share:

> `smbclient //<HOST>/<SHARE>`

Para obtener archivos contenidos en el Share:

> `get <nombreArchivo>`

## Cuarta Máquina
El objetivo de la maquina consiste en atacar la vulnerabilidad que contiene un equipo que hace uso de un **servicio de Redis** (Remote Dictionary Server). Redis es un almacén de datos de Clave-Valor en memoria, y muchas de sus  tareas consisten en servir como base de datos o cache de datos que necesitan un rápido acceso. De la misma forma que la anterior máquina, los servicios de Redis suelen ser mal configurados provocando que los datos sean fácilmente accesibles.


**Tareas realizadas**

- Escaneo de puertos abiertos haciendo uso de Nmap.
- Analizar el servicio encontrado y evaluar vectores de ataques, en este caso sera con el servicio de Redis (Puerto 6379). 
- Explotar el servicio redis gracias a las **Malas configuraciones**, El cual permite acceder a la base de datos sin autenticación con redis-cli.
- Obtener información de la base de datos
- Capturar la Bandera.
- Completar las preguntas teóricas de las maquinas.

**Comandos usados**

Para acceder remotamente a la base de datos:

> `redis-cli -h <HOST>`

Obtener información de la base de datos: (Dentro de redis)

> `info`

Seleccionar Base de datos: (Dentro de redis)

> `select <Identificador Lógico>`

Listar todas las llaves: (Dentro de redis)

> `keys *`

Obtener información de la llave: (Dentro de redis)

> `get <key>`

## Quinta Máquina
El objetivo de la maquina consiste en atacar la vulnerabilidad que contiene un equipo que hace uso de un **servicio de RDP** (Remote Desktop Protocol). De la misma forma que las anteriores máquinas, los servicios de RDP suelen ser mal configurados provocando que los datos sean fácilmente accesibles.


**Tareas realizadas**

- Escaneo de puertos abiertos haciendo uso de Nmap.
- Analizar el servicio encontrado y evaluar vectores de ataques, en este caso sera con el servicio de RDP (Puerto 3389). 
- Explotar el servicio de RDP gracias a las **Malas configuraciones**, El cual permite acceder al computador remoto saltándose los certificados con xfreerdp.
- Acceder con el usuario "Administrator" y dejar la contraseña en blanco
- Leer la Bandera.
- Completar las preguntas teóricas de las maquinas.

**Comandos usados**

Para acceder a la maquina remota:

> `xfreerdp /cert:ignore /u:<USER> /v:<IP>`

## Sexta Máquina
El objetivo de la maquina consiste en atacar la vulnerabilidad que contiene un equipo que hace uso de un **servicio de HTTP**. este tipo de servicio es usado para brindar servicios web, por lo tanto es posible apoyarse en un navegador.

**Tareas realizadas**

- Escaneo de puertos abiertos haciendo uso de Nmap.
- Analizar el servicio encontrado y evaluar vectores de ataques, en este caso sera con el servicio de HTTP (Puerto 80). 
- Búsqueda de rutas ocultas con **gobuster**
- Acceder a la pagina oculta de admin.php, el cual presenta un inicio de sesión.
- Explotar la plataforma al hacer uso de Credenciales por defecto, en este caso se accederá con el usuario y contraseña "admin".
- Leer la Bandera.
- Completar las preguntas teóricas de las maquinas.

**Comandos usados**

Para obtener las rutas ocultas del servicio web:

> `sudo gobuster dir -w <DIR_DE_WORDLIST> -u <HOST>`


