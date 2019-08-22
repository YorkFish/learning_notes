#include <stdio.h>

void showArray(int* p, int len)
{
    int i;
    for(i=0; i<len; ++i)
        printf("a[%d] = %d\n", i, *(p+i));
}

int main(void)
{
    int a[5] = {0, 1, 2, 3, 4};

    showArray(a, 5);    // a 正好是该数组乃第一个元素的地址，直接传即可
    
    return 0;
}

