import sys
import time
import  matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import pandas as pd
from scipy import signal
import numpy as np
import re

location = 'C:/Users/irakhmat/Desktop/Python/eeg_data.txt'

data_final = []
data_result = 0
data_test  = 0x7FFFFF
data_check = 0xFFFFFF
data_for_graph = []
ch_1 = []
ch_2 = []
ch_3 = []
ch_4 = []
marker = []
with open(location, 'r') as file:
    data = file.read()    
#   print (data)
#   sys.exit() 
#   data = [sublist[1:] for sublist in data]
#   print (data)
    data = [int(match) for match in re.findall(r'\d+', data)]

    #start remove maerker 
    amount = len(data)/121
    positions_to_remove = []
    for a in range (0,len(data),121):
        positions_to_remove.append(a)
        marker.append([data[a]])
    data = [data[i] for i in range(len(data)) if i not in positions_to_remove]
    #stop remove maerker 
    
    for a_count in range (1,len(data)+1,1):
        
        data_result = (data_result<<8)|data[a_count-1]
        if a_count % 3 == 0:
            convert_data = data_result|data_test                
            if (convert_data == data_check):
                result = (16777214 - data_result) 
            else:      
                result = data_result
            result=round(1000000*4.5*(result/16777215),2)
            data_for_graph.append(result)
            data_result = 0

ch_1 = [data_for_graph[i] for i in range(0, len(data_for_graph), 4)]
ch_2 = [data_for_graph[i] for i in range(1, len(data_for_graph), 4)]
ch_3 = [data_for_graph[i] for i in range(2, len(data_for_graph), 4)]
ch_4 = [data_for_graph[i] for i in range(3, len(data_for_graph), 4)]
    
print (len(data_for_graph))
data_raw = data_for_graph
plt.plot(ch_1)
plt.plot(ch_2)
plt.plot(ch_3)
plt.plot(ch_4)
plt.show()

#1.2 Band-pass filter
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y
def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a
def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

#1.3 Set plot
figure, axis = plt.subplots(4, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=2)

axis[0].set_xlabel('Ch_1')
axis[0].set_ylabel('Amplitude')
axis[0].set_title('Data after pass filter')
axis[0].grid(True)

axis[1].set_title('Ch_2')
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')
axis[1].grid(True)

axis[2].set_title('Ch_3')
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')
axis[2].grid(True)

axis[3].set_title('Ch_4')
axis[3].set_xlabel('Time')
axis[3].set_ylabel('Amplitude')
axis[3].grid(True)

line, = axis[0].plot([], [], marker='o', color='blue', linestyle='-', markersize=8)


x_data_power = []
y_data_power = []

axis_x = 0
axis_x_power = 0
fps = 250    
lowcut = 12
highcut = 8

#  data_for_graph = dataset 
ch_1_high = butter_highpass_filter(ch_1, highcut, fps)
ch_1_band_pass = butter_lowpass_filter(ch_1_high, lowcut, fps)

ch_2_high = butter_highpass_filter(ch_2, highcut, fps)
ch_2_band_pass = butter_lowpass_filter(ch_2_high, lowcut, fps)

ch_3_high = butter_highpass_filter(ch_3, highcut, fps)
ch_3_band_pass = butter_lowpass_filter(ch_3_high, lowcut, fps)

ch_4_high = butter_highpass_filter(ch_4, highcut, fps)
ch_4_band_pass = butter_lowpass_filter(ch_4_high, lowcut, fps)
#ch_1_band_pass = ch_1_band_pass#[20000:150000]

axis[0].plot(ch_1_band_pass)
axis[1].plot(marker)
axis[2].plot(ch_3_band_pass)
axis[3].plot(marker)

plt.show()
