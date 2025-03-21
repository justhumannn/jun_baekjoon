a,b = map(int,input().split())
c = []
for _ in range(a):
    c.append([])
for i in range(0,a):
    for _ in range(b):
        c[i].append(0)
d = list(map(int,input().split()))
for i in range(0,len(d)):
    if d[i] > 0:
        for j in range(len(c)-1,len(c)-d[i]-1,-1):
            c[j][i] = 1
d = 0
for i in range(a-1,-1,-1):
    j = len(c[i])-1
    while True:
        if j <= 1:
            break
        elif c[i][j] == 1:
            j1 = j
            j -= 1
            if c[i][j] == 0:
                while True:
                    if j <= 0:
                        break
                    elif c[i][j-1] == 0:
                        j -= 1
                    else:
                        d = d + (j1-j)
                        break
        elif c[i][j] == 0:
            j -= 1
print(d)