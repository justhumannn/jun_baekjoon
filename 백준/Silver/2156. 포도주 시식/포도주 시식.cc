#include <stdio.h>

int a, b[10001], c[10001];

int max(int x, int y, int z){
    int m = x > y ? x : y;
    return m > z ? m : z;
}

int main(){
    scanf("%d", &a);
    for(int i = 1; i <= a; i++) scanf("%d", &b[i]);
    c[1] = b[1];
    if(a >= 2) c[2] = b[1] + b[2];
    for(int i = 3; i <= a; i++){
        c[i] = max(c[i-1],
                   c[i-2] + b[i],
                   c[i-3] + b[i-1] + b[i]);
    }
    printf("%d\n", c[a]);
    return 0;
}
