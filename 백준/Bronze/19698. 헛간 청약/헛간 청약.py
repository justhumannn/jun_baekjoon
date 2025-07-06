a,b,c,d = map(int,input().split())
e = b // d
e *= c // d
if e >= a:
    print(a)
else:
    print(e)