a,b = map(int,input().split())
c = []
b -= 1
idx = 0
d = []
c = list(range(1, a + 1))
for _ in range(a):
    idx = (idx+b) % len(c)
    d.append(str(c.pop(idx)))
print('<'+', '.join(d)+'>')