d = 0
count = 0
a = int(input())
d = a
while True:
    if a == 0:
        count = 1
        break
    if a < 10:
        b,c = 0,a
        f = b + c
    else:
        a = str(a)
        b,c = a[0],a[1]
        b = int(b)
        c = int(c)
        if b + c >= 10:
            e = str(b + c)
            f = int(e[1])
        else:
            f = b + c
    a = (c * 10) + (f)
    count += 1
    if a == d:
        break
print(count)
