#include <stdio.h>

int sum(int n);

int main(void)
{
    printf("sum = %d\n", sum(3));   // sum = 6

    return 0;
}

int sum(int n)
{
    if(n == 1)
    {
        return 1;
    }
    else
    {
        return n + sum(n-1);
    }
}

