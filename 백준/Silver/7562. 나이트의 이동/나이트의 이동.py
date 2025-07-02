from collections import deque
a = int(input())
night = [(-1,2),(-1,-2),(-2,-1),(-2,1),(1,2),(1,-2),(2,-1),(2,1)]
for _ in range(a):
    b = int(input())
    visited = [[False] * b for _ in range(b)]
    chess_board = [[float('inf')] * b for _ in range(b)]
    c,d = map(int, input().split())
    chess_board[c][d] = 0
    sequence = deque([(c,d)])
    visited[c][d] = True
    e,f = map(int, input().split())
    while sequence:
        node1,node2 = sequence.popleft()
        if node1 == e and node2 == f:
            print(chess_board[node1][node2])
            break
        for i,j in night:
            if 0 <= node1 + i < b and 0 <= node2 + j < b and not visited[node1 + i][node2 + j]:
                chess_board[node1+i][node2+j] = min(chess_board[node1+i][node2+j], chess_board[node1][node2]+1)
                sequence.append((node1+i,node2+j))
                visited[node1+i][node2+j] = True