#include <stdio.h>
#include <string.h>

int main(void){
    char* coolStringBro = "Iterate over this string and print each char individually.";

    int counter;               // Declare a counter
    for (counter = 0; counter < strlen(coolStringBro); counter++){
        printf("%c", coolStringBro[counter]);
    }

    return 0;
}
