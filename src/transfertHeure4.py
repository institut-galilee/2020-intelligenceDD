""" Programme pour le transfert de données comme l'heure, la date, les données météorolique... de la raspberry à l'arduino
pour l'affichage sur la matrix.

La matrix ne peut pas recevoir une chaine de caractère, donc on enverra les données caractère par caractère.
Et aussi pour plus de 15 caractères envoyés il y'a un bug pour l'affichage au niveau de la matrix donc on veillera
à ne pas depasser ce nombre lors de l'envoie."""

#importation de la bibliotheque GPIO pour l'utilisation des broches
import RPi.GPIO as GPIO
#importation de la bibliotheque seral pour le transfert de données
import serial
#importation des librairies pour la gestion du temps
import time
import datetime
#importation des librairies pour la gestion du ruban led
import board
import neopixel


# Neopixels doit etre connecté soit au D10, D12, D18 ou D21 pour pouvoir marcher
# nous avons choisit le GPIO 21
pixel_pin = board.D21

# Nombre de neopixels
num_pixels = 60


# Ordre de couleur: soit RGB ou GRB
ORDER = neopixel.GRB

#initialisation du ruban
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

i = 0
# Utilisation de la numérotation électronique de la puce
GPIO.setmode(GPIO.BCM)
#initialisation du GPIO 16 comme entrée de notre capteur de luminosité
GPIO.setup(16,GPIO.IN)

#Port selectionné pour la connection entre le raspberry et l'arduino et le debit de transfert de données
ser = serial.Serial('/dev/ttyACM0',9600)
ser.flush()


a=5
#time.sleep(45)

#pour une bonne synchronisation des secondes
time.sleep(60-now.second)
while True:
    #obtention de la date et de l'heure
    b=time.asctime()
    
    print(b)
    #transfert de l'heure caractère par caractère
    ser.write((b[11]).encode())
    ser.write((b[12]).encode())
    ser.write((b[14]).encode())
    ser.write((b[15]).encode())
    
    a=int(b[17]) #on recupere le valeur du dizaine de seconde
    if a >=4 : #si on est à la 40ime seconde on envoie les données météorologique
        with open("data.txt", "r") as fichier: #onverture du fichier data.txt pour recuperer la temperature et l'humidité
            s=fichier.read()
        ser.write('a'.encode())
        ser.write(s[0].encode())
        ser.write(s[1].encode())
        ser.write(s[2].encode())
        ser.write(s[4].encode())
        ser.write(s[5].encode())
        ser.write(s[3].encode())
        ser.write(s[3].encode())
    else: #sinon on envoie caratere par caractere la date
        ser.write((b[0]).encode())
        ser.write((b[1]).encode())
        ser.write((b[2]).encode())

        ser.write((b[8]).encode())
        ser.write((b[9]).encode())
            
        ser.write((b[4]).encode())
        ser.write((b[5]).encode())
        ser.write((b[6]).encode())
    

    #on check s'il ya une forte presence de lumiere puison envoie la donnée
    if GPIO.input(16)==1:
        ser.write(('n').encode()) 
        print ("night")
    else:
        ser.write(('d').encode())
        print ("day")

    if c!=b[15] :
        i=0
        c=b[15]

    #animation du ruban led pour la simulation des seconde et aussi pour le jeu de couleur selon la luminosité
    for j in range(1,6):
        if GPIO.input(16)==1: #s'il y a pas de lumiere
            pixels.fill((0,0,255)) #le ruban en bleu
            pixels[i]=(255,0,0) #la seconde en rouge
        else: #s'il ya de la lumiere
            pixels.fill((255,0,0))#le ruban en rouge
            pixels[i]=(0,0,255) #l'equivalent de la seconde en bleu
        pixels.show()
        time.sleep(1)
        i = i + 1
        if (i==60 ): i = 0



