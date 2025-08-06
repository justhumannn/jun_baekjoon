#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int weight;
    int node;
} HeapNode;

typedef struct {
    HeapNode *data;
    int size;
    int capacity;
} MinHeap;

void swap(HeapNode *a, HeapNode *b) {
    HeapNode temp = *a;
    *a = *b;
    *b = temp;
}

MinHeap* createHeap(int capacity) {
    MinHeap *heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->data = (HeapNode*)malloc(sizeof(HeapNode) * capacity);
    heap->size = 0;
    heap->capacity = capacity;
    return heap;
}

void heapPush(MinHeap *heap, int weight, int node) {
    if (heap->size >= heap->capacity) return;
    heap->data[heap->size].weight = weight;
    heap->data[heap->size].node = node;
    int i = heap->size++;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap->data[parent].weight <= heap->data[i].weight) break;
        swap(&heap->data[parent], &heap->data[i]);
        i = parent;
    }
}

int heapPop(MinHeap *heap, int *weight, int *node) {
    if (heap->size == 0) return 0;
    *weight = heap->data[0].weight;
    *node = heap->data[0].node;
    heap->data[0] = heap->data[--heap->size];

    int i = 0;
    while (1) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int smallest = i;
        if (left < heap->size && heap->data[left].weight < heap->data[smallest].weight)
            smallest = left;
        if (right < heap->size && heap->data[right].weight < heap->data[smallest].weight)
            smallest = right;
        if (smallest == i) break;
        swap(&heap->data[i], &heap->data[smallest]);
        i = smallest;
    }
    return 1;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int limit = (n > m ? n : m) * 2 + 1;

    int *d = (int*)malloc(sizeof(int) * limit);
    int *way = (int*)malloc(sizeof(int) * (limit + 1));
    for (int i = 0; i < limit; i++) {
        d[i] = INT_MAX;
        way[i] = -1;
    }
    way[limit] = -1;

    d[n] = 0;

    MinHeap *heap = createHeap(limit * 3);
    heapPush(heap, 0, n);

    while (heap->size > 0) {
        int weight, node;
        heapPop(heap, &weight, &node);

        if (d[node] < weight) continue;

        int neighbors[3][2] = {
            {1, node + 1},
            {1, node * 2},
            {1, node - 1}
        };

        for (int i = 0; i < 3; i++) {
            int w = neighbors[i][0];
            int v = neighbors[i][1];
            if (v >= 0 && v < limit && d[v] > weight + w) {
                d[v] = weight + w;
                way[v] = node;
                heapPush(heap, d[v], v);
            }
        }
    }

    printf("%d\n", d[m]);

    // 경로 복원
    int path_size = 0;
    int *path = (int*)malloc(sizeof(int) * (limit + 1));
    int cur = m;
    while (cur != n) {
        path[path_size++] = cur;
        cur = way[cur];
    }
    path[path_size++] = n;

    for (int i = path_size - 1; i >= 0; i--) {
        printf("%d ", path[i]);
    }
    printf("\n");
    free(d);
    free(way);
    free(path);
    free(heap->data);
    free(heap);
    return 0;
}