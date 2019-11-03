#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

#define PASS_SIZE 16
		
int main(void){
    char *password;
    int i;
    srand(time(0));
    password = calloc(1, PASS_SIZE+1);
    for (i = 0; i < PASS_SIZE; i++) {
        password[i] = rand() % ('z'-' ') + ' ';
    }
    printf(password);
    free(password);
    return 0;
}
