#31 = Trigger
#32 = input
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(31,GPIO.OUT)
#GPIO.output(7,0)

GPIO.setup(32,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
#time.sleep(0.1)

print("Started taking measurements")

try:
    while True:

        GPIO.output(31,0)
        time.sleep(0.1)
        GPIO.output(31,1)
        time.sleep(0.0001)
        GPIO.output(31,0)

        while GPIO.input(32)==0:


            start = time.time()

        while GPIO.input(32)==1:

            s1 = time.time()

        total_time = s1 - start

        distance = total_time*170

        distance_in_cm = distance*100
        if distance_in_cm>40:
        GPIO.output(3,1)
        time.sleep(0.1)
        GPIO.output(3,0)
        else:
        GPIO.output(35,1)
        time.sleep(0.1)
        GPIO.output(35,0)

        print("Distance of the Object is:" , distance_in_cm)



except:
print("Error")

finally:
GPIO.cleanup((31,32))