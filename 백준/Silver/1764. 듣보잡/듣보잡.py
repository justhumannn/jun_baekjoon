n,m = map(int,input().split())
alist = []
blist = []
for i in range(n):
    alist.append(input())
for i in range(m):
    blist.append(input())
alist = set(alist)
blist = set(blist)
clist = alist.intersection(blist)
clist = list(clist)
clist.sort()
print(len(clist))
for c in clist:
    print(c)