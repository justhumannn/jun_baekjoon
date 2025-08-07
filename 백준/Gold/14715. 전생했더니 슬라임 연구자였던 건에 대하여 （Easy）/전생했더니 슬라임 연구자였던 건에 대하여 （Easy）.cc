#include <stdio.h>
int main(){
    int a;
    scanf("%d",&a);
    int b=0;
    int c=2;
    while(c*c<=a){
        while(a%c==0){
            b++;
            a/=c;
        }
        c++;
    }
    if(a>1) b++;
    int d=0;
    int e=1;
    while(e<b){
        e*=2;
        d++;
    }
    printf("%d",d);
    return 0;
}