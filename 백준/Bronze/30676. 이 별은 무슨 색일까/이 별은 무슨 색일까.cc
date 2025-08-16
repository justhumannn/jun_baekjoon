#include <stdio.h>

int a;

int main(){
    scanf("%d", &a);
    if (a >= 620 && a <= 780) printf("Red");
    else if (a >= 590) printf("Orange");
    else if (a >= 570) printf("Yellow");
    else if (a >= 495) printf("Green");
    else if (a >= 450) printf("Blue");
    else if (a >= 425) printf("Indigo");
    else if (a >= 380) printf("Violet");
    return 0;
}