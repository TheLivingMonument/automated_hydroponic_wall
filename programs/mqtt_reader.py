import paho.mqtt.client as mqtt
from datetime import datetime

# mqtt broker configuration 
MQTT_BROKER = "192.168.178.22"
MQTT_PORT = 1883
MQTT_USERNAME = 'mqtt_user'
MQTT_PASSWORD = 'Pi4polimi!'

topics = [("serial_temperature", 2),
("serial_humidity",2),
("TDS",2),
("pH",2),
("light",2),
("water_level",2),
("water_temperature",2)]

topic_names = ["serial_temperature", "serial_humidity", "TDS", "pH",
"light", "water_level", "water_temperature"]

def on_message(client,userdata,message):
    value = message.payload.decode()
    for topic_name in topic_names:
        if message.topic == topic_name:
            print(f"{topic_name} value: {value}")

# Create MQTT client
client = mqtt.Client(callback_api_version=1)
client.on_message = on_message
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Connect to broker
client.connect(MQTT_BROKER, MQTT_PORT)

while True:
    client.loop()
    client.subscribe(topics)




