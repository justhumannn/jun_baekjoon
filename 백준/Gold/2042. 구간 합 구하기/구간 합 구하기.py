import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = [0]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
tree = [0] * (n + 1)
for i in range(1, n + 1):
    tree[i] += arr[i]
    nxt = i + (i & (-i))
    if nxt <= n:
        tree[nxt] += tree[i]
for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        idx = b
        while idx <= n:
            tree[idx] += diff
            idx += idx & (-idx)
    elif a == 2:
        sum_c = 0
        idx = c
        while idx > 0:
            sum_c += tree[idx]
            idx -= idx & (-idx)
        sum_b_minus_1 = 0
        idx = b - 1
        while idx > 0:
            sum_b_minus_1 += tree[idx]
            idx -= idx & (-idx)
        print(sum_c - sum_b_minus_1)