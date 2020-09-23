import RPi.GPIO as GPIO
import time

WARTEZEIT=0.0001
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Muss noch implementiert werden 
#class Lichtsensor:
 #   def__init__(self):
class USsensor:
    def __init__ (self,trig,echo):
        self.A=trig
        self.B=echo
        
    def setup(self):
        GPIO.setup(self.A,GPIO.OUT)
        GPIO.setup(self.B,GPIO.IN)

    def distanz(self):
        GPIO.output(self.A,True)
        time.sleep(WARTEZEIT)
        GPIO.output(self.A,False)
    
        self.StartZeit=time.time()
        self.StopZeit=time.time()
    
        while GPIO.input(self.B) == 0:
            self.StartZeit=time.time()
        while GPIO.input(self.B):
            self.StopZeit=time.time()
    
        self.TimeElapsed=self.StopZeit-self.StartZeit
        self.abstand=(self.TimeElapsed*343.2)/2
        return self.abstand

#Initialisierung mit minimalem Sicherheitsabstand
class Erkennung:
    def __init__(self,sicherheitsabstand):
        self.S1=USsensor(18,23)
        self.S2=USsensor(25,8)
        self.S1.setup()
        self.S2.setup()
        self.GPIO_WARNING=24
        self.sicherheitsabstand=sicherheitsabstand
        GPIO.setup(self.GPIO_WARNING,GPIO.OUT)
             
    def kollision(self):
        self.warning=False
        GPIO.output(self.GPIO_WARNING,False)
        if self.sicherheitsabstand > self.S1.distanz() or self.sicherheitsabstand > self.S2.distanz():
            self.warning=True
            GPIO.output(self.GPIO_WARNING,True)
        return self.warning
		
#Ausgabe Abstand in Meter  
    def getabstand(self,position):
        if position =="v":
            self.abstand=self.S1.distanz()
        elif position == "h":
            self.abstand=self.S2.distanz()
        return self.abstand

GPIO.cleanup()
