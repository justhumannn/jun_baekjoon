a,b,c = input().split()
while a != '#':
    if int(b) > 17 or int(c) >= 80:
        print(a ,'Senior')
    else:
        print(a ,'Junior')
    a,b,c = input().split()