from collections import deque

def bfs(x, y, field, visited, M, N):
    # 상하좌우 이동 방향
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N:
                if field[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    M, N, K = map(int, input().split())
    # 배추밭 초기화
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    # 배추 심기
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    worm_count = 0

    # 전체 필드를 순회하며 BFS 실행
    for i in range(N):  # y 좌표 (세로)
        for j in range(M):  # x 좌표 (가로)
            if field[i][j] == 1 and not visited[i][j]:
                bfs(j, i, field, visited, M, N)
                worm_count += 1

    print(worm_count)
