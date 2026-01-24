N = int(input())
if N <= 28:
    count = 1
    while True:
        current_sum = count * (count + 1) // 2
        if current_sum >= N:
            print(count)
            break
        count += 1
else:
    target = N + 21
    ans = target // 7
    if target % 7 != 0:
        ans += 1
    print(ans)