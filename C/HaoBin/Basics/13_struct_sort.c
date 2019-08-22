#include <stdio.h>
#include <string.h>
#include <malloc.h>

struct Student1
{
    int age;
    float score;
    char name[100];
};

void inPut(struct Student1* pi, int len)
{
    int i;
    for(i=0; i<len; ++i)
    {
        /*printf("Please enter the age of student: ");
        scanf("%d\n", &pi[i].age);
        printf("Please enter the score of student: ");
        scanf("%f\n", &pi[i].score);
        printf("Please enter the name of student: ");
        scanf("%s\n", pi[i].name);*/
        printf("Please enter the age, score and name of No.%d student: ", i+1);
        scanf("%d %f %s", &pi[i].age, &pi[i].score, pi[i].name);
    }

    return;
}

void outPut(struct Student1* po, int len)
{
    int i;
    for(i=0; i<len; ++i)
    {
        printf("No.%d student: age = %d, score = %f, name = %s\n", \
        i+1, (po+i)->age, (po+i)->score, (po+i)->name);
    }

    return;
}

void sort(struct Student1* ps, int len)
{
    int i, j;
    struct Student1 t;
    printf("\nsorting...\n");
    for(i=0; i<len-1; ++i)
    {
        for(j=0; j<len-1-i; ++j)
        {
            if(ps[j].score > ps[j+1].score) // > increase; < decrease
            {
                t = ps[j];
                ps[j] = ps[j+1];
                ps[j+1] = t;
            }
        }
    }

    return;
}

int main(void)
{
    int len = 0;
    struct Student1* pArr;
    
    printf("h0\n");
    printf("Please enter the number of students: ");
    scanf("%d", &len);
    
    printf("h1\n");
    pArr = (struct Student1*)malloc(len * sizeof(struct Student1));
    
    printf("h2\n");
    inPut(pArr, len);
    
    printf("h3\n");
    outPut(pArr, len);

    printf("h4\n");
    sort(pArr, len);

    printf("h5\n");
    outPut(pArr, len);

    printf("h6\n");
    free(pArr);
    printf("h7\n");

    return 0;
}

