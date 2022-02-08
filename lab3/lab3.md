# Lab 3: Removing spaces

*Due Date: By the end of Wed, 2/9/2022*

Read the assignment carefully. 

Try your best to complete the lab assignment during the lab session.

*If you work on computers in the learning center or a UConn virtual desktop, 
save your files on P drive. Otherwise, you may lose your files.*

## Learning Objectives

* Access data in memory

* Compute with strings

## Description

In this lab, we write a program with RISC-V assembly language that performs
the following tasks:

1.  Read a string `str` from the console.
2.  Remove the spaces (ASCII value 32) in `str` and save the result in string `res`. 
3.  Print `res`.

Both strings are ASCII strings that end with a null character (NUL).

Skeleton code is provided in `lab3.s`. Step 1 is already done. Study the code.
Pseudocode for Step 2 is provided below. Step 3 is done by a system call.

**Constraints in your code:** Use only argument registers (like `a0` and `a1`)
and temporary registers (like `t0` and `t1`). This will help you in the next
lab. There is no need to use pseudo instruction `la`. Addresses are already in
`a0` and `a1`.

### Pseudocode

```
i = 0
j = 0
do
    c = str[i]
    if c != 32
       res[j] = c
       j += 1
    i += 1
while c != 0
```

The following are some examples of expected output of the program. The lines
that have spaces are input. Please test your code with more strings. 

```
a b c
abc

RISC-V: The Free and Open RISC Instruction Set Architecture
RISC-V:TheFreeandOpenRISCInstructionSetArchitecture
```

## Deliverables

Submit a report in PDF format. The report has two parts.

*   Code with good, concise comments. Do not include instructions provided in
    the skeleton code.

*   Describe the results of the code. Does the code work or only work for some
    inputs? Choose some strings yourself and show the program works correctly.
    Include a screenshot of "Run I/O" tab showing a few runs of the code. Include
    some strings you have selected. 
    
## Questions

Find out the answers to the following quetions. Discuss with other students.
You do not need to include the answers in the report.

*   What is the address of str? What is the address of res? What is their
    difference?
*   What is the character before the null charachter (NUL) in str? 
*   If you type nothing and just press enter, is str empty?  
*   Is the null character copied in the loop?
*   Is variable j the length of res after the loop terminates? 
*   Did you make any mistakes? If so, what mistakes?
