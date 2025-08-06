from collections import Counter

possible_password = "⧈⨂⧉╲⧉╲⦿⨂⧉⦿⧈⌂⦿⧉"

# Show different characters at password
possible_password_chars = set(possible_password)
print("Caracteres en la posible contraseña:", possible_password_chars)

list_chars_str = "█ : ◉ : ╳ : ⧈ : ⧉ : ▢ : ◌ : ⨂ : ╲ : ⌂ : ⧉ : ⌂ : ⨀ : ◀ : ⦿ : ⧈ : ⦿ : ⨂ : ⌂ : ╲ : ⦿ : ⧉ : ⨀ : ◀ : ⦿ : ⧈" 
abc = "abcdefghijklmnopqrstuvwxyz"
list_chars = list_chars_str.split(" : ")
char_count = Counter(list_chars)
list_chars_unicode = []

def find_all_char_positions(text_string, char_to_find):
    positions = []
    for i, char in enumerate(text_string):
        if char == char_to_find:
            positions.append(abc[i])
    return positions



translated_chars = []
for char in possible_password:
    translated_chars.append(find_all_char_positions("".join(list_chars), char))

# Mostrar caracteres traducidos
print("Caracteres traducidos:", translated_chars)
Drviktorkozlov



# Mostrar list_chars
print("List Chars:", list_chars)

# Mostrar tamaño lista
print("Tamaño lista:", len(list_chars))

# Mostrar ordenado por carácter y mostrar unicode
print("\nOrdenado por carácter:")
for char in sorted(char_count.keys()):
    print(f"'{char}' (Unicode: {char.encode('unicode_escape')}): {char_count[char]}")

# Mostrar ordenado por cantidad (descendente)
print("\nOrdenado por cantidad:")
for char, count in char_count.most_common():
    print(f"'{char}': {count}")

for char in list_chars:
    list_chars_unicode.append(char.encode("unicode_escape"))

sorted_chars_unicode = sorted(list_chars_unicode)

print("List Chars:", sorted_chars_unicode)
