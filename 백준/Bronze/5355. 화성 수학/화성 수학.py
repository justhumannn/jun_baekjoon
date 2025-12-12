T = int(input())

for _ in range(T):
    parts = input().split()
    num = float(parts[0])

    for op in parts[1:]:
        if op == '@':
            num *= 3
        elif op == '%':
            num += 5
        elif op == '#':
            num -= 7

    print(f"{num:.2f}")