T = int(input())
for tc in range(1, T + 1):
    D, K, N = map(int, input().split())
    dancers = list(range(1, D + 1))
    for i in range(1, N + 1):
        if i % 2 == 1:
            for j in range(0, D, 2):
                dancers[j], dancers[j + 1] = dancers[j + 1], dancers[j]
        else:
            for j in range(0, D, 2):
                a = (-j) % D
                b = (-j - 1) % D
                dancers[a], dancers[b] = dancers[b], dancers[a]
    idx = dancers.index(K)
    left = dancers[(idx + 1) % D]
    right = dancers[(idx - 1) % D]
    print(f"Case #{tc}: {left} {right}")