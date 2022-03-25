# CSE 3666 - Homework 4, Question 5

.globl main
.data
	
str: .space 100

.text

main:   
	la	  a0, str
    li	  a1, -1
	jal	  ra, uint2decstr

    la    a0, str
    addi  a7, x0, 4
    ecall

exit:
    addi  a7, x0, 10      
    ecall

# char* uint2decstr(char *s, unsigned int v) 
# the function converts unsigned value to decimal string
# Here are some examples:
# 0:    "0"
# 2022: "2022"
# -1:   "4294967295"

# char* uint2decstr(char *s, unsigned int v)
# {
#     unsigned int r;
#     if (v >= 10) {
#         s = uint2decstr(s, v / 10);
#     }

#     r = v % 10; // remainder
#     s[0] = '0' + r;
#     s[1] = 0;
#     return &s[1]; // return the address of s[1]
# }

uint2decstr:
    addi  sp, sp, -8         # allocate 8 bytes on the stack
    sw    ra, 4(sp)          # preserve ra by putting it on the stack
    sw    a1, 0(sp)          # preserve the string address by putting it on the stack
    addi  t0, x0, 10         # store the value of 10 in t0
    bltu  a1, t0, write       # if v < 10, the base case is reached, so jump to write
    divu  a1, a1, t0         # divide v by 10 and store the result in a1
    jal   ra, uint2decstr    # reinvoke uint2decstr

write:
    lw    ra, 4(sp)          # restore ra from the stack
    lw    a1, 0(sp)          # load s0 with the address of the string
    addi  t0, x0, 10         # store the value of 10 in t0
    remu  t1, a1, t0         # take the remainder of v / 10
    addi  t0, t1, '0'        # convert the remainder to a character
    sb    t0, 0(a0)          # store the character on the stack
    addi  a0, a0, 1          # increment the address of the string
    addi  sp, sp, 8          # restore the stack pointer
    jr    ra                 # return to the caller
