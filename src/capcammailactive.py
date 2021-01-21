#ici nous importons le package pour le caméra
import picamera

#ici nous importons les librairies de bases à savoir pour la gestion du temps et des GPIOS de la raspberry
import RPi.GPIO as GPIO
import time
from time import sleep

# Ici nous importons la librairie smtplib pour l'envoie de mail
import smtplib

# Ici nous importons la librairie imaplib pour la consultation de mails reçus
import imaplib

# Importation de la librairie pprint pour l'affichage au niveau du terminal pour des besoins de debbugs
import pprint

#ici nous importons les packages d'email que nous aurons besoin
import email
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import webbrowser
import os


# Utilisation de la numérotation électronique de la puce
GPIO.setmode(GPIO.BCM)

#initialisation du GPIO 17 comme entrée de notre capteur de mouvement
GPIO.setup(17,GPIO.IN)


#Supprimer commentaire apres
#time.sleep(45)

#Création des variables pour la connexion au serveur
imap_host = 'imap.gmail.com' #serveur
imap_user = 'horlywheaspy2@gmail.com' #adresse mail recepteur de notre projet
imap_pass = 'Iot2020!' #mot de passe

#variable pour l'activation et la fermeture de connexion
active=0
ferme=0

while True:
        # Se connecter à l'hote en utilisant le SSL
        imap = imaplib.IMAP4_SSL(imap_host)
        ## connexion au serveur
        imap.login(imap_user, imap_pass)

        # Selection de la boite de reception
        status, messages = imap.select("INBOX")

        # nombre de derniers messages à consulter
        N = 1
        
        # nombre total de mails
        messages = int(messages[0])

        #Recherche de message
        #Code copier sur le site de python sur comment lire un mail: https://www.thepythoncode.com/article/reading-emails-in-python
        #On l'a adapté selon notre besoin
        for i in range(messages, messages-N, -1):
            # Chercher les messages par ID
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode(encoding)
                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                        
                    #On regarde ici si le dernier mail recu est envoyé depuis notre adresse mail et s'il contient
                    #comme objet "active". Si oui on active le mode surveillance
                    if From=="Papa Madiodio Dieng <pdieng952@gmail.com>" and subject=="active":
                        active=1
                        
                        #Boucle du mode surveillance
                        while active==1:
                                print("boucle")
                                # On Check si le HC-SR501 détecte un mouvement
                                if GPIO.input(17):
                                        time.sleep(0.1)
                                        print ("Mouvement Detecte")
                                        #creer un objet pour la class PiCamera
                                        camera = picamera.PiCamera()
                                        #paramétrage de la résolution pour le capture
                                        camera.resolution = (1024, 768)
                                        camera.brightness = 60
                                        camera.start_preview()
                                        #Ajouter un titre plus la date au capture
                                        camera.annotate_text = 'ALERTE ' + time.asctime()
                                        time.sleep(1)
                                        #Enregistrer la photo
                                        camera.capture('intrusion.jpeg')
                                        #on arrete le capture
                                        camera.stop_preview()
                                        time.sleep(2)
                                        #paramétrage de la résolution pour la vidéo
                                        camera.resolution = (640, 480)
                                        titre = str(i)+'.h264'
                                        #démarage de l'enregistrement
                                        camera.start_recording(titre)
                                        #on enregistre pour 60 secondes
                                        camera.wait_recording(60)
                                        #on arrete l'enregistrement
                                        camera.stop_recording()
                                        #on met à l'arret le caméra
                                        camera.close()
                                        time.sleep(1)   

                                        #initialisation des parametres pour l'envoie de l'alerte par mail
                                        msg = MIMEMultipart() #instantiation de l'objet de la classe MIMEMultipart pour l'envoie d'image par mail
                                        password = 'Iot2020!'
                                        msg['Subject'] = 'ALERTE INTRUSION' #objet du mail
                                        me = 'horlywheaspy@gmail.com' #envoyeur
                                        dest = 'horlywheaspy@gmail.com' #revceveur
                                        msg['From'] = me
                                        msg['To'] = dest
                                        msg.preamble = 'ALERTE INTRUSION'
                                         
                                        # Trouver l'image à envoyer
                                        file = 'intrusion.jpeg'
                                        # l'ouvrir en mode binaire.  La classe MIMEImage s'en charge automatiquement
                                        fp = open(file, 'rb')
                                        img = MIMEImage(fp.read())
                                        fp.close()
                                        #on attache en piece jointe l'image de l'intru dans le mail
                                        msg.attach(img)
                                                 

                                        #envoie du mail via le serveur SMTP
                                        mailserver = smtplib.SMTP("smtp.gmail.com", 587)
                                        mailserver.ehlo()
                                        mailserver.starttls()
                                        mailserver.ehlo()
                                        mailserver.login(msg['From'], password)
                                        mailserver.sendmail(msg['From'], msg['To'], msg.as_string())
                                        mailserver.quit()
                                        time.sleep(1)
                                #on attend 15s
                                time.sleep(15)
                                
                                #On check si le proprietaire veut desactiver le mode surveillance

                                # Selection de la boite de reception
                                status, messages = imap.select("INBOX")
                                # nombre de derniers messages à consulter
                                N = 1
                                # nombre total de mails
                                messages = int(messages[0])

                                #Recherche de message
                                #Meme code qu'en haut
                                for i in range(messages, messages-N, -1):
                                    # fetch the email message by ID
                                    res, msg = imap.fetch(str(i), "(RFC822)")
                                    for response in msg:
                                        if isinstance(response, tuple):
                                            # parse a bytes email into a message object
                                            msg = email.message_from_bytes(response[1])
                                            # decode the email subject
                                            subject, encoding = decode_header(msg["Subject"])[0]
                                            if isinstance(subject, bytes):
                                                # if it's a bytes, decode to str
                                                subject = subject.decode(encoding)
                                            # decode email sender
                                            From, encoding = decode_header(msg.get("From"))[0]
                                                
                                            #On regarde ici si le dernier mail recu est envoyé depuis notre adresse mail et s'il contient
                                            #comme objet "desactive". Si oui on désactive le mode surveillance
                                            if From=="Papa Madiodio Dieng <pdieng952@gmail.com>" and subject=="desactive":
                                                active=0
                                                # fermeture de la connexion et deconnexion
                                                imap.close()
                                                imap.logout()
                                                ferme=1
                                                time.sleep(15)



        if ferme==0:
                # fermeture de la connexion et deconnexion
                imap.close()
                imap.logout()
        time.sleep(5)
        


