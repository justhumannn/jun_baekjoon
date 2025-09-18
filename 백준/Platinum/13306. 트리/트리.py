import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
N, Q = map(int, input().split())
p = [0]*(N+1)
for i in range(2, N+1):
    p[i] = int(input())
ops = []
for _ in range(N-1+Q):
    line = list(map(int, input().split()))
    ops.append(line)
parent = [i for i in range(N+1)]
removed = [False]*(N+1)
for op in ops:
    if op[0] == 0:
        removed[op[1]] = True
for i in range(2, N+1):
    if not removed[i]:
        union(i, p[i])
answers = []
for op in reversed(ops):
    if op[0] == 0:
        b = op[1]
        union(b, p[b])
    else:
        _, c, d = op
        if find(c) == find(d):
            answers.append("YES")
        else:
            answers.append("NO")
print("\n".join(reversed(answers)))