d = {'red': 1, 'yellow': 2, 'green': 3, 'brown': 4, 'blue': 5, 'pink': 6, 'black': 7}
n = int(input())
r = 0
o = []

for _ in range(n):
    s = input().strip()
    if s == 'red':
        r += 1
    else:
        o.append(d[s])

if not o:
    if r > 0:
        print(1)
    else:
        print(0)
elif r == 0:
    print(sum(o))
else:
    print(r * (max(o) + 1) + sum(o))