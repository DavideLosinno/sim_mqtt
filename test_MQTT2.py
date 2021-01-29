#   Prima installare: pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import time


def MessaggioRicevuto(client, userdata, message):
    print("Messaggio ricevuto: " + str(message.payload.decode("utf-8")))
    print("Topic: " + message.topic)
    print(" ")
    
#   Creo un nuovo client assegnando ID
client = mqtt.Client("P2")
client.on_message = MessaggioRicevuto
#   Mi connetto al broker
client.connect("192.168.0.43")
#   Mi sottoscrivo a un topic
client.subscribe("home-assistant/sensore/nebbiogeno")
#   Inizio loop gestione eventi
client.loop_start()
#   Aspetto
time.sleep(1000)
#   Fermo il loop gestione eventi
client.loop_stop()
