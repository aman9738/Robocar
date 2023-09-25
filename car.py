import RPi.GPIO as IO

import time

IO.setwarnings(False)
IO.setmode(IO.BCM)


#12,27,5,6
IO.setup(25,IO.OUT)
IO.setup(8,IO.OUT)

IO.setup(4,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(14,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(17,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Left terminal B

IO.setup(12,IO.OUT) #GPIO 12 -> Motor 1 terminal A
IO.setup(27,IO.OUT) #GPIO 27 -> Motor 1 terminal B
IO.setup(5,IO.OUT) #GPIO 5 -> Motor Left terminal A
IO.setup(6,IO.OUT) #GPIO 6 -> Motor Left terminal B

en1=25
en2=8

IO.output(en1,IO.LOW)
IO.output(en2,IO.LOW)
IO.output(4,True) #1A+
IO.output(14,True) #1B-
IO.output(17,True) #2A+
IO.output(18,True)
IO.output(12,True) #1A+
IO.output(27,True) #1B-
IO.output(5,True) #2A+
IO.output(6,True)

p=IO.PWM(en1,1000)
p.start(100)
q=IO.PWM(en2,1000)
q.start(100)

while True:
        user_input = input()
        if user_input == 'w':
            #back-right
            IO.output(4,True) #1A+
            IO.output(14,False) #1B-
            #back-left
            IO.output(17,True) #2A+
            IO.output(18,False)
            #front-right
            IO.output(12,True) #1A+
            IO.output(27,False) #1B-
            #front-left
            IO.output(5,True) #2A+
            IO.output(6,False)
        
        elif user_input == 's':
            IO.output(4,False)
            IO.output(14,True)
            IO.output(17,False)
            IO.output(18,True)
            IO.output(12,False) #1A+
            IO.output(27,True) #1B-
            IO.output(5,False) #2A+
            IO.output(6,True)

        elif user_input == 'a':
            IO.output(4,True) #1A+
            IO.output(14,False) #1B-
            IO.output(17,False) #2A+
            IO.output(18,True)
            IO.output(12,False) #1A+
            IO.output(27,True) #1B-
            IO.output(5,True) #2A+
            IO.output(6,False)
        
        elif user_input == 'd':
            IO.output(4,False) #1A+
            IO.output(14,True) #1B-
            IO.output(17,True) #2A+
            IO.output(18,False)
            IO.output(12,True) #1A+
            IO.output(27,False) #1B-
            IO.output(5,False) #2A+
            IO.output(6,True)

        
        elif user_input == 'c' :
            IO.output(4,True) #1A+
            IO.output(14,True) #1B-
            IO.output(17,True) #2A+
            IO.output(18,True)
            IO.output(12,True) #1A+
            IO.output(27,True) #1B-
            IO.output(5,True) #2A+
            IO.output(6,True)
            
        elif user_input == 'l':
            p.ChangeDutyCycle(25)
            q.ChangeDutyCycle(25)

        elif user_input == 'm':
            p.ChangeDutyCycle(50)
            q.ChangeDutyCycle(50)

        elif user_input == 'h':
            p.ChangeDutyCycle(100)
            q.ChangeDutyCycle(100)


IO.cleanup()
