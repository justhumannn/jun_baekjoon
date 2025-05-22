#include <stdio.h>

int main() {
    // 입력할 숫자 개수(100개 제한)를 입력하고 그 다음 줄에 숫자가 처음에 입력한 숫자만큼 입력된다
    // 입력된 숫자 중 소수의 개수를 출력
    int a;
    scanf("%d",&a);
    int count[101];
    int b[101];
    for (int i = 0; i < a; i++) {
        scanf("%d",&b[i]);
    }
    int c = 0;
    for (int i = 0; i < a; i++) {
        count[i] = 0;
        int j = 2;
        while (b[i] != 1) {
            if (j == b[i]) {
                break;
            }
            if (b[i] % j != 0) {
                count[i]++;
            }
            j++;
        }
        if (count[i] == b[i] - 2) {
            c ++;
        }
    }
    printf("%d",c);
    return 0;
}