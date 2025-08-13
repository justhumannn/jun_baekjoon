#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct { long long x; int y, z; } P;
typedef struct { P *d; int s, e, c; } Q;

void push(Q *q, P v){
    int i = q->e++;
    q->d[i] = v;
    while(i > 0){
        int p = (i - 1) / 2;
        if(q->d[p].x <= q->d[i].x) break;
        P t = q->d[p]; q->d[p] = q->d[i]; q->d[i] = t;
        i = p;
    }
}
P pop(Q *q){
    P r = q->d[0];
    q->d[0] = q->d[--q->e];
    int i = 0;
    while(1){
        int l = i * 2 + 1, rgt = i * 2 + 2, s = i;
        if(l < q->e && q->d[l].x < q->d[s].x) s = l;
        if(rgt < q->e && q->d[rgt].x < q->d[s].x) s = rgt;
        if(s == i) break;
        P t = q->d[s]; q->d[s] = q->d[i]; q->d[i] = t;
        i = s;
    }
    return r;
}

typedef struct { int v; long long w; struct E *n; } E;
E *g[10001];

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    for(int i=0;i<b;i++){
        int d, e; long long f;
        scanf("%d %d %lld", &d, &e, &f);
        E *u = malloc(sizeof(E)); u->v = e; u->w = f; u->n = g[d]; g[d] = u;
        E *v = malloc(sizeof(E)); v->v = d; v->w = f; v->n = g[e]; g[e] = v;
    }
    long long **dist = malloc((a+1)*sizeof(long long*));
    for(int i=0;i<=a;i++){
        dist[i] = malloc((c+1)*sizeof(long long));
        for(int j=0;j<=c;j++) dist[i][j] = LLONG_MAX;
    }
    Q q; q.d = malloc(sizeof(P)*((a*(c+1)) + 5)); q.e = 0;
    dist[1][0] = 0;
    push(&q,(P){0,1,0});
    while(q.e){
        P p = pop(&q);
        if(p.x != dist[p.y][p.z]) continue;
        for(E *h = g[p.y]; h; h = h->n){
            if(dist[h->v][p.z] > p.x + h->w){
                dist[h->v][p.z] = p.x + h->w;
                push(&q,(P){dist[h->v][p.z], h->v, p.z});
            }
            if(p.z < c && dist[h->v][p.z+1] > p.x){
                dist[h->v][p.z+1] = p.x;
                push(&q,(P){p.x, h->v, p.z+1});
            }
        }
    }
    long long ans = LLONG_MAX;
    for(int i=0;i<=c;i++) if(dist[a][i] < ans) ans = dist[a][i];
    printf("%lld\n", ans);
}