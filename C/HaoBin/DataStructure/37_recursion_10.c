#include <stdio.h>

int f(int m);
int g(int g);

int main(void)
{
    printf("val = %d\n", f(3));
    printf("val = %d\n", g(5));
    /* output:
        haha
        val = 8
        lala
        val = 2
    */

    return 0;
}

int f(int m)
{
    if(m > 7)
        printf("haha\n");
    else
        m = f(m+1);

    return m;
}

int g(int n)
{
    if(n < 3)
        printf("lala\n");
    else
        n = g(n-1);

    return n;
}

