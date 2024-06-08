#iteration 2:
import RPi.GPIO as IO
import time

IO.setwarnings(False) 
IO.setmode(IO.BCM)

IO.setup(2,IO.OUT)
IO.setup(3,IO.OUT)

IO.setup(17, IO.OUT)#front-left-forward
IO.setup(18,IO.OUT) #front-left-backward 
IO. setup(4, IO.OUT) #front-right-forward
IO.setup(14, IO.OUT) #front-right-backward

IO.setup(12, IO.OUT)#back-left-forward
IO.setup(27, IO.OUT) #back-right-forward
IO.setup(5, IO.OUT) #back-left-backward
IO.setup(6, IO.OUT)#back-right-backward

IO.output(17, True)
IO.output(18, True)
IO.output (4, True)
IO.output(14, True)
IO.output(12, True)
IO.output(27, True)
IO.output(5, True)
IO.output (6, True)

flf=IO.PWM(17,100)
flf.start(0)

flb=IO.PWM(18,100) 
flb.start(0)

frf=IO.PWM(4,100)
frf.start(0)

frb=IO.PWM(14,100)
frb.start(0)

blf-IO.PWM(12,100)
blf.start(0)

blb-IO.PWM(27,100)
blb.start(0)

brf=IO.PWM(5,200)
brf.start(0)

brb=IO.PM(6,100)
brb.start(0)

while True:

    if(IO.input(2)==False and IO.input(3)==False): #both will move forward
        flf.ChangeDutyCycle(100)
        flb.ChangeDutyCycle(0)
        frf.ChangeDutyCycle(100)
        frb.ChangeDutyCycle(0)
        blf.ChangeDutyCycle(100)
        blb.ChangeDutyCycle(0)
        brf.ChangeDutyCycle(100)
        brb.ChangeDutyCycle(0)

    elif(IO.input(2)==True and IO.input(3)==False): #turn right
        flf.ChangeDutyCycle(100)
        flb.ChangeDutyCycle(0)
        frf. ChangeDutyCycle(60) 
        frb.ChangeDutycycle(0)
        blf.ChangeDutyCycle(100)
        blb.ChangeDutyCycle(0)
        brf.ChangeDutyCycle(60)
        brb.ChangeDutyCycle(0)

    elif(IO.input(2)==False and IO.input(3)==True):
        flf.ChangeDutyCycle(60)
        flb.ChangeDutyCycle(0)
        frf.ChangeDutyCycle(100)
        frb.ChangeDutyCycle(0)
        blf.ChangeDutyCycle(60)
        blb.ChangeDutyCycle(0) 
        brf.ChangeDutyCycle(100)
        brb.ChangeDutycycle(0)
    else: #stay still
        flf.ChangeDutyCycle(0)
        flb.ChangeDutycycle (0) 
        frf.ChangeDutyCycle(0)
        frb.ChangeDutycycle(0)
        blf.ChangeDutyCycle(0) 
        b1b.ChangeDutyCycle(0)
        brf.ChangeDutyCycle(0)
        brb.ChangeDutyCycle(0)
        
IO.cleanup()