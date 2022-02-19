# CSE 3666 Lab 4: Remove spaces
.data

# allocating space for str
str: .space  128

.globl  main
.text

main:   
        # read a string into str
        # use pseudoinstruction la to load address into register
        la    a0, str

main_loop:
        # read a string
        addi  a1, x0, 100
        addi  a7, x0, 8
        ecall

        # check if the line is empty (has only the newline) 
        lb    t0, 0(a0)
        addi  t1, x0, '\n'
        beq   t0, t1, exit

        # a0 is already set. does not change during ecall
        jal	  ra, print_ns

        # the address of str should be in a0 
        beq   x0, x0, main_loop
 
exit:   addi  a7, x0, 10
        ecall

# DO NOT change code above this line

# function 
print_ns:
        # store the result pointer in a1
        add  a1, sp, x0

        # allocate 136 bytes to the stack
        # - 128 for the string
        # - 4 for the return address
        # - 4 for the original string
        addi  sp, sp, -136

        sw    ra, 4(sp)      # store current return address on the stack
        sw    a0, 0(sp)      # preserve original string so we can return it later
        jal   remove_spaces # invoke remove_spaces

        # use system call 4 to print the result to stdout
        addi  a0, a1, 0
        addi  a7, x0, 4
        ecall

        # restore state so we can return back to the main loop
        lw    ra, 4(sp)
        lw    a0, 0(sp)
        addi  sp, sp, 136
	    jr    ra

# function remove_spaces
remove_spaces:
        # compute address of str[i]:
        # given base address of str[0] stored in a0,
        # we can add i + a0 (since chars are 1-byte)
        # to get the resultant address of str[i]
        add     t2, t0, a0

        # load char from target address
        # str[0] + i, into register t3.
        lb      t3, 0(t2)

        addi    t0, t0, 1             # increment loop counter i
        bne     t3, t5, write         # if str[i] != 32 (SPACE), enter routine to save char
        beq     t3, x0, loop_exit     # if str[i] == 0  (NUL), enter exit routine
        beq     x0, x0, remove_spaces # continue the loop if this point is reached

write:
        # compute address of res[j]:
        # given base address of res[0] stored in a1,
        # we can add j + t1 (since chars are 1-byte)
        # to get resultant ddress of str[j]
    	add     t4, t1, a1

        # load char from target address
        # res[0] + j, into register t3
        sb      t3, 0(t4)

        addi    t1, t1, 1             # increment loop counter j
        bne     t3, x0, remove_spaces # if char != 0 (NUL), re-enter loop
        beq     t3, x0, loop_exit     # if char == 0 (NUL), exit program

loop_exit:
        jr      ra # return to the print_ns context