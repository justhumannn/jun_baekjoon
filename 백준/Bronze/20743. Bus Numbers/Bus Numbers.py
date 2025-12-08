import sys
m = int(sys.stdin.readline())
limit = int(round(m ** (1/3))) + 1

count = {}

for a in range(1, limit + 1):
    a3 = a * a * a
    if a3 > m:
        break
    for b in range(a, limit + 1):
        s = a3 + b * b * b
        if s > m:
            break
        count[s] = count.get(s, 0) + 1

bus_numbers = [k for k, v in count.items() if v >= 2]

if bus_numbers:
    print(max(bus_numbers))
else:
    print("none")