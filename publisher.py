import paho.mqtt.client as mqtt
import time

mqttBroker = "192.168.205.217"
client = mqtt.Client("sender")
client.username_pw_set("soumyajit", password=1234)
client.connect(mqttBroker,1883,60)

while True:
    msg=input("type the message you want to send")
    client.publish("topic", msg)
    print("sent the msg: " + str(msg) + " to the Topic named topic")
    time.sleep(1)
