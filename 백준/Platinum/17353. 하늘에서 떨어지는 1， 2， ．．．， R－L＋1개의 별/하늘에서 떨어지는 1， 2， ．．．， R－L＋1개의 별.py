import sys

tokens = sys.stdin.read().split()
n = int(tokens[0])
A = [0] + [int(x) for x in tokens[1:n+1]]
size = n + 2
b1 = [0] * (size + 1)
b2 = [0] * (size + 1)
def add(b, idx, val):
    while idx <= size:
        b[idx] += val
        idx += idx & -idx
def query(b, idx):
    s = 0
    while idx > 0:
        s += b[idx]
        idx -= idx & -idx
    return s
def range_add(l, r, val):
    add(b1, l, val)
    add(b1, r + 1, -val)
    add(b2, l, val * (l - 1))
    add(b2, r + 1, -val * r)
ans = []
idx = n + 2
q = int(tokens[n + 1])
for _ in range(q):
    cmd = int(tokens[idx])
    if cmd == 1:
        L = int(tokens[idx+1])
        R = int(tokens[idx+2])
        idx += 3
        range_add(L, R, 1)
        range_add(R + 1, R + 1, -(R - L + 1))
    else:
        X = int(tokens[idx+1])
        idx += 2
        val = A[X] + query(b1, X) * X - query(b2, X)
        ans.append(str(val))
sys.stdout.write('\n'.join(ans) + '\n')