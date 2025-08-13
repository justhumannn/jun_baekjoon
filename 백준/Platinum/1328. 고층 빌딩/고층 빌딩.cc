#include <stdio.h>
#define MOD 1000000007

int dp[101][101][101];

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    dp[1][1][1] = 1;
    for(int n = 2; n <= a; n++){
        for(int l = 1; l <= n; l++){
            for(int r = 1; r <= n; r++){
                long long v = 0;
                v += dp[n-1][l-1][r];
                v += dp[n-1][l][r-1];
                v += (long long)(n-2) * dp[n-1][l][r];
                dp[n][l][r] = v % MOD;
            }
        }
    }
    printf("%d\n", dp[a][b][c]);
    return 0;
}