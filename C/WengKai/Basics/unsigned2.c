#include <stdio.h>

int main()
{
    char c = -1;
    int i = -1;
    int num = 26;

    // printf 会把传入的低于 int 类型的变量转为 int 类型
    // 4294967295 = 2^32 -1
    printf("c = %u\n", c);      // c = 4294967295
    printf("i = %u\n", i);      // i = 4294967295

    // %x1a -> 0x1a
    // %X1a -> 0x1A
    printf("num = %x\n", num);  // num = 1a
    printf("num = %X\n", num);  // num = 1A

    /*
    notes:
    早期的计算机是 12 位、24 位的，所以用 8 进制表达比较方便
    如今的系统是 32 位、64 位的，用 16 进制表达比较方便
     */
	return 0;
}

