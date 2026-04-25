import sys
input = sys.stdin.readline

T_str = input().strip()
T = int(T_str or "0")
out = []
for _ in range(T):
    n = int(input())
    points = []
    for _ in range(n):
        x, y = input().split()
        points.append((int(x), int(y)))
    points.sort()
    lower = []
    for p in points:
        while len(lower) >= 2 and (lower[-1][0] - lower[-2][0]) * (p[1] - lower[-2][1]) - (lower[-1][1] - lower[-2][1]) * (p[0] - lower[-2][0]) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and (upper[-1][0] - upper[-2][0]) * (p[1] - upper[-2][1]) - (upper[-1][1] - upper[-2][1]) * (p[0] - upper[-2][0]) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    sz = len(hull)
    j = 1
    cands = []
    for i in range(sz):
        ni = (i + 1) % sz
        while sz > 2 and (hull[ni][0] - hull[i][0]) * (hull[(j + 1) % sz][1] - hull[j][1]) - (hull[ni][1] - hull[i][1]) * (hull[(j + 1) % sz][0] - hull[j][0]) > 0:
            cands.append(((hull[i][0] - hull[j][0])**2 + (hull[i][1] - hull[j][1])**2, hull[i][0], hull[i][1], hull[j][0], hull[j][1]))
            j = (j + 1) % sz
        cands.append(((hull[i][0] - hull[j][0])**2 + (hull[i][1] - hull[j][1])**2, hull[i][0], hull[i][1], hull[j][0], hull[j][1]))
    best = max(cands)
    out.append(f"{best[1]} {best[2]} {best[3]} {best[4]}")
sys.stdout.write('\n'.join(out) + '\n')