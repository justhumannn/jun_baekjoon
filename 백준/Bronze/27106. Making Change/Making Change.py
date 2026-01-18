import sys

input = sys.stdin.readline
p = int(input().strip())
change = 100 - p
coins = [25, 10, 5, 1]
result = []
for coin in coins:
    count = change // coin
    result.append(count)
    change %= coin
print(*(result))