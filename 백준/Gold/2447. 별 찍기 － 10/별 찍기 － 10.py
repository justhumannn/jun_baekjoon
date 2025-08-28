a=int(input())
def f(n):
    if n==1:
        return ["*"]
    t=f(n//3)
    r=[]
    for s in t:
        r.append(s*3)
    for s in t:
        r.append(s+" "*(n//3)+s)
    for s in t:
        r.append(s*3)
    return r
for line in f(a):
    print(line)
