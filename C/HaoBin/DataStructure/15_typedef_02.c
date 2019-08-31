#include <stdio.h>

typedef struct Student
{
    int sid;
    char gender;
    char name[100];
}* PST;                                 // PST 等价于 struct Student*

int main(void)
{
    struct Student st;
    PST pst = &st;
    pst->sid = 001;
    printf("st.sid = %d\n", pst->sid);  // st.sid = 1

    return 0;
}

