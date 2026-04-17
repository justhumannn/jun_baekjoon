import sys
input = sys.stdin.readline

n = int(input())
arr = input().split()
m = int(input())
queries = [[] for _ in range(n + 1)]
for q_idx in range(m):
    l, r = map(int, input().split())
    queries[r].append((l, q_idx))
ans = [0] * m
bit = [0] * (n + 1)
last_seen = {}
for i in range(1, n + 1):
    val = arr[i - 1]
    if val in last_seen:
        prev = last_seen[val]
        idx_bit = prev
        while idx_bit <= n:
            bit[idx_bit] -= 1
            idx_bit += idx_bit & -idx_bit
    last_seen[val] = i
    idx_bit = i
    while idx_bit <= n:
        bit[idx_bit] += 1
        idx_bit += idx_bit & -idx_bit
    if queries[i]:
        total_distinct = len(last_seen)
        for l, q_idx in queries[i]:
            sum_l_minus_1 = 0
            idx_bit = l - 1
            while idx_bit > 0:
                sum_l_minus_1 += bit[idx_bit]
                idx_bit -= idx_bit & -idx_bit
            ans[q_idx] = total_distinct - sum_l_minus_1
sys.stdout.write('\n'.join(map(str, ans)) + '\n')