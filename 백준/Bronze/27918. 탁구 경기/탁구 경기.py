a = int(input())
b, c = 0, 0
for _ in range(a):
    winner = input().strip()
    if winner == 'D':
        b += 1
    else:
        c += 1
    if abs(b - c) >= 2:
        break
print(f"{b}:{c}")