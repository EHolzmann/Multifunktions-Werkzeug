import RPi.GPIO as GPIO
from time import sleep 
import math 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


TIMEQUICK=0.004
TIMESLOW=0.07

class Motor:
    def __init__ (self,v,x,y,z):
        self.A=v # WHITE
        self.B=x # RED
        self.C=y # BLUE
        self.D=z # YELLOW
        
    def setup(self):
        GPIO.setup(self.A,GPIO.OUT)
        GPIO.setup(self.B,GPIO.OUT)
        GPIO.setup(self.C,GPIO.OUT)
        GPIO.setup(self.D,GPIO.OUT)
        GPIO.setup(self.A,False)
        GPIO.setup(self.B,False)
        GPIO.setup(self.C,False)
        GPIO.setup(self.D,False)
    	GPIO.setup(20, GPIO.OUT)
    	GPIO.setup(20, True)
    	GPIO.setup(12, GPIO.OUT)
    	GPIO.setup(12, True)
    	GPIO.setup(7, GPIO.OUT)
    	GPIO.setup(7, True)

    def gpio_einstellung_m(self,a,b,c,d):
        GPIO.output(self.A,a)
        GPIO.output(self.B,b)
        GPIO.output(self.C,c)
        GPIO.output(self.D,d)

    def step1(self,speed):
        self.gpio_einstellung_m(1,0,1,0)
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
        self.gpio_einstellung_m(0,1,0,1)
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

    def step14(self,speed):
        self.gpio_einstellung_m(1,0,0,0)
        if speed == 1:
            sleep(TIMEQUICK)
        elif speed == 2:
            sleep(TIMESLOW)

    def step43(self,speed):
        self.gpio_einstellung_m(0,0,0,1)
        if speed == 1:
            sleep(TIMEQUICK)
        elif speed == 2:
            sleep(TIMESLOW)

    def step32(self,speed):
        self.gpio_einstellung_m(0,1,0,0)
        if speed == 1:
            sleep(TIMEQUICK)
        elif speed == 2:
            sleep(TIMESLOW)

    def step21(self,speed):
        self.gpio_einstellung_m(0,0,1,0)
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
        
# distance Angabe in mm // Kleinste translatorische Bewegung 4mm         
        
    def vorwaertsstep(self,distance,speed):
        y=distance // 4
        z=distance % 4
        if z < 2:
            z=0
        else:
            z=1
        distance=y+z
        while distance:
            self.M1.step1(speed)
            self.M2.step3(speed)
    	    self.M1.step14(speed)
    	    self.M2.step43(speed)
            self.M1.step4(speed)
            self.M2.step4(speed)
    	    self.M1.step43(speed)
    	    self.M2.step14(speed)
            self.M1.step3(speed)
            self.M2.step1(speed)
    	    self.M1.step32(speed)
    	    self.M2.step21(speed)
            self.M1.step2(speed)
            self.M2.step1(speed)
    	    self.M1.step21(speed)
    	    self.M2.step14(speed)
            #self.M1.step1(speed)
	    distance=distance-1
        self.stopradantrieb()
    
    def rueckwaertsstep(self,distance,speed):
        y=distance // 4
        z=distance % 4
        if z < 2:
            z=0
        else:
            z=1
        distance=y+z
        while distance:
            self.M1.step1(speed)
            self.M2.step1(speed)
    	    self.M1.step21(speed)
    	    self.M2.step14(speed)
            self.M1.step2(speed)
            self.M2.step4(speed)
    	    self.M1.step32(speed)
    	    self.M2.step43(speed)
            self.M1.step3(speed)
            self.M2.step3(speed)
    	    self.M1.step43(speed)
    	    self.M2.step32(speed)
            self.M1.step4(speed)
            self.M2.step2(speed)
    	    self.M1.step14(speed)
    	    self.M2.step21(speed)
            distance=distance-1
        self.stopradantrieb()
    
    def linksdrehen(self,distance,speed):
        y=distance // 4
        z=distance % 4
        if z < 2:
            z=0
        else:
            z=1
        distance=y+z
        while distance:
            self.M1.step1(speed)
            self.M2.step1(speed)
    	    self.M1.step14(speed)
    	    self.M2.step14(speed)
            self.M1.step4(speed)
            self.M2.step4(speed)
    	    self.M1.step43(speed)
    	    self.M2.step43(speed)
            self.M1.step3(speed)
            self.M2.step3(speed)
    	    self.M1.step32(speed)
    	    self.M2.step32(speed)
            self.M1.step2(speed)
            self.M2.step2(speed)
    	    self.M1.step21(speed)
    	    self.M2.step21(speed)
            distance=distance-1
        self.stopradantrieb()
        
    def rechtsdrehen(self,distance,speed):
        y=distance // 4
        z=distance % 4
        if z < 2:
            z=0
        else:
            z=1
        distance=y+z
        while distance:
            self.M1.step1(speed)
            self.M2.step1(speed)
    	    self.M1.step21(speed)
    	    self.M2.step21(speed)
            self.M1.step2(speed)
            self.M2.step2(speed)
    	    self.M1.step32(speed)
    	    self.M2.step32(speed)
            self.M1.step3(speed)
            self.M2.step3(speed)
    	    self.M1.step43(speed)
    	    self.M2.step43(speed)
            self.M1.step4(speed)
            self.M2.step4(speed)
    	    self.M1.step14(speed)
    	    self.M2.step14(speed)
            distance=distance-1
        self.stopradantrieb()
    
    def hubhoch(self,distance,speed):
        y=distance // 4
        z=distance % 4
        if z < 2:
            z=0
        else:
            z=1
        distance=y+z
        while distance:
            self.M3.step1(speed)
    	    self.M3.step14(speed)
            self.M3.step4(speed)
    	    self.M3.step43(speed)
            self.M3.step3(speed)
    	    self.M3.step32(speed)
            self.M3.step2(speed)
    	    self.M3.step21(speed)
            distance=distance-1
                
    def hubrunter(self,distance,speed):
        y=distance // 4
        z=distance % 4
        if z < 2:
            z=0
        else:
            z=1
        distance=y+z
        while distance:
            self.M3.step3(speed)
    	    self.M3.step43(speed)
            self.M3.step4(speed)
    	    self.M3.step14(speed)
            self.M3.step1(speed)
    	    self.M3.step21(speed)
            self.M3.step2(speed)
    	    self.M3.step32(speed)
            distance=distance-1
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
                    self.M3.step3(speed)
                    self.M3.step4(speed)
                    self.M3.step1(speed)
                    self.M3.step2(speed)
                    steps=steps-1
            if richtung == "l":
                while steps:
                    self.M3.step1(speed)
                    self.M3.step4(speed)
                    self.M3.step3(speed)
                    self.M3.step2(speed)
                    steps=steps-1

