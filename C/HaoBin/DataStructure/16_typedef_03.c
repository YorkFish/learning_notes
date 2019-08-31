#include <stdio.h>

typedef struct Student
{
    int sid;
    char gender;
    char name[100];
}* PSTU, STU;                           // PSTU 等价于 struct Student*；STU 等价于 struct Student；顺序可换

int main(void)
{
    STU st;                             // 相比 16_typedef_02.c 方便了一点儿
    PSTU pst = &st;

    pst->sid = 100;
    printf("st.sid = %d\n", pst->sid);  // st.sid = 100

    return 0;
}

