a = int(input())
for _ in range(a):
    fast_hotel_num = []
    h,w,n = map(int,input().split())
    for i in range(1,w+1):
        for j in range(1,h+1):
            if i < 10:
                j *= 10
            j = str(j)
            i = str(i)
            hotel_num = j + i
            fast_hotel_num.append(hotel_num)
            i = int(i)
            j = int(j)
    print(fast_hotel_num[n-1])