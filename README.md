### Brain-Computer Interface [ironbci.com](https://ironbci.com)
                            
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/general_view.jpg "general view")​


####  ADS1299 and STM32F407VE 
1. [How it Works](https://github.com/Ildaron/ironbci/blob/master/README.md#1-how-it-works)  
2. [General pin information about ADS1299 signals](https://github.com/Ildaron/ironbci#2--general-pin-information-about-ads1299-signals)   
3. [Configuration of control registers](https://github.com/Ildaron/ironbci#3-configuration-of-control-registers)     
4. [Description of code ADS_1299.c](https://github.com/Ildaron/ironbci#4-description-of-code-ads_1299c)    
5. [STM32 programming](https://github.com/Ildaron/ironbci#5-stm32-programming)  
6. [Hardware and Signal processing demonstarations](https://github.com/Ildaron/ironbci#6-hardware-and-signal-processing-demonstarations)     
7. [Citation](https://github.com/Ildaron/ironbci/blob/master/README.md#7-citation)   
8. [Contacts](https://github.com/Ildaron/ironbci/blob/master/README.md#8-contacts)     

####  1. How it Works
Here provides all the information you need to develop a brain computer interface. In accordance with the presented license (MIT), using the files and documentation everybody can create a brain-computer interface.

#### Instructions
##### 1 step   
Make PCB boards order in PCB manufacturer, like pcbway.com or seeedstudio.com   
[Gerbers source](https://github.com/Ildaron/ironbci/tree/master/gerber_files)  


#####  2 Step   
By [electrical scheme](https://github.com/Ildaron/ironbci/tree/master/electrical_scheme)   create BOM file for PCB boards   
and make order in PCB manufacturer for Assembly Service  

#####  3 Step 
When boards were received   
Upload [Hex file](https://github.com/Ildaron/ironbci/blob/master/ironbci.hex) to STM32F407VE by ST-LINK V2 RST  


#####  4 Step  
By [brainflow](https://brainflow.readthedocs.io/en/stable/) instructions  start use device.   
 
board_id: 17  

You can re-write code and create a new hex file if will be necessary  
Files   

[1.ADS_1299.c ](https://github.com/Ildaron/ironbci/blob/master/1.ADS_1299.c) - code for Atollic TrueSTUDIO for STM32 F407VE  
[1.ADS_1299.ioc](https://github.com/Ildaron/ironbci/blob/master/ads1299.ioc) - file for STM32CubeMX


####  2.  General pin information about ADS1299 signals
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/stm1.bmp "stm32")​  
SPI2 for communicate with ADS1299  
UAART4 for send data to HC-12
2.1.DRDY output - goes high when conversion starts and low when data is ready  
2.2  Two ways to read data:  
      - RDATA C1 - continuous read command  
      - RDATA data read which requires a command to load the input offset  
2.3. The amount of input data is 24 bits * 8 = 192 bits, and 24 status bits, in total we get 216 bits  
2.4 To receive data from the device after executing the RDATAC command, the START pin must be high, or a START command has been issued.  

#### 3. Configuration of control registers  
2.1 Writing to the register  
Three bytes of register configuration  
0b11010110    
0b11010100
0b11100000

First command byte: 010r rrrr, where r rrrr is the starting register address.  
Second byte of the command: 000n nnnn, where n nnnn is the number of registers to be written - 1.  
Reading from a register, similarly but the first four bits from a byte of the following format
BYTE 1 = 0010 0000   

Baud rate  
Assuming the CLK is 2.048 MHz, then tSDECODE (4 tCLK) is 1.96 μs. When SCLK is 16 MHz, one byte can be transmitted in 500 ns. This byte transfer time does not conform to the tSDECODE specification; therefore a delay must be inserted so that the end of the second byte arrives 1.46 µs later.  

#### 4. Description of code ADS_1299.c  
Data transfer starts after receiving by the microcontroller - "s", ends after receiving - "p"  
Data is transmitted via Serial with baud rate - 115200  

#### 5. STM32 programming
For programm hex file to STM32 can be used - ST-LINK V2 
RST    
TCK    
gnd   
TMS  

![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/stl1.bmp "stm32")


#### 6. Hardware and Signal processing demonstarations  
Hardware demonstarations  
[![Hardware demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/hardware_ironbci.bmp)](https://youtu.be/kfbvYXvBCJk)    
Signal processing by brainflov via timeflux (https://timeflux.io/)    
[![Sowtware demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/software.bmp)](https://youtu.be/y1O7FNJLeh4)      


#### 7. Citation  
Original article coming soon  
#### 8. Contacts  
For any questions write to me by mail - ildar.o2010@yandex.ru   
