import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

button = 23  #Pin16
count = 0

#def setup():
GPIO.setwarnings(False)
if GPIO.getmode() != GPIO.BCM:
	GPIO.setmode(GPIO.BCM)
R,G,B = 15,14,18  #Pin10,8,12

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
pwmR = GPIO.PWM(R, 50)
pwmG = GPIO.PWM(G, 50)
pwmB = GPIO.PWM(B, 50)
 
pwmR.start(0)
pwmG.start(0)
pwmB.start(0)





# Final rgb led:
def rgbon():
    t = 0.2
    while True:
        # 红色灯全亮，蓝灯，绿灯全暗（红色）
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        if GPIO.input(button) == 0:
            print("0")
            break
         
        # 绿色灯全亮，红灯，蓝灯全暗（绿色）
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        if GPIO.input(button) == 0:
            print("0")
            break
         
        # 蓝色灯全亮，红灯，绿灯全暗（蓝色）
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)
         
        # 红灯，绿灯全亮，蓝灯全暗（黄色）
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        if GPIO.input(button) == 0:
            print("0")
            break
         
        # 红灯，蓝灯全亮，绿灯全暗（洋红色）
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        if GPIO.input(button) == 0:
            print("0")
            break
         
        # 绿灯，蓝灯全亮，红灯全暗（青色）
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        if GPIO.input(button) == 0:
            print("0")
            break

def rgboff():
    pwmR.stop()
    pwmG.stop()
    pwmB.stop()







def destroy():
    GPIO.output(button, GPIO.HIGH)
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':		# Program start from here
    #setup()
    try:
        rgbon()
        rgboff()
    except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destory()
    finally:
        GPIO.cleanup() # cleanup all GPIO