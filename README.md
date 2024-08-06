# Brain-Computer Interface ironbci
all updates here https://pieeg.com/  

[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=DIY%20Brain-Computer%20%20interface%20ironbci%20&url=https://github.com/Ildaron/ironbci&hashtags=EEG,biosignals,python,opensource)  [![Hardware demonstrations](https://img.shields.io/badge/Licence-FREE-blue)](https://github.com/Ildaron/ironbci/blob/master/license.txt)        
                            
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/general_view.jpg "general view")​

It is not medical device!!! And can not be used for any medical purposes!!!  
####  ADS1299 and STM32F407VE 
-  [How it Works](https://github.com/Ildaron/ironbci/blob/master/README.md#1-how-it-works)  
-  [Device pinout](https://github.com/Ildaron/ironbci#2--general-pin-information-about-ads1299-signals)   
-  [Configuration of control registers](https://github.com/Ildaron/ironbci#3-configuration-of-control-registers)     
-  [Description of code ADS_1299.c](https://github.com/Ildaron/ironbci#4-description-of-code-ads_1299c)    
-  [STM32 programming](https://github.com/Ildaron/ironbci#5-stm32-programming)  
-  [Hardware and Signal processing demonstrations](https://github.com/Ildaron/ironbci#6-hardware-and-signal-processing-demonstrations)     
-  [Citation](https://github.com/Ildaron/ironbci/blob/master/README.md#7-citation)   
-  [Contacts](https://github.com/Ildaron/ironbci/blob/master/README.md#8-contacts)     

[GNU license](https://github.com/Ildaron/ironbci/blob/master/license.txt)
#### How it Works  
[Gerbers files](https://github.com/Ildaron/ironbci/tree/master/gerber_files) for PCB boards.  
[Hex file](https://github.com/Ildaron/ironbci/blob/master/ironbci.hex) can be uploaded to STM32F407VE by ST-LINK V2 RST  
 Connection:  
                        - RST      
                        - TCK    
                        - gnd   
                        - TMS    
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/stl1.bmp "stm32")


####  2.  General pin information about ADS1299 signals
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/stm1.bmp "stm32")​  
SPI2 for communicate with ADS1299    
UAART4 for send data by HC-12  
2.1.DRDY output -  high when conversion starts    
2.2  Two ways to read data:      
      - RDATA - continuous read command;      
      - SDATA - on request.  
2.3. The amount of input data - 24 * 8 = 192 bits + 24 status bits, a total - 216 bits  

#### 3. Configuration of control registers  
Three bytes of register configuration  
0b11010110    
0b11010100
0b11100000

#### 4. Description of code ADS_1299.c  
Data transfer - "s", ends - "p"  
Serial with baud rate - 115200.
 
Hardware demonstrations  
[![Hardware demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/hardware_ironbci.bmp)](https://youtu.be/kfbvYXvBCJk)    
Signal processing by brainflov via timeflux (https://timeflux.io/)    
[![Software demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/software.bmp)](https://youtu.be/y1O7FNJLeh4)      


#### 6. Citation  
Rakhmatulin, I., Parfenov, A., Traylor, Z. et al. Low-cost brain computer interface for everyday use. Exp Brain Res (2021). https://doi.org/10.1007/s00221-021-06231-4

#### 7. Contacts   
https://pieeg.com/ 
