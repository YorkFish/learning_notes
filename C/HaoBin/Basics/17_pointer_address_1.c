#include <stdio.h>

void pointer(char* a, char* b)
{
    a = b; // 此时 a 指向了 b 的地址，即 main 中的 p 不再指向 c1 了；改变了 p，但不改变 c1
    (*a)++;
}

int main(void)
{
    char c1='A', c2='a', *p, *q;
    
    p = &c1;
    q = &c2;
    
    pointer(p, q);              // 可对比 10_pointer_pointer.c
    printf("%c %c\n", c1, c2);  // A b
    
    return 0;
}

