import sys
input = sys.stdin.readline

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    for _ in range(m):
        v, w,p = map(int, input().split())
        if p == 1:
            adj[v].append(w)
            radj[w].append(v)
        else:
            adj[v].append(w)
            radj[w].append(v)
            adj[w].append(v)
            radj[v].append(w)
    visited = [False] * (n + 1)
    order = []

    for i in range(1, n + 1):
        if not visited[i]:
            stack = [(i, 0)]
            visited[i] = True
            while stack:
                v, idx = stack[-1]
                if idx < len(adj[v]):
                    stack[-1] = (v, idx + 1)
                    u = adj[v][idx]
                    if not visited[u]:
                        visited[u] = True
                        stack.append((u, 0))
                else:
                    stack.pop()
                    order.append(v)
    visited2 = [False] * (n + 1)
    scc_count = 0
    check = True
    for v in reversed(order):
        if not visited2[v]:
            scc_count += 1
            if scc_count > 1:
                print(0)
                check = False
                break
            stack = [v]
            visited2[v] = True
            while stack:
                x = stack.pop()
                for y in radj[x]:
                    if not visited2[y]:
                        visited2[y] = True
                        stack.append(y)
    if check:
        print(1)