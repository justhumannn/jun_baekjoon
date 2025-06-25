a = int(input())
b = [0]
for _ in range(a):
    b.append(int(input()))
dp_score = [0] * (a + 1)
if a >= 1:
    dp_score[1] = b[1]
if a >= 2:
    dp_score[2] = b[1] + b[2]
for i in range(3, a+1):
    dp_score[i] = (max(b[i - 1] + dp_score[i-3] + b[i], dp_score[i - 2] + b[i]))
print(dp_score[a])