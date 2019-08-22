#include <stdio.h>
// #include <stdlib.h> // stdlib.h 中包含了 malloc.h
#include <malloc.h>

int main(void)
{
    int* p = (int*)malloc(4);
    free(p);    // 用完释放内存

    return 0;
}

