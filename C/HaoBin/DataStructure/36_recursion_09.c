#include <stdio.h>

int f(int m);
int g(int g);

int main(void)
{
    printf("val = %d\n", f(5));
    printf("val = %d\n", g(5));
    /* output:
        haha
        val = 5
        lala
        val = 2
    */

    return 0;
}

int f(int m)
{
    if(m < 3)
    {
        printf("haha\n");
    }
    else
    {
        // return f(m-1);  // 见 g()
        f(m-1);
    }

    return m;           // m=5 又是个实参、形参的问题
}

int g(int n)
{
    if(n < 3)
        printf("lala\n");
    else
        n = g(n-1);

    return n;
}

