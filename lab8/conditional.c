#include <stdio.h>
#include <string.h> // required for strcmp();

int main(void){
    char* myString = "Hello, World.";

    if (strcmp(myString, "Hello, World.") == 0){
        puts(myString);
    }else{
        puts("Unreachable code.\n");
    }

    return 0;
}
