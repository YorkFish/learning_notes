#include <stdio.h>

void f(int n);

int main(void)
{
    f(3);
    /* output:
        n = 3
        n = 2
        haha
    */

    return 0;
}

void f(int n)
{
    if(n == 1)
    {
        printf("haha\n");
    }
    else
    {
        printf("n = %d\n", n);
        f(n-1);
    }

	return;
}

