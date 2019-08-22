#include <stdio.h>

/*
    此程序仅为举例，因为这样写不安全
    无论什么类型的变量，想在函数外更改它，就发送它的地址
*/
void pointer1(int* q)
{
    q = (int*)0xfffffffe;   // 若不用 (int*) 强制转换，编译器会将后面的地址当作一个数字
}

void pointer2(int** q)
{
    *q = (int*)0xfffffffe;  // *q==p 改了 p 的内容，相当于改了 p 的指向
}

int main(void)
{
    int i = 10;
    int *p = &i;
    printf("p = %p\n", p);  // p = 000000000061FE4C
    
    pointer1(p);
    printf("p = %p\n", p);  // p = 000000000061FE4C
    
    pointer2(&p);           // 对比 17_pointer_address.c
    printf("p = %p\n", p);  // p = 00000000FFFFFFFE
    
    return 0;
}

