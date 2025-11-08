N, M = map(int, input().split())

for _ in range(N):
    line = input().rstrip()
    print(line[::-1])