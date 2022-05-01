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
    sig = RISCVSignals(init_pc)

    adder1 = Adder(sig.PC4, sig.PC, sig.Const4)
    adder2 = Adder(sig.BranchTarget, sig.PC, sig.immediate)
    
    mux1 = Mux2(sig.ALUInput2, sig.ReadData2, sig.immediate, sig.ALUSrc)
    mux2 = Mux2(sig.WriteData, sig.ALUResult, sig.MemReadData, sig.MemtoReg)
    mux3 = Mux2(sig.NextPC, sig.PC4, sig.BranchTarget, sig.PCSrc)
    
    regPC = RegisterE(sig.PC, sig.NextPC, sig.signal1, clock, reset)
    pcSrc = And2(sig.PCSrc, sig.Branch, sig.Zero)
    immGen = ImmGen(sig.immediate, sig.instruction)
    
    alu1 = ALU(sig.ALUResult, sig.Zero, sig.ReadData1, sig.ALUInput2, sig.ALUOperation)
    aluControl = ALUControl(sig.ALUOp, sig.instr30, sig.funct3, sig.ALUOperation)
    mainControl = MainControl(sig.opcode, sig.ALUOp, sig.ALUSrc, sig.Branch, sig.MemRead, sig.MemWrite, sig.MemtoReg, sig.RegWrite)
    
    regFile = RegisterFile(sig.ReadData1, sig.ReadData2, sig.rs1, sig.rs2, sig.rd, sig.WriteData, sig.RegWrite, rf, clock, posedge = True)
    
    insMemory = Rom(sig.instruction, sig.PC, imem)
    dataMemory = Ram(sig.MemReadData, sig.ReadData2, sig.ALUResult, sig.MemRead, sig.MemWrite, dmem, clock)

    @always_comb
    def set_done():
        env.done.next = sig.PC > max_pc  

    @always(clock.negedge)
    def print_logic():
        if env.print_enable:
            sig.print(env.cycle_number, env.print_option)

    return instances()

if __name__ == "__main__" :
    print("Error: Please start the simulation with rvsim.py")
    exit(1)