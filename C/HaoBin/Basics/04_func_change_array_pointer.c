#include <stdio.h>

void pointer(int* p)
{
    p[3] = 88;  // p[3] 与 *(p+3) 等价

    return;
}

int main(void)
{
    int a[5] = {1, 3, 5, 7, 9};
    printf("a[3] = %d\n", a[3]);        // a[3] = 7
    printf("*(a+3) = %d\n", *(a+3));    // *(a+3) = 7
    
    pointer(a);
    printf("a[3] = %d\n", a[3]);        // a[3] = 88

    return 0;
}

