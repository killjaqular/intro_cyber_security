#include <stdio.h>
#include <math.h> // compile with -lm at end of gcc call

int main(void){
    int var1 = 2;
    int var2 = 4;

    // Addition
    var1 += var2;

    // Subtraction
    var1 -= var2;

    // Division
    var2 = var2 / var1;

    // Multiplication
    var1 = var1 * var1;

    // Exponentiation
    var1 = pow(var1, var1);

    return 0;
}
