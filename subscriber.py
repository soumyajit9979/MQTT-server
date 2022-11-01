import paho.mqtt.client as mqtt
import time
def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "192.168.205.217"
client = mqtt.Client("client1")
client.username_pw_set("soumyajit", password=1234)
client.connect(mqttBroker,1883,60)

client.loop_start()
client.subscribe("topic")
client.on_message = on_message
time.sleep(30)
client.loop_end()
