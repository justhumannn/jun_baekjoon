import sys
from collections import deque

input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
        
    parts = line.split()
    if not parts:
        continue
        
    v = int(parts[0])
    e = int(parts[1])
    
    S = v + 1
    T = v
    
    adj = [[] for _ in range(2 * v + 1)]
    
    for i in range(2, v):
        adj[i].append([i + v, 1, 0, len(adj[i + v])])
        adj[i + v].append([i, 0, 0, len(adj[i]) - 1])
        
    for _ in range(e):
        u, to, cost = map(int, input().split())
        
        u_out = u + v if u != 1 else S
        to_in = to if to != v else T
        
        adj[u_out].append([to_in, 1, cost, len(adj[to_in])])
        adj[to_in].append([u_out, 0, -cost, len(adj[u_out]) - 1])
        
    total_cost = 0
    for _ in range(2):
        dist = [float('inf')] * (2 * v + 1)
        dist[S] = 0
        in_q = [False] * (2 * v + 1)
        q = deque([S])
        in_q[S] = True
        
        parent = [-1] * (2 * v + 1)
        parent_edge = [-1] * (2 * v + 1)
        
        while q:
            curr = q.popleft()
            in_q[curr] = False
            
            for i in range(len(adj[curr])):
                nxt, cap, cost, rev_idx = adj[curr][i]
                if cap > 0 and dist[nxt] > dist[curr] + cost:
                    dist[nxt] = dist[curr] + cost
                    parent[nxt] = curr
                    parent_edge[nxt] = i
                    if not in_q[nxt]:
                        q.append(nxt)
                        in_q[nxt] = True
                        
        total_cost += dist[T]
        
        curr = T
        while curr != S:
            p = parent[curr]
            idx_edge = parent_edge[curr]
            rev_idx = adj[p][idx_edge][3]
            
            adj[p][idx_edge][1] -= 1
            adj[curr][rev_idx][1] += 1
            curr = p
            
    print(total_cost)