#lee el archivo llamado misterio_sinresolver.txt
with open("misterio_sin_resolver.txt", "r") as file:
    contenido = file.read()

# Separa por salto de linea
lineas = contenido.split("\n")


with open("output.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(lineas))

#copia otro archivo pero con la cadena de binario a texto si es posible
with open("output_texto.txt", "w", encoding="utf-8") as file:
    for linea in lineas:
        texto = ''
        error = ''
        for b in linea.split():
            try:
                # Intenta convertir cada línea de binario a texto en caso contrario agregar a lista de error
                texto += chr(int(b, 2))
            except ValueError:
                error += b + ""

        if error:
            file.write(error + "\n")
