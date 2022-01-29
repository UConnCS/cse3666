# Printing bits

The deadline to submit the report in HuskyCT is Wed, 2/2/2022.

We strongly encourage students to complete the lab in the lab session.

*If you work on computers in the learning center or a UConn virtual desktop, 
save your files on P drive. Otherwise, you may lose your files.*

## Learning Objectives

* Logical and bit-wise operations 

* Binary representation of signed integers

* ASCII characters

## Description

In this lab, we write a program in RISC-V assembly language that prints
32 bits in a register.

The program reads a signed integer from the console and prints the 32 bits in
the integer, twice. 

Skeleton code in `lab2.s` already has the following steps. Study the code. 

*   Read an integer using a system call and save it in `s1`. 

*   Use a system call to print `s1` in binary. 

Implement the following steps with RISC-V instructions.

*   Use system call to print a newline character (ASCII value 10). Find the system call
    number in the document.

    We can use `'\n'` as the immediate in instructions. 

*   Write a loop to print the bits in `s1`, from bit 31 to bit 0. The printed bits should be 
    the same as the ones printed by the system call.

    Think aobut the strategy/algorithm first. One method is provided in
    pseudocode at the bottom of this page.

*   Use system call to print a newline character.   

Here are some example inputs/outputs of the program.

```
-1
11111111111111111111111111111111
11111111111111111111111111111111

3666
00000000000000000000111001010010
00000000000000000000111001010010

20220201
00000001001101001000100100101001
00000001001101001000100100101001

-3666
11111111111111111111000110101110
11111111111111111111000110101110

```

## Deliverables

Submit a report in PDF format. The report has two parts.

*   Code with good, concise comments. In this lab, there is no need to include
    instructions provided in the skeleton code.

*   Describe the results of the code. Does the code work or only work for some
    inputs? Include a screenshot of "Run I/O" tab showing a few runs of the code.

## Pseudocode 

Here is one method.

```
1.  mask = 0x80000000
2.  REPEAT the following steps 32 times:
2.1.    b31 = mask & s1
2.2.    IF b31 is 0
2.3.        print '0'
2.4.    ELSE
2.5.        print '1'
2.6.    s1 = s1 << 1
```

The above code changes `s1`. If we want to keep the value in `s1`, we can copy
it to antoher register. 

We can also use mask to control the loop. We shift the mask to right in
each iteration. The condition would be:

    WHILE mask != 0

Which instruction should we use to shift the mask?
