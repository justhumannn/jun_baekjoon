a = input()
if a[0] == '1' and a[2] == '2' and a[4] == '3' and a[6] == '4' and a[8] == '5' and a[10] == '6' and a[12] == '7' and a[14] == '8':
    print('ascending')
elif a[0] == '8' and a[2] == '7' and a[4] == '6' and a[6] == '5' and a[8] == '4' and a[10] == '3' and a[12] == '2' and a[14] == '1':
    print('descending')
else:
    print('mixed')