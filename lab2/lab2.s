# CSE 3666 Lab 2

.globl main
.text

main:          
    # use system call 5 to read integer
    addi    a7, x0, 5
    ecall
    addi    s1, a0, 0 # int in s1

    # use system call 35 to print a0 in binary
    # a0 has the integer we want to print
    addi    a7, x0, 35
    ecall
    
    # print newline
    addi    a7, x0, 11
    addi    a0, x0, 10
    ecall
    
    addi    a7, x0, 1   # set system call number to 1 (PrintInt)
    addi    t0, t0, 32  # i = 32 (traverse bits backwards)
    addi    t1, t1, 1   # keep 1 in t1 for the mask in loop
    j loop              # enter loop routine
    
    loop:
        addi t0, t0, -1 # decrement loop counter
        
    	# (k & (1 << n)) >> n
    	sll  t2, t1, t0 # t2 = (1 << i)
    	and  t3, s1, t2 # t3 = num & (1 << i)
    	srl  a0, t3, t0 # a0 = (num & (1 << i)) >> i)
    	ecall           # print extracted bit
    	
    	# restart loop, or exit if done
    	bne t0, x0, loop
    	beq t0, x0, loop_exit
    	
    loop_exit:
        # print newline
        addi    a7, x0, 11
        addi    a0, x0, 10
        ecall
	
    # exit program with exit code 0
    addi    a7, x0, 10      
    ecall
