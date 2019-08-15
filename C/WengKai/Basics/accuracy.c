#include <stdio.h>

int main()
{
    printf("%.3f\n",  -0.0049);     // -0.005
    printf("%.30f\n", -0.0049);     // -0.004899999999999999800000000000
    printf("%.3f\n",  -0.00049);    // -0.000

    return 0;
}

