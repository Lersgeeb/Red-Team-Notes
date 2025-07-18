# Simple CTF

## Detalles Maquina
- 2 Puertos abiertos, uno ssh en el puerto 2222 y otros http en el puerto 80
- Se encontró una ruta oculta `/simple`
- La ruta oculta contenía una plataforma web no actualizada 
- Haciendo uso de `searchsploit` se encontró una vulnerabilidad y un exploit
- El exploit nos brinda un usuario y contraseña que se puede usar para conectarse mediante SSH
- Se averigua que el usuario puede hacer ejecutar Vim sin requerir permisos de superusuario
- Se usa Vim para ejecutar la escalación de privilegio


## Comandos usados

Buscar vulnerabilidades del servicio/software/etc
> `searchsploit <BÚSQUEDA>`

Obtener mas informacion del Exploit
> `searchsploit x <EXPLOIT>`

Muestra la ruta del Exploit
> `searchsploit x <EXPLOIT>`

Usar vim para obtener privilegios de root
> `sudo vim -c ':!/bin/sh'`


