#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

double solution(int numbers[], size_t numbers_len) {
    double sum = 0;
    for (size_t i = 0; i < numbers_len; ++i) {
        sum += numbers[i];
    }
    double average = sum / numbers_len;
    return average;
}