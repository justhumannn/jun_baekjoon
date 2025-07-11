import sys
input = sys.stdin.readline
a = int(input())
sum1, start, end, count = 1, 1, 1, 0
while start <= a:
    if sum1 < a:
        end += 1
        sum1 += end
    elif sum1 > a:
        sum1 -= start
        start += 1
    else:
        count += 1
        sum1 -= start
        start += 1
print(count)
