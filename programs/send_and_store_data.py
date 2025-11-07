import serial
import paho.mqtt.client as mqtt
from datetime import datetime
import sys

#csvpath = "/home/pia-polimi/TheLivingMonument.github.io/data/livingMonumentData.txt"
csvpath = "/home/pia-polimi/Desktop/dataHarvesting/data/main_dataset.txt"


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

# MQTT broker configuration
#MQTT_BROKER = "10.0.3.3" 
MQTT_BROKER = "192.168.178.22"  
MQTT_PORT = 1883
MQTT_USERNAME = "mqtt_user"  
MQTT_PASSWORD = "Pi4polimi!" 

# MQTT topics
TOPIC_TEMP = "serial_temperature"
TOPIC_HUM = "serial_humidity"
topic_tds = 'TDS'
topic_ph = 'pH'
topic_light = 'light'
topic_waterlevel = 'water_level'
topic_watertemp = 'water_temperature'

# Create MQTT client
client = mqtt.Client(callback_api_version=1)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Connect to broker
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = ser.readline().decode('utf-8').strip()

    if line:  # Check if line is not empty
        try:
            string = f'{now},{line}\n'
            with open(csvpath, 'a', encoding='utf-8') as file:
                file.write(string)
            file.close()

            # These have to be in se same order as they are displayed in the serial port
            pH,TDS,temperature,humidity,light,water_level,water_temp= map(float, line.split(','))
            #water_level = 85
            #water_temp = 20.4
            #pH = 5.4
            client.publish(TOPIC_TEMP, temperature)
            client.publish(TOPIC_HUM, humidity)
            client.publish(topic_tds, TDS)
            client.publish(topic_ph, pH)
            client.publish(topic_light, light)
            client.publish(topic_waterlevel, water_level)
            client.publish(topic_watertemp, water_temp)

        except ValueError:
            print(f"Invalid data received: {line}")
            continue

client.loop_stop()
client.disconnect()
