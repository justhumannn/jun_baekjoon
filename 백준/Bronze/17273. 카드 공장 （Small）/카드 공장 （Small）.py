N, M = map(int, input().split())

cards = []
for _ in range(N):
    A, B = map(int, input().split())
    cards.append([A, B])
visible_front = [True] * N
commands = [int(input()) for _ in range(M)]
for K in commands:
    for i in range(N):
        current_value = cards[i][0] if visible_front[i] else cards[i][1]
        if current_value <= K:
            visible_front[i] = not visible_front[i]  # 뒤집기
result = 0
for i in range(N):
    result += cards[i][0] if visible_front[i] else cards[i][1]

print(result)