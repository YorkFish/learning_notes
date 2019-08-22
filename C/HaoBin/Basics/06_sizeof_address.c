#include <stdio.h>

int main(void)
{
    char c = 'c';
    int i = 0;
    float f = 0;
    double d = 0;

    char* p_c = &c;
    int* p_i = &i;
    float* p_f = &f;
    double* p_d = &d;
    
    printf("sizeof(p_c) = %d\n", sizeof(p_c));  // sizeof(p_c) = 8
    printf("sizeof(p_i) = %d\n", sizeof(p_i));  // sizeof(p_i) = 8
    printf("sizeof(p_f) = %d\n", sizeof(p_f));  // sizeof(p_f) = 8
    printf("sizeof(p_d) = %d\n", sizeof(p_d));  // sizeof(p_d) = 8

    return 0;
}

