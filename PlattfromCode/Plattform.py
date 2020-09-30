import Sensoren
import Antriebe
import math
from time import sleep

STEPSMOTOR=200
PIKENGRAD=45
ARMBEWEGUNGSWINKEL=45
SPEEDSCHNELL=1
SPEEDLANGSAM=2

#Initialisierung mit gewuenschtem minimalen Sicherheitsabstand und verwendetem Raddurchmesser
#Laengenangaben in Meter
#Aufsatz True=Piker / False = Schaufel
class Plattform():
    def __init__(self,sicherheitsabstand,raddurchmesser,aufsatz):
        self.sensorik=Sensoren.Erkennung(sicherheitsabstand)
        self.motoren=Antriebe.Antrieb()
        self.radumfang=raddurchmesser*math.pi
        self.aufsatz=aufsatz
        if self.aufsatz:
            self.motoren.hubhoch(1,1)
        else:
            self.motoren.hubhoch(0,1)
        
#Eingabe der zu fahrenden Strecke fuer Funktionen zur Fortbewegung in Meter
#Eingabe der gewuenschten Rotationen fuer Funktionen in Grad
#Speed -> 1 == schnell, 2 -> langsam
    def nachvorne(self,strecke,speed):
        #self.steps=round(strecke/self.radumfang*STEPSMOTOR)
	if not(self.sensorik.kollision()):
            self.motoren.vorwaertsstep(strecke,speed)
            
    def nachhinten(self,strecke,speed):
        #self.steps=round(strecke/self.radumfang*STEPSMOTOR)
        if not(self.sensorik.kollision()):
            self.motoren.rueckwaertsstep(strecke,speed)
            
#links und rechts Drehen auch bei Objektdetektion unter Abstand moeglich
    def linksrum(self,grad,speed):
        self.steps= 20
	#round(grad/360*STEPSMOTOR)
        self.motoren.linksdrehen(self.steps,speed)
        
    def rechtsrum(self,grad,speed):
        self.steps=20
        self.motoren.rechtsdrehen(self.steps,speed)
        
    def piken(self):
        speed=SPEEDSCHNELL
        self.steps=16
	self.motoren.hubhoch(self.steps,speed)
	sleep(0.5)
        self.motoren.hubrunter(self.steps,speed)
        sleep(0.5)
	self.motoren.hubhoch(self.steps,speed)
        
    def armabsetzen(self):
        speed=SPEEDLANGSAM
        self.steps=8
	#round(ARMBEWEGUNGSWINKEL/360*STEPSMOTOR)
        self.motoren.hubrunter(self.steps,speed)
        
    def armanheben(self):
        speed=SPEEDLANGSAM
	#round(ARMBEWEGUNGSWINKEL/360*STEPSMOTOR)
	self.steps = 8
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
 
