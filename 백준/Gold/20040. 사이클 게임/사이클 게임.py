import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
a,b = map(int, input().split())
parent = [i for i in range(a+1)]
result = 0
check = True
def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]
def union_root(x, y):
    x = find_root(x)
    y = find_root(y)
    if x != y:
        parent[y] = x
        return False
    return True
for i in range(1,b+1):
    c,d = map(int, input().split())
    if union_root(c, d) and check:
        result = i
        check = False
print(result)