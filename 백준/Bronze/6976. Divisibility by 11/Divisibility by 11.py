k = int(input())
for i in range(k):
    if i > 0:
        print()
    s = input().strip()
    n = int(s)
    print(s)
    while n >= 100:
        n = (n // 10) - (n % 10)
        print(n)
    if n % 11 == 0:
        print(f"The number {s} is divisible by 11.")
    else:
        print(f"The number {s} is not divisible by 11.")