#include <stdio.h>

int main()
{
    printf("abcdefg"
    "1234567\n");
    /*
    1. output:
    abcdefg1234567
    
    2. notes:
    若 printf 中的两个字符串如上相连（不加逗号），输出时会连起来
    */
    
    printf("abcdefg\
    1234567\n");
    /*
    1. output:
    abcdefg    1234567
    
    2. notes:
    若 printf 中一对双引号内的字符串要换行，可加上反斜杠 \
    这样会代入第二行的空格，若想不带空格，第二行可以顶格写
    */
    
    return 0;
}

