#include <stdio.h>

void f1(void)
{
    char word1[8];
    char word2[8];

    scanf("%s", word1);
    scanf("%s", word2);
    
    printf("%s##%s##\n", word1, word2);
}

void f2(void)
{
    char word1[8];
    char word2[8];
    
    scanf("%7s", word1);
    scanf("%7s", word2);
    
    printf("%s##%s##\n", word1, word2);
}

int main()
{
    //f1();
    /*
    1. input:
    1234567890
    abcdefghijklmn

    2. output:
    ijklmn##abcdefghijklmn##

    3. notes:
    不安全
    */

    f2();
    /*
    1.
    input1:
    123
    abcdefghij
    
    output1:
    123##abcdefg##

    2.
    input2:
    1234567890abcdefghijklmn
    
    output2:
    1234567##890abcd##

    3. notes:
    此法安全
    */

    return 0;
}

