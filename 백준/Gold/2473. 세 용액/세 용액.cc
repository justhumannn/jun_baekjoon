#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
    long long x = *(long long*)a;
    long long y = *(long long*)b;
    if(x<y) return -1;
    if(x>y) return 1;
    return 0;
}

int main(){
    int a;
    scanf("%d",&a);
    long long b[5000];
    for(int c=0;c<a;c++) scanf("%lld",&b[c]);
    qsort(b,a,sizeof(long long),cmp);
    long long d=3000000000LL,e,f,g;
    for(int c=0;c<a-2;c++){
        int h=c+1,i=a-1;
        while(h<i){
            long long j=b[c]+b[h]+b[i];
            if(llabs(j)<d){
                d=llabs(j);
                e=b[c];
                f=b[h];
                g=b[i];
            }
            if(j<0) h++;
            else i--;
        }
    }
    printf("%lld %lld %lld",e,f,g);
    return 0;
}