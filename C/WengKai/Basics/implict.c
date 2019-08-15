#include <stdio.h>

void cheer(int i)
{
    printf("cheer %d\n", i);
}

int main()
{
    double d = 2.8;
    cheer(2.0);         // cherr 2
    cheer(2.5);         // cherr 2
    cheer(d);           // cherr 2

    return 0;
}

