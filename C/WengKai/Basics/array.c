#include <stdio.h>

int main()
{
    // int a[13] = {[1]=2, 4, [5]=6};  // C99 ONLY

    int a[13] = {0};
    // int i;
    for(int i=0; i<13; i++)
    {
        printf("%d\t", a[i]);
    }
    printf("\n");

    return 0;
}

