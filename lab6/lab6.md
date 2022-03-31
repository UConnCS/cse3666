# Four-bit ALU

*Due Date: Submit the lab report in HuskyCT by the end of Friday, 3/25/2022*

As always, try to complete the assignment in the lab session.

*If you work on computers in the learning center or on a UConn virtual desktop, 
save your files on P drive. Otherwise, you may lose your files.*

## Learning Objectives

*   Implement combinational circuit from logic diagram.

*   Implement combinational circuit in MyHDL, using existing modules.

*   Use more features in MyHDL in design, for example, multi-bits signals and
    shadow signals.


## Description

In this lab, we implement a 4-bit ALU, using the 1-bit ALU we built in the
previous lab. A easy way for Python to find the 1-bit ALU module is to copy
`alu1.py` to the working directory for this lab. Students who have not finished
the privous lab can download `alu1.py` provided in this lab. Note that the
provided 1-bit ALU does not meet all requirements in the privous lab.

We have discussed the interface of ALU in lecture, which is also shown in the
following figure. The ALU performs the operation specified by `alu_operation`
on two inputs `a` and `b` and generates `Result`. Output signal `zero` is 1 if
and only if all bits in `Result` are 0.

![ALU Inteface](./alu_interface.png)

The internal circuit diagram of the 4-bit ALU is similar to a 32-bit ALU. See
`alu32.svg` directly if the figure does not shown below. Note that `bnegate`
and `operation` signals in the diagram are bits from `alu_operation`.

![alu32 diagram](./alu32.svg)

### Steps

The skeleton code is in `alu4.py`.  The implementation is in block `ALU4bits`.
**Read the code and comments provided in the skeleton code.**

The internal signals needed in the implementation of ALU4bits are already
created in the skeleton code. The steps we take to complete the design are as
follows. Budget 10 minutes for each step.
 
*   Step 1. Instantiate 1-bit ALUs. Connect correct signals to the input and
    output ports of 1-bit ALUs. The output of these ALUs are bits in in `cout`
    and `result_bits`.

    The skeleton code already instantiates the first 1-bit ALU, ALU0. Follow
    the example and instantiate other three 1-bit ALUs.  Another example of
    instantiating a block is in function `test_comb()`, which instantiates an
    ALU4bits. 

*   Step 2. Generat output signals `result` and `zero` from `result_bits`. The
    logic should be in `comb_output()` function. See the comments in the
    skeleton code.

### Running the program 

The program `alu4.py` accepts a few arguments from the command line. 

*   The first positional argument is the operation code. The default value is
    -1, which goes through all operations: 0, 1, 2, and 6.

*   `-a <number>`: specify the value at input `a`. The default value is 10. 

    We cannot specify input `b` from the command line. The program sends all
    bit patterns, from 0b0000 to 0b1111, to input `b` of the ALU. 

*   `-h`: display the help message.

Here are some examples of running `alu4.py`.

    # use default setting. op = [0, 1, 2, 6]. a = 10. 
    python alu4.py

    # test only addition. op = [2]. a = 10.
    python alu4.py 2 

    # test subtraction. op = [6]. a = 15.
    python alu4.py 6 -a 15 

The output of the program without any arguments is in `output.txt`. Test your
program with different input.

## Deliverables

Submit a PDF report. The report should include the following:

*   Your work for each Step.

*   Screen shots of output of the program for the following settings. For each
    setting, randomly pick a line in the output and explain the bits on that
    line. In Settings 3 and 4, find the number of rows where the 4-bit output
    is correct if a) all (4-bit) numbers are signed, and b) all numbers are
    unsigned. 

        #Setting 1 
        python alu4.py 0 -a 3

        #Setting 2
        python alu4.py 1 -a 9 

        #Setting 3 
        python alu4.py 2 -a 11

        #Setting 4
        python alu4.py 6 -a 15

## Misc

Here is an example of interpreting bits. The last line in `output.txt` is:

    0110         1010  1111 | 1011   0

The ALU performed subtraction. 

If all bits are signed, we have -6 - (-1) = -5. The result is correct.

If all bits are unsigned, we have 10 - 15 = 11. The result is not correct. 
