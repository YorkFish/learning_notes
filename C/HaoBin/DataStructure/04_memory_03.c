#include <stdio.h>
#include <malloc.h>

struct Student
{
    int sid;
    int age;
};

struct Student* creatStudent(void);
void showStudent(struct Student* p);

int main(void)
{
    struct Student* ps;
    ps = creatStudent();
    showStudent(ps);        // p->sid = 1, p->age = 80
    
    return 0;
}

struct Student* creatStudent(void)
{
    struct Student* p = (struct Student*)malloc(sizeof(struct Student));
    p->sid = 001;
    p->age = 80;

    return p;
}

void showStudent(struct Student* p)
{
    printf("p->sid = %d, p->age = %d\n", p->sid, p->age);
}

