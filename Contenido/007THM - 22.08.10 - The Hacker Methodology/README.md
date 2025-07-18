# Pentest 
> Información  obtenida de [The Hacker Methodology](https://tryhackme.com/room/hackermethodology)

**El Proceso que siguen los pentesters se resume en los siguientes pasos:**
- Reconocimiento 
- Enumeración/Escaneo 
- Explotación (Ganando acceso)
- Escalada de privilegios 
- cubriendo pistas 
- Informes


## Reconocimiento
- La primera fase de la Metodología Ethical Hacker es Reconocimiento. 
- El reconocimiento se trata de recopilar información sobre su objetivo. En términos generales, el reconocimiento generalmente no implica interacción con los objetivos o sistemas.

**Herrammientas para reconocimiento**
- Google (Especialmente Google Dorking)
- Wikipedia
- PeopleFinder.com
- who.is
- sublist3r
- hunter.io
- builtwith.com
- wappalyzer

## Enumeración/Escaneo
- La segunda fase de la Metodología Hacker es el Escaneo y Enumeración. 
- Aquí es donde un pirata informático comenzará a interactuar (escanear y enumerar) el objetivo para intentar encontrar vulnerabilidades relacionadas con el objetivo.
- El atacante está interactuando con el objetivo para determinar su **superficie de ataque** general.

**Herrammientas para enumeración/escaneo**
- **nmap:** Escaneo de puertos abiertos, servicios y sistema operativo
- **dirb/dirbuster:** se utiliza para encontrar directorios con nombres comunes en un sitio web
- **metasploit:** esta herramienta se usa principalmente para la explotación, pero también tiene algunas herramientas de enumeración integradas
- **enum4linux:** herramienta utilizada específicamente para Linux para encontrar vulnerabilidades
- **Burp Suite:** esta herramienta se puede usar para escanear un sitio web en busca de subdirectorios e interceptar el tráfico de red.
- **exploit-db**

## Explotación
La fase de explotación solo puede ser tan buena como las fases de reconocimiento y enumeración anteriores, si no enumeró todas las vulnerabilidades, puede perder una oportunidad, o si no se fijó lo suficiente en el objetivo: la explotación que ha elegido puede fallar por completo.

**Herrammientas para Explotación**
- Metasploit: tiene muchos scripts incorporados para tratar de simplificar la vida
- Burp Suite
- SQLMap
- msfvenom (for building custom payloads)
- BeEF (browser-based exploitation)

## Escalada de privilegios 
- Una vez que hayamos obtenido acceso a una máquina víctima a través de la fase de explotación, el siguiente paso es escalar los privilegios a una cuenta de usuario superior.
- Una vez que obtengamos acceso como usuario de nivel inferior, intentaremos ejecutar otro exploit o encontrar una manera de convertirnos en root o administrador.

**Objetivos frecuentes**
- En el mundo de Windows, la cuenta de destino suele ser: Administrador o Sistema. 
- En el mundo Linux, la cuenta de destino suele ser: root

**Acciones que se suelen hacer**
- Descifrado de hashes de contraseña encontrados en el objetivo 
- Encontrar un servicio vulnerable o una versión de un servicio que le permitirá escalar privilegios A TRAVÉS del servicio 
- Rociado de contraseñas de credenciales previamente descubiertas (reutilización de contraseñas) 
- Uso de credenciales predeterminadas 
- Encontrar claves secretas o claves SSH almacenadas en un dispositivo que permitirá pasar a otra máquina 
- Ejecutar scripts o comandos para enumerar configuraciones del sistema como 'ifconfig' para encontrar configuraciones de red, o el comando 'find / -perm -4000 -type f 2>/dev/null' para ver si el usuario tiene acceso a cualquier comando que pueda ejecutar como root

## Cubriendo pistas
- La mayoría de los probadores de penetración profesionales/éticos nunca tienen la necesidad de "cubrir sus huellas". Sin embargo, esto es todavía una fase en la metodología.

- Dado que las reglas de compromiso para una prueba de penetración deben acordarse antes de que se realice la prueba, el probador de penetración debe detenerse INMEDIATAMENTE cuando haya logrado la escalada de privilegios e informar el hallazgo al cliente.

## Informes
Esta es una de las fases más importantes donde describirás todo lo que encontraste.

La fase de presentación de informes a menudo incluye las siguientes cosas: 
- Los Hallazgos o Vulnerabilidades 
- La CRITICIDAD del Hallazgo 
- Una descripción o breve resumen de cómo se descubrió el hallazgo. 
- Recomendaciones de remediación para resolver el hallazgo