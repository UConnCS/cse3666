# CSE 3666 Homework 1, Question 6

.globl  main
.text

main:   
        # use system call 5 to read integers
        addi    a7, x0, 5
        ecall
        addi    s1, a0, 0       # a in s1

        # using pseudoinstructions
        li      a7, 5
        ecall
        mv      s2, a0          # b in s2

        # compute GCD(a, b) and print it
        bne s1, s2, loop  # enter the loop
	beq s1, s2, exit  # 

loop:
        ble s1, s2, lte   # if a < b, enter the "lte" routine
        j gt              # if a > b, enter the "gt" routine

gt:
        sub s1, s1, s2    # a = a - b
	    beq s1, s2, exit  # if a == b, exit the loop
        bne s1, s2, loop  # if a != b, restart the loop

lte:
        sub s2, s2, s1    # b = b - a
	    beq s1, s2, exit  # if a == b, exit the loop
        bne s1, s2, loop  # if a != b, restart the loop

exit:   
	    li, a7, 1       # set a7, the service number, to 1 (PrintInt)
        add a0, s1, x0  # load determined GCD into argument register a0
        ecall           # execute the syscall to print to stdout

        # sys call to exit
        addi a7, x0, 10
        ecall
        
