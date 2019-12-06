#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;  // 其实应该用 ElementType，我偷懒了~
    struct Node* pNext;
} NODE, *PNODE;

typedef struct {
    PNODE pHead;
} LIST, *PLIST;

bool is_empty(PLIST pList);
int  length(PLIST pList);
void add_first(PLIST pList, int val);
void append(PLIST pList, int val);
void insert(PLIST pList, int pos, int val);
void remove_(PLIST pList, int val);
bool search(PLIST pList, int val);
void traverse(PLIST pList);


int main() {
    LIST list;
    list.pHead = NULL;
    PLIST pList = &list;
    if (is_empty(pList)) {
        printf("The list is empty.\n");
    }

    add_first(pList, 2);
    add_first(pList, 1);
    append(pList, 4);
    append(pList, 5);
    insert(pList, 2, 3);
    if (search(pList, 1)) {
        printf("1 is in the list.\n");
    }
    remove_(pList, 1);
    remove_(pList, 4);
    printf("len(list) = %d\n", length(pList));
    if (!search(pList, 1)) {
        printf("1 is not in the list.\n");
    }
    traverse(pList);
}


bool is_empty(PLIST pList) {
    bool empty = false;
    if (NULL == pList->pHead) {
        empty = true;
    }
    return empty;
}

int length(PLIST pList) {
    PNODE p = pList->pHead;
    int len = 0;
    while (NULL != p) {
        ++len;
        p = p->pNext;
    }
    return len;
}

void add_first(PLIST pList, int val) {
    PNODE pNew = (PNODE)malloc(sizeof(NODE));
    pNew->data = val;
    if (NULL == pList->pHead) {
        pList->pHead = pNew;
        pNew->pNext = NULL;
    }
    else {
        pNew->pNext = pList->pHead;
        pList->pHead = pNew;
    }
    return ;
}

void append(PLIST pList, int val) {
    if (is_empty(pList)) {
        printf("list is empty");
        return ;
    }

    PNODE pNew = (PNODE)malloc(sizeof(NODE));
    pNew->data = val;
    pNew->pNext = NULL;
    PNODE p = pList->pHead;
    while (NULL != p->pNext) {
        p = p->pNext;
    }
    p->pNext = pNew;
    return ;
}

void insert(PLIST pList, int pos, int val) {
    if (pos <= 0) {
        add_first(pList, val);
    }
    else if (length(pList) - 1 < pos) {
        append(pList, val);
    }
    else {
        PNODE pNew = (PNODE)malloc(sizeof(NODE));
        pNew->data = val;

        int cnt = 0;
        PNODE pre = pList->pHead;
        while (cnt < (pos - 1)) {
            pre = pre->pNext;
            ++cnt;
        }
        pNew->pNext = pre->pNext;
        pre->pNext = pNew;
    }
    return ;
}

void remove_(PLIST pList, int val) {
    PNODE pCur = pList->pHead;
    PNODE pPre = NULL;
    PNODE pTmp = (PNODE)malloc(sizeof(NODE));
    while (pCur) {
        if (pCur->data == val) {
            if (!pPre) {
                pTmp = pList->pHead;
                pList->pHead = pCur->pNext;
            }
            else {
                pTmp = pCur;
                pPre->pNext = pCur->pNext;
            }
            free(pTmp);
            break;
        }
        else {
            pPre = pCur;
            pCur = pCur->pNext;
        }
    }
}

bool search(PLIST pList, int val) {
    bool res = false;
    PNODE pCur = pList->pHead;
    while (pCur) {
        if (pCur->data == val) {
            res = true;
            break;
        }
        pCur = pCur->pNext;
    }
    return res;
}

void traverse(PLIST pList) {
    if (is_empty(pList)) {
        printf("list is empty");
        return ;
    }

    PNODE p = pList->pHead;
    while (NULL != p) {
        printf("%d ", p->data);
        p = p->pNext;
    }
    printf("\n");
    return ;
}
