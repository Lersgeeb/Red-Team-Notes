# Abrir el archivo como binario
with open('Flag.txt', 'rb') as f:
    byte_data = f.read()

# Traducir los bytes
traduccion = []
for b in byte_data:
    if b == 0x09:
        traduccion.append("0")
    elif b == 0x20:
        traduccion.append("1")
    else:
        traduccion.append("UNK")  # Puedes omitirlo o cambiarlo si quieres

# Mostrar resultado
texto=''.join(traduccion)
print(texto)