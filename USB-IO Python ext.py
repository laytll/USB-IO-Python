"""RDS SensConnect USB-IO Python demo
This is an example program to send a serial packet, recieve a response
and a method on processing the response.

"""
import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM24" 
ser.bytesize=8
ser.parity='N'
ser.stopbits=1
ser.timeout = 1 ## readline() for 1s timeout

"""function for extracting data spread accross >1 byte
This takes the arguments: list[], start index int, end index int.

This takes a list of which the data has 0x notation
Then iterates the list removing the "0x" and also padding single charecters to create "02" from "2"


This is useful on the USB-IO to get sensor readings, versions, dates.

"""
def extractDataString (srcList, start, end):
    rem0x = [None] *len(srcList)
    for d in range(start, end):
        rem0x[d] = srcList[d][2:4].zfill(2)
    print(''.join(rem0x[start:end]))


    ## create a command for command 'V' (0x56). This gives a 15B response.
request = 0x1b, 0x02, 0x56, 0x1b, 0x03
    ## create a command to turn onboard red LED on
#request = 0x1b, 0x02, 0x43, 0x20, 0xff, 0x1b, 0x03

ser.open()
#print(ser.is_open) #check serial port name which opened

ser.write(request)
#result = list(ser.read(15)) # decimal list from a known 15B length response
result = ser.readline() ## this is a slow method. Use above when length is known.
hexResult = [None] *len(result) ## initialise hex list of same length

for i in range(0, len(result)):
    hexResult[i] = hex(result[i])
    
print(hexResult)
#extractDataString(hexResult, 3, 6) ## This returns the 3B serial number

