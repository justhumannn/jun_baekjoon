import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])

D = [int(x) for x in input_data[1:n]]

X = [0] * n
for i in range(n - 1):
    X[i+1] = X[i] + D[i]
    
P = [int(x) for x in input_data[n::2]]
S = [int(x) for x in input_data[n+1::2]]

INF = 10**18

tree_m = [0] * (4 * n + 5)
tree_c = [INF] * (4 * n + 5)

dp = 0

for i in range(n - 1):
    m = S[i]
    c = dp + P[i] - S[i] * X[i]
    
    node = 1
    l = 0
    r = n - 1
    while True:
        mid = (l + r) >> 1
        curr_m = tree_m[node]
        curr_c = tree_c[node]
        
        val_new = m * X[mid] + c
        val_curr = curr_m * X[mid] + curr_c
        
        if val_new < val_curr:
            tree_m[node] = m
            tree_c[node] = c
            m = curr_m
            c = curr_c
            
        if l == r:
            break
            
        loser_val_l = m * X[l] + c
        winner_val_l = tree_m[node] * X[l] + tree_c[node]
        
        if loser_val_l < winner_val_l:
            node = node << 1
            r = mid
        else:
            node = (node << 1) | 1
            l = mid + 1
            
    x_idx = i + 1
    x = X[x_idx]
    
    node = 1
    l = 0
    r = n - 1
    res = INF
    while True:
        val = tree_m[node] * x + tree_c[node]
        if val < res:
            res = val
            
        if l == r:
            break
            
        mid = (l + r) >> 1
        if x_idx <= mid:
            node = node << 1
            r = mid
        else:
            node = (node << 1) | 1
            l = mid + 1
            
    dp = res
    
print(dp)