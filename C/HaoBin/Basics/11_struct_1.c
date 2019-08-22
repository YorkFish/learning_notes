#include <stdio.h>

// 方法1
struct Student1
{
    int age;
    float score;
    char gender;
};

// 方法2
struct Student2
{
    int age;
    float score;
    char gender;
} st2;

// 方法3
struct
{
    int age;
    float score;
    char gender;
} st3;

int main(void)
{
    struct Student1 st1 = {80, 99, 'F'};
    st2.age = 18;
    st2.score = 98;
    st2.gender = 'M';

    printf("%d %f %c\n", st1.age, st1.score, st1.gender);   // 80 99.000000 F
    printf("%d %f %c\n", st2.age, st2.score, st2.gender);   // 18 98.000000 M

    return 0;
}

