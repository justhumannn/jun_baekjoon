#include <stdio.h>
#define MOD 1000000000

int dp[101][10];

int main(){
    int a;
    scanf("%d", &a);
    for(int j = 1; j <= 9; j++) dp[1][j] = 1;
    for(int i = 2; i <= a; i++){
        dp[i][0] = dp[i-1][1] % MOD;
        for(int j = 1; j <= 8; j++){
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD;
        }
        dp[i][9] = dp[i-1][8] % MOD;
    }
    int sum = 0;
    for(int j = 0; j <= 9; j++){
        sum = (sum + dp[a][j]) % MOD;
    }
    printf("%d\n", sum);
    return 0;
}