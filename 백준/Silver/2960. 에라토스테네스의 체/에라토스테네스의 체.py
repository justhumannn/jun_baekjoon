a,b = map(int,input().split())
c = []
d = 0
for i in range(2,a+1):
    c.append(i)
while d != b:
    e = min(c)
    c.remove(min(c))
    f = e
    d += 1
    i = 0
    while d != b:
        if i >= len(c):
            i = len(c) - 1
        if c[i] % e == 0:
            f = c[i]
            c.remove(c[i])
            d += 1
        if i >= len(c):
            i = len(c) - 1
        if c[i] == c[-1]:
            break
        else:
            i += 1
print(f)