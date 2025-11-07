import paho.mqtt.client as mqtt
import time
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

PUMP_TDS_TOPIC = "insert/topic"
PUMP_PH_TOPIC = "insert/topic"

received_data = {}
class Data:
	def __init__(self, tds=None, ph=None):
		self.tds = tds
		self.ph = ph
            


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker.")
        for topic in topics:
            client.subscribe(topic)
    else:
        print(f"Connection failed: {rc}")

def on_message(client,userdata,message):
    value = message.payload.decode()
    topic = message.topic
    received_data[topic]=value
	

# Create MQTT client
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Connect to broker
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()
print("Waiting, for MQTT connection...\n")
time.sleep(5)

tds_value = float(received_data.get("TDS", 9999))
ph_value = float(received_data.get("pH",7))

data = Data(tds_value, ph_value)
#data.control()
print(received_data)
time.sleep(2)


client.loop_stop()
client.disconnect()














