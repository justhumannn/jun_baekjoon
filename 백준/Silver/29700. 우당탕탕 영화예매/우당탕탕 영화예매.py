n, m, k = map(int, input().split())
ans = 0
for _ in range(n):
    row = input()
    cnt = 0
    for x in row:
        if x == '0':
            cnt += 1
            if cnt >= k:
                ans += 1
        else:
            cnt = 0           
print(ans)