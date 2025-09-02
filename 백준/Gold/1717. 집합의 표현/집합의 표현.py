import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
a,b = map(int, input().split())
parent = [-1] * (a + 2)
def find_root(x):
    if parent[x] < 0:
        return x
    parent[x] = find_root(parent[x])
    return parent[x]
def union_root(x, y,check):
    x = find_root(x)
    y = find_root(y)
    if x != y:
        if check == 1:
            if x < y:
                parent[x] += parent[y]
                parent[y] = x
            else:
                parent[y] += parent[x]
                parent[x] = y
        return False
    return True
for i in range(1,b+1):
    c,d,e = map(int, input().split())
    if c == 0:
        union_root(d, e,1)
    else:
        if union_root(d, e,-1):
            print('yes')
        else:
            print('no')