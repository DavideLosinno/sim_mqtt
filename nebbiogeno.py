import paho.mqtt.client as mqtt
import time


def MessaggioRicevuto(client, userdata, message):
    print("comando ricevuto: " + str(message.payload.decode("utf-8")) )
    if (str(message.payload.decode("utf-8")) == "ON"):
        print("Accendo")
        client.publish("home-assistant/sensore/nebbiogeno","ON")
    else:
        print("Spengo")
        client.publish("home-assistant/sensore/nebbiogeno","OFF")

        
#   Creo un nuovo client assegnando ID
client = mqtt.Client("Nebbiogeno")
#   Associo l'evento di arrivo di un nuovo messaggio ad una funzione
client.on_message = MessaggioRicevuto
#Mi connetto con utente e password al broker
client.username_pw_set(username="tiesrl",password="tiesrl")
client.connect("192.168.0.43")

#   Mi sottoscrivo a un topic così se qualcuno pubblica su questo topic lo vedo
client.subscribe("home-assistant/sensore/nebbiogeno/set")
#   Inizio loop gestione eventi
client.loop_start()

#   Tengo il programma aperto
while True:
    time.sleep(1)
#   Fermo il loop di gestione eventi
client.loop_stop()
