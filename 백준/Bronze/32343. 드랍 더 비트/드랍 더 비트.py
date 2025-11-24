N = int(input())
a, b = map(int, input().split())
if a + b <= N:
    D = a + b
else:
    D = 2 * N - (a + b)
if D == 0:
    print(0)
else:
    print((1 << N) - (1 << (N - D)))