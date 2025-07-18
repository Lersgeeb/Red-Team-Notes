# Business Logic Vulnerabilities Labs

## High-level logic vulnerability
La vulnerabilidad del laboratorio consiste en que al interceptar una petición se pueden establecer cantidades negativas en los objetos enviados al carrito

## Low-level logic flaw
La vulnerabilidad del laboratorio se observa al momento de agregar un numero gigante de algun objeto en especifico, obteniendo que la cantidad del precio tome un comportamiento indeseado al llegar a establecerse como negativo. 


## Inconsistent handling of exceptional input

Se realiza una enumeración de rutas de la pagina
> `BurpSuite > Target > Site_map > Click Derecho en el target > Engagement Tools > Discover Content`

En encuentra la ruta 
> `/admin`

Se observa que la ruta admin solo es accesible si se tiene una cuenta con dominio de `@donwannacry.com`

Se crea una cuenta con un nombre lo suficientemente extenso y se activa la cuenta con la cuenta de email del usuario
> `0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184000ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b218401a00db0ab000bc04038a8dc05b2@exploit-0a71002c04448ae9c0262180017200b2.web-security-academy.net`

Se observa que a pesar de que el correo de activación es enviado, debido a que el correo es muy largo, se corta en cierta parte
> `0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184000ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b218401a00db0ab000bc04038a8dc0`

a traves de ello es posible simular el tener una cuenta con el dominio `@donwannacry.com` a traves de dar siguiente correo al momento de registrarse
> `0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184000ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b2184001a00db0ab000bc04038a8dc05b218401a00db0ab000bc04038a8dc05b2@dontwannacry.com.exploit-0a71002c04448ae9c0262180017200b2.web-security-academy.net`

## Inconsistent security controls
La vulnerabilidad consiste en crear una cuenta de manera normal y una vez accediendo a ella cambiar el dominio del correo con una que mantenga privilegios.

## Weak isolation on dual-use endpoint
La vulnerabilidad consiste en que la petición de cambiar contraseña contenía un comportamiento no deseado al momento de quitar el parámetro de actual contraseña, lo que permitía cambiar la contraseña del usuario sin necesidad de tener la contraseña actual

## Insufficient workflow validation
La vulnerabilidad consiste en el flujo de la validación de compra, lo cual permite saltarse las fases de compra  y no validar los fondos del usuario para realizar la orden.

## Authentication bypass via encryption oracle
Se aprovecha una vulnerabilidad que permite encriptar y desencriptar las cookies mediante dos peticiones diferentes (conocido como `encryption oracle`). Por lo tanto se puede alterar la cookie de `stay-logged-in` para mantener una sesión como el usuario `administrator`.
