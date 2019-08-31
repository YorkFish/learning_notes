#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node
{
    int data;
    struct Node* pNext;
}NODE, *PNODE;

typedef struct Stack
{
    PNODE pTop;
    PNODE pBottom;
}STACK, *PSTACK;

void init(PSTACK pS);
void push(PSTACK pS, int val);
void traverse(PSTACK pS);
bool pop(PSTACK pS, int* pVal);
bool is_empty(PSTACK pS);

int main(void)
{
    int val;
    STACK S;
    init(&S);                       // 造出一个空栈
    push(&S, 10);                   // 压栈
    push(&S, 28);
    push(&S, -5);
    push(&S, 39);
    push(&S, -27);
    traverse(&S);                   // 遍历
    if(pop(&S, &val))
    {
        printf("Pop successfully! The data is: %d\n", val);
        traverse(&S);
    }
    else
    {
        printf("Pop unsuccessfully!\n");
    }

    return 0;
}

void init(PSTACK pS)
{
    pS->pTop = (PNODE)malloc(sizeof(NODE));
    if(NULL == pS->pTop)
    {
        printf("Memory allocation failed!");
        exit(-1);
    }
    else
    {
        pS->pBottom = pS->pTop;
        pS->pTop->pNext = NULL;     // pS->pBottom->pNext = NULL; 也行
        return;
    }
}

void push(PSTACK pS, int val)
{
    PNODE pNew = (PNODE)malloc(sizeof(NODE));
    if(NULL == pNew)
    {
        printf("Memory allocation failed!");
        exit(-1);
    }
    else
    {
        pNew->data = val;
        pNew->pNext = pS->pTop;
        pS->pTop = pNew;
        // pNew->pNext = NULL; // 不要写这句
        return;
    }
}

void traverse(PSTACK pS)
{
    PNODE pT = pS->pTop;
    /*for(pT=pS->pTop; pT!=pS->pBottom; pT=pT->pNext)
    {
        printf("%d ", pT->data);
    }*/
    while(pT != pS->pBottom)
    {
        printf("%d ", pT->data);
        pT = pT->pNext;
    }
    printf("\n");
    // printf("%d\n", pS->pBottom->data); // 这句会输出垃圾值

    return;
}

bool pop(PSTACK pS, int* pVal)
{
    // if(NULL == pS)
    if(is_empty(pS))
    {
        printf("There exsit no data!\n");
        return false;
    }
    else
    {
        PNODE q = pS->pTop;
        *pVal = q->data;
        pS->pTop = q->pNext;
        free(q);
        q = NULL;
        return true;
    }
}

bool is_empty(PSTACK pS)
{
    // if(NULL == pS)
    if(pS->pTop == pS->pBottom)
        return true;
    else
        return false;
}

