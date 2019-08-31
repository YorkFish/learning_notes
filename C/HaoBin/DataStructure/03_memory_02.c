#include <stdio.h>
#include <malloc.h>

struct Student
{
    int sid;
    int age;
    int gender;
};

int main(void)
{
    struct Student st;
    int* p;
    printf("sizeof(st) = %d\n",             sizeof(st));    // sizeof(st) = 12
    printf("sizeof(p) = %d\n",              sizeof(p));     // sizeof(p) = 8
    printf("sizeof(int) = %d\n",            sizeof(int));   // sizeof(int) = 4
    
    return 0;
}

