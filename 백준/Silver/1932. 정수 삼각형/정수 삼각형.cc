#include <stdio.h>

int a, b[501][501], c[501][501];

int max(int x, int y){
    return x>y ? x : y;
}

int main(){
    scanf("%d", &a);
    for(int i=0;i<a;i++){
        for(int j=0;j<=i;j++){
            scanf("%d", &b[i][j]);
        }
    }
    c[0][0] = b[0][0];
    for(int i=1;i<a;i++){
        c[i][0] = c[i-1][0] + b[i][0];
        for(int j=1;j<i;j++){
            c[i][j] = max(c[i-1][j-1], c[i-1][j]) + b[i][j];
        }
        c[i][i] = c[i-1][i-1] + b[i][i];
    }
    int ans = 0;
    for(int j=0;j<a;j++){
        if(c[a-1][j] > ans) ans = c[a-1][j];
    }
    printf("%d\n", ans);
    return 0;
}