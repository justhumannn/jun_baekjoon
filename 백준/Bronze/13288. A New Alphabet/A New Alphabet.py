mapping = {
    'a': "@", 'b': "8", 'c': "(", 'd': "|)", 'e': "3", 'f': "#", 'g': "6",
    'h': "[-]", 'i': "|", 'j': "_|", 'k': "|<", 'l': "1", 'm': r"[]\/[]",
    'n': r"[]\[]", 'o': "0", 'p': "|D", 'q': "(,)", 'r': "|Z", 's': "$",
    't': "']['", 'u': "|_|", 'v': r"\/", 'w': r"\/\/", 'x': "}{", 'y': "`/", 'z': "2"
}
text = input()
result = []
for char in text:
    lower_char = char.lower()
    if lower_char in mapping:
        result.append(mapping[lower_char])
    else:
        result.append(char)
print("".join(result))