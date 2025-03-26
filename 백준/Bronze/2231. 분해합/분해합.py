a = int(input())
b = 1
d = 0
while True:
    c = []
    if a == d:
        print(b-1)
        break
    elif a < b:
        print(0)
        break
    else:
        b = str(b)
        d = 0
        for i in range(0,len(b)):
            c.append(b[i])
        for i in range(0,len(c)):
            d += int(c[i])
        b = int(b)
        d += b
        b += 1