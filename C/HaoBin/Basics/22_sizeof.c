#include <stdio.h>

int main(void)
{
    /*
    1. 规定符
        %d 十进制有符号整数
        %u 十进制无符号整数
        %f 浮点数
        %s 字符串
        %c 单个字符
        %p 指针的值
        %e 指数形式的浮点数
        %x, %X 无符号以十六进制表示的整数
        %o 无符号以八进制表示的整数
        %g 把输出的值按照 %e 或者 %f 类型中输出长度较小的方式输出
        %p 输出地址符
        %lu 32位无符号整数
        %llu 64位无符号整数
    */
    
    // 2. 数据类型
    printf("sizeof(char) = %d\n",           sizeof(char));              // 1sizeof(char) = 1
    printf("sizeof(unsigned char) = %d\n",  sizeof(unsigned char));     // sizeof(unsigned char) = 1
    printf("sizeof(short) = %d\n",          sizeof(short));             // sizeof(short) = 2
    printf("sizeof(unsigned short) = %d\n", sizeof(unsigned short));    // sizeof(unsigned short) = 2
    printf("sizeof(int) = %d\n",            sizeof(int));               // sizeof(int) = 4
    printf("sizeof(unsigned int) = %d\n",   sizeof(unsigned int));      // sizeof(unsigned int) = 4
    printf("sizeof(long) = %d\n",           sizeof(long));              // sizeof(long) = 4
    printf("sizeof(unsigned long) = %d\n",  sizeof(unsigned long));     // sizeof(unsigned long) = 4
    printf("sizeof(float) = %d\n",          sizeof(float));             // sizeof(float) = 4
    printf("sizeof(double) = %d\n",         sizeof(double));            // sizeof(double) = 8
    printf("sizeof(long int) = %d\n",       sizeof(long int));          // sizeof(long int) = 4
    printf("sizeof(long long) = %d\n",      sizeof(long long));         // sizeof(long long) = 8
    printf("sizeof(long double) = %d\n",    sizeof(long double));       // sizeof(long double) = 16
    
    return 0;
}

