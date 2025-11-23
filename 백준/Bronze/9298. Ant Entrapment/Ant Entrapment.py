import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xs = []
    ys = []
    for _ in range(N):
        x, y = map(float, input().split())
        xs.append(x)
        ys.append(y)

    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)

    width = xmax - xmin
    height = ymax - ymin

    area = width * height
    perimeter = 2 * (width + height)

    print(f"Case {tc}: Area {area}, Perimeter {perimeter}")