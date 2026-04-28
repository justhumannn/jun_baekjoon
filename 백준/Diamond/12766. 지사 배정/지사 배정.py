import sys
import heapq

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

N = int(input_data[0])
B = int(input_data[1])
S = int(input_data[2])
R = int(input_data[3])

# 단방향 그래프이므로 정방향, 역방향 분리
adj = [[] for _ in range(N + 1)]
rev_adj = [[] for _ in range(N + 1)]

for i in range(R):
    u = int(input_data[4 + i * 3])
    v = int(input_data[5 + i * 3])
    l = int(input_data[6 + i * 3])
    adj[u].append((v, l))
    rev_adj[v].append((u, l))

INF = float('inf')

def get_dists(graph, start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        for v, l in graph[u]:
            nxt_d = d + l
            if dist[v] > nxt_d:
                dist[v] = nxt_d
                heapq.heappush(pq, (nxt_d, v))
    return dist

hq_node = B + 1
dist_from_hq = get_dists(adj, hq_node)
dist_to_hq = get_dists(rev_adj, hq_node)
branches = []
for i in range(1, B + 1):
    branches.append(dist_from_hq[i] + dist_to_hq[i])
branches.sort()
P = [0] * (B + 1)
for i in range(B):
    P[i + 1] = P[i] + branches[i]
if S >= B:
    print(0)
    sys.exit()
dp_prev = [INF] * (B + 1)
dp_prev[0] = 0
for i in range(1, B + 1):
    if i <= 1:
        dp_prev[i] = 0
    else:
        dp_prev[i] = (i - 1) * P[i]
for k in range(2, S + 1):
    dp_curr = [INF] * (B + 1)
    stack = [(k, B, k - 1, B - 1)]
    while stack:
        l, r, opt_l, opt_r = stack.pop()
        if l > r:
            continue
            
        mid = (l + r) // 2
        best_val = INF
        best_idx = -1
        
        limit = mid - 1
        if limit > opt_r:
            limit = opt_r
            
        for i in range(opt_l, limit + 1):
            c = mid - i
            if c <= 1:
                cost = dp_prev[i]
            else:
                cost = dp_prev[i] + (c - 1) * (P[mid] - P[i])
                
            if cost < best_val:
                best_val = cost
                best_idx = i
                
        dp_curr[mid] = best_val
        
        stack.append((mid + 1, r, best_idx, opt_r))
        stack.append((l, mid - 1, opt_l, best_idx))
        
    dp_prev = dp_curr

print(dp_prev[B])