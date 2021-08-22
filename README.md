# Brain-Computer Interface [ironbci.com](https://ironbci.com)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=DIY%20Brain-Computer%20%20interface%20ironbci%20&url=https://github.com/Ildaron/ironbci&hashtags=laser,mosquitoes,python,opensource)  [![Hardware demonstrations](https://img.shields.io/badge/Licence-FREE-blue)](https://github.com/Ildaron/ironbci/blob/master/license.txt)        
                            
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/general_view.jpg "general view")​


####  ADS1299 and STM32F407VE 
-  [How it Works](https://github.com/Ildaron/ironbci/blob/master/README.md#1-how-it-works)  
-  [Device pinout](https://github.com/Ildaron/ironbci#2--general-pin-information-about-ads1299-signals)   
-  [Configuration of control registers](https://github.com/Ildaron/ironbci#3-configuration-of-control-registers)     
-  [Description of code ADS_1299.c](https://github.com/Ildaron/ironbci#4-description-of-code-ads_1299c)    
-  [STM32 programming](https://github.com/Ildaron/ironbci#5-stm32-programming)  
-  [Hardware and Signal processing demonstarations](https://github.com/Ildaron/ironbci#6-hardware-and-signal-processing-demonstarations)     
-  [Citation](https://github.com/Ildaron/ironbci/blob/master/README.md#7-citation)   
-  [Contacts](https://github.com/Ildaron/ironbci/blob/master/README.md#8-contacts)     

Low-cost brain computer interface with [GNU license](https://github.com/Ildaron/ironbci/blob/master/license.txt)
#### Instructions
##### 1 step   
[Gerbers files](https://github.com/Ildaron/ironbci/tree/master/gerber_files) for PCB boards.  
An example of our order at [PCBWAY](https://www.pcbway.com/?adwgc=666&campaignid=172480651&adgroupid=8787904531&feeditemid=&targetid=kwd-96217560494&loc_physical_ms=1009306&matchtype=p&network=g&device=c&devicemodel=&creative=347469560617&keyword=pcbway&placement=&target=&adposition=&gclid=CjwKCAjwxo6IBhBKEiwAXSYBs2ps2-PbZhsKTEathEQYGyJbzSM-ZocwmjvOCRQQF-C-VqjU3FY89xoCQAgQAvD_BwE)  
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/gerber_DIY.bmp "Gerber")​

#####  2 Step   
BOM files can be created by [electrical schemes](https://github.com/Ildaron/ironbci/tree/master/electrical_scheme)

#####  3 Step 
[Hex file] (https://github.com/Ildaron/ironbci/blob/master/ironbci.hex) can be uploaded to STM32F407VE by ST-LINK V2 RST  
 With the next 4 pins:  
                        - RST      
                        - TCK    
                        - gnd   
                        - TMS    
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/stl1.bmp "stm32")

#####  4 Step  
By [brainflow](https://brainflow.readthedocs.io/en/stable/) software instructions with [MIT lisence](https://brainflow.readthedocs.io/en/stable/License.html) start signal processing.
board_id: 17  


Files   
[1.ADS_1299.c ](https://github.com/Ildaron/ironbci/blob/master/1.ADS_1299.c) - code for Atollic TrueSTUDIO for STM32 F407VE  
[1.ADS_1299.ioc](https://github.com/Ildaron/ironbci/blob/master/ads1299.ioc) - file for STM32CubeMX

####  2.  General pin information about ADS1299 signals
![alt tag](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/stm1.bmp "stm32")​  
SPI2 for communicate with ADS1299  
UAART4 for send data to HC-12
2.1.DRDY output - becomes high when conversion starts and low when data is ready    
2.2  Two ways to read data:      
      - RDATA C1 - continuous read command;      
      - Reading RDATA data that requires a command to load an input offset.  
2.3. The amount of input data - 24 bits * 8 = 192 bits + 24 status bits, a total of 216 bits  

#### 3. Configuration of control registers  
Three bytes of register configuration  
0b11010110    
0b11010100
0b11100000

#### 4. Description of code ADS_1299.c  
Data transfer starts after receiving by the microcontroller - "s", ends after receiving - "p"  
Data is transmitted via Serial with a baud rate - 115200  

#### 5. Hardware and Signal processing demonstarations  
Hardware demonstarations  
[![Hardware demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/hardware_ironbci.bmp)](https://youtu.be/kfbvYXvBCJk)    
Signal processing by brainflov via timeflux (https://timeflux.io/)    
[![Sowtware demonstrations](https://github.com/Ildaron/ironbci/blob/master/Supplementary%20files/software.bmp)](https://youtu.be/y1O7FNJLeh4)      


#### 6. Citation  
Original article coming soon  
#### 7. Contacts  
For any questions write to me by mail - ildar.o2010@yandex.ru   
