import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
rects = []
idx = 1
for _ in range(N):
    w = int(input_data[idx])
    h = int(input_data[idx+1])
    idx += 2
    rects.append((w, h))

rects.sort()

filtered = []
for w, h in rects:
    while filtered and filtered[-1][1] <= h:
        filtered.pop()
    filtered.append((w, h))

M = len(filtered)
W = [0] * (M + 1)
H = [0] * (M + 1)
for i in range(M):
    W[i+1] = filtered[i][0]
    H[i+1] = filtered[i][1]

dp = [0] * (M + 1)

lines_m = [0] * (M + 1)
lines_c = [0] * (M + 1)
lines_m[0] = H[1]
lines_c[0] = 0

head = 0
tail = 1

for i in range(1, M + 1):
    x = W[i]
    
    while tail - head >= 2:
        m1, c1 = lines_m[head], lines_c[head]
        m2, c2 = lines_m[head+1], lines_c[head+1]
        if (c2 - c1) <= x * (m1 - m2):
            head += 1
        else:
            break
            
    dp[i] = lines_m[head] * x + lines_c[head]
    
    if i < M:
        nm = H[i+1]
        nc = dp[i]
        
        while tail - head >= 2:
            m1, c1 = lines_m[tail-2], lines_c[tail-2]
            m2, c2 = lines_m[tail-1], lines_c[tail-1]
            
            if (c2 - c1) * (m2 - nm) >= (nc - c2) * (m1 - m2):
                tail -= 1
            else:
                break
        
        lines_m[tail] = nm
        lines_c[tail] = nc
        tail += 1

print(dp[M])