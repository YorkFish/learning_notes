#include <stdio.h>

void hanoi(char t1, char t2, char t3, int n);
void hanoi2(char t1, char t2, char t3, int n);

int main(void)
{
    hanoi2('A', 'B', 'C', 3);

    return 0;
}

// 将 t1 的 n 个金盘借助 t2 移到 t3
void hanoi(char t1, char t2, char t3, int n)
{
    if(n > 1)
    {
        hanoi(t1, t3, t2, n-1);
        printf("%c -> %c\n", t1, t3);
        hanoi(t2, t1, t3, n-1);
    }
    else if(n == 1)
        printf("%c -> %c\n", t1, t3);
}

// 将 t1 的 n 个金盘借助 t2 移到 t3
void hanoi2(char t1, char t2, char t3, int n)
{
    if(n > 1)
    {
        hanoi2(t1, t3, t2, n-1);
        printf("金片 No.%d, %c -> %c\n", n, t1, t3); // 自顶向下，记金片的序号为 1~n
        hanoi2(t2, t1, t3, n-1);
    }
    else if(n == 1)
        printf("%d, %c -> %c\n", n, t1, t3);
}

