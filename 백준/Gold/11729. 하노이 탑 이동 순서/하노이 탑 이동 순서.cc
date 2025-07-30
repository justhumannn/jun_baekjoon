#include <stdio.h>
int hanoi(int n, int start,int end, int temp);
int main(){
    int a;
    scanf("%d",&a);
    int b = 1;
    for (int i = 0;i<a;i++) {
        b *= 2;
    }
    printf("%d\n",b-1);
    hanoi(a,1,3,2);
    return 0;
}
int hanoi(int n, int start,int end, int temp) {
    if (n == 1) {
        printf("%d %d\n",start,end);
        return 0;
    }
    hanoi(n-1,start,temp,end);
    printf("%d %d\n",start,end);
    hanoi(n-1,temp,end,start);
    return 0;
}