import sys

input = sys.stdin.readline
n = int(input())
tree = [0] * 1000001
for _ in range(n):
    req = list(map(int, input().split()))
    a = req[0]
    if a == 1:
        b = req[1]
        idx = 0
        for i in range(19, -1, -1):
            step = 1 << i
            nxt = idx + step
            if nxt <= 1000000 and tree[nxt] < b:
                idx = nxt
                b -= tree[nxt]
        target = idx + 1
        print(target)
        curr = target
        while curr <= 1000000:
            tree[curr] -= 1
            curr += curr & (-curr)
    elif a == 2:
        b = req[1]
        c = req[2]
        curr = b
        while curr <= 1000000:
            tree[curr] += c
            curr += curr & (-curr)