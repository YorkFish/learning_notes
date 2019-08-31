#include <stdio.h>

int  factorial_01(int n);
void factorial_02();
long sum_n(long n);

int main(void)
{
    // printf("factorial(8) = %d\n", factorial_01(8));
    // factorial_02();
    
    printf("sum(1~100) = %ld\n", sum_n(100));

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
    printf("factorial(%d) = %d\n", val, fac);

    return;
}

// 假设 n>=1
long sum_n(long n)
{
    if(n == 1)
    {
        return 1;
    }
    else
    {
        return n + sum_n(n-1);
    }
}

