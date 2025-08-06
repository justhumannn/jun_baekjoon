#include <stdio.h>

int max(int x, int y) {
    return (x > y) ? x : y;
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    int w, v;
    int stuff_w[a];
    int stuff_v[a];

    for (int i = 0; i < a; i++) {
        scanf("%d %d", &w, &v);
        stuff_w[i] = w;
        stuff_v[i] = v;
    }

    int dp[a + 1][b + 1];

    for (int i = 0; i <= a; i++) {
        for (int j = 0; j <= b; j++) {
            dp[i][j] = 0;
        }
    }

    for (int i = 1; i <= a; i++) {
        w = stuff_w[i - 1];
        v = stuff_v[i - 1];
        for (int j = 0; j <= b; j++) {
            if (j < w) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v);
            }
        }
    }

    printf("%d\n", dp[a][b]);
    return 0;
}
