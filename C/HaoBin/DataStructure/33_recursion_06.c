#include <stdio.h>

int  factorial_01(int n);
void factorial_02();

int main(void)
{
    /*
    f(100) 会溢出
    简单地说，int 不够用，可以试试 double

    8!  < 2^16-1 = 65535      < 9!
    12! < 2^32-1 = 4294967296 < 13!

    “阶乘爆炸”，算了一下，换成 long long，也就能撑到 20!
    */
    printf("factorial(8) = %d\n", factorial_01(8));     // factorial(8) = 40320
    factorial_02();

    return 0;
}

int factorial_01(int n)
{
    if(n == 1)
    {
        return 1;
    }
    else
    {
        return n * factorial_01(n-1);
    }
}

void factorial_02()
{
    int val;
    int i, fac=1;
    printf("Please enter a number: ");
    scanf("%d", &val);

    for(i=1; i<=val; ++i)
    {
        fac *= i;
    }
    // 13!(bin) = 0001 0111 0011 0010 1000 1100 1100 0000 0000，int 只保 32 位，在 printf 中，fac 开头的 0001 会溢出
    printf("factorial(%d) = %d\n", val, fac);           // 输入大于等于 13，开始溢出

    return;
}

