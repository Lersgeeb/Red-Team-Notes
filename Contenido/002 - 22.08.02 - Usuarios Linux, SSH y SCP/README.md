

# **Laboratorio Usuarios, SSH y SCP**
## **Creación de usuario**
Creación del usuario “red-gabriel” y asignación de contraseña.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.007.png)

La contraseña que se utilizará es “kali123”

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.008.png)

También se crearon los siguientes usuarios

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.009.png)

A continuación, podemos verificar la creación de usuarios mostrando el contenido del archivo /etc/passwd 

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.010.png)
## **Conexión SSH**
Conectado con SSH al usuario “red-gabriel” a través de la consola de la maquina Local.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.011.png)

Conectado con SSH al usuario “red-gabriel” a través del software PUTTY en la maquina Local.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.012.png)



## **Permisos y creación de archivo**
Se creó la carpeta para el usuario “red-gabriel” y se le asigno total permiso a ella.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.013.png)

Ahora se preparan algunos archivos en la carpeta remota del usuario “red-gabriel”, como en alguna carpeta en la maquina local que hace uso de Windows.

En la carpeta remota se creó un archivo llamado “ejemplo.txt” que contiene el mensaje “Texto Ejemplo”. Esto se hizo haciendo uso de la conexión SSH con el usuario “red-gabriel”, el cual ya tiene los permisos requeridos para modificar la carpeta.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.014.png)


Por otra parte, se creó una carpeta en Windows en la siguiente ruta:

> `C:\Users\baneg\OneDrive\Documents\linux\_scp/`

En ella también se creará un archivo, el cual se llamará “ejemploLocal.txt” y que se le agregó un texto de ejemplo.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.015.png)










## **Uso de SCP** 
### **Local a Remoto**
Primero se copiará el archivo local hacia la maquina remota. Para esto se usará el siguiente comando:

> `scp  C:\Users\baneg\OneDrive\Documents\linux\_scp\ejemploLocal.txt red-gabriel@192.168.1.18:./ejemploLocal.txt`

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.016.png)

para verificar que se haya copiado con éxito, nos dirigiremos a la carpeta del usuario “red-gabriel” y mostraremos su contenido.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.017.png)
### **Remoto a Local**
Lo segundo será copiar el archivo en la maquina remota hacia la maquina local. Para esto se usará el siguiente comando:

> `scp red-gabriel@192.168.1.18:./ejemplo.txt C:\Users\baneg\OneDrive\Documents\linux\_scp\`

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.018.png)

Para verificar que se haya copiado con éxito, nos dirigiremos a la carpeta local mencionada anteriormente y mostraremos su contenido.

![](assets/Aspose.Words.ec5c3079-43ae-41e8-8f7d-91d860124cab.019.png)


