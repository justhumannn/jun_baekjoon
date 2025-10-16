import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
used1 = [0] * (2 * n)
used2 = [0] * (2 * n)

blacks, whites = [], []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if (i + j) % 2 == 0:
                blacks.append((i, j))
            else:
                whites.append((i, j))

def dfs(idx, bishops, cells):
    if idx == len(cells):
        return bishops
    r, c = cells[idx]
    res = dfs(idx + 1, bishops, cells)

    if not used1[r + c] and not used2[r - c + n]:
        used1[r + c] = used2[r - c + n] = 1
        res = max(res, dfs(idx + 1, bishops + 1, cells))
        used1[r + c] = used2[r - c + n] = 0
    return res

ans = dfs(0, 0, blacks) + dfs(0, 0, whites)
print(ans)