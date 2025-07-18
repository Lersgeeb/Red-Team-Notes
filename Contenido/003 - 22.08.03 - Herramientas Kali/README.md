## Herramientas de Kali Linux
---

### Nmap
Es una utilidad para el descubrimiento de red y auditoría de seguridad. Nmap provee información acerca de que puertos, protocolos, servicios y el estado de estos para una o mas direcciones IP.

También ofrece opciones adicionales como obtención de Sistema Operativo, tipo de dispositivos, Direcciones MAC y detección de vulnerabilidades.

**Nmap Scripting Engine (NSE):** Permite a los usuarios escribir (y compartir) scripts simples (utilizando el lenguaje de programación Lua) para automatizar una amplia variedad de tareas de red.

**Parámetros útiles**
> **"-T paranoid|sneaky|polite|normal|aggressive|insane"** :  Forma de operar

> **"-sV"** : Sondear puertos abiertos para determinar la información de servicio o versión

> **"-O"** : Sistemas operativo

> **"-v"** : verbosity

> **"-p"** : define el puerto

**Scripts Nmap**

Se encuentran en la siguiente dirección

> /usr/share/nmap/scripts

Se pueden usar de la siguiente forma:
> nmap -sV -p80 -script http-svn-enum.nse 192.168.0.20

> nmap -sV -p80 -script "http-vuln-*" 192.168.0.20


## Otras herramientas de Kali Linux
- Metasploit (Explotation) 
- OWASP ZAP: Herramienta de auditoria que busca encontrar la mayor cantidad de vulnerabilidades de un sitio. (Reconocimiento, Análisis de vulnerabilidades y Explotación).
- HYDRA: Es utilizada para crackear contraseñas (Explotación)
- Maltego: Es una herramienta para encontrar y organizar información de manera gráfica sobre una entidad basándose en servidores THS (Reconocimiento)
- SQLmap: Es una herramienta de inyección SQL, Maneja los mas famosos gestores de base de datos, y tiene soporte para explotar HASHES de contraseñas. (Explotación)
