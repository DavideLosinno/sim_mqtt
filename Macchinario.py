import paho.mqtt.client as mqtt
import math
import random
import time
import json

#creo la classe macchinario
class Macchinario:

    def __init__(self,id,utente,password):
        self.id = str(id)
        #Mi connetto con utente e password al broker
        self.client = mqtt.Client(self.id)
        self.client.username_pw_set(username = utente ,password = password)
        self.client.connect("192.168.0.43")
        self.consumo = 0
        self.pressione = 0
        self.allarme = 0
        

    def InviaDati(self):
        self.LeggiDati()
        dati = {}
        dati["consumo"] = self.consumo
        dati["pressione"] = self.pressione
        dati["allarme"] = self.allarme
        self.client.publish("home-assistant/sensore/"+ self.id +"/status", json.dumps(dati) )

    def LeggiDati(self):
        self.consumo = random.randint(0, 50)
        self.pressione = random.randint(0, 50)
        self.allarme = random.choice(["on", "off"])

    
#Creo Macchinari
macchine = []
for i in range (1,6):
    m = Macchinario(i, "tiesrl", "tiesrl")
    macchine.append(m)


 #Invia dati
while True:
    for m in macchine:
        m.InviaDati()
    time.sleep(random.randint(1, 4))        

#fhjcghdcds
