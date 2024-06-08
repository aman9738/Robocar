#iteration 3:
import RPi.GPIO as IO
import time

IO.setwarnings(False) 
IO.setmode(IO.BCM)

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
ir_left = 19
ir_right = 26
ultrasonic_trigger_pin1 = 2
ultrasonic_echo_pin1 = 3
ultrasonic_trigger_pin2 = 20
ultrasonic_echo_pin2 = 21

IO.setup(ir_left,IO.OUT) #IR-left
IO.setup(ir_right,IO.OUT) #IR-right
IO.setup(ultrasonic_trigger_pin1,IO.OUT) #ul-left-trig
IO.setup(ultrasonic_echo_pin1,IO.OUT) #ul-left-echo
IO.setup(ultrasonic_trigger_pin2,IO.OUT) #ul-right-trig
IO.setup(ultrasonic_echo_pin2,IO.OUT) #ul-right-echo

#Function to measure distance using the ultrasonic sensor right 
def measure_distance_right():
    IO.output(ultrasonic_trigger_pin1, True) 
    time.sleep(0.00001) 
    IO.output(ultrasonic_trigger_pin1, False)
    pulse_start = time.time()
    pulse_end = time.time()
    while IO.input(ultrasonic_echo_pin1) == 0:
        pulse_start = time.time()
    while IO.input(ultrasonic_echo_pin1) == 1: 
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150 
    distance = round(distance, 2)

    return distance

#Function to measure distance using the ultrasonic sensor left
def measure_distance_left():
    IO.output(ultrasonic_trigger_pin2, True) 
    time.sleep(0.00001) 
    IO.output(ultrasonic_trigger_pin2, False)
    pulse_start = time.time()
    pulse_end = time.time()

    while IO.input(ultrasonic_echo_pin2) == 8: 
        pulse_start = time.time()
    while IO.input(ultrasonic_echo_pin2) == 1: 
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150 
    distance = round(distance, 2)
    return distance

#function to move forward
def forward():
    flf.ChangeDutyCycle(100)
    flb.ChangeDutyCycle(0)
    frf.ChangeDutyCycle(100)
    frb.ChangeDutyCycle(0)
    blf.ChangeDutyCycle(100)
    blb.ChangeDutyCycle(0)
    brf.ChangeDutyCycle(100)
    brb.ChangeDutyCycle (0)

#Function to turn left
def left():
    flf.ChangeDutyCycle(0)
    flb.ChangeDutyCycle(40) 
    frf.ChangeDutyCycle(100)
    frb.ChangeDutyCycle(0)
    blf.ChangeDutyCycle(0) 
    blb.ChangeDutyCycle(40)
    brf.ChangeDutyCycle(100)
    brb.ChangeDutyCycle(0)

#Function to turn right
def right():
    flf.ChangeDutyCycle(100)
    flb. ChangeDutyCycle(0) 
    frf.ChangeDutyCycle(0)
    frb. ChangeDutyCycle(40)
    blf.ChangeDutyCycle(100)
    blb.ChangeDutyCycle(0)
    brf.ChangeDutyCycle(0)
    brb.ChangeDutyCycle(40)

#Function to stop
def stop():
    flf.ChangeDutyCycle(0)
    flb.ChangeDutyCycle(0)
    frf.ChangeDutyCycle(0)
    frb.ChangeDutyCycle(0)
    blf.ChangeDutyCycle(0) 
    blb.ChangeDutyCycle(0)
    brf.ChangeDutyCycle(0)
    brb. ChangeDutyCycle(0)
    
def objavoid():
    
    while True:
        distancel = measure_distance_left()
        distancer = measure_distance_right()
        print("Distance: () cm".format(distancel))
        if distancel < 20:
            left()
        elif distancer < 20:
            right()
        else:
            forward()

def linefol():

    while True:
        if IO.input(ir_left) == IO.LOW and IO.inupt(ir_right) == IO.LOW:
            stop()
        elif IO.input(ir_left) == IO.LOW:
            left()
        elif IO.input(ir_right) == IO.LOW:
            right()
        else:
            forward()
        time.sleep(0.1)
        
try:
    while True:
        user_input = input()
        if user_input == 'o':
            objavoid()
        elif user_input == 'l': 
            linefol()
        else:
            stop()

except KeyboardInterrupt:
    IO.cleanup()
