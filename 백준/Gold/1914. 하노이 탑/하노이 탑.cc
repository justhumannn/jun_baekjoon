#include <stdio.h>
#include <string.h>
char result[310];
void power_of_two(int n) {
    int res[310] = {1};  // res[0] = 1
    int len = 1;

    for (int i = 0; i < n; i++) {
        int carry = 0;
        for (int j = 0; j < len; j++) {
            int tmp = res[j] * 2 + carry;
            res[j] = tmp % 10;
            carry = tmp / 10;
        }
        while (carry) {
            res[len++] = carry % 10;
            carry /= 10;
        }
    }
    res[0] -= 1;
    for (int i = 0; i < len; i++) {
        if (res[i] < 0) {
            res[i] += 10;
            res[i + 1]--;
        }
    }
    int start = len - 1;
    while (start > 0 && res[start] == 0) start--;
    for (int i = start; i >= 0; i--) {
        printf("%d", res[i]);
    }
    printf("\n");
}
void hanoi(int n, int start, int end, int temp) {
    if (n == 1) {
        printf("%d %d\n", start, end);
        return;
    }
    hanoi(n - 1, start, temp, end);
    printf("%d %d\n", start, end);
    hanoi(n - 1, temp, end, start);
}
int main() {
    int a;
    scanf("%d", &a);
    power_of_two(a);
    if (a <= 20) {
        hanoi(a, 1, 3, 2);
    }
    return 0;
}
