H, W, N, M = map(int, input().split())
rows = (H + N) // (N + 1)
cols = (W + M) // (M + 1)
print(rows * cols)
