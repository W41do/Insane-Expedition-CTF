#include <stdio.h>
#include <string.h>
// #include <iostream>
#include <stdlib.h>
#include <unistd.h>


/*
Original link used to turn of vulnerabilities and proper file compilation:
https://gist.github.com/apolloclark/6cffb33f179cc9162d0a


To turn off Vulnerabilities:
sudo bash -c 'echo "kernel.randomize_va_space = 0" >> /etc/sysctl.conf'
ulimit -c unlimited


Verification:
cat /proc/sys/kernel/randomize_va_space
sudo sysctl -p
ulimit -c

File Compilation:
gcc -z execstack -fno-stack-protector -mpreferred-stack-boundary=3 -g BufferOverflow.c -o BufferOverflow


Exploit by: James Lyne - How They Hack: Simple Buffer Overflow
https://www.youtube.com/watch?v=B4v56Ns3QhQ
*/


int main() {
    char command[50];
    char sys[50];
    char password[32];
    int passcheck = 0;

    #ifdef _WIN32
        // strcpy(sys, "Windows 32-bit");
        strcpy(sys, "Windows");
    #elif _WIN64
        // strcpy(sys, "Windows 64-bit");
        strcpy(sys, "Windows");
    #elif __APPLE__ || __MACH__
        strcpy(sys, "Mac OSX");
    #elif __linux__
        strcpy(sys, "Linux");
    #elif __FreeBSD__
        strcpy(sys, "FreeBSD");
    #elif __unix || __unix__
        strcpy(sys, "Unix");
    #else
        strcpy(sys, "Other");
    #endif

    if (strcmp(sys, "Windows") == 0) {
        strcpy(command, "cls" );
    } else {
        strcpy(command, "clear" );
    }

    system(command);
    system(command);

    while (1)
    {

        printf("\n  [ You have arrived at the OBHAJOBA PROJEKTU station and realized that you have forgotten your ISIC card for entry into the building.                                    ]");
        printf("\n  [ You don't have time to go back to the PURKYNOVY dorms and the project defense starts in 5 minutes. So you thought of trying to guess the entry code for the building. ]");
        printf("\n  [ You only have 5 minutes, so hurry up or you'll get 0 points for the project.                                                                                          ]\n");
        printf("\n  [ ENTER PASSWORD ]> ");
        gets(password);
        // gets(password);

        // printf(sys);
        
        
        if(strcmp(password, "JumboRustyDrone")) {
            printf("\n  [ Wrong ]\n");
        } else {
            printf("\n  [ Correct ]\n");
            passcheck = 1;
        }

        if(passcheck) {
            printf("[ FLAG: greencat69695 ]");
        }

        sleep(1);

        system(command);
    }
    return 0;
}