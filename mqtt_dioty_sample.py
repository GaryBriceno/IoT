import paho.mqtt.client as mqtt
from internte_of_thing.constant import MQTT_USER
from internte_of_thing.constant import MQTT_PASSWORD
from internte_of_thing.constant import MQTT_CHANNEL


# Define event callbacks
def on_connect(client, userdata, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connection failed. rc= "+str(rc))


def on_publish(client, userdata, mid):
    print("Message "+str(mid)+" published.")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid "+str(mid)+" received.")


def on_message(client, userdata, msg):
    print("===========================================")
    print("Message received on topic " + msg.topic)
    print("with QoS: " + str(msg.qos))
    print("and payload: " + str(msg.payload.decode("utf-8")))
    print("===========================================")


mqttclient = mqtt.Client()

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish
mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

# Connect
mqttclient.username_pw_set(MQTT_USER, MQTT_PASSWORD)
mqttclient.connect("www.dioty.co", 1883)

# Start subscription
mqttclient.subscribe(MQTT_CHANNEL+"globant")

# Start publish
mqttclient.publish(MQTT_CHANNEL+"globant", "Hello World Message IoT!")

# Add new subscription
mqttclient.subscribe(MQTT_CHANNEL+"nuevo")

# Loop; exit on error
rc = 0
while rc == 0:
    rc = mqttclient.loop()
    # Publish a message
print("rc: " + str(rc))
