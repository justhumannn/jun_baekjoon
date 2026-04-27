import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])

adj = [[] for _ in range(N)]
idx = 2
for _ in range(N - 1):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    w = int(input_data[idx+2])
    adj[u].append((v, w))
    adj[v].append((u, w))
    idx += 3

sz = [0] * N
deleted = [False] * N
INF = 10**9
min_edges = [INF] * (K + 1)
min_edges[0] = 0
ans = INF

q = [0]
while q:
    start = q.pop()
    
    stack = [(start, -1)]
    order = []
    while stack:
        u, p = stack.pop()
        order.append((u, p))
        for v, w in adj[u]:
            if v != p and not deleted[v]:
                stack.append((v, u))
    
    for u, p in reversed(order):
        sz[u] = 1
        for v, w in adj[u]:
            if v != p and not deleted[v]:
                sz[u] += sz[v]
    
    total_size = sz[start]
    c = start
    p = -1
    while True:
        next_node = -1
        for v, w in adj[c]:
            if v != p and not deleted[v] and sz[v] > total_size // 2:
                next_node = v
                break
        if next_node == -1:
            break
        p = c
        c = next_node
        
    modified = []
    for v, w in adj[c]:
        if not deleted[v]:
            path_stack = [(v, c, w, 1)]
            paths = []
            while path_stack:
                u, p_node, l, e = path_stack.pop()
                if l > K:
                    continue
                paths.append((l, e))
                for next_v, next_w in adj[u]:
                    if next_v != p_node and not deleted[next_v]:
                        path_stack.append((next_v, u, l + next_w, e + 1))
            
            for l, e in paths:
                if ans > e + min_edges[K - l]:
                    ans = e + min_edges[K - l]
            
            for l, e in paths:
                if min_edges[l] > e:
                    min_edges[l] = e
                    modified.append(l)
                    
    for l in modified:
        min_edges[l] = INF
        
    deleted[c] = True
    for v, w in adj[c]:
        if not deleted[v]:
            q.append(v)

if ans >= INF:
    print(-1)
else:
    print(ans)