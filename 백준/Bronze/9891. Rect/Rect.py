import sys

input = sys.stdin.read
data = input().split()

if not data:
    exit()

iterator = iter(data)
try:
    n = int(next(iterator))
except StopIteration:
    exit()

rects = []
for _ in range(n):
    x1 = int(next(iterator))
    y1 = int(next(iterator))
    x2 = int(next(iterator))
    y2 = int(next(iterator))
    
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    
    if w > h:
        rects.append((h, w))
    else:
        rects.append((w, h))

rects.sort()

max_h = 10005
tree = [0] * max_h

def update(i):
    i += 1
    while i < max_h:
        tree[i] += 1
        i += i & (-i)

def query(i):
    i += 1
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & (-i)
    return s

comparable_pairs = 0

for w, h in rects:
    comparable_pairs += query(h)
    update(h)

total_pairs = n * (n - 1) // 2
print(total_pairs - comparable_pairs)