#include <stdio.h>

int f(int m);
int g(int g);

int main(void)
{
    printf("%d\n", f(5));   // 10

    return 0;
}

/* f 与 g 形成间接递归，不要这样
void f(int m)
{
    g(m);
}

void g(int n)
{
    f(n);
}
*/

int f(int m)
{
    return g(m);
}

int g(int n)
{
    return 2 * n;
}

