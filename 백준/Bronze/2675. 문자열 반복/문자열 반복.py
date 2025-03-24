a = int(input())
for _ in range(a):
    c1 = ''
    b,c = input().split()
    b = int(b)
    for i in range(0,len(c)):
        c1 += c[i]*b
    print(c1)