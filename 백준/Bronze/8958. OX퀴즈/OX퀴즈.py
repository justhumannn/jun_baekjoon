a = int(input())
for _ in range(a):
    num,score = 0,0
    ans = input()
    for i in range(0,len(ans)):
        if ans[i] == 'O':
            num += 1
            score += num
        else:
            num = 0
    print(score)