import RPi.GPIO as GPIO
import time

LedPin = 27 #Pin13

#def setup():
GPIO.setwarnings(False)
if GPIO.getmode() != GPIO.BCM:
	GPIO.setmode(GPIO.BCM) # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.LOW)





# Final LED:
def cameraLEDon():
    GPIO.output(LedPin, GPIO.HIGH)

def cameraLEDoff():
    GPIO.output(LedPin, GPIO.LOW)

def cameraLED():
    cameraLEDon()
    time.sleep(5)
    cameraLEDoff()






def destroy():
	GPIO.output(LedPin, GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':		# Program start from here
    try:
        cameraLED()
    except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destory()
    finally:
        GPIO.cleanup() # cleanup all GPIO