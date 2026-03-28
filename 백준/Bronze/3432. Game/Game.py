import sys

z_str = sys.stdin.readline().strip()
if z_str:
    z = int(z_str)
    
    for _ in range(z):
        board = []
        for _ in range(5):
            board.append(sys.stdin.readline().strip())
            
        a_win = False
        b_win = False
        
        for i in range(5):
            for j in range(5):
                target = board[i][j]
                
                if target not in ('A', 'B'):
                    continue
                    
                if j <= 2 and board[i][j+1] == target and board[i][j+2] == target:
                    if target == 'A':
                        a_win = True
                    else:
                        b_win = True
                        
                if i <= 2 and board[i+1][j] == target and board[i+2][j] == target:
                    if target == 'A':
                        a_win = True
                    else:
                        b_win = True
                        
                if i <= 2 and j <= 2 and board[i+1][j+1] == target and board[i+2][j+2] == target:
                    if target == 'A':
                        a_win = True
                    else:
                        b_win = True
                        
                if i >= 2 and j <= 2 and board[i-1][j+1] == target and board[i-2][j+2] == target:
                    if target == 'A':
                        a_win = True
                    else:
                        b_win = True
                        
        if a_win and not b_win:
            print("A wins")
        elif b_win and not a_win:
            print("B wins")
        else:
            print("draw")