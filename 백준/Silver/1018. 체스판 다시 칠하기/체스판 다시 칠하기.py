a, b = map(int, input().split())
board = [input().strip() for _ in range(a)]
def count_repaints(x, y):
    patterns = ['W','B']
    min_paint = float('inf')
    for k in patterns:
        c = 0
        for i in range(8):
            for j in range(8):
                expected = k if (i + j) % 2 == 0 else ('B' if k == 'W' else 'W')
                if board[x + i][y + j] != expected:
                    c += 1
        min_paint = min(min_paint, c)
    return min_paint
result = float('inf')
for i in range(a-7):
    for j in range(b-7):
        result = min(result, count_repaints(i, j))
print(result)