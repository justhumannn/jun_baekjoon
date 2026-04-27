import sys

input_data = sys.stdin.read().split()

m = int(input_data[0])
n = int(input_data[1])
q = int(input_data[2])

ptr = 3
mn = m * n

heights_flat = [0] * mn
nodes = [None] * mn

for i in range(mn):
    h = int(input_data[ptr])
    ptr += 1
    heights_flat[i] = h
    nodes[i] = (h, i)
    
nodes.sort(key=lambda x: x[0])

parent = list(range(mn))

def find(i):
    curr = i
    while parent[curr] != curr:
        curr = parent[curr]
    p = i
    while p != curr:
        nxt = parent[p]
        parent[p] = curr
        p = nxt
    return curr

tree_p = [-1] * mn
visited = [False] * mn

for i in range(mn):
    h, u = nodes[i]
    visited[u] = True
    
    r = u // n
    c = u % n
    
    if r > 0:
        v = u - n
        if visited[v]:
            root_v = find(v)
            if root_v != u:
                tree_p[root_v] = u
                parent[root_v] = u
    if r < m - 1:
        v = u + n
        if visited[v]:
            root_v = find(v)
            if root_v != u:
                tree_p[root_v] = u
                parent[root_v] = u
    if c > 0:
        v = u - 1
        if visited[v]:
            root_v = find(v)
            if root_v != u:
                tree_p[root_v] = u
                parent[root_v] = u
    if c < n - 1:
        v = u + 1
        if visited[v]:
            root_v = find(v)
            if root_v != u:
                tree_p[root_v] = u
                parent[root_v] = u

depth = [0] * mn
for i in range(mn - 1, -1, -1):
    h, u = nodes[i]
    if tree_p[u] != -1:
        depth[u] = depth[tree_p[u]] + 1
        
LOG = 19
up = [-1] * (mn * LOG)

for i in range(mn):
    up[i] = tree_p[i]
    
for j in range(1, LOG):
    curr_offset = j * mn
    prev_offset = (j - 1) * mn
    for i in range(mn):
        prev = up[prev_offset + i]
        if prev != -1:
            up[curr_offset + i] = up[prev_offset + prev]
            
out = []
for _ in range(q):
    x1 = int(input_data[ptr]) - 1
    y1 = int(input_data[ptr+1]) - 1
    x2 = int(input_data[ptr+2]) - 1
    y2 = int(input_data[ptr+3]) - 1
    ptr += 4
    
    u = x1 * n + y1
    v = x2 * n + y2
    
    if depth[u] < depth[v]:
        u, v = v, u
    
    diff = depth[u] - depth[v]
    for j in range(LOG):
        if (diff >> j) & 1:
            u = up[j * mn + u]
            
    if u == v:
        out.append(str(heights_flat[u]))
        continue
        
    for j in range(LOG - 1, -1, -1):
        offset = j * mn
        anc_u = up[offset + u]
        anc_v = up[offset + v]
        if anc_u != anc_v:
            u = anc_u
            v = anc_v
            
    lca = up[u]
    out.append(str(heights_flat[lca]))
    
sys.stdout.write('\n'.join(out) + '\n')