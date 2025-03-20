a = int(input())
def test(b,c):
    while c != 0:
        b,c = c, b%c
    return b
for _ in range(a):
    b,c = map(int,input().split())
    if b > c:
        d = test(b,c)
    else:
        d = test(c,b)
    e = (b * c) // d
    print(e)