#include <stdio.h>

int factorial(int givenInteger);

int main(void){
    printf("Factorial of 5 is = %d", factorial(5));

    return 0;
}

int factorial(int givenInteger){
    if (givenInteger >= 1){
        return givenInteger * factorial(givenInteger - 1);
    }else{
        return 1;
    }
}
