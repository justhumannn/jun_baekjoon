def diff_one(a, b):
    if len(a) != len(b):
        return False
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
    return diff == 1

while True:
    words = []
    while True:
        s = input().strip()
        if s == "#":
            break
        words.append(s)

    if not words:
        break

    ok = True
    for i in range(len(words) - 1):
        if not diff_one(words[i], words[i+1]):
            ok = False
            break

    print("Correct" if ok else "Incorrect")