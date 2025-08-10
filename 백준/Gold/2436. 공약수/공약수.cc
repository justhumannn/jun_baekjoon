#include <stdio.h>
long long gcd(long long a, long long b){
    while(b){
        long long t = b;
        b = a % b;
        a = t;
    }
    return a;
}
int main(){
    long long a, b;
    scanf("%lld %lld", &a, &b);
    long long c = b / a;
    long long x = 1, y = c;
    for(long long i = 1; i * i <= c; i++){
        if(c % i == 0){
            long long j = c / i;
            if (gcd(i, j) == 1) {
                x = i;
                y = j;
            }
        }
    }
    printf("%lld %lld", x * a, y * a);
    return 0;
}