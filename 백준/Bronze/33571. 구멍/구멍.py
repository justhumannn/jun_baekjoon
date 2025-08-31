a = input().rstrip()
comp = "ABBDOPQRabdegopq@"
ans = 0
for c in a:
    ans += comp.count(c)
print(ans)