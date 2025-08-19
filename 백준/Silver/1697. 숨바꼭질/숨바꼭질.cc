#include <stdio.h>

int min(int a, int b) {
    if (a < b) return a;
    return b;
}
int front = 0;
int rear = 1;
int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    int time[200011];
    for (int i = 0; i <= b+10; i++) {
        time[i] = 2000000000;
    }
    int sequence[200011] = {0};
    sequence[0] = a;
    int node;
    int visited[200011] = {0};
    time[a] = 0;
    if (a > b) printf("%d",a-b);
    else{
      while (front < rear) {
          node = sequence[front];
          front ++;
          if (node < 0 || visited[node] == 1) continue;
          if (node == b) break;
          visited[node] = 1;
          time[node-1] = min(time[node-1], time[node] + 1);
          sequence[rear] = node-1;
          rear ++;
          if (node > b) continue;
          time[node+1] = min(time[node+1],time[node] + 1);
          sequence[rear] = node+1;
          rear ++;
          time[node*2] = min(time[node*2], time[node] + 1);
          sequence[rear] = node*2;
          rear ++;
      }
      printf("%d\n",time[b]);
    }
    return 0;
}