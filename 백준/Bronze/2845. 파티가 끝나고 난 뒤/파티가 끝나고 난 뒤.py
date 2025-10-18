L, P = map(int, input().split())
nums = list(map(int, input().split()))
total = L * P
print(*[x - total for x in nums])
