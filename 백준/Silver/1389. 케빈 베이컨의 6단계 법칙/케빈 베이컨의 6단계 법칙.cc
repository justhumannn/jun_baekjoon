#include <stdio.h>
#define INF 1000000000

int main() {
    int a, bus;
    scanf("%d %d", &a, &bus);
    int cost[a + 1][a + 1];
    int cabin[a + 1];
    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= a; j++) {
            if (i == j)
                cost[i][j] = 0;
            else
                cost[i][j] = INF;
        }
    }
    for (int i = 0; i < bus; i++) {
        int b, d;
        scanf("%d %d", &b, &d);
        cost[b][d] = 1;
        cost[d][b] = 1;
    }
    for (int k = 1; k <= a; k++) {
        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= a; j++) {
                if (cost[i][k] + cost[k][j] < cost[i][j]) {
                    cost[i][j] = cost[i][k] + cost[k][j];
                }
            }
        }
    }
    int minSum = INF;
    int result = 0;
    for (int i = 1; i <= a; i++) {
        int sum = 0;
        for (int j = 1; j <= a; j++) {
            sum += cost[i][j];
        }
        if (sum < minSum) {
            minSum = sum;
            result = i;
        }
    }
    printf("%d\n", result);
    return 0;
}