#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

#define MAX 300

int night[8][2] = {
    {-1, 2}, {-1, -2}, {-2, -1}, {-2, 1},
    {1, 2}, {1, -2}, {2, -1}, {2, 1}
};

typedef struct {
    int x, y;
} Point;

typedef struct {
    Point data[MAX * MAX];
    int front, rear;
} Queue;

void initQueue(Queue *q) {
    q->front = q->rear = 0;
}

bool isEmpty(Queue *q) {
    return q->front == q->rear;
}

void push(Queue *q, int x, int y) {
    q->data[q->rear].x = x;
    q->data[q->rear].y = y;
    q->rear++;
}

Point pop(Queue *q) {
    return q->data[q->front++];
}

int bfs(int size, int startX, int startY, int endX, int endY) {
    bool visited[MAX][MAX] = {false};
    int chess_board[MAX][MAX];
    Queue q;
    initQueue(&q);

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            chess_board[i][j] = INT_MAX;
        }
    }

    chess_board[startX][startY] = 0;
    visited[startX][startY] = true;
    push(&q, startX, startY);

    while (!isEmpty(&q)) {
        Point cur = pop(&q);
        int cx = cur.x;
        int cy = cur.y;

        if (cx == endX && cy == endY) {
            return chess_board[cx][cy];
        }

        for (int i = 0; i < 8; i++) {
            int nx = cx + night[i][0];
            int ny = cy + night[i][1];

            if (nx >= 0 && nx < size && ny >= 0 && ny < size && !visited[nx][ny]) {
                visited[nx][ny] = true;
                chess_board[nx][ny] = chess_board[cx][cy] + 1;
                push(&q, nx, ny);
            }
        }
    }

    return -1;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int size;
        scanf("%d", &size);

        int startX, startY;
        int endX, endY;
        scanf("%d %d", &startX, &startY);
        scanf("%d %d", &endX, &endY);

        printf("%d\n", bfs(size, startX, startY, endX, endY));
    }

    return 0;
}
