#include <stdio.h>

int main()
{
    int count = 12;
    count = (count>20)?(count<50)?count-10:count-5:(count<10)?count+10:count+5; // don't do this
    printf("%d\n", count);
    /*
    1. output:
    17

    2. notes:
    不同版本的编译器可能会有不同的结果
    这个版本是“从外到内”，如下
    count = (count>20)?[******]:count+5;
    */

    return 0;
}

