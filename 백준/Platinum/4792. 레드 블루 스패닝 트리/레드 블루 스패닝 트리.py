import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union_root(x, y):
    x, y = find(x), find(y)
    if x == y:
        return False
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return True

def kruskal(edges, n, blue_first):
    global parent
    parent = [-1] * (n + 1)
    cnt = 0
    if blue_first:
        edges.sort(key=lambda x: 0 if x[0] == 'B' else 1)
    else:
        edges.sort(key=lambda x: 0 if x[0] == 'R' else 1)
    for c, f, t in edges:
        if union_root(f, t):
            if c == 'B':
                cnt += 1
    return cnt

while True:
    n, m, k = map(int, input().split())
    if n == 0 and m == 0 and k == 0:
        break
    edges = [input().split() for _ in range(m)]
    for i in range(m):
        edges[i][1] = int(edges[i][1])
        edges[i][2] = int(edges[i][2])
    min_b = kruskal(edges, n, False)
    max_b = kruskal(edges, n, True)
    print(1 if min_b <= k <= max_b else 0)