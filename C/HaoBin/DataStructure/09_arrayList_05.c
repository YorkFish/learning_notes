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
// bool delete_arr();
// int get();
bool is_empty(struct Arr* pArr);
bool is_full(struct Arr* pArr);
void show_arr(struct Arr* pArr); 
// void sort_arr();
// void reverse_arr();

int main(void)
{
    struct Arr arr;
    init_arr(&arr, 6);
    show_arr(&arr);                                     // Array is empty!
    
    append_arr(&arr, 1);
    append_arr(&arr, 2);
    append_arr(&arr, 3);
    append_arr(&arr, 4);
    show_arr(&arr);                                     // 1 2 3 4
    
    insert_arr(&arr, 2, 66);

    /*if(append_arr(&arr, 8))
    {
        printf("append successfully!\n");
    }
    else
    {
        printf("append unsuccessfully!\n");
    }*/
    show_arr(&arr);                                     // 1 66 2 3 4

    // printf("arr.len = %d\n", arr.len);
    // printf("arr.cnt = %d\n", arr.cnt);

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

bool insert_arr(struct Arr* pArr, int pos, int val)
{
    // 此处的 pos 是从 1 开始数的
    int i;
    if(is_full(pArr))
        return false;
    else if(pos<1 || pos>pArr->cnt+1 || pos>pArr->len)  // 左边、右边均不能越界
        return false;
    else
    {
        for(i=pArr->cnt-1; i>=pos-1; --i)
        {
            pArr->pBase[i+1] = pArr->pBase[i];
        }
        pArr->pBase[pos-1] = val;
        pArr->cnt++;
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

