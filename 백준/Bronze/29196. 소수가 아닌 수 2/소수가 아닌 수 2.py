k = input().strip()
if '.' in k:
    integer, frac = k.split('.')
    p = int(frac)
    q = 10 ** len(frac)
else:
    p = int(k)
    q = 1
print("YES")
print(p, q)