import time
import serial

arduinoCountData = serial.Serial('com3', 115200)
time.sleep(1)
i = 0
while i < 51:
    i += 1
    while (arduinoCountData.inWaiting() == 0): # While there is no data, wait
        pass
    data = (str(arduinoCountData.readline(), 'utf-8')).strip('\r\n') # Convert the data which has a byte format to a string and then remove the \r\n part of the data that means a new line
    #print(data)
    dataArray = data.split(',')
    x = dataArray[0]
    y = dataArray[1]
    z = dataArray[2]
    print(f'X = {x}, Y = {y}, Z = {z}')