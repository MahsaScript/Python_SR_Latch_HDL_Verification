# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:07:07 2021

@author: mahsa
"""
#  Write and verify an HDL structural description of the machine having the circuit diagram
# (schematic) shown in Fig. 5.5. 

import random
from myhdl import *
from BinPy import *

randrange = random.randrange
# Connector to connect output of second NAND gate with input of first NAND gate
con1 = Connector()

# Connector to connect output of first NAND gate with input of second NAND gate
con2 = Connector()

t_state = enum('Set', 'Reset', 'NoChange')
@block
def S_R_Latch_NAND_Logic(t_state):
    @always(delay(1))
    def behave():
        if t_state =='Set':
            En=1
            S =1  #Set State
            R =0 
            SNext =NAND(S, En)
            RNext =NAND(S, En)
            
            NAND1 = NAND(con1, SNext)  # First NOR gate
            NAND1.setOutput(con2)  # Set output for NOR gate
            
            NAND2 = NAND(con2, RNext)  # Second NOR gate
            NAND2.setOutput(con1)  # Set output for NOR gate
            
            NAND1.setInput(1, SNext)  # S=0  En=1
            NAND2.setInput(1, RNext)  # Set state  
            print('Set state      En:1 S:1 R:0 ->','\t','Q: ', NAND2.output())
        if t_state =='Reset':
            En=1
            S =0  
            R =1 #Reset State
            SNext =NAND(S, En)
            RNext =NAND(S, En)
            
            NAND1 = NAND(con1, SNext)  # First NOR gate
            NAND1.setOutput(con2)  # Set output for NOR gate
            
            NAND2 = NAND(con2, RNext)  # Second NOR gate
            NAND2.setOutput(con1)  # Set output for NOR gate
            
            NAND1.setInput(1, SNext)  # S=0  En=1
            NAND2.setInput(1, RNext)  # Set state  
            print('Reset state    En:1 S:0 R:1 ->','\t','Q: ', NAND2.output())
        
        if t_state =='NoChange':
            En=0 #NoChange State
            S =0  
            R =1 
            SNext =NAND(S, En)
            RNext =NAND(S, En)
            
            NAND1 = NAND(con1, SNext)  # First NOR gate
            NAND1.setOutput(con2)  # Set output for NOR gate
            
            NAND2 = NAND(con2, RNext)  # Second NOR gate
            NAND2.setOutput(con1)  # Set output for NOR gate
            
            NAND1.setInput(1, SNext)  # S=0  En=1
            NAND2.setInput(1, RNext)  # Set state  
            print('NoChange state En:0 S:0 R:1 ->','\t','Q: ', NAND2.output())     
    return behave

inst1 = S_R_Latch_NAND_Logic('Set')
inst2 = S_R_Latch_NAND_Logic('Reset')
inst3 = S_R_Latch_NAND_Logic('NoChange')
inst1.run_sim(1)
inst1.quit_sim()
inst2.run_sim(1)
inst2.quit_sim()
inst3.run_sim(1)
inst3.quit_sim()
