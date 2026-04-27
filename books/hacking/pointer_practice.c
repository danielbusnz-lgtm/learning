

// POINTER PRACTICE
// Predict what each printf will output BEFORE running the code
// Write your answers in the comments

#include <stdio.h>

int main() {

    // Question 1: Basic pointer
    int x = 5;
    int *p = &x;

    printf("Q1a: %d\n", x);     // Your answer:  5???
    printf("Q1b: %d\n", *p);    // Your answer:   5???


    // Question 2: Changing the original
    x = 20;

    printf("Q2: %d\n", *p);     // still  Your answer: still 5????


    // Question 3: Changing through the pointer
    *p = 100;

    printf("Q3: %d\n", x);      // 20 Your answer: ???


    // Question 4: Two variables
    int a = 10;
    int b = 30;
    int *ptr = &a;

    printf("Q4a: %d\n", *ptr);  // 10  Your answer: ???

    ptr = &b;  // Now ptr points to b

    printf("Q4b: %d\n", *ptr);  // memory address of b Your answer: ???


    // Question 5: What does this do?
    int num = 7;
    int *pointer = &num;
    *pointer = *pointer + 3;

    printf("Q5: %d\n", num);    // Your answer: ???


    return 0;
}
