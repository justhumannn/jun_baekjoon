A, B = map(int, input().split())
turn = 0
while True:
    if turn == 0:
        B += A
        if B >= 5:
            print("yt")
            break
    else:
        A += B
        if A >= 5:
            print("yj")
            break
    turn ^= 1