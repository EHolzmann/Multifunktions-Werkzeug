import Plattform 
import Sensoren
import Antriebe2
import RPi.GPIO as GPIO
from time import sleep

#sicherheitsabstand = 0.1
#raddurchmesser = 0.65

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#hub = Antriebe.Motor(10,9,11,5)
#hub.setup()
#GPIO.setup(12, GPIO.OUT)
#GPIO.setup(12, True)

#try:
#	hub.step1(1)
#	hub.step2(1)
#	hub.step3(1)
#	hub.step4(1)
#except KeyBoardInterrupt:
#	hub.gpio_einstellung_m(0,0,0,0)
#test = Antriebe.Antrieb()
#test.hubhoch(2,2)
#sleep(2)
#test.hubrunter(1,2)
#test.vorwaertsstep(20,1)
#test.stophubantrieb()
#test.stopradantrieb()
pf = Plattform.Plattform(0.1,0.65)
pf.nachvorne(0.5,1)
#sleep(1)
#pf.armanheben()
#sleep(1)
#pf.linksrum(3,1)
#sleep(2)
#pf.nachvorne(0.2,1)
#sleep(1)
#pf.rechtsrum(3,1)
#sleep(1)
#pf.nachhinten(0.5,1)
#sleep(1)
#pf.piken()
#sleep(1)
#pf.armabsetzen()
#sleep(1)

