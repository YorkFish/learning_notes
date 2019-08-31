#include <stdio.h>

void f();
void g();
void k();

int main(void)
{
    // 会炸，不过出于保护，递归一定次数系统会退出
    f();

    return 0;
}

void f()
{
    printf("fff\n");
    g();
}

void g()
{
    printf("ggg\n");
    k();
}

void k()
{
    printf("kkk\n");
    f();
}

