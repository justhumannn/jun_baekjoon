import sys
from array import array
input = sys.stdin.readline

n = int(input())
w = [0] + list(map(int, input().split()))

h = n.bit_length()
leaf = 1 << (h - 1)

rows = [array('q', [0] * (1 << dep)) for dep in range(h)]
x_idx = [0] * h

stack = [(1, 0, 0)]
while stack:
    node, dep, state = stack.pop()
    if node > n:
        continue
    if state == 0:
        stack.append((node * 2 + 1, dep + 1, 0))
        stack.append((node, dep, 1))
        stack.append((node * 2, dep + 1, 0))
    else:
        rows[dep][x_idx[dep]] = w[node]
        x_idx[dep] += 1

full_mat = [[0] * n for _ in range(h)]
node_dep = [-1] * n

for dep in range(h):
    stride = leaf >> dep
    row_len = 1 << dep
    for j in range(row_len):
        xc = stride * (2 * j + 1) - 1
        full_mat[dep][xc] = rows[dep][j]
        node_dep[xc] = dep

ans = -10**18

for top in range(h):
    temp = [0] * n
    for bottom in range(top, h):
        for x in range(n):
            temp[x] += full_mat[bottom][x]

        cur = -10**18
        has_real = False
        for x in range(n):
            nd = node_dep[x]
            in_range = (top <= nd <= bottom)
            if cur <= 0:
                if in_range:
                    cur = temp[x]
                    has_real = True
                else:
                    cur = -10**18
                    has_real = False
            else:
                cur += temp[x]
                if in_range:
                    has_real = True
            if has_real and cur > ans:
                ans = cur

print(ans)