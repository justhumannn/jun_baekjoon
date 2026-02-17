N = int(input())
grid = [input() for _ in range(N)]
target = "MOBIS"
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
count = 0
for r in range(N):
    for c in range(N):
        for dr, dc in directions:
            match = True
            for i in range(5):
                nr, nc = r + dr * i, c + dc * i
                if 0 <= nr < N and 0 <= nc < N:
                    if grid[nr][nc] != target[i]:
                        match = False
                        break
                else:
                    match = False
                    break
            if match:
                count += 1
print(count)