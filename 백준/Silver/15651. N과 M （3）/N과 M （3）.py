a,b = map(int,input().split())
if b == 1:
    for i in range(1,a+1):
        print(i)
elif b == 2:
    for i in range(1,a+1):
        for j in range(1,a+1):
            print(i,j)
elif b == 3:
    for i in range(1,a+1):
        for j in range(1,a+1):
            for k in range(1,a+1):
                print(i,j,k)
elif b == 4:
    for i in range(1,a+1):
        for j in range(1,a+1):
            for k in range(1,a+1):
                for l in range(1,a+1):
                    print(i,j,k,l)
elif b == 5:
    for i in range(1,a+1):
        for j in range(1,a+1):
            for k in range(1,a+1):
                for l in range(1,a+1):
                    for m in range(1,a+1):
                        print(i,j,k,l,m)
elif b == 6:
    for i in range(1,a+1):
        for j in range(1,a+1):
            for k in range(1,a+1):
                for l in range(1,a+1):
                    for m in range(1,a+1):
                        for n in range(1,a+1):
                            print(i,j,k,l,m,n)
else:
    for i in range(1,a+1):
        for j in range(1,a+1):
            for k in range(1,a+1):
                for l in range(1,a+1):
                    for m in range(1,a+1):
                        for n in range(1,a+1):
                            for o in range(1,a+1):
                                print(i,j,k,l,m,n,o)