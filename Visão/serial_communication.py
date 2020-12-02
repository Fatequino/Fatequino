import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

for x in range(1,10):
arduino.write(b'0')
time.sleep(0.5)
arduino.write(b'1')
time.sleep(0.5)
