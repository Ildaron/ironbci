


import asyncio
import sys
from bleak import BleakClient
import time
from matplotlib import pyplot as plt

data_f = []
FIRST_NAME_ID = '0000fe42-8e22-4541-9d4c-21edae82ed19'
address = "00:80:E1:26:0E:AA"
#global data_for_graph
data_for_graph = []
axis_x = 0 
async def main(address):
    async with BleakClient(address) as client:
        def callback(FIRST_NAME_ID, data):
            print (data[0], data[1])
            data_result = 0
            data_check = 0xFFFFFF
            data_test  = 0x7FFFFF
            step = 5
            data_received = data
            
            for a_count in range (1,19,1):                
                data_read = data_received[a_count]
                data_result = (data_result<<8)|data_read
                
                if a_count % 3 == 0: 
                    convert_data = data_result|data_test                
                    if (convert_data == data_check):
                        result = (16777214 - data_result) 
                    else:      
                        result = data_result
                    result=round(1000000*4.5*(result/16777215),2)

                    #print (a_count, result)
                    global data_for_graph
                    data_for_graph.append(result)
                    
                    global axis_x
                    if len(data_for_graph)==step:
                        #print (len(data_for_graph), data_for_graph[1])
                        plt.plot(range(axis_x, axis_x+step,1),data_for_graph,color = '#0a0b0c') 
                        plt.axis([axis_x-500, axis_x+2000, (data_for_graph[1]) - 100, (data_for_graph[1])+100])
                        axis_x=axis_x+step
                        data_for_graph = []
                        plt.pause(0.001)
                        plt.draw()
                        
                    data_result = 0
                    convert_data = 0
                    result = 0
                    data_read = 0
                        
        await client.start_notify(FIRST_NAME_ID, callback)
        print ("was connected")
        
        while 1: 
          if not event.is_set():    
              await event.wait()  
          #await asyncio.sleep(0)
          event.clear()
          
event = asyncio.Event()
print('address:', address)
asyncio.run(main(address))
