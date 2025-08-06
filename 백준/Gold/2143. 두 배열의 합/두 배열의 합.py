a = int(input())
b = int(input())
c = list(map(int, input().split()))
d = int(input())
e = list(map(int, input().split()))
f = []
for i in range(b):
    s = 0
    for j in range(i, b):
        s += c[j]
        f.append(s)
g = {}
for i in range(d):
    s = 0
    for j in range(i, d):
        s += e[j]
        g[s] = g.get(s, 0) + 1
z = 0
for v in f:
    z += g.get(a - v, 0)
print(z)