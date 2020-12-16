import serial
import time
from datetime import datetime
ser = serial.Serial('/dev/ttyACM0',9600)
ser.flush()

while True:
    #c=str(datetime.now())
    b=time.asctime();
    ser.write(b[11])
    time.sleep(0.02)
    ser.write(b[12])
    time.sleep(0.02)
    ser.write(b[14])
    time.sleep(0.02)
    ser.write(b[15])
    time.sleep(0.02)

    
   """ #jour
    ser.write(b[8])
    time.sleep(0.02)
    ser.write(b[9])
    time.sleep(0.02)

    #Annee
    ser.write(b[20])
    time.sleep(0.02)
    ser.write(b[21])
    time.sleep(0.02)
    ser.write(b[22])
    time.sleep(0.02)
    ser.write(b[23])
    time.sleep(5)
        #Mois
    ser.write(b[4])
    ser.write(b[5])
    ser.write(b[6])
    
    """
    """#jour semaine
    ser.write(b[0])
    ser.write(b[1])
    ser.write(b[2])
    time.sleep(0.1)
    time.sleep(10)"""
    
#time.sleep(1)
#ans = "2"
#ser.write(ans)
#time.sleep(1)
#ans = "3"
#ser.write(ans)
#time.sleep(1)
