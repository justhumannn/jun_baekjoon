a = int(input())
sum = 0
apart = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,0]]*15
for i in range(1,15):
    apart[i] = [0]*14
    for j in range(0,14):
        for k in range(0,j+1):
            apart[i][j] += apart[i-1][k]
for _ in range(a):
    k = int(input())
    n = int(input())
    print(apart[k][n-1])