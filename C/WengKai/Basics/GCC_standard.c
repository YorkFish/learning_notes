#include <stdio.h>

int main()
{
/*
$ gcc -v
...
Target: x86_64-w64-mingw32
...
Thread model: win32
gcc version 8.1.0 (x86_64-win32-seh-rev0, Built by MinGW-W64 project)


$ gcc -posix -E -dM - </dev/null
...
#define __STDC_VERSION__ 201112L
...


$ man gcc
...
gnu11
gnu1x
    GNU dialect of ISO C11. This is the default for C code. The name gnu1x is deprecated.
...
*/
    // $ gcc -std=c99 -o GCC_standard GCC_standard.c
    // $ gcc -std=c99 GCC_standard.c -o GCC_standard
    int a[13] = {[1]=2, 4, [5]=6};
    
    for(int i=0; i<13; i++)
    {
        printf("a[%d] = %d\n", i, a[i]);
    }
    
    return 0;
}

