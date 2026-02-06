import math

i = 1
while True:
    try:
        line = input().split()
        if not line:
            break
        a, b, c = map(int, line)
        
        if a == 0 and b == 0 and c == 0:
            break

        print(f"Triangle #{i}")

        if c == -1:
            print(f"c = {math.sqrt(a**2 + b**2):.3f}")
        elif a == -1:
            if c <= b:
                print("Impossible.")
            else:
                print(f"a = {math.sqrt(c**2 - b**2):.3f}")
        elif b == -1:
            if c <= a:
                print("Impossible.")
            else:
                print(f"b = {math.sqrt(c**2 - a**2):.3f}")
        
        print()
        i += 1
    except EOFError:
        break