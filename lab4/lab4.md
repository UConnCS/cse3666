# Lab 4: Functions: removing spaces

*Due Date: By the end of Fri, 2/18/2022*

Try your best to complete the lab assignment during the lab session.

*If you work on computers in the learning center or a UConn virtual desktop, 
save your files on P drive. Otherwise, you may lose your files.*

## Learning Objectives

* Write and call functions

* Use storage on stack in a function

* Pass arrays/strings to functions

## Description

In this lab, we refactor the code we wrote in lab 3. We will implement two functions. 

### Function: remove spaces

The first funciton is `remove_spaces()`. Its prototype is as follows. Note the
function does not return a value.

```
void    remove_spaces(char *str, char *res);
```

This is a leaf function. We can copy the code in Step 2 from lab3. Revise it if
necessary.

Note the following:

*   `str` and `res` are strings. Like an array, when we pass a string to a
    function, we only put its starting address in an argument register. For
    example, register `a0` has the starting address of string str. 

*   This function is a leaf function. It does not need to use the stack.

*   The function does not return a value.

### Function: print non spaces  

The second function is `print_ns()`. The prototype is as follows. 

```
char * print_ns(char *s);
```

The funciton takes a string `s` as its input, calls `remove_spaces()` to
remove spaces in `str`, prints ther result, and then returns its parameter
`str`. 

The steps to be implemtned in the function are listed below. Do NOT use 
`la`. All the information the function needs is the argument.

1.  Save registers. This step should be done later after Steps 2 to 4 are completed.

2.  Create local array `res` of 128 bytes on the stack. We only need to move the
    stack pointer to allocate space (128 bytes) for the string. 

    Question: Where is the starting address of `res`?

3.  Call `remove_spaces` funcition to remove spaces in `s` and save the result in `res`.

    `remove_spaces(s, res);`

    Note that we need to put string s's address in `a0`, and res's address in `a1`.  

4.  Print `res` with a system call. 

5.  Restore registers and stack, and return `s`. 

    Question: Do we need to save the starting address of `s` on stack?

Clearly mark each step in your code.

Again, we write code for Steps 2, 3, and 4 first so that we know what registers
to save and restore in Steps 1 and 5.

Step through the function and observe the values in registers `ra` and `sp`. Also
examine the stack in Data Segment window. 

### Skeleton code

Skeleton code is in `lab4.s`. The main function does the following.

1.   Read a string from the console into `str`.
2.   If the line is empty, goto Step 5.
3.   Call `print_ns(str)`.
4.   Goto Step 1.
5.   Exit.

Do not modify the main function.

The following is an example of the expected output of the program. Note that
the program is started only once. Test your code with more strings.

```
a b c
abc
RISC-V: The Free and Open RISC Instruction Set Architecture
RISC-V:TheFreeandOpenRISCInstructionSetArchitecture

```

## Deliverables

Submit a report in PDF format. The report should have the following.

*   Code in `print_ns()` function, with concise comments. Clearly mark each of 
    the five steps in the function.

*   A screenshot of "Run I/O" tab showing that the program works and can
    process multiple lines from the console. Select some input lines yourself.

*   A screenshot of Data Segment window showing the stack after registers are
    saved on the stack, i.e., after Step 1 in `print_ns()`. Find the saved
    return address on the stack and write down its value and address in text. 

