import sys
from math import gcd

data = sys.stdin.read().split()
N = int(data[0])
A = [int(x) for x in data[1:N+1]]
Q = int(data[N+1])
ptr = N + 2

D = [0] * N
D[0] = A[0]
for i in range(1, N):
    D[i] = A[i] - A[i-1]

bit = [0] * (N + 1)
def update_bit(i, val):
    i += 1
    while i <= N:
        bit[i] += val
        i += i & (-i)
        
def get_bit(i):
    i += 1
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

for i in range(N):
    update_bit(i, D[i])

tree = [0] * (2 * N)
for i in range(N):
    tree[N + i] = abs(D[i])
for i in range(N - 1, 0, -1):
    tree[i] = gcd(tree[i << 1], tree[i << 1 | 1])

def update_seg(i, val):
    idx = i + N
    tree[idx] = abs(val)
    while idx > 1:
        idx >>= 1
        tree[idx] = gcd(tree[idx << 1], tree[idx << 1 | 1])

def query_seg(l, r):
    l += N
    r += N
    res = 0
    while l < r:
        if l & 1:
            res = gcd(res, tree[l])
            l += 1
        if r & 1:
            r -= 1
            res = gcd(res, tree[r])
        l >>= 1
        r >>= 1
    return res

out = []
for _ in range(Q):
    T = int(data[ptr])
    L = int(data[ptr+1]) - 1
    R = int(data[ptr+2]) - 1
    ptr += 3
    
    if T != 0:
        D[L] += T
        update_bit(L, T)
        update_seg(L, D[L])
        if R + 1 < N:
            D[R+1] -= T
            update_bit(R + 1, -T)
            update_seg(R + 1, D[R+1])
    else:
        ans = gcd(abs(get_bit(L)), query_seg(L + 1, R + 1))
        out.append(str(ans))
        
sys.stdout.write('\n'.join(out) + '\n')