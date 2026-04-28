import sys
import math
from functools import cmp_to_key
from collections import defaultdict

input_data = sys.stdin.read().split()

N = int(input_data[0])
pts = []
idx = 1
for _ in range(N):
    pts.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])))
    idx += 3
    
pts.sort(key=lambda x: (x[0], x[1]))

X = [0] * N
Y = [0] * N
W = [0] * N
for i in range(N):
    X[i], Y[i], W[i] = pts[i]
    
pos = list(range(N))
p = list(range(N))

sz = 1
while sz < N:
    sz <<= 1
    
tot = [0] * (sz << 1)
lmax = [0] * (sz << 1)
rmax = [0] * (sz << 1)
mmax = [0] * (sz << 1)

def update(idx, val):
    idx += sz
    tot[idx] = val
    if val > 0:
        lmax[idx] = rmax[idx] = mmax[idx] = val
    else:
        lmax[idx] = rmax[idx] = mmax[idx] = 0
    
    p_idx = idx >> 1
    while p_idx:
        left = p_idx << 1
        right = left | 1
        
        t_l = tot[left]
        t_r = tot[right]
        tot[p_idx] = t_l + t_r
        
        lm_l = lmax[left]
        rm_r = rmax[right]
        
        cand1 = t_l + lmax[right]
        lmax[p_idx] = lm_l if lm_l > cand1 else cand1
        
        cand2 = t_r + rmax[left]
        rmax[p_idx] = rm_r if rm_r > cand2 else cand2
        
        m1 = mmax[left]
        m2 = mmax[right]
        m3 = rmax[left] + lmax[right]
        
        mx = m1
        if m2 > mx: mx = m2
        if m3 > mx: mx = m3
        mmax[p_idx] = mx
        
        p_idx >>= 1

for i in range(N):
    update(i, W[i])
    
max_ans = mmax[1]

slopes = defaultdict(list)
for i in range(N):
    xi, yi = X[i], Y[i]
    for j in range(i+1, N):
        dx = X[j] - xi
        dy = Y[j] - yi
        g = math.gcd(dx, abs(dy))
        slopes[(dx//g, dy//g)].append((i, j))
        
def cmp(k1, k2):
    dx1, dy1 = k1
    dx2, dy2 = k2
    if dx1 == 0 and dx2 == 0: return 0
    if dx1 == 0: return 1
    if dx2 == 0: return -1
    val = dy1 * dx2 - dy2 * dx1
    if val < 0: return -1
    if val > 0: return 1
    return 0
    
sorted_slopes = sorted(slopes.keys(), key=cmp_to_key(cmp))

for slope in sorted_slopes:
    dx, dy = slope
    lines = {}
    for u, v in slopes[slope]:
        C = dy * X[u] - dx * Y[u]
        if C not in lines:
            lines[C] = [u, v]
        else:
            lines[C].append(u)
            lines[C].append(v)
            
    for C, pts_list in lines.items():
        unique_pts = list(set(pts_list))
        min_p = N
        max_p = -1
        for x in unique_pts:
            cur = pos[x]
            if cur < min_p: min_p = cur
            if cur > max_p: max_p = cur
            
        left, right = min_p, max_p
        while left < right:
            p[left], p[right] = p[right], p[left]
            pos[p[left]] = left
            pos[p[right]] = right
            left += 1
            right -= 1
            
        for idx in range(min_p, max_p + 1):
            update(idx, W[p[idx]])
            
    if mmax[1] > max_ans:
        max_ans = mmax[1]
        
print(max_ans)