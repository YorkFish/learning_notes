#include <stdio.h>

void pointer(int** q)           // 用“指针的指针”接收“指针的地址”
{
    int i = 5;
    *q = &i;                    // 从某种角度看，*q 相当于 p
    printf("**q = %d\n", **q);

    return;
}

int main(void)
{
    int* p;
    pointer(&p);                // **q = 5
    printf("*p = %d\n", *p);    // *p = 5

    return 0;
}

