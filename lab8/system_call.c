#include <stdio.h>
#include <syscall.h>
#include <unistd.h>

int main(void){
    int syscallResult = 0;

    syscallResult = syscall(SYS_chmod, "./system_call", 700);

    if (syscallResult != 0){
        fprintf(stderr, "chmod failed, errno = %d\n", syscallResult);
    }

    return 0;
}
