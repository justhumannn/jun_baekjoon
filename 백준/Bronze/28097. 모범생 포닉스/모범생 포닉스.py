a = int(input())
b = list(map(int, input().split()))
result = sum(b) + (a-1) * 8
print(result // 24,result % 24)