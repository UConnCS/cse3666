from myhdl import block, always_comb, concat, instances
from alu1 import ALU1bit

# ALU1bit(a, b, carryin, binvert, operation, result, carryout):

@block
def ALU4bits(a, b, alu_operation, result, zero):

    """ 4-bit ALU

    """
    # create internal signals
    # note that these signals are internl to this 4-bit ALU, 
    # but not internal to submodules like 1-bit ALUs 

    # bnegate and operation are shadow signals, not regular signals
    # They follow the bits in alu_operation 
    # If alu_operation changes, they change 
    # So we do not need to set value for bnegate and operation manually
    # If we use bit slicing, like alu_operation[2], we only get current value 
    # of bit 2 in alu_operation. It is not a signal.
    # We could create regular Signal objects. Then we have to copy 
    # values from alu_operation with a combinational function
    bnegate = alu_operation(2)      # bit 2    
    # like any range in Python, upper bound is open and lower is closed. 
    operation = alu_operation(2,0)  # bits 1 and 0

    # cout is a list of Signals
    # Each element on the list, like cout[0] is an object of Signal class 
    # These are connected to the output of 1-bit ALUs
    cout = [Signal(bool(0)) for _ in range(4)]

    # Create signals connected the output of 1-bit ALUs
    # These signals are driven by 1-bit ALUs
    # We will have to copy them to result
    # We cannot use shadow signals from result because shadow
    # signals are read only
    result_bits = [Signal(bool(0)) for _ in range(4)]

    # TODO
    # instantiat four 1-bit ALUs
    # 
    # Use shadow signals to connnect individual bits in 
    # signals `a` and `b` to 1-bit ALUs. 
    # a(0) is a shadow signal that follows bit 0 in a
    # a[0] is bit 0's current value and it is not a Signal
    alu1_0 = ALU1bit(a(0), b(0), bnegate, bnegate, operation, result_bits[0], cout[0]);
    alu1_1 = ALU1bit(a(1), b(1), bnegate, bnegate, operation, result_bits[1], cout[1]);
    alu1_2 = ALU1bit(a(2), b(2), bnegate, bnegate, operation, result_bits[2], cout[2]);
    alu1_3 = ALU1bit(a(3), b(3), bnegate, bnegate, operation, result_bits[3], cout[3]);

    @always_comb
    def comb_output():
        # TODO
        # Generate output signals `result` and `zero`
        # from the output of 1-bit ALUs
        # Recall that every element in result_bits is an individual object
        # of Signal class
        #
        # To set individual bits in `result`, we can do
        #   result.next[0] = ... 
        # To generate zero, we use Python operators `or` and `not`
        

    # return all logic  
    return instances()

if __name__ == "__main__":
    from myhdl import intbv, delay, instance, Signal, StopSimulation, bin
    import argparse

    # testbench itself is a block
    @block
    def test_comb(args):

        # create signals
        # use intbv for multiple bits
        a = Signal(intbv(0)[4:])
        b = Signal(intbv(0)[4:])
        result = Signal(intbv(0)[4:0])
        alu_operation = Signal(intbv(0)[4:])
        zero = Signal(bool(0))

        # instantiating a block
        alu = ALU4bits(a, b, alu_operation, result, zero)

        @instance
        def stimulus():
            print("ALU_opration a     b    | result zero")
            for op in args.operation_list:
                alu_operation.next = op
                for i in range(16):
                    bi = intbv(i)
                    a.next = args.a
                    b.next = bi[4:]
                    yield delay(10)
                    print("{:11}  {}  {} | {}   {}".format(
                        bin(op, 4), bin(a, 4), bin(b, 4),
                        bin(result, 4), int(zero)))

            # stop simulation
            raise StopSimulation()

        return alu, stimulus

    operation_list = [-1, 0, 1, 2, 6]
    parser = argparse.ArgumentParser(description='4-bit ALU')
    parser.add_argument('op', nargs='?', type=int, default=-1, choices=operation_list, 
            help='alu operation in decimal. -1 for all operations')

    parser.add_argument('-a', type=int, default=0b1010, help='input a in decimal')
    parser.add_argument('--trace', action='store_true', help='generate trace file')

    args = parser.parse_args()
    # print(args)

    if args.op < 0:
        args.operation_list = operation_list[1:]
    else:
        args.operation_list = [args.op]

    tb = test_comb(args)
    tb.config_sim(trace=args.trace)
    tb.run_sim()

