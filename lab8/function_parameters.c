#include <stdio.h>

char copyFirstLetter(char* givenString);

int main(void){
    char* someString = "The first char in this string is 'T'";
    char printChar;

    printChar = copyFirstLetter(someString);

    printf("%c", printChar);

    return 0;
}

char copyFirstLetter(char* givenString){
    char firstChar = givenString[0];

    return firstChar;
}
