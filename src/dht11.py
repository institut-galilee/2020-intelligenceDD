"""Ici nous avons juger necessaire d'isoler le capteur de temperature car la lecture des données de celui ci
prenais un temps fou que si on l'integrait directement sur notre transfertheure.py ça allait relentir le programme
et ainsi occasionner des bugs pour la simulation des secondes avec le ruban led.
Pour le relier à notre programme de transfert des données de la raspberry à l'arduino nous avons utiliser un fichier txt
comme tremplin afin que les deux programmes puisssent communiquer"""


#importation de la librairie qui gere le capteur de temperature et d'humidité
import Adafruit_DHT

#importation de la librairie de gestion de temps
import time
 
# Ininiatisation du type de capteur utilisé: Les options sont DHT11,DHT22 ou AM2302
#ici on choisit le DHT11
capteur=Adafruit_DHT.DHT11
 
# Initialisaton du GPIO utilisé pour la connecté avec notre raspberry
gpio=4
 

while True:
  #cette capteur necessite 2 secondes entre chaque requete por obtenir les données
  humidite, temperature = Adafruit_DHT.read_retry(capteur, gpio)
  
  if humidite is not None and temperature is not None: #On check si la lecture fut bonne
    t=str(temperature)
    h=str(humidite)
    with open("data.txt", "w") as fichier: #on écrit sur le fichier data.txt les données du capteur
      fichier.write(t)
      fichier.write(h)
      print(t)
      print(h)
  else: #si la lecture s'est mal passé
    print('Failed to get reading. Try again!')

  time.sleep(60) #on attend une minure avant de relire
  
