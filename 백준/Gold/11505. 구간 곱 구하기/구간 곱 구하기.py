import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
tree = [1] * (2 * n)
for i in range(n):
    tree[n + i] = int(input())
for i in range(n - 1, 0, -1):
    tree[i] = (tree[i << 1] * tree[(i << 1) | 1]) % 1000000007
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = b - 1 + n
        tree[idx] = c
        idx >>= 1
        while idx > 0:
            tree[idx] = (tree[idx << 1] * tree[(idx << 1) | 1]) % 1000000007
            idx >>= 1
    elif a == 2:
        l = b - 1 + n
        r = c - 1 + n
        res = 1
        
        while l <= r:
            if l & 1:
                res = (res * tree[l]) % 1000000007
                l += 1
            if not (r & 1):
                res = (res * tree[r]) % 1000000007
                r -= 1
            l >>= 1
            r >>= 1
        print(res)