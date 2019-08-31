#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Arr
{
    int* pBase;                                         // 存储数组第一个元素的地址
    int len;                                            // 数组最大长度
    int cnt;                                            // 当前有效元素的个数
};


void init_arr(struct Arr* pArr, int length);
bool append_arr(struct Arr* pArr, int val);             // 需要头文件 <stdbool.h>
bool insert_arr(struct Arr* pArr, int pos, int val);    // pos 的值从 1 开始
bool delete_arr(struct Arr* pArr, int pos, int* pVal);
// int get();
bool is_empty(struct Arr* pArr);
bool is_full(struct Arr* pArr);
void show_arr(struct Arr* pArr); 
void sort_arr1(struct Arr* pArr);
void sort_arr2(struct Arr* pArr);
void reverse_arr(struct Arr* pArr);

int main(void)
{
    struct Arr arr;
    int val;

    init_arr(&arr, 6);
    show_arr(&arr);
    
    append_arr(&arr, 10);
    append_arr(&arr, 2);
    append_arr(&arr, 33);
    append_arr(&arr, 24);
    show_arr(&arr);
    
    insert_arr(&arr, 5, 6);
    /*if(append_arr(&arr, 8))
    {
        printf("append successfully!\n");
    }
    else
    {
        printf("append unsuccessfully!\n");
    }*/
    // show_arr(&arr);
    /*if(delete_arr(&arr, 6, &val))
    {
        printf("delete successfully!\n");
        printf("The number you delete is: %d\n", val);
    }
    else
    {
        printf("delete unsuccessfully!\n");
    }*/
    // delete_arr(&arr, 4, &val);
    show_arr(&arr);
    
    reverse_arr(&arr);
    show_arr(&arr);
    
    sort_arr1(&arr);
    show_arr(&arr);
    
    sort_arr2(&arr);
    show_arr(&arr);

    return 0;
}

void init_arr(struct Arr* pArr, int length)
{
    pArr->pBase = (int*)malloc(sizeof(int) * length);
    // 若内存已满，会分配失败，程序会把 NULL 赋给 pArr-pBase
    if(NULL == pArr->pBase)
    {
        printf("Dynamic memory allocation failed!\n");
        exit(-1);                                       // 终止整个程序，需要头文件 <stdlib.h>
    }
    else
    {
        pArr->len = length;
        pArr->cnt = 0;
    }

    return;
}

bool append_arr(struct Arr* pArr, int val)              // Python 中 append 返回 None
{
    // 满，返回 false
    if(is_full(pArr))
        return false;
    // 不满，追加
    /*else
    {
        pArr->pBase[pArr->cnt] = val;
        pArr->cnt++; // -> 的优先级比 ++ 高

        return true;
    }*/
    // 可以不用 else
    pArr->pBase[pArr->cnt] = val;
    pArr->cnt++;
    return true;
}

bool insert_arr(struct Arr* pArr, int pos, int val)     // 可以理解成：在第 pos 个数字之前插入 val
{
    int i;
    if(is_full(pArr))
        return false;
    else if(pos<1 || pos>pArr->cnt+1)
        // 1. 放缩，不需要写 pos>pArr->len；只要 pos<=pArr->cnt 即可
        // 2. 如 pos=len cnt==len-1 时，满足 insert 规则，不该返回 false，所以 pos>pArr->cnt+1
        return false;
    else
    {
        for(i=pArr->cnt; i>=pos; --i)
        {
            pArr->pBase[i] = pArr->pBase[i-1];
        }
        pArr->pBase[pos-1] = val;
        pArr->cnt++;
        return true;
    }
}

bool delete_arr(struct Arr* pArr, int pos, int* pVal)
{
    int i;
    if(is_empty(pArr))
        return false;
    else if(pos<1 || pos>pArr->cnt)
        return false;
    else
    {
        *pVal = pArr->pBase[pos-1];
        for(i=pos; i<pArr->cnt; ++i)
        {
            pArr->pBase[i-1] = pArr->pBase[i];
        }
        pArr->cnt--;
        return true;
    }
}

bool is_empty(struct Arr* pArr)                         // 理论上，接收 pArr->cnt 也行，但不好
{
    if(0 == pArr->cnt)
        return true;
    else
        return false;
}

bool is_full(struct Arr* pArr)
{
    if(pArr->cnt == pArr->len)
        return true;
    else
        return false;
}

void show_arr(struct Arr* pArr)
{
    /* 伪算法 / 伪代码
    if(数组为空)
    {
        提示用户数组为空
    }
    else
    {
        输出数组有效内容
    }*/
    if(is_empty(pArr))                                  // 理论上，直接 !pArr->cnt 或 is_empty(pArr->cnt) 都行
    {
        printf("Array is empty!\n");
    }
    else
    {
        for(int i=0; i<pArr->cnt; ++i)
        {
            printf("%d ", pArr->pBase[i]);
        }
        printf("\n");
    }
}

void reverse_arr(struct Arr* pArr)
{
    int i = 0;
    int j = pArr->cnt-1;
    int t;
    while(i < j)
    {
        t = pArr->pBase[i];
        pArr->pBase[i] = pArr->pBase[j];
        pArr->pBase[j] = t;
        ++i;
        --j;
    }

    return;
}

void sort_arr1(struct Arr* pArr)                        // 冒泡（升序）
{
    int i, j, t;
    for(i=0; i<pArr->cnt-1; ++i)
        for(j=0; j<pArr->cnt-1-i; ++j)
        {
            if(pArr->pBase[j] > pArr->pBase[j+1])
            {
                t = pArr->pBase[j];
                pArr->pBase[j] = pArr->pBase[j+1];
                pArr->pBase[j+1] = t;
            }
        }
}

void sort_arr2(struct Arr* pArr)                        // 选择（降序）
{
    int i, j, t;
    for(i=0; i<pArr->cnt-1; ++i)
        for(j=i+1; j<pArr->cnt; ++j)
        {
            if(pArr->pBase[i] < pArr->pBase[j])
            {
                t = pArr->pBase[i];
                pArr->pBase[i] = pArr->pBase[j];
                pArr->pBase[j] = t;
            }
        }
}

