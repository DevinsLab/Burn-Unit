# Josh Thornburg and Thomas Kierski
# 24 January 2017
# Using Max30100
# This version will save data to a CSV for analysis. Borrowing the
# data collection from version 2. Bug not quite worked out, might
# try and sort out with digital filtering.

#UPDATE: A Median filter seems to work well in eliminating spikes from the data stream.

import smbus
import time

bus=smbus.SMBus(1)

slave_add=0x57

######## Register addresses ##########
Interrupt_Status=0x00
Interrupt_Enable=0x01
FIFO_Write_Pointer=0x02
Over_Flow_Counter=0x03
FIFO_Read_Pointer=0x04
FIFO_Data_Register=0x05
Mode_Configuration=0x06
SPO2_Configuration=0x07
LED_Configuration=0x09
Temp_Integer=0x16
Temp_Fraction=0x17
Revision_ID=0xFE
Part_ID=0xFF
#######################################

######### Mode Control ################
Test_Mode=0x03 #Should be only SPO2 enabled
Reset=0x40
#######################################

def request_reading(data_add):
    reading=hex(bus.read_byte_data(slave_add,data_add))
    return reading

def write_data(data_add,data_byte):
    bus.write_byte_data(slave_add,data_add,data_byte)

def mode_enable(mode_byte):
    write_data(Mode_Configuration,mode_byte)
    if mode_byte != Reset:
        print("Mode set successfully")

def SPO2_config(SPO2_SR,LED_PW):
    byte=(0b01000000)|(SPO2_SR<<2)
    byte=byte|LED_PW
    write_data(SPO2_Configuration,byte)
    print("SPO2 configuration successful")

def LED_config(RED_PA,IR_PA):
    byte=(RED_PA<<4)|(IR_PA)
    write_data(LED_Configuration,byte)
    print("LED configuration successful")
    
def Read_FIFO():
    block=[]
    byte=request_reading(Over_Flow_Counter)
    if byte!='0x0':
        print("Losing samples")
        print(byte)
    for i in range(1,5):
        block.append(request_reading(FIFO_Data_Register))
    return block

def display_data(block):
    IR=(int(block[0],16)<<8)|(int(block[1],16))
    RED=(int(block[2],16)<<8)|(int(block[3],16))
    print("IR: "+str(IR)+" || RED: "+str(RED))
    
#Configuration
print("Initializing . . . ")
mode_enable(Reset)
mode_enable(Test_Mode)  # Only SPO2
SPO2_config(0b001,0b11) # Testing, 100 samples/sec, 1.6 ms PW --> 16-bit ADC
LED_config(0b0011,0b0011) # Testing, 11 mA for both LEDs

#Reading Data
print('\n')
#count=0
f=open("test_data.txt","w")
try:
    while True:  
        #Streaming data points, use CTRL-C on keyboard to stop

        temp1=request_reading(FIFO_Write_Pointer)
        temp2=request_reading(FIFO_Read_Pointer)

        while temp1 != temp2:
            block=Read_FIFO()
##            count=count+1
##
##            if count%50==0:
##                display_data(block)
            
            IR=(int(block[0],16)<<8)|(int(block[1],16))
            RED=(int(block[2],16)<<8)|(int(block[3],16))

            f.write("%d,%d,"%(IR,RED))
            
            temp1=request_reading(FIFO_Write_Pointer)
            temp2=request_reading(FIFO_Read_Pointer)
          
except KeyboardInterrupt:
    f.close()
    print("\nInterrupted")
    mode_enable(Reset) 


