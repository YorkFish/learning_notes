#include <stdio.h>

void buy_chicken();

int main() {
    buy_chicken();
    
    return 0;
}

void buy_chicken() {
    int cocks = -1, hens, chicks;
    while (cocks < 20) {
        cocks++;
        hens = -1;
        while (hens < 33) {
            hens++;
            chicks = 100 - cocks - hens;
            if (chicks % 3) {
                continue;
            }
            if (5*cocks + 3*hens + chicks/3 == 100) {
                printf("百钱可买公鸡 %2d 只，母鸡 %2d 只，小鸡 %d 只\n", cocks, hens, chicks);
            }
        }
    }
}
