#include <stdio.h>

int main(){
    int a,bus,b,c,d;
    int cost[101][101];
    scanf("%d",&a);
    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= a; j++) {
            cost[i][j] = 2147483600;
        }
    }
    scanf("%d",&bus);
    for (int i = 1; i <= bus; i++) {
        scanf("%d %d %d",&b,&c,&d);
        if (cost[b][c] > d) cost[b][c] = d;
    }
    for (int i = 1; i <= a; i++) {
        cost[i][i] = 0;
    }
    for (int k = 1; k <= a; k++) {
        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= a; j++) {
                if (cost[i][k] != 2147483600 && cost[k][j] != 2147483600) {
                    if (cost[i][j] > cost[i][k] + cost[k][j]) {
                        cost[i][j] = cost[i][k] + cost[k][j];
                    }
                }

            }
        }
    }
    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= a; j++) {
            if (cost[i][j] == 2147483600) printf("0 "); // 연결 안 된 경우
            else printf("%d ", cost[i][j]);
        }
        printf("\n");
    }
    return 0;
}