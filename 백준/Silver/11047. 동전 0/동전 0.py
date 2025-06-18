a, b = map(int,input().split())
c = []
for _ in range(a):
    c.append(int(input()))
count = 0
for i in range(len(c)-1, -1,-1):
    if c[i] <= b:
        count += b // c[i]
        b %= c[i]
        if b == 0:
            print(count)
            break