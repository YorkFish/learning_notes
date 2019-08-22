#include <stdio.h>

int main()
{
    int num1 = 0xffffffef;
    printf("num1 = %x\n", num1);    // num1 = ffffffef
    printf("num1 = %#x\n", num1);   // num1 = 0xffffffef
    
    char num2 = 0b10000000;
    printf("num2 = %d\n", num2);    // num2 = -128
    
    char num3 = 0x80;               // 1000 0000
    printf("num3 = %d\n", num3);    // num3 = -128

    return 0;
}

