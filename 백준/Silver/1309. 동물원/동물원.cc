#include <stdio.h>
int main() {
    int a;
    scanf("%d", &a);
    int b = 1, c = 1, d = 1;
    int nb, nc, nd;
    for (int i = 2; i <= a; i++) {
        nb = (b + c + d) % 9901;
        nc = (b + d) % 9901;
        nd = (b + c) % 9901;
        b = nb;
        c = nc;
        d = nd;
    }
    printf("%d\n", (b + c + d) % 9901);
    return 0;
}