#include <stdio.h>

void pointer1(int* p)
{
    while(*p)
    {
        p++;
        printf("%d\t", *p);
    }
    printf("\n");

    return;
}

void pointer2(int* p)
{
    while(*p++)
    {
        printf("%d\t", *p);  
    }
    printf("\n");

    return;
}

void pointer3(int* p)
{
    while(*p)
    {
        printf("%d\t", *p);
        p++;
    }
    printf("\n");

    return;
}

void pointer4(int* p)
{
    while(*p)
    {
        printf("%d\t", *p++);  
    }
    printf("\n");

    return;
}

int main(void)
{
    int a[5] = {1, 3, 5, 7, 9};

    pointer1(a);    // 3       5       7       9       0
    pointer2(a);    // 3       5       7       9       0
    pointer3(a);    // 1       3       5       7       9
    pointer4(a);    // 1       3       5       7       9

    return 0;
}

