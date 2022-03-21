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
    addi  sp, sp, -16        # allocate 16 bytes on the stack
    sw    ra, 12(sp)         # preserve ra by putting it on the stack
    sw    s0, 8(sp)          # load s0 with the address of the string
    mv    s0, a1             # load s0 with the value of v
    addi  a5, x0, 10         # load a5 with the value of 9
    bgeu  a1, a5, recurse    # if v > 10, call recurse

write:
    addi  a1, x0, 10         # load a1 with the value of 10
    remu  s0, s0, a1         # s0 = v % 10
    addi  s0, s0, 48         # s0 = s0 + 48
    sb    s0, 0(a0)          # store the result in the string
    sb    x0, 1(a0)          # store the null terminator
    addi  a0, a0, 1          # increment the address of the string
    lw    ra, 12(sp)         # restore ra
    lw    s0, 8(sp)          # restore s0
    addi  sp, sp, 16         # move stack pointer back
    jr    ra                 # return to caller

recurse:
    addi  a1, x0, 10         # load a1 with the value of 10
    divu  a1, s0, a1         # a1 = v / 10
    auipc t0, 0              # save current address in t0
    jalr  ra, t0, 0xFFFFFFB8 # invoke write 
    jal   write              # jump to write