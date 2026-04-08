import sys
input = sys.stdin.readline

n, m = map(int, input().split())
min_tree = [1000000001] * (2 * n)
max_tree = [0] * (2 * n)
for i in range(n):
    val = int(input())
    min_tree[n + i] = val
    max_tree[n + i] = val
for i in range(n - 1, 0, -1):
    left = i << 1
    right = left | 1
    min_tree[i] = min_tree[left] if min_tree[left] < min_tree[right] else min_tree[right]
    max_tree[i] = max_tree[left] if max_tree[left] > max_tree[right] else max_tree[right]
for _ in range(m):
    a, b = map(int, input().split())
    a += n - 1
    b += n - 1
    ans_min = 1000000001
    ans_max = 0
    while a <= b:
        if a & 1:
            if min_tree[a] < ans_min:
                ans_min = min_tree[a]
            if max_tree[a] > ans_max:
                ans_max = max_tree[a]
            a += 1
        if not (b & 1):
            if min_tree[b] < ans_min:
                ans_min = min_tree[b]
            if max_tree[b] > ans_max:
                ans_max = max_tree[b]
            b -= 1
        a >>= 1
        b >>= 1
    print(ans_min, ans_max)