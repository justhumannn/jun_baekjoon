N = int(input())
swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))
sum_s = 0
sum_m = 0
answer = 0
for i in range(N):
    sum_s += swifts[i]
    sum_m += semaphores[i]
    if sum_s == sum_m:
        answer = i + 1
print(answer)