#include <stdio.h>

void f();

int main(void)
{
    // 直至溢栈，退出
    f();

    return 0;
}

void f()
{
    printf("fff\n");
    f();
}

