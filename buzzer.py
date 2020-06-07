import RPi.GPIO as GPIO
import time

from pygame import mixer

#BuzzerPin = 17    # pin11

#SPEED = 1 

# List of tone-names with frequency
# TONES = {"c6":1047,
# 	"b5":988,
# 	"a5":880,
# 	"g5":784,
# 	"f5":698,
# 	"e5":659,
# 	"eb5":622,
# 	"d5":587,
# 	"c5":523,
# 	"b4":494,
# 	"a4":440,
# 	"ab4":415,
# 	"g4":392,
# 	"f4":349,
# 	"e4":330,
# 	"d4":294,
# 	"c4":262}

# # Song is a list of tones with name and 1/duration. 16 means 1/16
# SONG =	[
# 	["b4",16],["c5",16],
# 	["d5",16],["c6",8]
# 	]

# #def setup():
GPIO.setwarnings(False)
# if GPIO.getmode() != GPIO.BCM:
# 	GPIO.setmode(GPIO.BCM)
# GPIO.setup(BuzzerPin, GPIO.OUT)
# GPIO.output(BuzzerPin, GPIO.LOW)

# def playTone(p,tone):
#         # calculate duration based on speed and tone-length
# 	duration = (1./(tone[1]*0.25*SPEED))

# 	if tone[0] == "p": # p => pause
# 		time.sleep(duration)
# 	else: # let's rock
# 		frequency = TONES[tone[0]]
# 		p.ChangeFrequency(frequency)
# 		p.start(0.5)
# 		time.sleep(duration)
# 		p.stop()




# # Final sound:
# def successSound():
# 	p = GPIO.PWM(BuzzerPin, 440)
# 	p.start(0.5)
# 	for t in SONG:
# 		playTone(p,t)

# def beep():
#     GPIO.output(BuzzerPin, GPIO.HIGH)
#     time.sleep(0.2)

mixer.init()

def successSound():
	mixer.music.load('success.mp3')
	mixer.music.play()

def failSound():
	mixer.music.load('fail.mp3')
	mixer.music.play()


def destroy():
	pass
	#GPIO.cleanup()                     # Release resource

if __name__ == '__main__':		# Program start from here
	successSound()
	time.sleep(10)
	# try:
	# 	successSound()
	# except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	# 	destory()
	# finally:
    #      GPIO.cleanup() # cleanup all GPIO