import serial
import paho.mqtt.client as mqtt
from datetime import datetime
import sys



# Serial port setup with timeout
try:
    ser = serial.Serial(
        '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',
        115200,
        timeout=10  # Timeout in seconds original timeout of 1 second
    )
    print("Serial port opened successfully.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)

while True: 
    print(ser.readline())
    now = datetime.now()
    line = ser.readline().decode('utf-8').strip()
    if line:
        print(f'\n{now}: {line}')
