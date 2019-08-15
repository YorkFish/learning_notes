#include <stdio.h>

int main()
{
    int a = 0;
    while(++a > 0);
    printf("a = %d\n", a-1);    // a = 2147483647, 2^31 - 1 = 2147483647
    

    int b = 1;
    char cnt = 0;
    while(cnt < 31)
    {
        cnt++;
        b *= 2;
        // printf("%d\n", b);      // last time, b = -2147483648
    }
    printf("b = %d\n", b-1);    // b = 2147483647


    printf("%d\n", -1);         // -1
    printf("%u\n", -1);         // 4294967295, 2^32 - 1 = 4294967295
    /*
    Similar to char_int.c:
     2147483648 | 2147483647
    /                       \
    |                       |
    \                       /
     4294967295 | 0
               <- 0-1
    */
    
	return 0;
}

