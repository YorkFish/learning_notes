#include <stdio.h>

void sum(int, int);

int main()
{
    sum(10, 20);

    return 0;
}

void sum(int start, int end)
{
    int sum = 0;
    int i = 0;
    for(i=start; i<=end; i++)
    {
        sum += i;
    }
    printf("sum = %d\n", sum);
}

