#include <stdio.h>

int main()
{   
    printf("1234\b\n5678\n");
    /*
    1. output:
    1234
    5678

    2. notes:
    \b
    逃逸字符，回退一格
    不同的 Shell 对逃逸字符的处理可能不同
    如，有些地方输入 \b，会输出 BS，意为 BackSpace
    */
    
    printf("1234\bA\n5678\n");
    /*
    1. output:
    123A
    5678

    2. notes:
    \b
    结合上一条 printf，可知 \b 后有东西才回退
    */

    return 0;
}

