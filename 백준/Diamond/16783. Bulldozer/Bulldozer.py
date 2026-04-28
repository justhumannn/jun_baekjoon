import sys
from math import gcd

input_data = sys.stdin.buffer.read().split()

N = int(input_data[0])

pts = []
idx = 1
for _ in range(N):
    pts.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])))
    idx += 3

pts.sort(key=lambda x: (x[0], x[1]))

X = [pt[0] for pt in pts]
Y = [pt[1] for pt in pts]
W = [pt[2] for pt in pts]

pos = list(range(N))
p = list(range(N))

sz = 1
while sz < N:
    sz <<= 1

tot = [0] * (sz << 1)
lmax = [0] * (sz << 1)
rmax = [0] * (sz << 1)
mmax = [0] * (sz << 1)

def update(index, val):
    index += sz
    tot[index] = val
    v = val if val > 0 else 0
    lmax[index] = rmax[index] = mmax[index] = v

    p_idx = index >> 1
    while p_idx:
        left = p_idx << 1
        right = left | 1

        t_l = tot[left]; t_r = tot[right]
        tot[p_idx] = t_l + t_r

        lm_l = lmax[left]; lr = t_l + lmax[right]
        lmax[p_idx] = lm_l if lm_l > lr else lr

        rm_r = rmax[right]; rl = t_r + rmax[left]
        rmax[p_idx] = rm_r if rm_r > rl else rl

        m1 = mmax[left]; m2 = mmax[right]; m3 = rmax[left] + lmax[right]
        mx = m1 if m1 > m2 else m2
        mmax[p_idx] = mx if mx > m3 else m3

        p_idx >>= 1

for i in range(N):
    update(i, W[i])

max_ans = mmax[1]

def normalize(dy, dx):
    if dx < 0: dy, dx = -dy, -dx
    elif dx == 0:
        dy = 1
    g = gcd(abs(dy), dx) if dx != 0 else abs(dy)
    return (dy // g, dx // g) if g else (dy, dx)

events = []
for i in range(N):
    xi, yi = X[i], Y[i]
    for j in range(i + 1, N):
        dy = Y[j] - yi
        dx = X[j] - xi
        if dx < 0: dy, dx = -dy, -dx
        elif dx == 0: dy = 1
        g = gcd(abs(dy), dx) if dx != 0 else abs(dy)
        if g > 1: dy //= g; dx //= g
        events.append((dy, dx, i, j))

events.sort()

n_events = len(events)
idx = 0
epoch = 0
visited = [-1] * N

while idx < n_events:
    start_idx = idx
    dy0, dx0 = events[idx][0], events[idx][1]

    idx += 1
    while idx < n_events and events[idx][0] == dy0 and events[idx][1] == dx0:
        idx += 1

    pair_count = idx - start_idx

    if pair_count == 1:
        u = events[start_idx][2]
        v = events[start_idx][3]
        left = pos[u]
        right = pos[v]
        if left > right:
            left, right = right, left

        p[left], p[right] = p[right], p[left]
        pos[p[left]] = left
        pos[p[right]] = right
        update(left, W[p[left]])
        update(right, W[p[right]])
    else:
        epoch += 1
        unique_pts = []
        for k in range(start_idx, idx):
            u = events[k][2]
            v = events[k][3]
            if visited[u] != epoch:
                visited[u] = epoch
                unique_pts.append(u)
            if visited[v] != epoch:
                visited[v] = epoch
                unique_pts.append(v)

        unique_pts.sort(key=lambda x: pos[x])

        i = 0
        k_len = len(unique_pts)
        while i < k_len:
            start_pt = unique_pts[i]
            C = X[start_pt] * dy0 - Y[start_pt] * dx0
            j = i + 1
            while j < k_len:
                pt = unique_pts[j]
                if X[pt] * dy0 - Y[pt] * dx0 == C:
                    j += 1
                else:
                    break

            left = pos[unique_pts[i]]
            right = pos[unique_pts[j - 1]]

            while left < right:
                u = p[left]; v = p[right]
                p[left] = v; p[right] = u
                pos[u] = left; pos[v] = right
                update(left, W[v])
                update(right, W[u])
                left += 1
                right -= 1

            i = j

    if mmax[1] > max_ans:
        max_ans = mmax[1]

print(max_ans)