# Metasploit

> Información  obtenida de [TryHackMe - Metasploit: Introduction](https://tryhackme.com/room/metasploitintro)


Metasploit es el marco de explotación más utilizado. Metasploit es una herramienta poderosa que puede respaldar todas las fases de un compromiso de prueba de penetración, desde la recopilación de información hasta la explotación posterior.

## Definiciones fundamentos de metasploit 

### Versiones
- **Metasploit Pro**: La versión comercial. Esta versión tiene una interfaz gráfica de usuario
- **Metasploit Framework**: versión de código abierto. Funciona desde la línea de comandos.

### Componentes
- **msfconsole**: la principal interfaz de línea de comandos.
- **Módulos**: módulos de soporte como exploits, escáneres, cargas útiles, etc.
- **Herramientas**: herramientas que ayudarán a la investigación de vulnerabilidades, la evaluación de vulnerabilidades o las pruebas de penetración.

### Conceptos importantes: 
- **Exploit**: Una pieza de código que utiliza una vulnerabilidad presente en el sistema de destino.
- **Vulnerability**: Una falla de diseño, codificación o lógica que afecta el sistema de destino
- **Payload**: Un `exploit` se aprovechará de una vulnerabilidad y después los `payloads` son el código que se ejecutará en el sistema de destino.

### Categorías de módulos 

- **Auxiliary (Auxiliar)**: cualquier módulo de soporte, como escáneres, rastreadores y fuzzers, se puede encontrar aquí.

- **Encoders (Codificadores)**: permitirán codificar el `exploit` y los `payloads` con la esperanza de que una solución antivirus basada en firmas los pase por alto.

- **Evasion (Evasión)**: si bien los `encoders` codificarán la carga útil, no deben considerarse un intento directo de evadir el software antivirus.

- **Exploits**: Exploits, perfectamente organizados por sistema de destino.

- **NOPs**: NOPs (No OPeration) no hacen nada, literalmente. A menudo se usan como un búfer para lograr tamaños de `payloads` consistentes.

- **Payloads**:  son códigos que se ejecutarán en el sistema de destino.
    - Singles: `payloads` autónomos que no necesitan descargar un componente adicional para ejecutarse.
    - Stagers: Responsable de configurar un canal de conexión entre Metasploit y el sistema de destino Luego descargará el resto del `payload`.
    - Stages: Descargado por el `stager`. Esto le permitirá utilizar `payloads` de mayor tamaño.


## Comandos útiles

Establecer el contexto en el modulo de `ms17_010_eternalblue`
> `use exploit/windows/smb/ms17_010_eternalblue `

Comando `show options`

- El comando mostrar opciones tendrá diferentes resultados según el contexto en el que se utilice.

- Es posible que un módulo posterior a la explotación solo necesite que configuremos una ID DE SESIÓN. Una sesión es una conexión existente con el sistema de destino que utilizará el módulo posterior a la explotación

Todos los parámetros se configuran usando la misma sintaxis de comando
> `set <PARAMETER_NAME> <VALUE>`

Para establecer valores que se usarán para todos los módulos
> `setg <PARAMETER_NAME> <VALUE>`

Borrar cualquier valor de parámetro usando
> `unset <PARAMETER>`

Borrar todos los parámetros establecidos
> `unset all`

Mostrar opciones de cada modulo
> `show <MODULE-TYPE>` 

> `MODULE-TYPE: auxiliary, payload, exploit, etc.`

Abandonar el contexto
> `back`

Más información sobre cualquier módulo en el contexto actual
> `info`

Más información sobre cualquier módulo especificado
> `info exploit/windows/smb/ms17_010_eternalblue`

Buscar en la base de datos de Metasploit Framework los módulos relevantes para el parámetro de búsqueda dado
> `search ms17-010`

Ejemplo:

```
Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   1  auxiliary/scanner/smb/smb_ms17_010                         normal   No     MS17-010 SMB RCE Detection
   2  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   3  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   4  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution
```

Usar cualquier módulo devuelto en un resultado de búsqueda usando `use 0` en cambio de `use auxiliary/admin/smb/ms17_010_command`

Mas información del Ranking: https://docs.metasploit.com/docs/using-metasploit/intermediate/exploit-ranking.html

Filtrar búsqueda por modulo de tipo auxiliares
> `search type:auxiliary telnet`

Ejecutar el modulo
> `run` or `exploit`

Ejecutar el modulo y mandarlo a segundo plano una vez una session fue abierta
> `run -z`