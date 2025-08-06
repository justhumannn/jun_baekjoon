#include <stdio.h>

#define MAX 1001

int graph[MAX][MAX];
int indegree[MAX];
int queue[MAX];
int front = 0, rear = 0;
int a, b;

void enqueue(int x) {
    queue[rear++] = x;
}

int dequeue() {
    return queue[front++];
}

int main() {
    scanf("%d %d", &a, &b);
    for (int i = 1; i <= a; i++) {
        indegree[i] = 0;
        for (int j = 1; j <= a; j++) {
            graph[i][j] = 0;
        }
    }
    for (int t = 0; t < b; t++) {
        int cnt;
        scanf("%d", &cnt);
        int prev, cur;
        if (cnt > 0) {
            scanf("%d", &prev);
            for (int i = 1; i < cnt; i++) {
                scanf("%d", &cur);
                if (!graph[prev][cur]) {
                    graph[prev][cur] = 1;
                    indegree[cur]++;
                }
                prev = cur;
            }
        }
    }
    for (int i = 1; i <= a; i++) {
        if (indegree[i] == 0) {
            enqueue(i);
        }
    }
    int sequence[MAX];
    int seqIndex = 0;
    while (front < rear) {
        int num = dequeue();
        sequence[seqIndex++] = num;
        for (int i = 1; i <= a; i++) {
            if (graph[num][i]) {
                indegree[i]--;
                if (indegree[i] == 0) {
                    enqueue(i);
                }
            }
        }
    }
    if (seqIndex != a) {
        printf("0\n");
    } else {
        for (int i = 0; i < seqIndex; i++) {
            printf("%d\n", sequence[i]);
        }
    }
    return 0;
}