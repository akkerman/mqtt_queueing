#!/usr/local/bin/python -u
import time
import sys
from killer import Killer
import paho.mqtt.client as mqtt
import mqtthandler

killer = Killer()

def setup_mqtt():
    client = mqtt.Client(client_id="recv", clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    try:
        client.connect("mqtt", 1883, 60)
        return client
    except:
        print("failed to connect to mqtt")
        sys.exit(-1)

def on_connect(client, userdata, flags, rc):
    print("connected to mqtt")
    client.subscribe("messages", 1)
    connected = True

def on_message(client, userdata, msg):
    print("got message: ", msg.payload)

def on_disconnect(client, userdata, rc):
    sys.exit(rc)

client = setup_mqtt()
while killer.cont:
    client.loop()
    time.sleep(0.1)

client.disconnect()
