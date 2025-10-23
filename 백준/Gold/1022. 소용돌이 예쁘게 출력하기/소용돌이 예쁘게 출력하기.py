r1, c1, r2, c2 = map(int, input().split())

def get_value(r, c):
    n = max(abs(r), abs(c))
    max_val = (2*n + 1)**2
    if r == n:
        return max_val - (n - c)
    elif c == -n:
        return max_val - (2*n) - (n - r)
    elif r == -n:
        return max_val - (4*n) - (c + n)
    else:
        return max_val - (6*n) - (r + n)

table = [[get_value(r, c) for c in range(c1, c2+1)] for r in range(r1, r2+1)]

max_len = len(str(max(map(max, table))))

for row in table:
    print(' '.join(str(x).rjust(max_len) for x in row))