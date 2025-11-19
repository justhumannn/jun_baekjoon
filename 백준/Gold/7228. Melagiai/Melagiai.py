import sys
sys.setrecursionlimit(10**7)

def find(x):
    if p[x] != x:
        root = find(p[x])
        d[x] = d[x] ^ d[p[x]]
        p[x] = root
    return p[x]

n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]
d = [0] * (n + 1)
chk = True

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if not chk:
        continue
        
    ra = find(a)
    rb = find(b)
    
    if ra != rb:
        p[rb] = ra
        d[rb] = d[a] ^ d[b] ^ c
    else:
        if (d[a] ^ d[b]) != c:
            chk = False

if chk:
    print("EGZISTUOJA")
else:
    print("NEEGZISTUOJA")