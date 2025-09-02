import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
a,b = map(int, input().split())
parent = [i for i in range(a+1)]
edges = []
for _ in range(b):
    c,d,e = map(int, input().split())
    edges.append((e,c,d))
edges.sort()
result = []
def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]
def union_root(x, y):
    x = find_root(x)
    y = find_root(y)
    if x != y:
        parent[y] = x
        return True
    return False
for c,d,e in edges:
    if union_root(d, e):
        result.append(c)
print(sum(result) - max(result))