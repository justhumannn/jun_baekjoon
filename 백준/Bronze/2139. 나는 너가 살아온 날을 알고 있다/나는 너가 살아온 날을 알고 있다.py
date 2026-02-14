import sys

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
            
        d, m, y = map(int, line.split())
        
        if d == 0 and m == 0 and y == 0:
            break
        
        is_leap = False
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            is_leap = True
            
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if is_leap:
            days_in_month[1] = 29
            
        total_days = sum(days_in_month[:m-1]) + d
        
        print(total_days)
        
    except EOFError:
        break