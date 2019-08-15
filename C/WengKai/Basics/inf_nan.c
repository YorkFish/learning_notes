#include <stdio.h>

int main()
{
    printf("%f\n",  12/0.0);    //  1.#INF00 有些地方编译结果为  inf
    printf("%f\n", -12/0.0);    // -1.#INF00 有些地方编译结果为 -inf
    printf("%f\n", 0.0/0.0);    // -1.#IND00 有些地方编译结果为  nan

    return 0;
}

