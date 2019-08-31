#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Arr
{
    int* pBase;                         // 存储数组第一个元素的地址
    int len;                            // 数组最大长度
    int cnt;                            // 当前有效元素的个数
};


void init_arr(struct Arr* pArr, int length);
// bool append_arr();                      // 需要头文件 <stdbool.h>
// bool insert_arr();
// bool delete_arr();

// int get();
// bool is_empty():
// bool is_full();
// void show_arr(struct Arr* pArr); 
// void sort_arr();
// void reverse_arr();

int main(void)
{
    struct Arr arr;
    init_arr(&arr, 6);

    printf("arr.len = %d\n", arr.len);  // arr.len = 6
    printf("arr.cnt = %d\n", arr.cnt);  // arr.cnt = 0

    return 0;
}

void init_arr(struct Arr* pArr, int length)
{
    pArr->pBase = (int*)malloc(sizeof(int) * length);
    // 若内存已满，会分配失败，程序会把 NULL 赋给 pArr-pBase
    if(NULL == pArr->pBase)
    {
        printf("Dynamic memory allocation failed!\n");
        exit(-1); // 终止整个程序，需要头文件 <stdlib.h>
    }
    else
    {
        pArr->len = length;
        pArr->cnt = 0;
    }

    return;
}

