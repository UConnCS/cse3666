# Multiplier

*Due Date: Submit a PDF report in HuskyCT by the end of Friday, 4/1/2022*

As always, try to complete the assignment in the lab session.

*If you work on computers in the learning center or on a UConn virtual desktop, 
save your files on P drive. Otherwise, you may lose your files.*

## Learning Objectives

* Implement sequential circuit in MyHDL 

* Build circuit from existing modules

## Description

In this lab, we implement the multiplier we have discussed in lecture. The
multiplicand and multipler are of 8 bits (although we can easily change
that). The multiplicand and the product are stored in 16-bit registers.
The adder adds two 16-bit numbers. 

### Registers
The registers we use in this lab are described below.  All registers are
triggered by positive clock edges.

`RegisterE` has an enable signal. The register is updated with `din` if the
enable input is 1.

`RegisterShiftLeft` is a shift left register. `load` and `load_data` allow us
to set a specific value in the register. When `load` is 1, the register is set
to `load_data`. If `load` is 0 and `shift_en` is 1, the regiser shifts in bits
the register to left by 1. The bit shifted in is always 0. If both `load` and
`shift_en` are 0, the regisrer is not changed. 

`RegisterShiftRight` works simialrly to `RegisterShiftLeft`. The difference is
that the register shifts bits to right.

The registers do not care about the number of bits in the input and output
signals much. The number of bits in signals is specified when a signal is
created. 

### Skeleton code

The skeleton code is in `mul.py`.  The implementation of the multiplier is in
block `Mul2x`.  `2x` indicates the width of the adder is doubled. 

The implementation needs three registers to hold values for `p`, `x`, and `y`.
`p` is the prodcut, `x` is the multiplicand, and `y` is the multiplier. Often,
when we say `p` register, we mean the register that stores/drives signal `p`.
Let us call the instance of registers `reg_p`, `reg_x`, and `reg_y`, for `p`,
`x`, and `y`, respectively.

### Operation of the multiplier  

The multiplier has two ports `load` and `done`, in addition to data, clock, and
reset signals.

When `load` is asserted, the multiplier loads the inputs `x_init` and `y_init`
into registers `x` and `y`, respectively, and clears the product.

When `load` is deasserted, the multiplier starts to work. When the
multiplication is completed (all bits in `y` have been checked), `done` is
asserted. After that, register `p` is not updated and the final product is
saved in the register. 

We can keep the `shift-en` signal to 1 registers `x` and `y`. Therefore, the
bits in `x` and `y` are always shfited, even if the multiplication is done.
Always shifting `reg_x` and `reg_y` does not affect the correctness of the
result in `p`.

See `output.txt` and `output100.txt` for detailed signal values. 

### Tasks 

The internal signals needed in the implementation are already created in the
skeleton code. 

The control module has been implemented. `done` is generated in the module.
You may use `done` signal if needed. However, **DO NOT** use the counter
register directly as the implementation may change. 

The tasks to be completed in this lab are as follows. Budget 10 minutes for
coding.

*   Instantiate registers for `p`, `x`, and `y`. Note that although `p` is the
    output of the multiplier, it can be connected to the output of a register
    directly (i.e., driven directly by the register).  `x` and `y` are internal
    signals in the multiplier. 

    Let us call the instances `reg_p`, `reg_x`, and `reg_y`, for `p`, `x`, and
    `y`, respectively.

*   Generat input signals to `reg_p` in `comb_regs`. `p_en` is the only
    signal that needs to be set.
  
### Running the program
The program `mul.py` accepts a few arguments from the command line. 

* `-h`: display the help message.

* `<list of numbers>`: specify a list of numbers. The multipler will multiply
  adjacent numbers. The default is `255 255`.

   ```
   # 255 * 255
   py mul.py 

   # 36 * 66
   py mul.py 36 66

   # 100 * 200
   # 200 * 255
   py mul.py 100 200 255
   ```

* `--trace`: generate a trace file, which can be viewed by waveform viewer like GTKWave.

The output of the program without any arguments is in `output.txt`.  When the
number list is "100 200 255", the output is in `output100.txt`. 

## Deliverables

Submit a PDF report. The report should include the following:

*   Your work for each Step.

*   Screen shots of output of the program for the following command.

        python mul.py 17 36 202

## Extra

*   We can save signal traces with `--trace` option and examine the signal
    waves with [GTKWave](https://github.com/gtkwave/gtkwave).

*   Set `x_en` and `y_en` signals to "not done" in `comb_regs`. When the
    multiplication is done, `x` and `y` are no longer shifted. 

