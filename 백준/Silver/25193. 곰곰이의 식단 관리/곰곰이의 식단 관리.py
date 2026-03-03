N = int(input())
S = input()
chicken = S.count('C')
others = N - chicken
if others == 0:
    print(chicken)
else:
    slots = others + 1
    ans = chicken // slots
    if chicken % slots != 0:
        ans += 1
    print(ans)