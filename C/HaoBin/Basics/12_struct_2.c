#include <stdio.h>

struct Student1
{
    int age;
    float score;
    char gender;
};

int main(void)
{
    struct Student1 st1 = {80, 99, 'F'};
    struct Student1* pst = &st1;

    st1.age = 18;
    (*pst).score = 66.6f;   // 不加 f 也能运行；不加 f 默认 double 类型；加上 f/F 就是 float
    pst->gender = 'M';      // -> 主要是为了方便输入，但不能用 *pst.gender 代替 (*pst).gender
    

    printf("%d %f %c\n", st1.age, st1.score, st1.gender);           // 18 66.599998 M
    printf("%d %f %c\n", (*pst).age, (*pst).score, (*pst).gender);  // 18 66.599998 M
    printf("%d %f %c\n", pst->age, pst->score, pst->gender);        // 18 66.599998 M

    return 0;
}

