import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
U = int(input_data[1])
D = int(input_data[2])
S = int(input_data[3])

markets = []
idx = 4
for _ in range(N):
    T = int(input_data[idx])
    L = int(input_data[idx+1])
    M = int(input_data[idx+2])
    markets.append((T, L, M))
    idx += 3

markets.sort(key=lambda x: (x[0], x[1]))

INF = 10**15
MAX_L = 500005
OFFSET = MAX_L

tree_D = [-INF] * (2 * MAX_L)
tree_U = [-INF] * (2 * MAX_L)

idx_S = OFFSET + S
tree_D[idx_S] = D * S
curr = idx_S >> 1
while curr > 0:
    tree_D[curr] = tree_D[curr<<1] if tree_D[curr<<1] > tree_D[(curr<<1)|1] else tree_D[(curr<<1)|1]
    curr >>= 1
    
tree_U[idx_S] = -U * S
curr = idx_S >> 1
while curr > 0:
    tree_U[curr] = tree_U[curr<<1] if tree_U[curr<<1] > tree_U[(curr<<1)|1] else tree_U[(curr<<1)|1]
    curr >>= 1

i = 0
while i < N:
    j = i
    while j < N and markets[j][0] == markets[i][0]:
        j += 1
        
    k = j - i
    group_L = [0] * k
    group_M = [0] * k
    for x in range(k):
        group_L[x] = markets[i+x][1]
        group_M[x] = markets[i+x][2]
        
    P = [0] * k
    for x in range(k):
        L = group_L[x]
        
        l, r = 1 + OFFSET, L + OFFSET
        qD = -INF
        while l <= r:
            if l & 1:
                if tree_D[l] > qD: qD = tree_D[l]
                l += 1
            if not (r & 1):
                if tree_D[r] > qD: qD = tree_D[r]
                r -= 1
            l >>= 1
            r >>= 1
        qD -= D * L
        
        l, r = L + OFFSET, MAX_L - 1 + OFFSET
        qU = -INF
        while l <= r:
            if l & 1:
                if tree_U[l] > qU: qU = tree_U[l]
                l += 1
            if not (r & 1):
                if tree_U[r] > qU: qU = tree_U[r]
                r -= 1
            l >>= 1
            r >>= 1
        qU += U * L
        
        P[x] = qD if qD > qU else qU

    L_max = [0] * k
    L_max[0] = P[0] + group_M[0]
    for x in range(1, k):
        prev_val = L_max[x-1] - D * (group_L[x] - group_L[x-1]) + group_M[x]
        curr_val = P[x] + group_M[x]
        L_max[x] = prev_val if prev_val > curr_val else curr_val
        
    R_max = [0] * k
    R_max[k-1] = P[k-1] + group_M[k-1]
    for x in range(k-2, -1, -1):
        next_val = R_max[x+1] - U * (group_L[x+1] - group_L[x]) + group_M[x]
        curr_val = P[x] + group_M[x]
        R_max[x] = next_val if next_val > curr_val else curr_val
        
    for x in range(k):
        val = L_max[x] if L_max[x] > R_max[x] else R_max[x]
        L = group_L[x]
        
        idx_upd = OFFSET + L
        val_D = val + D * L
        if val_D > tree_D[idx_upd]:
            tree_D[idx_upd] = val_D
            idx_i = idx_upd >> 1
            while idx_i > 0:
                tree_D[idx_i] = tree_D[idx_i<<1] if tree_D[idx_i<<1] > tree_D[(idx_i<<1)|1] else tree_D[(idx_i<<1)|1]
                idx_i >>= 1
                
        val_U = val - U * L
        if val_U > tree_U[idx_upd]:
            tree_U[idx_upd] = val_U
            idx_i = idx_upd >> 1
            while idx_i > 0:
                tree_U[idx_i] = tree_U[idx_i<<1] if tree_U[idx_i<<1] > tree_U[(idx_i<<1)|1] else tree_U[(idx_i<<1)|1]
                idx_i >>= 1
                
    i = j

qD = -INF
l, r = 1 + OFFSET, S + OFFSET
while l <= r:
    if l & 1:
        if tree_D[l] > qD: qD = tree_D[l]
        l += 1
    if not (r & 1):
        if tree_D[r] > qD: qD = tree_D[r]
        r -= 1
    l >>= 1
    r >>= 1
ans_D = qD - D * S

qU = -INF
l, r = S + OFFSET, MAX_L - 1 + OFFSET
while l <= r:
    if l & 1:
        if tree_U[l] > qU: qU = tree_U[l]
        l += 1
    if not (r & 1):
        if tree_U[r] > qU: qU = tree_U[r]
        r -= 1
    l >>= 1
    r >>= 1
ans_U = qU + U * S

ans = ans_D if ans_D > ans_U else ans_U
print(ans)