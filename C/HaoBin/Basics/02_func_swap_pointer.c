#include <stdio.h>

void change(int* p, int* q)
{
    int t = *p;
    *p = *q;
    *q = t;
    
    return;
}

int main()
{
    int a = 3;
    int b = 5;
    printf("before:\ta = %d, b = %d\n", a, b);  // before: a = 3, b = 5

    change(&a, &b);
    
    printf("after:\ta = %d, b = %d\n", a, b);   // after:  a = 5, b = 3

    return 0;
}

