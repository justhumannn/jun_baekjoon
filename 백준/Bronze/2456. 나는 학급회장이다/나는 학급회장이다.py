a = int(input())
b = [] # 1번 후보
c = [] # 2번 후보
d = [] # 3번 후보
b2, c2, d2 = 0,0,0
for i in range(0,a):
    b1, c1, d1 = map(int,input().split())
    b.append(b1)
    c.append(c1)
    d.append(d1)
    b2 += b1
    c2 += c1
    d2 += d1
b3 = b.count(3)
c3 = c.count(3)
d3 = d.count(3)
b4 = b.count(2)
c4 = c.count(2)
d4 = d.count(2)
if b2 > c2:
    if b2 > d2:
        print(1,b2)
    elif b2 < d2:
        print(3,d2)
    else:
        if b3 > d3:
            print(1,b2)
        elif b3 < d3:
            print(3,d2)
        else:
            if b4 > d4:
                print(1,b2)
            elif b4 < d4:
                print(3,d2)
            else:
                print(0,b2) 
elif b2 < c2:
    if c2 > d2:
        print(2,c2)
    elif c2 < d2:
        print(3,d2)
    else:
        if c3 > d3:
            print(2,c2)
        elif c3 < d3:
            print(3,d2)
        else:
            if c4 > d4:
                print(2,c2)
            elif c4 < d4:
                print(3,d2)
            else:
                print(0,c2)
elif b2 == c2 and c2 < d2:
    print(3,d2)
elif b2 == c2 and c2 != d2:
    if b3 > c3:
        print(1,b2)
    elif b3 < c3:
            print(2,c2)
    else:
        if b4 > c4:
            print(1,b2)
        elif b4 < c4:
            print(2,c2)
        else:
            print(0,b2)
else:
    if b3 > c3:
        if b3 > d3:
            print(1,b2)
        elif b3 < d3:
            print(3,d2)
        else:
            if b4 > d4:
                print(1,b2)
            elif b4 < d4:
                print(3,d2)
            else:
                print(0,b2)
    elif b3 < c3:
        if c3 > d3:
            print(2,c2)
        elif c3 < d3:
            print(3,d2)
        else:
            if c4 > d4:
                print(2,c2)
            elif b4 < d4:
                print(3,d2)
            else:
                print(0,c2)
    elif b3 == c3 and c3 < d3:
        print(3,d2)
    elif b3 == c3 and c3 != d3:
        if b4 > c4:
            print(1,b2)
        elif b4 < c4:
            print(2,c4)
        else:
            print(0,b2)
    else:
        if b4 > c4:
            if b4 > d4:
                print(1,b2)
            elif b4 < d4:
                print(3,d2)
            else:
                print(0,b2)
        elif b4 < c4:
            if c4 > d4:
                print(2,c2)
            elif b4 < d4:
                print(3,d2)
            else:
                print(0,c2)
        elif b4 == c4 and c4 < d4:
            print(3,d2)
        else:
            print(0,b2)