#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len) {
    int* answer = (int*)malloc(num_list_len * sizeof(int)); 
    if (answer == NULL) { 
    return NULL;
    }
    
    for (size_t i = 0; i < num_list_len; i++) {
        answer[i] = num_list[num_list_len - i - 1];
    }
    
    return answer;
}
