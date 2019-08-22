#include <stdio.h>

enum Weekday1
{
    Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
};  // 默认从 0 开始，之后自增为 1

enum Weekday2
{
    MonDay=4, TuesDay, WednesDay, ThursDay, FriDay, SaturDay, SunDay
};  // 有初始值，则从初始值开始，自增仍为 1

int main()
{
    enum Weekday1 day1 = Wednesday;
    printf("day1 = %d\n", day1);    // day1 = 2

    enum Weekday2 day2 = WednesDay;
    printf("day2 = %d\n", day2);    // day2 = 6

    return 0;
}

