# Copyright 2021-2022 Zhijie Shi. All rights reserved. See LICENSE.txt.
from myhdl import * 

from hardware.register import RegisterE
from hardware.memory import Ram, Rom
from hardware.mux import Mux2
from hardware.gates import And2
from hardware.alu import ALU
from hardware.adder import Adder
from hardware.registerfile import RegisterFile

from sc_signals import RISCVSignals
from immgen import ImmGen 
from maincontrol import MainControl
from alucontrol import ALUControl

@block
def RISCVCore(imem, dmem, rf, clock, reset, env):
    """
    All signals are input

    imem:   instruction memory. A dictionary
    dmem:   data memory. A dictionary
    rf:     register file. A list of 32 integers
    clock:  clock 
    reset:  reset
    env:    additonal info, mainly for controlling print

    env.done:   asserted when simulation is done
    """

    max_pc = max(imem.keys()) 
    init_pc = min(imem.keys()) 

    # signals
    sig = RISCVSignals(init_pc)

    # TODO
    # instantiate hardware modules 
    # check the diagram, make sure nothing is missing
    # and signals are connected correctly
    # 

    # for example, PC register is instantiated with the following line
    regPC = RegisterE(sig.PC, sig.NextPC, sig.signal1, clock, reset)

    # instantiate the ALU
    alu = ALU(sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)

    # instantiate the Adder
    adder = Adder(sig.signal1, sig.signal2, sig.signal3, clock, reset)

    # instantiate the mux
    mux = Mux2(sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)

    # instantiate the register file
    regfile = RegisterFile(rf, sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)

    # instantiate the main control
    mainctrl = MainControl(sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)

    # instantiate the ALU control
    aluctrl = ALUControl(sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)

    # instantiate the immediate generator
    immgen = ImmGen(sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)

    # instantiate the RAM
    ram = Ram(dmem, sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)

    # instantiate the ROM
    rom = Rom(imem, sig.signal1, sig.signal2, sig.signal3, sig.signal4, clock, reset)


    ##### No need to change the following logics
    @always_comb
    def set_done():
        env.done.next = sig.PC > max_pc  

    # print at the negative edge. for simulation only 
    @always(clock.negedge)
    def print_logic():
        if env.print_enable:
            sig.print(env.cycle_number, env.print_option)

    return instances()

if __name__ == "__main__" :
    print("Error: Please start the simulation with rvsim.py")
    exit(1)
