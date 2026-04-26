import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
q = int(input_data[1])

p = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
root = 0

for i in range(1, n + 1):
    p[i] = int(input_data[1 + i])
    if p[i] == 0:
        root = i
    else:
        adj[p[i]].append(i)

order = []
queue = [root]
depth = [0] * (n + 1)
up = [[0] * 18 for _ in range(n + 1)]

head = 0
while head < len(queue):
    u = queue[head]
    head += 1
    order.append(u)
    for v in adj[u]:
        depth[v] = depth[u] + 1
        up[v][0] = u
        for i in range(1, 18):
            up[v][i] = up[up[v][i-1]][i-1]
        queue.append(v)

size = [0] * (n + 1)
for u in reversed(order):
    size[u] = 1
    for v in adj[u]:
        size[u] += size[v]

in_time = [0] * (n + 1)
out_time = [0] * (n + 1)
node_at = [0] * (n + 1)
timer = 0

stack = [root]
edge_idx = [0] * (n + 1)

while stack:
    u = stack[-1]
    if edge_idx[u] == 0:
        timer += 1
        in_time[u] = timer
        node_at[timer] = u
        
    if edge_idx[u] < len(adj[u]):
        v = adj[u][edge_idx[u]]
        edge_idx[u] += 1
        stack.append(v)
    else:
        out_time[u] = timer
        stack.pop()

MAX_NODES = (n + 2) * 20
ls = [0] * MAX_NODES
rs = [0] * MAX_NODES
val = [0] * MAX_NODES
root_pst = [0] * (n + 1)
pst_cnt = 0

def insert_pst(prev, l, r, v):
    global pst_cnt
    pst_cnt += 1
    curr = pst_cnt
    new_root = curr
    
    while True:
        ls[curr] = ls[prev]
        rs[curr] = rs[prev]
        val[curr] = val[prev] + 1
        
        if l == r:
            break
            
        mid = (l + r) // 2
        if v <= mid:
            pst_cnt += 1
            ls[curr] = pst_cnt
            curr = ls[curr]
            prev = ls[prev]
            r = mid
        else:
            pst_cnt += 1
            rs[curr] = pst_cnt
            curr = rs[curr]
            prev = rs[prev]
            l = mid + 1
    return new_root

for i in range(1, n + 1):
    root_pst[i] = insert_pst(root_pst[i - 1], 1, n, node_at[i])

queries = [[] for _ in range(n + 1)]
idx = 2 + n

ans = [0] * q
for j in range(q):
    k = int(input_data[idx])
    idx += 1
    
    x = (k - 1) // n + 1
    rem = (k - 1) % n + 1
    queries[x].append((rem, j))

bit = [0] * (n + 1)

def fenwick_add(i, v):
    while i <= n:
        bit[i] += v
        i += i & (-i)
        
def fenwick_find_kth(k):
    i = 0
    for step in range(17, -1, -1):
        next_i = i + (1 << step)
        if next_i <= n and bit[next_i] < k:
            i = next_i
            k -= bit[i]
    return i + 1, k

def get_jump(u, k_step):
    for i in range(18):
        if (k_step >> i) & 1:
            u = up[u][i]
    return u

def query_pst(a1, a2, s1, s2, l, r, k):
    while l < r:
        mid = (l + r) // 2
        left_val = 0
        if a1: left_val += val[ls[a1]]
        if a2: left_val += val[ls[a2]]
        if s1: left_val -= val[ls[s1]]
        if s2: left_val -= val[ls[s2]]
        
        if left_val >= k:
            a1 = ls[a1] if a1 else 0
            a2 = ls[a2] if a2 else 0
            s1 = ls[s1] if s1 else 0
            s2 = ls[s2] if s2 else 0
            r = mid
        else:
            k -= left_val
            a1 = rs[a1] if a1 else 0
            a2 = rs[a2] if a2 else 0
            s1 = rs[s1] if s1 else 0
            s2 = rs[s2] if s2 else 0
            l = mid + 1
    return l

stack2 = [root]
edge_idx2 = [0] * (n + 1)

fenwick_add(root, size[root])

while stack2:
    u = stack2[-1]
    
    if edge_idx2[u] == 0:
        for rem, j in queries[u]:
            z, r_prime = fenwick_find_kth(rem)
            
            if z == u:
                w = 0
            else:
                w = get_jump(u, depth[u] - depth[z] - 1)
                
            if w == 0:
                a1 = root_pst[out_time[z]]
                s1 = root_pst[in_time[z] - 1]
                a2 = s2 = 0
            else:
                a1 = root_pst[in_time[w] - 1]
                s1 = root_pst[in_time[z] - 1]
                a2 = root_pst[out_time[z]]
                s2 = root_pst[out_time[w]]
                
            y = query_pst(a1, a2, s1, s2, 1, n, r_prime)
            
            ans[j] = (u - 1) * n * n + (z - 1) * n + (y - 1)
            
    if edge_idx2[u] < len(adj[u]):
        v = adj[u][edge_idx2[u]]
        edge_idx2[u] += 1
        
        fenwick_add(u, -size[v])
        fenwick_add(v, size[v])
        stack2.append(v)
    else:
        stack2.pop()
        if stack2:
            p_node = stack2[-1]
            fenwick_add(u, -size[u])
            fenwick_add(p_node, size[u])

print('\n'.join(map(str, ans)))