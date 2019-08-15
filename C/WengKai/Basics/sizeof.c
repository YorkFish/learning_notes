#include <stdio.h>

int main()
{
    printf("sizeof(char) = %I64d\n",        sizeof(char));          // 1
    printf("sizeof(short) = %I64d\n",       sizeof(short));         // 2
    printf("sizeof(int) = %I64d\n",         sizeof(int));           // 4
    printf("sizeof(float) = %I64d\n",       sizeof(float));         // 4
    printf("sizeof(double) = %I64d\n",      sizeof(double));        // 8
    printf("sizeof(long) = %I64d\n",        sizeof(long));          // 4
    printf("sizeof(long int) = %I64d\n",    sizeof(long int));      // 4
    printf("sizeof(long long) = %I64d\n",   sizeof(long long));     // 8

    printf("sizeof('a') = %I64d\n",         sizeof('a'));           // 4
    printf("sizeof(2) = %I64d\n",           sizeof(2));             // 4
    printf("sizeof(2.0) = %I64d\n",         sizeof(2.0));           // 8
    
    printf("sizeof(sizeof('a')) = %I64d\n", sizeof(sizeof('a')));   // 8
    printf("sizeof(sizeof(2)) = %I64d\n",   sizeof(sizeof(2)));     // 8
    printf("sizeof(sizeof(2.0)) = %I64d\n", sizeof(sizeof(2.0)));   // 8
    
	return 0;
}

