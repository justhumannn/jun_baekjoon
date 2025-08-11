#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAX 100000

int cnt[MAX + 1];

void factor(int x, int op){
    int m = (int)sqrt(x);
    for(int i = 2; i <= m; i++){
        while(x % i == 0){
            cnt[i] += op;
            x /= i;
        }
    }
    if(x > 1) cnt[x] += op;
}

int main(){
    int a;
    scanf("%d", &a);
    int op = 1, b;
    scanf("%d", &b);
    if(b == 0){
        printf("mint chocolate");
        return 0;
    }
    factor(abs(b), op);
    for(int i = 1; i < a; i++){
        char c;
        scanf(" %c %d", &c, &b);
        if(b == 0){
            printf("mint chocolate");
            return 0;
        }
        factor(abs(b), c == '*' ? 1 : -1);
    }
    for(int i = 2; i <= MAX; i++){
        if(cnt[i] < 0){
            printf("toothpaste");
            return 0;
        }
    }
    printf("mint chocolate");
    return 0;
}