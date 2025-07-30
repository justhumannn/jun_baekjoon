#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    long long b[200002];
    for (int i = 0; i < a; i++) {
        scanf("%lld", &b[i]);
    }
    int c;
    scanf("%d", &c);
    for (int q = 0; q < c; q++) {
        int d0;
        scanf("%d", &d0);
        if (d0 == 1) {
            int d1;
            long long d2;
            scanf("%d %lld", &d1, &d2);
            int i = d1 - 1;
            long long noise = d2;
            while (i >= 0 && noise > 0) {
                long long add_noise = b[i] < noise ? b[i] : noise;
                b[i] += add_noise;
                noise -= add_noise;
                i--;
            }
            i = d1;
            noise = d2;
            while (i < a && noise > 0) {
                long long add_noise = b[i] < noise ? b[i] : noise;
                b[i] += add_noise;
                noise -= add_noise;
                i++;
            }
        } else {
            int d1;
            scanf("%d", &d1);
            printf("%lld\n", b[d1 - 1]);
        }
    }
    return 0;
}