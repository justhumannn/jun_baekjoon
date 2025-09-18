import sys, random
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def mulmod(a, b, mod):
    return (a * b) % mod

def powmod(a, d, mod):
    r = 1
    while d:
        if d & 1:
            r = mulmod(r, a, mod)
        a = mulmod(a, a, mod)
        d >>= 1
    return r
def is_prime(n):
    if n < 2:
        return False
    small = [2,3,5,7,11,13,17,19,23,29,31,37]
    if n in small:
        return True
    if any(n % p == 0 for p in small):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = powmod(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = mulmod(x, x, n)
            if x == n-1:
                break
        else:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        c = random.randrange(1, n)
        f = lambda x: (mulmod(x, x, n) + c) % n
        x, y, d = 2, 2, 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        if d != n:
            return d
def factorize(n, res):
    if n == 1:
        return
    if is_prime(n):
        res.append(n)
        return
    d = pollard_rho(n)
    factorize(d, res)
    factorize(n // d, res)

n = int(input())
res = []
factorize(n, res)
res.sort()
for x in res:
    print(x)