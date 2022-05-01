# Cache simulator in RARS

*Due Date: Submit the lab report in a PDF file in HuskyCT by the end of Friday, 5/29/2022.* 

*If you work on computers in the learning center or on a UConn virtual desktop,
save your files on P drive. Otherwise, you may lose your files.*

## Learning Objectives

* Use the data cache simiulator in RARS.

* Collect and interpret experiment data.

## Description

In this lab, we experiment with data cache simulator in RARS. It helps us
understand how cache works. 

### The program

The RISC-V program we will use in experiment is `lab9-cache.s`. The program
reads words from a word array `warray` for 10240 times, starting from
`warray[0]`. The index is incremented by the stride size after each read. The
default stride size is 1.  If the index is out of range, it is reset to 0. The
pseudocode is as follows.

```
index = 0
for i in range(10240)
    read warray[index]
    index += stride
    if index >= len(warray)
        index = 0
```

### Data cache simulator

RARS has a data cache simulator. The steps to collect data from programs are as follows. 

*   Open data cache simulator, by selecting "Tools/Data cache simulator" from
    the menu. The cache simulator interface is shown in Appendix.
*   Configure the cache. We will experiment with direct mapped cache only. The
    options we need to change are "Number of blocks" and "Cache block size".
*   Press the "Connect to Program" button to connect the simulator to the program
    in RARS.
*   Enable "Runtime log".
*   Run programs in RARS as usual. We should be able to see cache events and
    statistics in the cache simulator. The numbers will stop changing when the
    program stops at a breakpoint or after it terminates.
*   If needed, reset the cache by pressing the "Reset" button at the bottom.
    The cache is reset if the cache configuration is changed.

### Task 1. Default cache configuration

We first experiment with the default cache configuration. The Number of blocks
is 8 and the cache block size is 4 words. The cache size is 128 bytes. 

1.  Find out the number of bits in block offset, cache index, and tag for the
    default cache configuration.  

2.  Assemble the program and set a breakpoint at the instruciton right after LW.
    The instruction is `add x5,x5,x7`, located around 0x00400058.

3.  Start the data simulator. Check the configuration is correct. Enable "Runtime log".
    
4.  Connect data simulator to the program.

5.  Run the program. It should stop at the breakpoint.

6.  Observe the cache event in data cache simulator. The "Runtime log" shows the address and
    fields in the address. Check if all fields are correct. Record the
    information in a table.

7.  Repeat Steps 4 and 5 at least 10 times, and until you see a pattern and can predict 
    the cache hit rate.

8.  Rmove the brekpoint. Run the program until it finishes. Did you predict the correct hit rate?

The following is an example of the table for recording data. 


| Address    | Cache index | tag        | Block offset | Hit/Miss |
| ------     | ------      | ------     | ------       | ------   |
| 0x10010000 | 0           | 0x00200200 | 0            | Miss     |
|            |             |            |              |          |

#### Report 

Include the following in the report.

*   The number of bits in each field and your explanations. 
*   The cache hit rate you predicted and your explanations.
*   The cache hit rate you observed and your explanations.
*   The table.

### Task 2. Block size = 4 words

In this set of experiment, we keep the block size as 4 words. We find out the
hit rates when running the program with three caches configurations, each
having a different number of cache blocks. Since the block size is the same,
the cache size is increased as we increase the number of cache blocks. 

Based on the eariler experiment, predict the hit rate for each cache
configuration. 

Run the program and record the cache hit rates and miss counts from the
simulator. For large numbers of blocks, you may need to make the data cache
simulator window larger by dragging the board of the window. 

| Number of blocks | Cache size | Hit rate | Miss count |
| ------           | ------     | ------   | ------     |
| 8                | 128 bytes  |          |            |
| 16               |            |          |            |
| 32               |            |          |            |
| 64               |            |          |            |
| 128              |            |          |            |

One way to collect the data is to go through the following steps for each cache
configuration.

1.  Set the correct number of cache blocks in the data cache simulator. 
2.  Reset the cache, if it is not already reset.
3.  Make sure the simulator is connected to the program.
4.  Assemble/Reset the program if necessary. 
5.  Run the program and wait until the program terminates.
7.  Record the cache hit rates and miss counsts in the table.

#### Report 

Include the following in the report.

*   The table.
*   The cache hit rates you predicted and your explanations. 
*   Explanations for the cache hit rates you observed.
*   Explanations for the miss counts you observed.
*   Your method for predicting hit rates and miss counts if  
    the size of `warray` is increased, e.g., doubled.

## Task 3. Block size = 8 words

Now we change the block size to 8 words and repeat the experiment in Task 2 and
document your results in the report (as in Task 2).

