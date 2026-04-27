

#include <unistd.h>

// Our own print function
void myprinty(char *text) {
    int i = 0;
    while(text[i] != '\0') {  // Loop until end of string
        write(1, &text[i], 1);  // Write one character to screen
        i++;
    }
}

int main() {
    myprint("Hello from my own function!\n");
    return 0;
}
