#include <stdio.h>

void pointer(int* p)
{
    *p = 20;
}

int main(void)
{
    int i = 10;
    pointer(&i);
    printf("i = %d\n", i); // 注意
    
    return 0;
}

