
## Tipos de Aplicaciones

- **Nativas:** Son aquellas aplicaciones desarrolladas única y exclusivamente para sistemas operativos móviles, ya sea Android o IOS.
- **Híbrido:** Estas aplicaciones utilizan tecnologías como HTML, CSS y JavaScript, todas estas enlazadas y procesadas a través de frameworks.

## Smali
Cuando se crea un código de aplicación, el archivo apk contiene un archivo .dex, que contiene el código de bytes binario de Dalvik. Smali es un **lenguaje ensamblador** que se ejecuta en Dalvik VM, que es la JVM de Android.

- Los registros son siempre de 32 bits y pueden contener cualquier tipo de valor. Se utilizan 2 registros para contener tipos de 64 bits (largo y doble).
- El número total de registros incluiría los registros necesarios para contener los parámetros del método.
- los argumentos de un método se colocarían en los últimos registros
- El primer parámetro de un método no estático es siempre el objeto en el que se invoca el método (como un `this`, o `self`).

Por ejemplo tomando en cuenta 5 registros y teniendo 3 parámetros
```
Local	Param	
v0		the first local register
v1		the second local register
v2	p0	the first parameter register
v3	p1	the second parameter register
v4	p2	the third parameter register
```

### Long/Double values
Como se mencionó anteriormente, las primitivas `long` y `double` (J y D respectivamente) son valores de 64 bits y requieren 2 registros. 

Por lo tanto si se tiene el siguiente método `LMyObject;->MyMethod(IJZ)V`. se obtendrán 5 registros en total
```
Register	Type
p0	this
p1	I
p2, p3	J
p4	Z
```

## Estructura de un APK

- **AndroidManifest.xml:** el archivo de manifiesto en formato XML binario. 
- **classes.dex:** código de la aplicación compilado en formato dex. 
- **resources.arsc:** archivo que contiene los recursos de la aplicación precompilados, en XML binario.
- **res/:** carpeta que contiene recursos no compilados en resources.arsc 
- **assets/:** carpeta opcional que contiene activos de aplicaciones, que puede recuperar AssetManager. 
- **lib/:** carpeta opcional que contiene código compilado, es decir, bibliotecas de código nativo.
- **META-INF/:** carpeta que contiene el archivo MANIFEST.MF, que almacena metadatos sobre el contenido del JAR. que a veces se almacenará en una carpeta llamada original. La firma del APK también se almacena en esta carpeta.

## Usando ADB
Contenido Obtenido de:

> https://jonathandata1.medium.com/android-phone-hacking-101-adb-android-debug-bridge-320a7651e574

Ver dispositivos
> `.\adb devices`

Enumere todas las propiedades de su dispositivo
> `.\adb shell getprop`

Registro en vivo de todo lo que se ejecuta en su dispositivo
> `.\adb shell logcat`

Enumere todas las aplicaciones del sistema y las aplicaciones instaladas por el usuario en el dispositivo
> `.\adb shell pm list packages`

Obtener path de un paquete en especifico
> `.\adb shell pm path com.amaze.filemanager`

se obtiene
> `package:/system/app/Amaze/Amaze.apk`

Extraer apk
> `.\adb pull <REMOTE_PATH> [<LOCAL_PATH>]`

Abrir Shell
> `.\adb shell`

## Usando JADX

Carga un APK y mira su código fuente Java
> `jadx -d [path-output-folder] [path-apk-or-dex-file]`

cat AndroidManifest.xml | grep "activity" --color


## Análisis estático

Uso de criptografía débil o inadecuado
- `grep -r "SecretKeySpec" *`
- `grep -rli "aes" *`
- `grep -rli "iv"`

Actividades de preferencias exportadas
> `cat AndroidManifest.xml | grep "activity" --color`

Aplicaciones que permiten copias de seguridad
> `cat AndroidManifest.xml | grep "android:allowBackup" --color`

Aplicaciones que son depurables
> `cat AndroidManifest.xml | grep "android:debuggable" --color`

bases de datos de Firebase desprotegidas
- `git clone https://github.com/shivsahni/FireBaseScanner`
- `python2 FirebaseMisconfig.py --path <APK>` 

## Frameworks de Análisis estático
- [MARA Framework](https://github.com/xtiankisutsa/MARA_Framework)
- [QARK](https://github.com/linkedin/qark)
- [MobSF](https://mobsf.github.io/docs/#/)

## Frameworks de Análisis Dinámico
- [Pidcat](https://github.com/JakeWharton/pidcat)
- [Drozer](https://github.com/WithSecureLabs/drozer)
- Frida
