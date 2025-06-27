a = int(input())
b,c,d = 1,1,1
for i in range(2, a+1):
    nb = b + c + d
    nc = b + d
    nd = b + c
    b,c,d = nb, nc, nd
print((b+c+d) % 9901)