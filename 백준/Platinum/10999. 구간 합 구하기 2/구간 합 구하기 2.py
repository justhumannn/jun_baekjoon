import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
bit1 = [0] * (n + 2)
bit2 = [0] * (n + 2)
def update(bit, i, val):
    while i <= n:
        bit[i] += val
        i += i & -i
def query(bit, i):
    ans = 0
    while i > 0:
        ans += bit[i]
        i -= i & -i
    return ans
def range_update(l, r, val):
    update(bit1, l, val)
    update(bit1, r + 1, -val)
    update(bit2, l, val * (l - 1))
    update(bit2, r + 1, -val * r)
def prefix_sum(i):
    return query(bit1, i) * i - query(bit2, i)
for i in range(1, n + 1):
    val = int(input())
    range_update(i, i, val)
for _ in range(m + k):
    q = list(map(int, input().split()))
    if q[0] == 1:
        range_update(q[1], q[2], q[3])
    else:
        sys.stdout.write(str(prefix_sum(q[2]) - prefix_sum(q[1] - 1)) + '\n')