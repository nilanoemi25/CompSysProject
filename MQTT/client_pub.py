#!/usr/bin/python3
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import time
import sys 
sys.path.insert(0, '../')
from employee_data import *
from camera_test import capture_image
import BlynkLib

sense = SenseHat()
sense.clear()

IMAGE_PATH="../images/sensehat_image.jpg"
BLYNK_AUTH = 'z275UI1-xYpfjeR4JM-TroJ1R4l28_HN'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# parse mqtt url for connection details. DON'T FORGET TO UPDATE YOUR_ID TO A UNIQUE ID
URL = urlparse("mqtt://broker.emqx.io:1883/nilanoemi25/home")
BASE_TOPIC = URL.path[1:]
DEVICE_ID = "device1"

# MQTT event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message ID: {mid} published successfully")

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")
    if rc != 0:
        print("Unexpected disconnection. Reconnecting...")
        client.reconnect()

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish


# check if useame and password in the url (there isn't in this basic example)
if (URL.username):
    mqttc.username_pw_set(URL.username, URL.password)
# Connect
mqttc.connect(URL.hostname, URL.port)
mqttc.loop_start()

# Publish a message to only when the button is pressed on Rasberry Pi
while True:
   
    for event in sense.stick.get_events():
        print(event.direction, event.action) 
        if event.action == "pressed":
            capture_image(IMAGE_PATH)
            blynk.log_event("clockin")
            msgFromClient = get_employee_data(DEVICE_ID)
            handle_v0_write("V0")
            mqttc.publish(f"{BASE_TOPIC}/environment",str(msgFromClient))

    time.sleep(15)