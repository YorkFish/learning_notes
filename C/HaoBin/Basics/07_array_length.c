#include <stdio.h>

int main(void)
{
    int len = 10;
    int a[len];                     // ANSI C 不能这么写，C99 及以后可以
    printf("a[1] = %d\n", a[1]);    // a[1] = 0

    return 0;
}

