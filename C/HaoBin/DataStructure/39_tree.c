#include <stdio.h>
#include <malloc.h>

struct BTNode
{
    int data;
    struct BTNode* pLchild;                 // p:指针 L:左 child:孩子
    struct BTNode* pRchild;
};

struct BTNode* CreateBTree(void);
void preTraverseBTree(struct BTNode* pT);   // 先序
void inTraverseBTree(struct BTNode* pT);    // 中序
void postTraverseBTree(struct BTNode* pT);  // 后序

int main(void)
{
    struct BTNode* pT = CreateBTree();

    // preTraverseBTree(pT);
    // inTraverseBTree(pT);
    postTraverseBTree(pT);

    return 0;
}

/*   A
 *  / \
 * B   C
 *    /
 *   D
 *    \
 *     E
 */
struct BTNode* CreateBTree(void)
{
    struct BTNode* pA = (struct BTNode*)malloc(sizeof(struct BTNode));
    struct BTNode* pB = (struct BTNode*)malloc(sizeof(struct BTNode));
    struct BTNode* pC = (struct BTNode*)malloc(sizeof(struct BTNode));
    struct BTNode* pD = (struct BTNode*)malloc(sizeof(struct BTNode));
    struct BTNode* pE = (struct BTNode*)malloc(sizeof(struct BTNode));

    pA->data = 'A';
    pB->data = 'B';
    pC->data = 'C';
    pD->data = 'D';
    pE->data = 'E';

    pA->pLchild = pB;
    pA->pRchild = pC;
    pB->pLchild = pB->pRchild = NULL;
    pC->pLchild = pD;
    pC->pRchild = NULL;
    pD->pLchild = NULL;
    pD->pRchild = pE;
    pE->pLchild = pE->pRchild = NULL;

    return pA;
};

void preTraverseBTree(struct BTNode* pT)    // 先序
{
    // 先访问根节点，再先序左，最后先序右
    if(NULL != pT)
    {
        printf("%c \n", pT->data);
        
        if(NULL != pT->pLchild)
        {
            preTraverseBTree(pT->pLchild);
        }
        if(NULL != pT->pRchild)
        {
            preTraverseBTree(pT->pRchild);
        }
    }
}

void inTraverseBTree(struct BTNode* pT)     // 中序
{
    // 先中序左，再访问根节点，最后中序右
    if(NULL != pT)
    {
        if(NULL != pT->pLchild)
        {
            inTraverseBTree(pT->pLchild);
        }

        printf("%c \n", pT->data);
        
        if(NULL != pT->pRchild)
        {
            inTraverseBTree(pT->pRchild);
        }
    }
}

void postTraverseBTree(struct BTNode* pT)   // 后序
{
    // 先后序左，再后序右，最后访问根节点
    if(NULL != pT)
    {
        if(NULL != pT->pLchild)
        {
            postTraverseBTree(pT->pLchild);
        }

        if(NULL != pT->pRchild)
        {
            postTraverseBTree(pT->pRchild);
        }

        printf("%c \n", pT->data);
    }
}

