#!/usr/local/bin/python -u
import time
import sys
from killer import Killer
import paho.mqtt.client as mqtt
import mqtthandler

killer = Killer()
current = 0
last = 0

def setup_mqtt():
    client = mqtt.Client(client_id="send", clean_session=False)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    try:
        client.connect("mqtt", 1883, 60)
        return client
    except:
        print("failed to connect to mqtt")
        sys.exit(-1)

def on_connect(client, userdata, flags, rc):
    print("connected to mqtt")
    client.subscribe("messages", 1)

def on_disconnect(client, userdata, rc):
    sys.exit(rc)

def on_publish(client, userdata, mid):
    print("message published", mid)


client = setup_mqtt()
while killer.cont:
    client.loop()
    current = current + 1
    client.publish("messages", current, 1)
    time.sleep(2)

client.disconnect()
print("exit")

