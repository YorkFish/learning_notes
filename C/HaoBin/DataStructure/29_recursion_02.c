#include <stdio.h>

void f();
void g();
void k();

int main(void)
{
    f();
    /* output:
        fff
        ggg
        kkk
        333
        222
        111
    */

    return 0;
}

void f()
{
    printf("fff\n");
    g();
    printf("111\n");
}

void g()
{
    printf("ggg\n");
    k();
    printf("222\n");
}

void k()
{
    printf("kkk\n");
    printf("333\n");
}

