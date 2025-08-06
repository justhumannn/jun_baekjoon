#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    int **c = (int **)malloc(a * sizeof(int *));
    for (int i = 0; i < a; i++) {
        c[i] = (int *)malloc(b * sizeof(int));
        for (int j = 0; j < b; j++) {
            c[i][j] = 0;
        }
    }

    int *d = (int *)malloc(b * sizeof(int));
    for (int i = 0; i < b; i++) {
        scanf("%d", &d[i]);
    }

    for (int i = 0; i < b; i++) {
        if (d[i] > 0) {
            for (int j = a - 1; j >= a - d[i]; j--) {
                c[j][i] = 1;
            }
        }
    }

    int sum = 0;
    for (int i = a - 1; i >= 0; i--) {
        int j = b - 1;
        while (1) {
            if (j <= 1) break;
            if (c[i][j] == 1) {
                int j1 = j;
                j--;
                if (c[i][j] == 0) {
                    while (1) {
                        if (j <= 0) break;
                        if (c[i][j - 1] == 0) {
                            j--;
                        } else {
                            sum += (j1 - j);
                            break;
                        }
                    }
                }
            } else if (c[i][j] == 0) {
                j--;
            }
        }
    }

    printf("%d\n", sum);

    for (int i = 0; i < a; i++) {
        free(c[i]);
    }
    free(c);
    free(d);

    return 0;
}
