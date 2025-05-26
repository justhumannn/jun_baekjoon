T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
        continue

    # 1의 자리 숫자의 패턴은 항상 주기성이 있음
    cycle = []
    x = a
    while x not in cycle:
        cycle.append(x)
        x = (x * a) % 10

    index = (b - 1) % len(cycle)
    result = cycle[index]
    print(result if result != 0 else 10)
