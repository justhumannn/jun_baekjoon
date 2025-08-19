#include <stdio.h>

int max(int a, int b) {
    if (a > b) return a;
    return b;
}

int main() {
    int a;
    scanf("%d",&a);
    int b[10001];
    for (int i = 1; i <= a; i++) scanf("%d",&b[i]);
    int dp[10001] = {0};
    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= i; j++) {
            dp[i] = max(dp[i],b[j]+dp[i-j]);
        }
    }
    printf("%d",dp[a]);
    return 0;
}