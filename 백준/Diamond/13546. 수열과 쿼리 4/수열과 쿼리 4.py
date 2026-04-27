import sys
input_data = sys.stdin.read().split()
    
N = int(input_data[0])
K = int(input_data[1])
A = [0] * (N + 1)
for i in range(1, N + 1):
    A[i] = int(input_data[1 + i])
M = int(input_data[N + 2])
queries = []
idx = N + 3
for i in range(M):
    l = int(input_data[idx])
    r = int(input_data[idx+1])
    queries.append((l, r, i))
    idx += 2
B = int(N / (M ** 0.5))
if B < 1:
    B = 1
queries.sort(key=lambda q: (q[0] // B, q[1]))
ans = [0] * M
first_occ = [0] * (K + 1)
last_occ = [0] * (K + 1)
naive_first_occ = [0] * (K + 1)
blocks = {}
for q in queries:
    b = q[0] // B
    if b not in blocks:
        blocks[b] = []
    blocks[b].append(q)
    
for b in sorted(blocks.keys()):
    group = blocks[b]
    R_start = (b + 1) * B
    R_curr = R_start - 1
    max_ans = 0
    
    for l, r, q_idx in group:
        if r < R_start:
            tmp_ans = 0
            for i in range(l, r + 1):
                x = A[i]
                if naive_first_occ[x] == 0:
                    naive_first_occ[x] = i
                else:
                    dist = i - naive_first_occ[x]
                    if dist > tmp_ans:
                        tmp_ans = dist
            for i in range(l, r + 1):
                naive_first_occ[A[i]] = 0
            ans[q_idx] = tmp_ans
        else:
            while R_curr < r:
                R_curr += 1
                x = A[R_curr]
                if first_occ[x] == 0:
                    first_occ[x] = R_curr
                last_occ[x] = R_curr
                dist = R_curr - first_occ[x]
                if dist > max_ans:
                    max_ans = dist
                    
            tmp_ans = max_ans
            for i in range(R_start - 1, l - 1, -1):
                x = A[i]
                if last_occ[x] == 0:
                    last_occ[x] = i
                dist = last_occ[x] - i
                if dist > tmp_ans:
                    tmp_ans = dist
                    
            ans[q_idx] = tmp_ans
            
            for i in range(l, R_start):
                x = A[i]
                if last_occ[x] < R_start:
                    last_occ[x] = 0
                    
    for i in range(R_start, R_curr + 1):
        x = A[i]
        first_occ[x] = 0
        last_occ[x] = 0

print('\n'.join(map(str, ans)))