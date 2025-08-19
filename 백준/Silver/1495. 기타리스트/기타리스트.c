#include <stdio.h>

int main() {
    int n, s, m;
    scanf("%d %d %d", &n, &s, &m);

    int v[101]; // 곡 수 n 최대 100
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int d[101][1001] = {0}; // n은 최대 100, m은 최대 1000
    d[0][s] = 1; // 시작 볼륨

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (d[i - 1][j] == 1) {
                if (j - v[i - 1] >= 0) {
                    d[i][j - v[i - 1]] = 1;
                }
                if (j + v[i - 1] <= m) {
                    d[i][j + v[i - 1]] = 1;
                }
            }
        }
    }

    int result = -1;
    for (int i = m; i >= 0; i--) {
        if (d[n][i] == 1) {
            result = i;
            break;
        }
    }

    printf("%d\n", result);
    return 0;
}