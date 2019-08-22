#include <stdio.h>

int main()
{
    int a = 5;
    a = a++;
    printf("a = %d\n", a);
    /*
    1. output:
    a = 5
    
    2. notes:
    可以这样看：
    虽然 a++ -> 6
    但是 a++ 返回其原值
    c++, java 也是如此
    */

    return 0;
}

