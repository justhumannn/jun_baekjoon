a, b, c = map(int, input().split())
def f(a, b, c):
    if b == 0:
        return 1
    t = f(a, b // 2, c)
    t %= c
    if b % 2 == 0:
        return (t * t) % c
    else:
        return (t * t * (a % c)) % c

print(f(a, b, c))