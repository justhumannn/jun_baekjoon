import sys

input = sys.stdin.readline

n, t = map(int, input().split())
a = list(map(int, input().split()))

block_size = int(n ** 0.5) + 1

queries = []
for i in range(t):
    l, r = map(int, input().split())
    queries.append((l - 1, r - 1, i))
    
queries.sort(key=lambda x: (x[0] // block_size, x[1] if (x[0] // block_size) % 2 == 0 else -x[1]))

ans = [0] * t
cnt = [0] * 1000005

curr_l, curr_r = 0, -1
power = 0

for l, r, idx in queries:
    while curr_l > l:
        curr_l -= 1
        v = a[curr_l]
        c = cnt[v]
        power += (2 * c + 1) * v
        cnt[v] += 1
        
    while curr_r < r:
        curr_r += 1
        v = a[curr_r]
        c = cnt[v]
        power += (2 * c + 1) * v
        cnt[v] += 1
        
    while curr_l < l:
        v = a[curr_l]
        cnt[v] -= 1
        c = cnt[v]
        power -= (2 * c + 1) * v
        curr_l += 1
        
    while curr_r > r:
        v = a[curr_r]
        cnt[v] -= 1
        c = cnt[v]
        power -= (2 * c + 1) * v
        curr_r -= 1
        
    ans[idx] = power
    
for i in range(t):
    print(ans[i])