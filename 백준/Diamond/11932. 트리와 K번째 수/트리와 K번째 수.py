import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])

W = [0] + [int(x) for x in input_data[2:N+2]]
sorted_W = sorted(list(set(W[1:])))
comp_W = {v: i for i, v in enumerate(sorted_W)}

adj = [[] for _ in range(N + 1)]
idx = N + 2
for _ in range(N - 1):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

MAX_NODES = N * 20 + 100
lc = [0] * MAX_NODES
rc = [0] * MAX_NODES
cnt = [0] * MAX_NODES
roots = [0] * (N + 1)
node_cnt = 0

def insert(prev_root, l, r, val):
    global node_cnt
    node_cnt += 1
    curr = node_cnt
    lc[curr] = lc[prev_root]
    rc[curr] = rc[prev_root]
    cnt[curr] = cnt[prev_root] + 1
    
    curr_node = curr
    prev_node = prev_root
    
    while l < r:
        mid = (l + r) // 2
        node_cnt += 1
        next_node = node_cnt
        if val <= mid:
            lc[curr_node] = next_node
            rc[curr_node] = rc[prev_node]
            curr_node = next_node
            prev_node = lc[prev_node]
            r = mid
        else:
            lc[curr_node] = lc[prev_node]
            rc[curr_node] = next_node
            curr_node = next_node
            prev_node = rc[prev_node]
            l = mid + 1
        cnt[curr_node] = cnt[prev_node] + 1
    
    return curr

depth = [0] * (N + 1)
parent = [[0] * 18 for _ in range(N + 1)]

roots[1] = insert(0, 0, len(sorted_W) - 1, comp_W[W[1]])
depth[1] = 1
vis = [False] * (N + 1)
vis[1] = True

queue = [1]
q_idx = 0
while q_idx < len(queue):
    u = queue[q_idx]
    q_idx += 1
    for v in adj[u]:
        if not vis[v]:
            vis[v] = True
            depth[v] = depth[u] + 1
            parent[v][0] = u
            roots[v] = insert(roots[u], 0, len(sorted_W) - 1, comp_W[W[v]])
            queue.append(v)

for i in range(1, 18):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for i in range(18):
        if (diff >> i) & 1:
            u = parent[u][i]
    if u == v:
        return u
    for i in range(17, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]
    return parent[u][0]

out = []
max_val_idx = len(sorted_W) - 1

for _ in range(M):
    X = int(input_data[idx])
    Y = int(input_data[idx+1])
    K = int(input_data[idx+2])
    idx += 3
    
    L = lca(X, Y)
    P = parent[L][0]
    
    u_root = roots[X]
    v_root = roots[Y]
    l_root = roots[L]
    p_root = roots[P]
    
    l, r = 0, max_val_idx
    while l < r:
        mid = (l + r) // 2
        count = cnt[lc[u_root]] + cnt[lc[v_root]] - cnt[lc[l_root]] - cnt[lc[p_root]]
        
        if count >= K:
            u_root = lc[u_root]
            v_root = lc[v_root]
            l_root = lc[l_root]
            p_root = lc[p_root]
            r = mid
        else:
            K -= count
            u_root = rc[u_root]
            v_root = rc[v_root]
            l_root = rc[l_root]
            p_root = rc[p_root]
            l = mid + 1
            
    out.append(str(sorted_W[l]))

print('\n'.join(out))