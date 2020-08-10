#include <stdio.h>
#include <string.h>
#include <math.h>

int titleToNumber(char * s){
    int sum = 0;
    int DIFF = 'Z' - 'A' + 1;
    for (int i = 0, l = strlen(s); i < l; i++) {
        sum += pow(DIFF, i) * (s[l - i - 1] - 'A' + 1);
    }
    return sum;
}
