#include <stdio.h>
#include <stdlib.h>


int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) return 0;

    int size = 1;
    while (size < a) size <<= 1;

    int tree_size = size << 1;
    int *tree = (int*)malloc((tree_size + 5) * sizeof(int));

    for (int i = 0; i <= tree_size; ++i) tree[i] = 0;

    for (int i = 0; i < a; ++i) tree[size + i] = 1;
    for (int i = size - 1; i >= 1; --i) tree[i] = tree[i << 1] + tree[(i << 1) + 1];

    int d = a;
    int c = 0;

    printf("<");
    for (int _ = 0; _ < a; ++_) {
        int e = (c + b - 1) % d + 1;

        int node = 1;
        int k = e;
        while (node < size) {
            int left_sum = tree[node << 1];
            if (k <= left_sum) {
                node = node << 1;
            } else {
                k -= left_sum;
                node = (node << 1) + 1;
            }
        }
        int idx = node - size;

        printf("%d", idx + 1);
        if (_ != a - 1) printf(", ");

        node = size + idx;
        tree[node] = 0;
        node >>= 1;
        while (node >= 1) {
            tree[node] = tree[node << 1] + tree[(node << 1) + 1];
            node >>= 1;
        }

        d -= 1;
        if (d > 0) {
            int prev_t_minus1 = (c + b - 1) % (d + 1);
            c = prev_t_minus1 % d;
        } else {
            c = 0;
        }
    }
    printf(">\n");

    free(tree);
    return 0;
}