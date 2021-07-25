# ironbci
Brain-Computer Interface, ADS1299

This code is for STM32F407VE microcontroller to receive data from ADS1299 over 8 channels. 
=====================

Data processing due BrainFlow https://brainflow.readthedocs.io/en/stable/  board_id: 17

File   
1.ADS_1299.c   - code for Atollic TrueSTUDIO for STM32 9.3.0  
1.ADS_1299.ioc - STM32CubeMX


#### 1.  General pin information about ADS1299 signals  
1.1. Reset - to the low position - reset all settings
1.2.DRDY output - goes high when conversion starts and low when data is ready  
1.3  Two ways to read data:  
      - RDATA C1 - continuous read command  
      - RDATA data read which requires a command to load the input offset  
1.4. The amount of input data is 24 bits * 8 = 192 bits, and 24 status bits, in total we get 216 bits  
1.5 To receive data from the device after executing the RDATAC command, the START pin must be high, or a START command has been issued.  

#### 2. Configuration of control registers  
2.1 Writing to the register  
Three bytes of register configuration  
0b11010110    
0b11010100
0b11100000

First command byte: 010r rrrr, where r rrrr is the starting register address.
Second byte of the command: 000n nnnn, where n nnnn is the number of registers to be written - 1.
2.2 Reading from a register, similarly but the first four bits from a byte of the following format
BYTE 1 = 0010 0000 

2.3 Baud rate
Assuming the CLK is 2.048 MHz, then tSDECODE (4 tCLK) is 1.96 μs. When SCLK is 16 MHz, one byte can be transmitted in 500 ns. This byte transfer time does not conform to the tSDECODE specification; therefore a delay must be inserted so that the end of the second byte arrives 1.46 µs later.  

#### 3.Description of code ADS_1299.c  
Data transfer starts after receiving by the microcontroller - "s", ends after receiving - "s"  
Data is transmitted via Serial with baud rate - 115200  

[![Hardware demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/hardware_ironbci.bmp)](https://youtu.be/kfbvYXvBCJk)

[![Sowtware demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/software.bmp)](https://youtu.be/y1O7FNJLeh4)
