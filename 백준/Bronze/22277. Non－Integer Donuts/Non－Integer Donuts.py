N = int(input())
balance = int(input().replace('$', '').replace('.', ''))
late_count = 0
for _ in range(N):
    deposit = int(input().replace('$', '').replace('.', ''))
    balance += deposit
    if balance % 100 != 0:
        late_count += 1
print(late_count)