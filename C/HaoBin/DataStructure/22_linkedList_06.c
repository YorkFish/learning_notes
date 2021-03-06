#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node
{
    int data;               // 数据域
    struct Node* pNext;     // 指针域
}NODE, *PNODE;

// 函数声明
PNODE create_list(void);
void traverse_list(PNODE pHead);
bool is_empty(PNODE pHead);
int length_list(PNODE pHead);
bool insert_list(PNODE pHead, int pos, int val);
bool delete_list(PNODE pHead, int pos, int* pVal);
void sort_list(PNODE pHead);

int main(void)
{
    int val; // 用来存储删除的值
    PNODE pHead = NULL;
    pHead = create_list();
    /*if(is_empty(pHead))
    {
        printf("Your linked list is empty!\n");
        printf("len(linked list) = %d\n", length_list(pHead));
    }
    else
    {
        traverse_list(pHead);
        printf("len(linked list) = %d\n", length_list(pHead));
    }*/
    // sort_list(pHead);
    // insert_list(pHead, 3, 66);
    // delete_list(pHead, 3, &val);
    if(delete_list(pHead, 3, &val))
        printf("Delete successfully! The number is: %d\n", val);
    else
        printf("Delete unsuccessfully!\n");
    traverse_list(pHead);

    return 0;
}

PNODE create_list(void)
{
    int len;                // 有效节点个数
    int i;
    int val;                // 临时存放用户输入的节点值
    printf("Please enter the number of the linked list: ");
    scanf("%d", &len);

    PNODE pHead = (PNODE)malloc(sizeof(NODE));
    if(NULL == pHead)
    {
        printf("Memory allocation failed! The program terminates!\n");
        exit(-1);
    }
    PNODE pTail = pHead;
    pTail->pNext = NULL;

    for(i=0; i<len; ++i)
    {
        printf("No.%d: ", i+1);
        scanf("%d", &val);
        PNODE pNew = (PNODE)malloc(sizeof(NODE));
        if(NULL == pNew)
        {
            printf("Memory allocation failed! The program terminates!\n");
            exit(-1);
        }
        /* 此法不可行
        pNew->data = val;
        pHead->pNext = pNew;
        pNew->pNext = NULL;*/
        pNew->data = val;
        pTail->pNext = pNew;
        pNew->pNext = NULL;
        pTail = pNew;
    }

    return pHead;
}

void traverse_list(PNODE pHead)
{
    PNODE p = pHead->pNext;
    printf("\n");
    while(NULL != p)
    {
        printf("%d ", p->data);
        p = p->pNext;
    }
    printf("\n");

    return;
}

bool is_empty(PNODE pHead)
{
    if(NULL == pHead->pNext)
        return true;
    else
        return false;
}

int length_list(PNODE pHead)
{
    PNODE p = pHead->pNext;
    int len = 0;

    while(NULL != p)
    {
        ++len;
        // p->pNext = pHead->pNext; // 这样会死循环
        // p = pHead->pNext; // 这样也会死循环
        p = p->pNext;
    }

    return len;
}

// 在第 pos 个节点之前插入数据 val；pos 的值从 1 开始
bool insert_list(PNODE pHead, int pos, int val)
{
    int i = 0;
    PNODE p = pHead;
    while(NULL!=p && i<pos-1)
    {
        p = p->pNext;
        ++i;
    }
    if(i>pos-1 || NULL==p)
        return false;

    PNODE pNew = (PNODE)malloc(sizeof(NODE));
    if(NULL == pNew)
    {
        printf("Dynamic memory allocation failed\n");
        exit(-1);
    }
    pNew->data = val;
    pNew->pNext = p->pNext;
    p->pNext = pNew;
    return true;
}

// 删除第 pos 个数据
bool delete_list(PNODE pHead, int pos, int* pVal)
{
    int i = 0;
    PNODE p = pHead;
    while(NULL!=p && i<pos-1)
    {
        p = p->pNext;
        ++i;
    }
    if(i>pos-1 || NULL==p)
        return false;

    PNODE q = p->pNext;
    *pVal = q->data;
    p->pNext = q->pNext;
    free(q);
    q = NULL;
    return true;
}

void sort_list(PNODE pHead) // 升序
{
    // int len = length_list(pHead);
    /*PNODE p, q, t; // 可以用 len，也可以将 t 定义成 int
    for(p=pHead->pNext; NULL!=p->pNext; p=p->pNext)
        for(q=p->pNext; NULL!=q; q=q->pNext)
        {
            if(p->data > q->data)
            {
                t->data = p->data;
                p->data = q->data;
                q->data = t->data;
            }
        }*/
    int t;
    PNODE p, q;
    for(p=pHead->pNext; NULL!=p->pNext; p=p->pNext)
        for(q=p->pNext; NULL!=q; q=q->pNext)
        {
            if(p->data > q->data)
            {
                t = p->data;
                p->data = q->data;
                q->data = t;
            }
        }

    return;
}

