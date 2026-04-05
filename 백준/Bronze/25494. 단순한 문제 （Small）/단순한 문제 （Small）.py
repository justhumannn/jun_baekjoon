import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())
    count = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            x_mod_y = x % y
            for z in range(1, c + 1):
                if x_mod_y == y % z and x_mod_y == z % x:
                    count += 1             
    print(count)