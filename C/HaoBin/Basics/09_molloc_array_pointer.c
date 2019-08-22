#include <stdio.h>
#include <malloc.h>

int main(void)
{
    int len;
    int * pArr;
    int i;

    printf("Please enter the number of elements you want to save: ");
    scanf("%d", &len);
    pArr = (int *)malloc(sizeof(int) * len);    // int, long 所占字节与 CPU, OS, Compiler 有关

    // 感觉书中是 i++ 多见，老师的代码是 ++i 多见；有一种说法是 ++i 比 i++ 效率高一点点，但对于现在的机器，这点可以忽略
    for(i=0; i<len; i++)
        scanf("%d", &pArr[i]);

    printf("\nYou entered %d number(s): \n", len);
    for(i=0; i<len; i++)
        printf("%d\t", pArr[i]);
    printf("\n");

    free(pArr);                                 // 别忘

    return 0;
}

