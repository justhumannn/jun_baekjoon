T = int(input())
for _ in range(T):
    N, A, D = map(int, input().split())
    total = N * (2*A + (N-1)*D) // 2
    print(total)