#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int a,b;
int c[1001][2];
int d[1001][1001];
int e[1001][1001];

int f(int g,int h){
    if(g==a || h==a) return 0;
    if(d[g][h]!=-1) return d[g][h];
    int i = (g>h?g:h)+1;
    int j,k;
    if(g==0) j = abs(c[i][0]-1)+abs(c[i][1]-1);
    else j = abs(c[i][0]-c[g][0])+abs(c[i][1]-c[g][1]);
    if(h==0) k = abs(c[i][0]-b)+abs(c[i][1]-b);
    else k = abs(c[i][0]-c[h][0])+abs(c[i][1]-c[h][1]);
    int l = f(i,h)+j;
    int m = f(g,i)+k;
    if(l<m){
        e[g][h] = 1;
        return d[g][h] = l;
    }else{
        e[g][h] = 2;
        return d[g][h] = m;
    }
}

int main(){
    scanf("%d %d",&b,&a);
    for(int i=1;i<=a;i++) scanf("%d %d",&c[i][0],&c[i][1]);
    for(int i=0;i<=a;i++) for(int j=0;j<=a;j++) d[i][j] = -1;
    printf("%d\n",f(0,0));
    int g=0,h=0;
    for(int i=0;i<a;i++){
        printf("%d\n",e[g][h]);
        if(e[g][h]==1) g = (g>h?g:h)+1;
        else h = (g>h?g:h)+1;
    }
}