#include <stdio.h>
#include <malloc.h>

int main()
{
    int len;
    printf("Please enter the number of length: ");
    scanf("%d", &len);          // scanf 里不要加 \n

    int* pArr = (int*)malloc(sizeof(int) * len);
    for(int i=0; i<len; ++i)
    {
        printf("Please enter the No.%d number: ", i+1);
        scanf("%d", &pArr[i]);
    }

    printf("\nsaving...\nloading...\n\n");
    for(int i=0; i<len; ++i)    // C99 之前，如果上方定义过 i，这里可以继续使用
    {
        printf("No.%d number is: %d\n", i+1, *(pArr+i));
    }

    free(pArr);

    return 0;
}

