a, b, c = map(int, input().split())
print(a * b // c, end="")
rem = (a * b) % c
if rem != 0:
    print(".", end="")
    for _ in range(20):
        rem *= 10
        print(rem // c, end="")
        rem %= c
else:
    print(".0")
print()