import sys
import collections

input_data = sys.stdin.read().split()

T = int(input_data[0])
idx = 1
out = []

for _ in range(T):
    n = int(input_data[idx])
    m = int(input_data[idx+1])
    idx += 2
    
    grid = input_data[idx : idx+n]
    idx += n
    
    b_count = 0
    w_count = 0
    b_id = [-1] * (n * m)
    w_id = [-1] * (n * m)
    
    for r in range(n):
        row = grid[r]
        for c in range(m):
            if row[c] == 'B':
                b_id[r * m + c] = b_count
                b_count += 1
            elif row[c] == 'W':
                w_id[r * m + c] = w_count
                w_count += 1
                
    if w_count != 2 * b_count or b_count == 0:
        out.append("NO")
        continue
        
    U_count = w_count
    V_count = 2 * b_count
    
    max_edges = 4 * U_count
    head = [-1] * U_count
    to = [0] * max_edges
    nxt = [0] * max_edges
    edge_cnt = 0
    
    for r in range(n):
        row = grid[r]
        for c in range(m):
            if row[c] == 'W':
                u = w_id[r * m + c]
                if c > 0 and grid[r][c-1] == 'B':
                    to[edge_cnt] = b_id[r * m + c - 1]
                    nxt[edge_cnt] = head[u]
                    head[u] = edge_cnt
                    edge_cnt += 1
                if c < m - 1 and grid[r][c+1] == 'B':
                    to[edge_cnt] = b_id[r * m + c + 1]
                    nxt[edge_cnt] = head[u]
                    head[u] = edge_cnt
                    edge_cnt += 1
                if r > 0 and grid[r-1][c] == 'B':
                    to[edge_cnt] = b_id[(r - 1) * m + c] + b_count
                    nxt[edge_cnt] = head[u]
                    head[u] = edge_cnt
                    edge_cnt += 1
                if r < n - 1 and grid[r+1][c] == 'B':
                    to[edge_cnt] = b_id[(r + 1) * m + c] + b_count
                    nxt[edge_cnt] = head[u]
                    head[u] = edge_cnt
                    edge_cnt += 1
                    
    match_U = [-1] * U_count
    match_V = [-1] * V_count
    dist = [0] * (U_count + 1)
    INF_NODE = U_count
    INF = 10**9
    
    ptr = [0] * U_count
    v_stack = [-1] * U_count
    
    def bfs():
        queue = collections.deque()
        for u in range(U_count):
            if match_U[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[INF_NODE] = INF
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[INF_NODE]:
                e = head[u]
                while e != -1:
                    v = to[e]
                    match_u_next = match_V[v]
                    if match_u_next == -1:
                        dist[INF_NODE] = dist[u] + 1
                    elif dist[match_u_next] == INF:
                        dist[match_u_next] = dist[u] + 1
                        queue.append(match_u_next)
                    e = nxt[e]
        return dist[INF_NODE] != INF
        
    def dfs_iter(start_u):
        stack = [start_u]
        
        while stack:
            u = stack[-1]
            advanced = False
            
            e = ptr[u]
            while e != -1:
                v = to[e]
                ptr[u] = nxt[e]
                
                match_u_next = match_V[v]
                if match_u_next == -1:
                    match_V[v] = u
                    match_U[u] = v
                    stack.pop()
                    while stack:
                        prev_u = stack.pop()
                        prev_v = v_stack[prev_u]
                        match_V[prev_v] = prev_u
                        match_U[prev_u] = prev_v
                    return True
                elif dist[match_u_next] == dist[u] + 1:
                    v_stack[u] = v
                    stack.append(match_u_next)
                    advanced = True
                    break
                    
                e = ptr[u]
                
            if not advanced:
                dist[u] = INF
                stack.pop()
                
        return False

    matching_size = 0
    while bfs():
        for i in range(U_count):
            ptr[i] = head[i]
        for u in range(U_count):
            if match_U[u] == -1:
                if dfs_iter(u):
                    matching_size += 1
                    
    if matching_size == U_count:
        out.append("YES")
    else:
        out.append("NO")
        
print('\n'.join(out))