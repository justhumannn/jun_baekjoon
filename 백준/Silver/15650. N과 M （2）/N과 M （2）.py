a,b = map(int,input().split())
if b == 1:
    for i in range(1,a+1):
        print(i)
elif b == 2:
    for i in range(1,a):
        for j in range(i+1,a+1):
            print(i,j)
elif b == 3:
    for i in range(1,a-1):
        for j in range(i+1,a):
            for k in range(j+1,a+1):
                print(i,j,k)
elif b == 4:
    for i in range(1,a-2):
        for j in range(i+1,a-1):
            for k in range(j+1,a):
                for l in range(k+1,a+1):
                    print(i,j,k,l)
elif b == 5:
    for i in range(1,a-3):
        for j in range(i+1,a-2):
            for k in range(j+1,a-1):
                for l in range(k+1,a):
                    for m in range(l+1,a+1):
                        print(i,j,k,l,m)
elif b == 6:
    for i in range(1,a-4):
        for j in range(i+1,a-3):
            for k in range(j+1,a-2):
                for l in range(k+1,a-1):
                    for m in range(l+1,a):
                        for n in range(m+1,a+1):
                            print(i,j,k,l,m,n)
elif b == 7:
    for i in range(1,a-5):
        for j in range(i+1,a-4):
            for k in range(j+1,a-3):
                for l in range(k+1,a-2):
                    for m in range(l+1,a-1):
                        for n in range(m+1,a):
                            for o in range(n+1,a+1):
                                print(i,j,k,l,m,n,o)
else:
    for i in range(1,a-6):
        for j in range(i+1,a-5):
            for k in range(j+1,a-4):
                for l in range(k+1,a-3):
                    for m in range(l+1,a-2):
                        for n in range(m+1,a-1):
                            for o in range(n+1,a):
                                for p in range(o+1,a+1):
                                    print(i,j,k,l,m,n,o,p)