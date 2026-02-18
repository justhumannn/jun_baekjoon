n = int(input())
for _ in range(n):
    a, b = map(float, input().split())
    result = abs(a - b)
    print(f"{result:.1f}")