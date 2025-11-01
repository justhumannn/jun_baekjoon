N = int(input())
prev = int(input())
answer = 0

for _ in range(N):
    cur = int(input())
    d = abs(prev - cur)
    answer += min(d, 360 - d)
    prev = cur

print(answer)