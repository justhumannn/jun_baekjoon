import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
penguins = [0] * (N + 1)
for i in range(1, N + 1):
    penguins[i] = int(input_data[i])
    
Q = int(input_data[N + 1])
queries = []
idx = N + 2
for _ in range(Q):
    op_str = input_data[idx]
    u = int(input_data[idx+1])
    v = int(input_data[idx+2])
    if op_str == "bridge":
        op = 0
    elif op_str == "penguins":
        op = 1
    else:
        op = 2
    queries.append((op, u, v))
    idx += 3
    
dsu_parent = list(range(N + 1))

def find(i):
    root = i
    while dsu_parent[root] != root:
        root = dsu_parent[root]
    curr = i
    while curr != root:
        nxt = dsu_parent[curr]
        dsu_parent[curr] = root
        curr = nxt
    return root

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        dsu_parent[root_i] = root_j
        return True
    return False

adj = [[] for _ in range(N + 1)]
for op, u, v in queries:
    if op == 0:
        if find(u) != find(v):
            union(u, v)
            adj[u].append(v)
            adj[v].append(u)
            
for i in range(1, N + 1):
    if find(i) == i:
        adj[0].append(i)
        adj[i].append(0)

sz = [0] * (N + 1)
parent = [0] * (N + 1)
depth = [0] * (N + 1)
heavy = [0] * (N + 1)
head = [0] * (N + 1)
pos = [0] * (N + 1)

stack = [(0, 0, 0)]
post_order = []
while stack:
    u, p, d = stack.pop()
    parent[u] = p
    depth[u] = d
    post_order.append(u)
    for nxt in adj[u]:
        if nxt != p:
            stack.append((nxt, u, d + 1))
            
for u in reversed(post_order):
    sz[u] = 1
    max_sub = 0
    for nxt in adj[u]:
        if nxt != parent[u]:
            sz[u] += sz[nxt]
            if sz[nxt] > max_sub:
                max_sub = sz[nxt]
                heavy[u] = nxt

stack = [(0, 0, 0)]
current_pos = 0
while stack:
    u, p, h = stack.pop()
    head[u] = h
    current_pos += 1
    pos[u] = current_pos
    for nxt in adj[u]:
        if nxt != p and nxt != heavy[u]:
            stack.append((nxt, u, nxt))
    if heavy[u] != 0:
        stack.append((heavy[u], u, h))

seg_sz = 1
while seg_sz <= N + 1:
    seg_sz *= 2
    
tree = [0] * (2 * seg_sz)

def update(idx, val):
    idx += seg_sz - 1
    tree[idx] = val
    idx //= 2
    while idx > 0:
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        idx //= 2
        
def query_seg(l, r):
    l += seg_sz - 1
    r += seg_sz - 1
    res = 0
    while l <= r:
        if l % 2 == 1:
            res += tree[l]
            l += 1
        if r % 2 == 0:
            res += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return res

for i in range(1, N + 1):
    update(pos[i], penguins[i])

for i in range(N + 1):
    dsu_parent[i] = i

def query_path(u, v):
    res = 0
    while head[u] != head[v]:
        if depth[head[u]] > depth[head[v]]:
            u, v = v, u
        res += query_seg(pos[head[v]], pos[v])
        v = parent[head[v]]
    if depth[u] > depth[v]:
        u, v = v, u
    res += query_seg(pos[u], pos[v])
    return res

out = []
for op, u, v in queries:
    if op == 0:
        if find(u) != find(v):
            union(u, v)
            out.append("yes")
        else:
            out.append("no")
    elif op == 1:
        update(pos[u], v)
    elif op == 2:
        if find(u) != find(v):
            out.append("impossible")
        else:
            out.append(str(query_path(u, v)))
            
print('\n'.join(out))