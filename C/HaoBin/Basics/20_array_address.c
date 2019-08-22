#include <stdio.h>

int main(void)
{
    int a[5] = {0, 1, 2, 3, 4};     // a 存放的是数组 a 的第一个元素的地址

    printf("&a[1] = %p\n",  a+1);   // &a[1] = 000000000061FE34 不同的机器，运行结果不同，但可以看间隔
    printf("&a[2] = %p\n",  a+2);   // &a[2] = 000000000061FE38
    printf("&a[3] = %p\n",  a+3);   // &a[2] = 000000000061FE3C
    printf(" a[3] = %d\n", *a+3);   // *a+3 等价于 a[0]+3
    
    return 0;
}

