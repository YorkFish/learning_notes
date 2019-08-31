#include <stdio.h>

#define uchar unsigned char                         // 注意 #define 与 typedef 使用时参数的顺序
typedef unsigned int uint;

struct Student_1
{
    int sid;
    char gender;
    char name[100];
};

typedef struct Student_2
{
    int sid;
    char gender;
    char name[100];
}ST2;

int main(void)
{
    uchar num1 = 128;
    uint num2 = 32768;
    struct Student_1 st1 = {001, 'F', "Lily"};
    ST2 st2_1 = {002, 'F', "Lucy"};
    struct Student_2 st2_2 = {003, 'F', "Liya"};    // typedef 后，两种定义方法均可用

    printf("num1 = %d, num2 = %d\n", num1, num2);   // num1 = 128, num2 = 32768
    printf("st1.name = %s, st2_1.name = %s, st2_2.name = %s\n", st1.name, st2_1.name, st2_2.name);
                                                    // st1.name = Lily, st2_1.name = Lucy, st2_2.name = Liya

    return 0;
}

