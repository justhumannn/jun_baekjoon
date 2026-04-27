import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
Q = int(input_data[1])

adj = [[] for _ in range(N + 1)]
idx = 2
for _ in range(N - 1):
    u, v = int(input_data[idx]), int(input_data[idx+1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2
    
parent = [0] * (N + 1)
depth = [0] * (N + 1)
order = [1]

children = [[] for _ in range(N + 1)]
head = 0
while head < len(order):
    u = order[head]
    head += 1
    for v in adj[u]:
        if v != parent[u]:
            parent[v] = u
            depth[v] = depth[u] + 1
            children[u].append(v)
            order.append(v)
            
sz = [1] * (N + 1)
for u in reversed(order):
    if not children[u]:
        continue
    heavy_sz = 0
    heavy_idx = 0
    for i, v in enumerate(children[u]):
        sz[u] += sz[v]
        if sz[v] > heavy_sz:
            heavy_sz = sz[v]
            heavy_idx = i
    children[u][0], children[u][heavy_idx] = children[u][heavy_idx], children[u][0]
    
top = [0] * (N + 1)
in_time = [0] * (N + 1)
timer = 0

stack = [1]
top[1] = 1
while stack:
    u = stack.pop()
    in_time[u] = timer
    timer += 1
    
    if not children[u]:
        continue
        
    for i in range(len(children[u]) - 1, 0, -1):
        v = children[u][i]
        top[v] = v
        stack.append(v)
        
    hv = children[u][0]
    top[hv] = top[u]
    stack.append(hv)
    
H = 19
SZ = 524288

tree = [0] * (2 * SZ)
lazy_add = [0] * (2 * SZ)
lazy_mul = [1] * (2 * SZ)
length = [0] * (2 * SZ)

for i in range(SZ, 2 * SZ):
    length[i] = 1
for i in range(SZ - 1, 0, -1):
    length[i] = length[i<<1] + length[i<<1|1]
    
def push_down(p):
    for s in range(H, 0, -1):
        i = p >> s
        if lazy_mul[i] != 1 or lazy_add[i] != 0:
            m, a = lazy_mul[i], lazy_add[i]
            
            left = i << 1
            tree[left] = (tree[left] * m + a * length[left]) & 0xFFFFFFFF
            if left < SZ:
                lazy_mul[left] = (lazy_mul[left] * m) & 0xFFFFFFFF
                lazy_add[left] = (lazy_add[left] * m + a) & 0xFFFFFFFF
                
            right = left | 1
            tree[right] = (tree[right] * m + a * length[right]) & 0xFFFFFFFF
            if right < SZ:
                lazy_mul[right] = (lazy_mul[right] * m) & 0xFFFFFFFF
                lazy_add[right] = (lazy_add[right] * m + a) & 0xFFFFFFFF
                
            lazy_mul[i] = 1
            lazy_add[i] = 0

def push_up(p):
    p >>= 1
    while p:
        tree[p] = ((tree[p<<1] + tree[p<<1|1]) * lazy_mul[p] + lazy_add[p] * length[p]) & 0xFFFFFFFF
        p >>= 1

def update_seg(L, R, m, a):
    L += SZ
    R += SZ
    L0, R0 = L, R
    push_down(L0)
    push_down(R0)
    
    while L <= R:
        if L & 1:
            tree[L] = (tree[L] * m + a * length[L]) & 0xFFFFFFFF
            if L < SZ:
                lazy_mul[L] = (lazy_mul[L] * m) & 0xFFFFFFFF
                lazy_add[L] = (lazy_add[L] * m + a) & 0xFFFFFFFF
            L += 1
        if not (R & 1):
            tree[R] = (tree[R] * m + a * length[R]) & 0xFFFFFFFF
            if R < SZ:
                lazy_mul[R] = (lazy_mul[R] * m) & 0xFFFFFFFF
                lazy_add[R] = (lazy_add[R] * m + a) & 0xFFFFFFFF
            R -= 1
        L >>= 1
        R >>= 1
        
    push_up(L0)
    push_up(R0)

def query_seg(L, R):
    L += SZ
    R += SZ
    push_down(L)
    push_down(R)
    res = 0
    while L <= R:
        if L & 1:
            res = (res + tree[L]) & 0xFFFFFFFF
            L += 1
        if not (R & 1):
            res = (res + tree[R]) & 0xFFFFFFFF
            R -= 1
        L >>= 1
        R >>= 1
    return res
    
def update_path(u, v, m, a):
    while top[u] != top[v]:
        if depth[top[u]] < depth[top[v]]:
            u, v = v, u
        update_seg(in_time[top[u]], in_time[u], m, a)
        u = parent[top[u]]
    if depth[u] > depth[v]:
        u, v = v, u
    update_seg(in_time[u], in_time[v], m, a)

def query_path(u, v):
    res = 0
    while top[u] != top[v]:
        if depth[top[u]] < depth[top[v]]:
            u, v = v, u
        res = (res + query_seg(in_time[top[u]], in_time[u])) & 0xFFFFFFFF
        u = parent[top[u]]
    if depth[u] > depth[v]:
        u, v = v, u
    res = (res + query_seg(in_time[u], in_time[v])) & 0xFFFFFFFF
    return res

ans = []
for _ in range(Q):
    op = int(input_data[idx])
    if op == 1:
        X, V = int(input_data[idx+1]), int(input_data[idx+2])
        idx += 3
        update_seg(in_time[X], in_time[X] + sz[X] - 1, 1, V)
    elif op == 2:
        X, Y, V = int(input_data[idx+1]), int(input_data[idx+2]), int(input_data[idx+3])
        idx += 4
        update_path(X, Y, 1, V)
    elif op == 3:
        X, V = int(input_data[idx+1]), int(input_data[idx+2])
        idx += 3
        update_seg(in_time[X], in_time[X] + sz[X] - 1, V, 0)
    elif op == 4:
        X, Y, V = int(input_data[idx+1]), int(input_data[idx+2]), int(input_data[idx+3])
        idx += 4
        update_path(X, Y, V, 0)
    elif op == 5:
        X = int(input_data[idx+1])
        idx += 2
        ans.append(str(query_seg(in_time[X], in_time[X] + sz[X] - 1)))
    elif op == 6:
        X, Y = int(input_data[idx+1]), int(input_data[idx+2])
        idx += 3
        ans.append(str(query_path(X, Y)))
        
print('\n'.join(ans))