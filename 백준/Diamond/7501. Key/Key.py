import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n <= a: break
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True
a, b = map(int, input().split())
ans = []
for k in range(a, b + 1):
    if k % 2 == 1:
        if k == 9 or is_prime(k):
            ans.append(k)
sys.stdout.write(" ".join(map(str, ans)) + "\n")