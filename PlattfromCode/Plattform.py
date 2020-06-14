import Sensoren
import Antriebe
import math

STEPSMOTOR=512
PIKENGRAD=45
ARMBEWEGUNGSWINKEL=45
SPEEDSCHNELL=1
SPEEDLANGSAM=2

#Initialisierung mit gewünschtem minimalen Sicherheitsabstand und verwendetem Raddurchmesser
#Längenangaben in Meter
class Plattform():
    def __init__(self,sicherheitsabstand,raddurchmesser):
        self.sensorik=Sensoren.Erkennung(sicherheitsabstand)
        self.motoren=Antriebe.Antrieb()
        self.radumfang=raddurchmesser*math.pi
        
#Eingabe der zu fahrenden Strecke für Funktionen zur Fortbewegung in Meter
#Eingabe der gewünschten Rotationen für Funktionen in Grad
#Speed -> 1 == schnell, 2 -> langsam
    def nachvorne(self,strecke,speed):
        self.steps=round(strecke/self.radumfang*STEPSMOTOR)
        if not(self.sensorik.kollision()):
            self.motoren.vorwaertsstep(self.steps,speed)
            
    def nachhinten(self,strecke,speed):
        self.steps=round(strecke/self.radumfang*STEPSMOTOR)
        if not(self.Sensorik.kollision()):
            self.motoren.rueckwaertsstep(self.steps,speed)
            
#links und rechts Drehen auch bei Objektdetektion unter Abstand möglich
    def linksrum(self,grad,speed):
        self.steps=round(grad/360*STEPSMOTOR)
        self.motoren.linksdrehen(self.steps,speed)
        
    def rechtsrum(self,grad,speed):
        self.steps=round(grad/360*STEPSMOTOR)
        self.motoren.rechtsdrehen(self.steps,speed)
        
    def piken(self):
        speed=SPEEDSCHNELL
        self.steps=round(PIKENGRAD/360*STEPSMOTOR)
        self.motoren.hubrunter(self.steps,speed)
        self.motoren.hubhoch(self.steps,speed)
        
    def armabsetzen(self):
        speed=SPEEDLANGSAM
        self.steps=round(ARMBEWEGUNGSWINKEL/360*STEPSMOTOR)
        self.motoren.hubrunter(self.steps,speed)
        
    def armanheben(self):
        speed=SPEEDLANGSAM
        self.steps=round(ARMBEWEGUNGSWINKEL/360*STEPSMOTOR)
        self.motoren.hubhoch(self.steps,speed)

#Motorwahl (1/2/3), Richtung("l","r"), Grad(0-360)        
    def konfig(self,motorwahl,richtung,grad):
        speed=SPEEDLANGSAM
        self.steps=round(grad/360*STEPSMOTOR)
        self.motoren.motorausrichten(motorwahl,richtung,self.steps,speed)
        
    def geringsterabstand(self):
        self.vorne=self.sensorik.getabstand("v")
        self.hinten=self.sensorik.getabstand("h")
        self.result = self.vorne
        if self.hinten < self.vorne:
            self.result = self.hinten
        return self.result
    

        

