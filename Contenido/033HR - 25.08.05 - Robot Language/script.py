from collections import Counter

possible_password = "⧈⨂⧉╲⧉╲⦿⨂⧉⦿⧈⌂⦿⧉"

list_chars_str = "█ : ◉ : ╳ : ⧈ : ⧉ : ▢ : ◌ : ⨂ : ╲ : ⌂ : ⧉ : ⌂ : ⨀ : ◀ : ⦿ : ⧈ : ⦿ : ⨂ : ⌂ : ╲ : ⦿ : ⧉ : ⨀ : ◀ : ⦿ : ⧈" 
list_chars = list_chars_str.split(" : ")
char_count = Counter(list_chars)
list_chars_unicode = []

print(list_chars)

# O mostrar ordenado por carácter
print("\nOrdenado por carácter:")
for char in sorted(char_count.keys()):
    print(f"'{char}': {char_count[char]}")

# O mostrar ordenado por cantidad (descendente)
print("\nOrdenado por cantidad:")
for char, count in char_count.most_common():
    print(f"'{char}': {count}")

for char in list_chars:
    list_chars_unicode.append(char.encode("unicode_escape"))

sorted_chars_unicode = sorted(list_chars_unicode)

print("List Chars:", sorted_chars_unicode)
