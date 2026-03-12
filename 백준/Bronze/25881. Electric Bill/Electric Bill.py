r1, r2 = map(int, input().split())
n = int(input())
for _ in range(n):
    usage = int(input())
    if usage <= 1000:
        bill = usage * r1
    else:
        bill = (1000 * r1) + ((usage - 1000) * r2)
    print(usage, bill)