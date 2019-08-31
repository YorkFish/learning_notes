#include <stdio.h>
#include <stdbool.h>

struct Arr
{
    int* pBase;                         // 存储数组第一个元素的地址
    int len;                            // 数组最大长度
    int cnt;                            // 当前有效元素的个数
    int increment;                      // 自动增长因子
};


void init_arr(struct Arr* pArr);
/*bool append_arr();
bool insert_arr();
bool delete_arr();

int get();
bool is_empty():
bool is_full();
void show_arr(); 
void sort_arr();
void reverse_arr();*/

int main(void)
{
    struct Arr arr;
    bool t = true;                      // true -> 1, false -> 0
    init_arr(&arr);

    printf("arr.len = %d\n", arr.len);  // arr.len = 99
    printf("t = %d\n", t);              // t = 1

    return 0;
}

void init_arr(struct Arr* pArr)
{
    (*pArr).len = 99;
}

