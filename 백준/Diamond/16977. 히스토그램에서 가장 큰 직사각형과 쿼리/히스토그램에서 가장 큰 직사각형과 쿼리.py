import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
H = [int(x) for x in input_data[1:N+1]]
Q = int(input_data[N+1])

Q_l = []
Q_r = []
Q_w = []

idx = N + 2
for _ in range(Q):
    Q_l.append(int(input_data[idx]) - 1)
    Q_r.append(int(input_data[idx+1]) - 1)
    Q_w.append(int(input_data[idx+2]))
    idx += 3
    
U_list = sorted(list(set(H)))
K = len(U_list)
val_to_idx = {val: i for i, val in enumerate(U_list)}
pos = [[] for _ in range(K)]
for i, h in enumerate(H):
    pos[val_to_idx[h]].append(i)
    
N_pow2 = 1
while N_pow2 < N:
    N_pow2 <<= 1
    
tree_len = [0] * (2 * N_pow2)
for i in range(N_pow2):
    tree_len[N_pow2 + i] = 1
for i in range(N_pow2 - 1, 0, -1):
    tree_len[i] = tree_len[i << 1] + tree_len[(i << 1) | 1]
    
q_L = [0] * Q
q_R = [K - 1] * Q

mids = [[] for _ in range(K)]

while True:
    active_queries = False
    for i in range(Q):
        L = q_L[i]
        R = q_R[i]
        if L < R:
            active_queries = True
            mid = (L + R + 1) // 2
            mids[mid].append(i)
            
    if not active_queries:
        break
        
    tree_max = [0] * (2 * N_pow2)
    tree_pref = [0] * (2 * N_pow2)
    tree_suff = [0] * (2 * N_pow2)
    
    for x in range(K - 1, -1, -1):
        for p in pos[x]:
            curr = N_pow2 + p
            tree_max[curr] = 1
            tree_pref[curr] = 1
            tree_suff[curr] = 1
            curr >>= 1
            while curr > 0:
                l_node = curr << 1
                r_node = l_node | 1
                
                tp_l = tree_pref[l_node]
                tl_l = tree_len[l_node]
                if tp_l == tl_l:
                    tree_pref[curr] = tl_l + tree_pref[r_node]
                else:
                    tree_pref[curr] = tp_l
                    
                ts_r = tree_suff[r_node]
                tl_r = tree_len[r_node]
                if ts_r == tl_r:
                    tree_suff[curr] = tl_r + tree_suff[l_node]
                else:
                    tree_suff[curr] = ts_r
                    
                m1 = tree_max[l_node]
                m2 = tree_max[r_node]
                m3 = tree_suff[l_node] + tree_pref[r_node]
                
                nm = m1 if m1 > m2 else m2
                if m3 > nm:
                    nm = m3
                tree_max[curr] = nm
                
                curr >>= 1
                
        if mids[x]:
            for q_idx in mids[x]:
                l = Q_l[q_idx]
                r = Q_r[q_idx]
                w = Q_w[q_idx]
                
                L_node = l + N_pow2
                R_node = r + N_pow2
                left_nodes = []
                right_nodes = []
                while L_node <= R_node:
                    if L_node & 1:
                        left_nodes.append(L_node)
                        L_node += 1
                    if not (R_node & 1):
                        right_nodes.append(R_node)
                        R_node -= 1
                    L_node >>= 1
                    R_node >>= 1
                    
                cur_max = 0
                cur_pref = 0
                cur_suff = 0
                cur_len = 0
                
                for node in left_nodes:
                    new_len = cur_len + tree_len[node]
                    if cur_pref == cur_len:
                        new_pref = cur_pref + tree_pref[node]
                    else:
                        new_pref = cur_pref
                        
                    ts_n = tree_suff[node]
                    tl_n = tree_len[node]
                    if ts_n == tl_n:
                        new_suff = tl_n + cur_suff
                    else:
                        new_suff = ts_n
                        
                    m1 = cur_max
                    m2 = tree_max[node]
                    m3 = cur_suff + tree_pref[node]
                    new_max = m1 if m1 > m2 else m2
                    if m3 > new_max:
                        new_max = m3
                        
                    cur_max = new_max
                    cur_pref = new_pref
                    cur_suff = new_suff
                    cur_len = new_len
                    
                for i in range(len(right_nodes)-1, -1, -1):
                    node = right_nodes[i]
                    new_len = cur_len + tree_len[node]
                    if cur_pref == cur_len:
                        new_pref = cur_pref + tree_pref[node]
                    else:
                        new_pref = cur_pref
                        
                    ts_n = tree_suff[node]
                    tl_n = tree_len[node]
                    if ts_n == tl_n:
                        new_suff = tl_n + cur_suff
                    else:
                        new_suff = ts_n
                        
                    m1 = cur_max
                    m2 = tree_max[node]
                    m3 = cur_suff + tree_pref[node]
                    new_max = m1 if m1 > m2 else m2
                    if m3 > new_max:
                        new_max = m3
                        
                    cur_max = new_max
                    cur_pref = new_pref
                    cur_suff = new_suff
                    cur_len = new_len
                    
                if cur_max >= w:
                    q_L[q_idx] = x
                else:
                    q_R[q_idx] = x - 1
                    
            mids[x].clear()
            
out = [str(U_list[q_L[i]]) for i in range(Q)]
print('\n'.join(out))