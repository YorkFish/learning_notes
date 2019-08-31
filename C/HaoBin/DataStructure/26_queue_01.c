#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>

typedef struct Queue
{
    int* pBase;
    int front;
    int rear;
}QUEUE;

void init(QUEUE* pQ);
bool full_queue(QUEUE* pQ);
bool extend_queue(QUEUE* pQ, int val);
void traverse_queue(QUEUE* pQ);


int main(void)
{
    QUEUE Q;
    init(&Q);                                   // 初始化
    extend_queue(&Q, 1);                        // 入队
    extend_queue(&Q, 2);
    extend_queue(&Q, 3);
    extend_queue(&Q, 4);
    extend_queue(&Q, 5);
    extend_queue(&Q, 6);
    extend_queue(&Q, 7);
    traverse_queue(&Q);                         // 遍历

    return 0;
}

void init(QUEUE* pQ)
{
    pQ->pBase = (int*)malloc(sizeof(int) * 6);  // 设置默认长度为 6 个
    pQ->front = 0;
    pQ->rear = 0;
}

bool full_queue(QUEUE* pQ)
{
    if((pQ->rear+1)%6 == pQ->front)
        return true;
    else
        return false;                           // 此时 pQ->rear = 5
}

bool extend_queue(QUEUE*pQ, int val)
{
    if(full_queue(pQ))
    {
        return false;
    }
    else
    {
        pQ->pBase[pQ->rear] = val;
        pQ->rear = (pQ->rear + 1) % 6;          // 默认 6 个长度
        return true;
    }
}

void traverse_queue(QUEUE* pQ)
{
    int t = pQ->front;
    while(t != pQ->rear)
    {
        // printf("%d %d\n", pQ->pBase[t], t);
        printf("%d ", pQ->pBase[t]);
        t = (t + 1) % 6;
    }
    printf("\n");

    return;
}

