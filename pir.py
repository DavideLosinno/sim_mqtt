#   Prima installare: pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import time
import random


#   Creo un nuovo client assegnando ID
client = mqtt.Client("Pir")

#Mi connetto con utente e password al broker
client.username_pw_set(username="tiesrl",password="tiesrl")
client.connect("192.168.0.43")
client.publish("home-assistant/sensore/pir", "Attivo")

#   Inizio loop gestione eventi
client.loop_start()

#   Tengo il programma aperto
while True:
    time.sleep(1)
#   Fermo il loop di gestione eventi
client.loop_stop()
