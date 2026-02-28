T = int(input())
for _ in range(T):
    card_num = input().strip()
    total_sum = 0
    for i in range(16):
        digit = int(card_num[i])
        if i % 2 == 0:
            digit *= 2
            if digit >= 10:
                digit = (digit // 10) + (digit % 10) 
        total_sum += digit
    if total_sum % 10 == 0:
        print("T")
    else:
        print("F")