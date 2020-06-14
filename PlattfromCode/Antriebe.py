import RPi.GPIO as GPIO
from time import sleep 
import math 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TIMEQUICK=0.0008
TIMESLOW=0.003

class Motor:
    def __init__ (self,v,x,y,z):
        self.A=v
        self.B=x
        self.C=y
        self.D=z
        
    def setup(self):
        GPIO.setup(self.A,GPIO.OUT)
        GPIO.setup(self.B,GPIO.OUT)
        GPIO.setup(self.C,GPIO.OUT)
        GPIO.setup(self.D,GPIO.OUT)
        GPIO.setup(self.A,False)
        GPIO.setup(self.B,False)
        GPIO.setup(self.C,False)
        GPIO.setup(self.D,False)

    def gpio_einstellung_m(self,a,b,c,d):
        GPIO.output(self.A,a)
        GPIO.output(self.B,b)
        GPIO.output(self.C,c)
        GPIO.output(self.D,d)

    def step1(self,speed):
        self.gpio_einstellung_m(0,0,1,1)
        if speed == 1:
            sleep(TIMEQUICK)
        elif speed == 2:
            sleep(TIMESLOW)
        
    def step2(self,speed):
        self.gpio_einstellung_m(0,1,1,0)
        if speed == 1:
            sleep(TIMEQUICK)
        elif speed == 2:
            sleep(TIMESLOW)
    
    def step3(self,speed):
        self.gpio_einstellung_m(1,1,0,0)
        if speed == 1:
            sleep(TIMEQUICK)
        elif speed == 2:
            sleep(TIMESLOW)
    
    def step4(self,speed):
        self.gpio_einstellung_m(1,0,0,1)
        if speed == 1:
            sleep(TIMEQUICK)
        elif speed == 2:
            sleep(TIMESLOW)

class Antrieb:
    def __init__(self):
        self.M1=Motor(4,17,27,22)
        self.M2=Motor(6,13,19,26)
        self.M3=Motor(10,9,11,5)
        self.M1.setup()
        self.M2.setup()
        self.M3.setup()
		
    def stopradantrieb(self):
        self.M1.gpio_einstellung_m(0,0,0,0)
        self.M2.gpio_einstellung_m(0,0,0,0)
        
    def stophubantrieb(self):
        self.M3.gpio_einstellung_m(0,0,0,0)
        
    def vorwaertsstep(self,anzahlsteps,speed):
        while anzahlsteps:
            self.M1.step1(speed)
            self.M2.step1(speed)
            self.M1.step2(speed)
            self.M2.step2(speed)
            self.M1.step3(speed)
            self.M2.step3(speed)
            self.M1.step4(speed)
            self.M2.step4(speed)
            anzahlsteps=anzahlsteps-1
        self.stopradantrieb()
    
    def rueckwaertsstep(self,anzahlsteps,speed):
        while anzahlsteps:
            self.M1.step1(speed)
            self.M2.step1(speed)
            self.M1.step4(speed)
            self.M2.step4(speed)
            self.M1.step3(speed)
            self.M2.step3(speed)
            self.M1.step2(speed)
            self.M2.step2(speed)
            anzahlsteps=anzahlsteps-1
        self.stopradantrieb()
    
    def linksdrehen(self,anzahlsteps,speed):
        while anzahlsteps:
            self.M1.step1(speed)
            self.M2.step1(speed)
            self.M1.step2(speed)
            self.M2.step4(speed)
            self.M1.step3(speed)
            self.M2.step3(speed)
            self.M1.step4(speed)
            self.M2.step2(speed)
            anzahlsteps=anzahlsteps-1
        self.stopradantrieb()
        
    def rechtsdrehen(self,anzahlsteps,speed):
        while anzahlsteps:
            self.M1.step1(speed)
            self.M2.step1(speed)
            self.M1.step4(speed)
            self.M2.step2(speed)
            self.M1.step3(speed)
            self.M2.step3(speed)
            self.M1.step2(speed)
            self.M2.step4(speed)
            anzahlsteps=anzahlsteps-1
        self.stopradantrieb()
    
    def hubhoch(self,anzahlsteps,speed):
        while anzahlsteps:
            self.M3.step1(speed)
            self.M3.step2(speed)
            self.M3.step3(speed)
            self.M3.step4(speed)
            anzahlsteps=anzahlsteps-1
        self.stophubantrieb()
                
    def hubrunter(self,anzahlsteps,speed):
        while anzahlsteps:
            self.M3.step1(speed)
            self.M3.step4(speed)
            self.M3.step3(speed)
            self.M3.step2(speed)
            anzahlsteps=anzahlsteps-1
        self.stophubantrieb()
        
#beliebigen Motor ausrichten    
    def motorausrichten(self,motorwahl,richtung,steps,speed):
        if motorwahl==1:
            if richtung == "r":
                while steps:
                    self.M1.step1(speed)
                    self.M1.step2(speed)
                    self.M1.step3(speed)
                    self.M1.step4(speed)
                    steps=steps-1
            if richtung == "l":
                while steps:
                    self.M1.step1(speed)
                    self.M1.step4(speed)
                    self.M1.step3(speed)
                    self.M1.step2(speed)
                    steps=steps-1
        if motorwahl==2:
            if richtung == "r":
                while steps:
                    self.M2.step1(speed)
                    self.M2.step2(speed)
                    self.M2.step3(speed)
                    self.M2.step4(speed)
                    steps=steps-1
            if richtung == "l":
                while steps:
                    self.M2.step1(speed)
                    self.M2.step4(speed)
                    self.M2.step3(speed)
                    self.M2.step2(speed)
                    steps=steps-1
        if motorwahl==3:
            if richtung == "r":
                while steps:
                    self.M3.step1(speed)
                    self.M3.step2(speed)
                    self.M3.step3(speed)
                    self.M3.step4(speed)
                    steps=steps-1
            if richtung == "l":
                while steps:
                    self.M3.step1(speed)
                    self.M3.step4(speed)
                    self.M3.step3(speed)
                    self.M3.step2(speed)
                    steps=steps-1


