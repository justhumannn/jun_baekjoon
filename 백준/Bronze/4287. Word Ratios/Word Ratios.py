while True:
    line = input()
    if line == "#":
        break
    a, b, c = line.split()
    res = []
    for x, y, z in zip(a, b, c):
        diff = (ord(y) - ord(x)) % 26
        new_char = chr((ord(z) - ord('a') + diff) % 26 + ord('a'))
        res.append(new_char)

    print(a, b, c, ''.join(res))