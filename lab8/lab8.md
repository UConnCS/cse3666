# A RISC-V Simulator

*Due Date: Submit `sc_core.py` in HuskyCT by the end of Friday, 4/22/2022*

**This lab is worth 200 points**

*If you work on computers in the learning center or on a UConn virtual desktop, 
save your files on P drive. Otherwise, you may lose your files.*

## Learning Objectives

* Implement a single-cycle RISC-V processor in MyHDL 

* Build a processor from existing modules

## Description

In this lab, we complete the design of a single-cycle RISC-V processor. 

### Instructions supported by the processor

The processor supports the subset of instructons we have studied.

```
ADD, SUB, AND, OR, LW, SW, BEQ
```

### Code

Implementing a processor requires a lot of work. we have done the heavy
lifting. The remaining work is limited to one file, or a few files if 
you would like to improve the processor.

The files provided to you are in a single ZIP file. Descriptions of the files
in the package are in `README.md`. Read it carefully.

Note that the software is copyrighted to limit its distribution.  A lot of
efforts have been put in the design of the assignment so students can learn
from the code provided and also have opportunities to explore themselves.
Please limit the use of the code in this course. See `LICENSE.txt` in the
downloaded files for detail. 

### Tasks 

The main task is to complete the design of a single-cycle RISC-V core.  Since
all supporting modules are already provided, the main task is to follow Figure
4.21 in the textbook and put everything together. 

We will mainly work on `sc_core.py`. Read the code provided in `sc_core.py`
carefully.  Many packages are imported at the beginning of the file. From the
import statements, we can find out where to find the file for a particular
module. 

Study the signals in `sc_signals.py` and locate the signals in the diagram.

Starting from PC (already in the file), create the modules in the diagram one 
by one.  

* Find a module that are connected to the modules that are already created. For
  example, PC is already created, the next one would be the instruction memory.

* Find the interface of the module by reading the documentations and studying its
  source code.

* Instantiate the module with proper signals connected to it.

After the diagram is implemented in Python code, test the simulator. See
`README.md` for more instructions. Although some expected outputs are provided,
some programs generate different output when argument registers like `a0` and
`a1` are changed.  Run those programs with different initial values in
registers and explain the results from the simulator.

## Deliverables

Submit revised `sc_core.py` in HuskyCT. Do not change the filename.

