#include <stdio.h>
#include <malloc.h>

int assignment()
{
    int j = 20;

    return j;
}

int main(void)
{
    int i;
    i = assignment();
    printf("i = %d\n", i);  // i = 20

    return 0;
}

