# Stegnow

## Uso de Stegsnow
stegsnow es una herramienta de línea de comandos que oculta información dentro de archivos de texto ASCII añadiendo espacios y tabulaciones invisibles al final de cada línea. Puede comprimir y cifrar el mensaje para darle una capa extra de protección.

Sintaxis Basica
`stegsnow [opciones] [infile [outfile]]`

## Opciones más útiles
| Opción            | Función                                                                |
| ----------------- | ---------------------------------------------------------------------- |
| `-m "mensaje"`    | Oculta una cadena literal.                                             |
| `-f secreto.bin`  | Oculta el contenido de un archivo.                                     |
| `-C`              | Comprime (o descomprime al extraer).                                   |
| `-p "contraseña"` | Cifra/descifra con ICE CFB-1.                                          |
| `-l 72`           | Garantiza que las líneas no excedan 72 caracteres (útil para e-mails). |
| `-S`              | Solo calcula la capacidad oculta disponible.                           |
| `-Q`              | Modo silencioso (no muestra estadísticas).([Ubuntu Manpages][1])       |


## Ejemplos
| Objetivo                                      | Comando                                                           |
| --------------------------------------------- | ----------------------------------------------------------------- |
| **1. Calcular capacidad**                     | `stegsnow -S -l 72 portada.txt`                                   |
| **2. Ocultar texto rápido**                   | `stegsnow -m "la luna es de queso" portada.txt > estego.txt`      |
| **3. Ocultar archivo + compresión + cifrado** | `stegsnow -C -p "S3cr3t0!" -f secreto.zip portada.txt estego.txt` |
| **4. Extraer mensaje (con contraseña)**       | `stegsnow -C -p "S3cr3t0!" estego.txt > recuperado.zip`           |
