#include <stdio.h>
#define MIN(a,b) ((a)<(b)?(a):(b))
int main() {
    int a;
    scanf("%d", &a);
    int cost[1001][3];
    int dp[1001][3];
    for (int i = 0; i < a; i++) {
        scanf("%d %d %d", &cost[i][0], &cost[i][1], &cost[i][2]);
    }
    dp[0][0] = cost[0][0];
    dp[0][1] = cost[0][1];
    dp[0][2] = cost[0][2];
    for (int i = 1; i < a; i++) {
        dp[i][0] = MIN(dp[i-1][1], dp[i-1][2]) + cost[i][0];
        dp[i][1] = MIN(dp[i-1][0], dp[i-1][2]) + cost[i][1];
        dp[i][2] = MIN(dp[i-1][0], dp[i-1][1]) + cost[i][2];
    }
    int result = MIN(dp[a-1][0], MIN(dp[a-1][1], dp[a-1][2]));
    printf("%d\n", result);
    return 0;
}