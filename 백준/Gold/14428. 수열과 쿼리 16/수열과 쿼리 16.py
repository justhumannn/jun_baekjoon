import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
tree = [(10000000001, 10000000001)] * (2 * n)
for i in range(n):
    tree[n + i] = (arr[i], i + 1)
for i in range(n - 1, 0, -1):
    left = i << 1
    right = left | 1
    tree[i] = tree[left] if tree[left] < tree[right] else tree[right]
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        idx = query[1] - 1 + n
        tree[idx] = (query[2], query[1])
        idx >>= 1
        while idx > 0:
            left = idx << 1
            right = left | 1
            tree[idx] = tree[left] if tree[left] < tree[right] else tree[right]
            idx >>= 1
    elif query[0] == 2:
        l = query[1] - 1 + n
        r = query[2] - 1 + n
        res = (10000000001, 10000000001)
        while l <= r:
            if l & 1:
                if tree[l] < res:
                    res = tree[l]
                l += 1
            if not (r & 1):
                if tree[r] < res:
                    res = tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        print(res[1])