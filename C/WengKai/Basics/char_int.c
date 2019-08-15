#include <stdio.h>

int main()
{
    char num1_1 = 254, num1_2 = 255;
    char num1_3 = 256; // warning: overflow in conversion from 'int' to 'char' changes value from '256' to ''\000'' [-Woverflow]
    
    int num2 = 255;
    
	printf("num1_1 = %d, num1_2 = %d, num1_3 = %d\n", num1_1, num1_2, num1_3);
    printf("num2 = %d\n", num2);
    /*
    1. output:
    num1_1 = -2, num1_2 = -1, num1_3 = 0
    num2 = 255

    2. notes:
         <- 127+1
     -128 | 127
    /          \
    |          |
    \          /
       -1 | 0
    */

	return 0;
}

