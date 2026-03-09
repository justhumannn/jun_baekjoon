while True:
    line = input().split()
    if not line:
        break
    n, m, k = map(int, line)
    if n == 0 and m == 0 and k == 0:
        break
    callers = list(range(1, n + 1))
    index = 0
    result = 0
    for _ in range(k):
        index = (index + m - 1) % len(callers)
        result = callers.pop(index)
    print(result)