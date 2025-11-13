record = input().strip()

a = b = 0

for i in range(0, len(record), 2):
    player = record[i]
    points = int(record[i + 1])

    if player == 'A':
        a += points
    else:
        b += points
    if a >= 11 or b >= 11:
        if (a >= 11 and a - b >= 2) or (a >= 11 and b < 10):
            print('A')
            break
        elif (b >= 11 and b - a >= 2) or (b >= 11 and a < 10):
            print('B')
            break
