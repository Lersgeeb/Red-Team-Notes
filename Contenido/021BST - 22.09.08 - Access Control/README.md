# Access Control

## Escalacion vertical

### Unprotected admin functionality
se observa en el archivo robots.txt que existe una ruta `administrator-panel`, el cual no necesita ningún tipo de autenticación o control de acceso.

### Unprotected admin functionality with unpredictable URL
En el código de javascript se muestra la ruta de administración el cual tampoco tiene ningún tipo de control de acceso.

### User role controlled by request parameter
El control de acceso para entrar a la vista de Admin, se podía alterar fácilmente debido a que se encontraba como una cookie con un valor booleano.

### User role can be modified in user profile
La petición de cambio de correo se puede usar para cambiar otros atributos del usuario, Ademas esta petición retorna los nombres de cada atributo del usuario, por lo tanto se puede cambiar el rol añadiéndolo en el cuerpo de la petición.

### URL-based access control can be circumvented
Algunos Frameworks admiten varios encabezados HTTP no estándar que se pueden usar para anular la URL en la solicitud original, como X-Original-URL y X-Rewrite-URL.

Establecer la ruta de la petición como `/` y colocar el siguiente encabezado
> `X-Original-URL: /admin`

### Method-based access control can be circumvented
A pesar de que el método `POST` es cambiado, la acción de cambiar de privilegios es realizada.

## Escalacion Horizontal

### User ID controlled by request parameter 
Se puede obtener datos de otros usuarios con solo cambiar ID que se encuentra en la URL como parámetro.

### User ID controlled by request parameter, with unpredictable user IDs 
Se puede obtener datos de otros usuarios con solo cambiar ID que se encuentra en la URL como parámetro.

### User ID controlled by request parameter with data leakage in redirect
A pesar de existir algunos controles de denegación de acceso, todavía se puede encontrar información relevante en la respuesta de la petición 

### User ID controlled by request parameter with password disclosure
Se puede obtener información relevante de otros usuarios con solo cambiar ID que se encuentra en la URL como parámetro.

### Insecure direct object references
Las referencias directas a objetos inseguros (IDOR) son una subcategoría de vulnerabilidades de control de acceso. IDOR surge cuando una aplicación utiliza la entrada proporcionada por el usuario para acceder a los objetos directamente y un atacante puede modificar la entrada para obtener acceso no autorizado.

El chat permite crear una petición que pueda descargar cualquier archivo dado en el parámetro. 

## Vulnerabilidades de control de acceso
A veces, un sitio web implementará controles de acceso rigurosos sobre algunos de estos pasos, pero ignorará otros. Por ejemplo, suponga que los controles de acceso se aplican correctamente al primer y segundo paso, pero no al tercero.

Algunos sitios web basan los controles de acceso en el encabezado Referer enviado en la solicitud HTTP. El encabezado Referer generalmente se agrega a las solicitudes de los navegadores para indicar la página desde la que se inició una solicitud.

> `Referer: https://0a3e00be042b1d67c0cf86d7007200b4.web-security-academy.net/admin`