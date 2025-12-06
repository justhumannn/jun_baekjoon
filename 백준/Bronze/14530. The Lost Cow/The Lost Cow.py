x, y = map(int, input().split())

dist = 0
cur = x
step = 1
dir = 1

while True:
    nxt = x + dir * step

    if min(cur, nxt) <= y <= max(cur, nxt):
        dist += abs(cur - y)
        break
    else:
        dist += abs(cur - nxt)
    cur = nxt
    step *= 2
    dir *= -1
print(dist)