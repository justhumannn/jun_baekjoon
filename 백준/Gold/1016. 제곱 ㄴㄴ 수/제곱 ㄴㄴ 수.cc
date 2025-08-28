#include <stdio.h>
int arr[1000001] = {0};

int main(void)
{
    long long cont = 0;
    unsigned long long min, max;
    scanf("%lld %lld", &min, &max);
    for (unsigned long long i = 2; i * i <= max; i++)
    {
        unsigned long long search = ((min + (i * i) - 1) / (i * i)) * (i * i);

        if (search != 0)
        {
            for (unsigned long long j = search; j <= max; j += i * i)
            {
                arr[j - min] = 1;
            }
        }
    }
    for (unsigned long long i = 0; i <= max - min; i++)
    {
        if (arr[i] == 0)
        {
            cont++;
        }
    }
    printf("%lld", cont);
    return 0;
}