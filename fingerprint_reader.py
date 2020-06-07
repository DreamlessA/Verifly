# Import other files
import picscreen
import buzzer
# modified library
import fingerprint as adafruit_fingerprint

import board
import time
#import busio
import serial
from digitalio import DigitalInOut, Direction
#import adafruit_fingerprint


led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

#uart = busio.UART(board.TX, board.RX, baudrate=57600)

# If using with a computer such as Linux/RaspberryPi, Mac, Windows with USB/serial converter:
#import serial
#uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=5)

# If using with Linux/Raspberry Pi and hardware UART:
#import serial
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=5)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

#Debug
DEBUG_FLAG = False

#import Constants
FINGERPRINT_VERIFICATION_THRESHOLD = 50

##################################################
def fingerprint_to_file():
    print("Place finger on sensor")
    print("Scaning finger", end="", flush=True)
    while True:
        res_code = finger.get_image()
        if res_code == adafruit_fingerprint.OK:
            break
        elif res_code != adafruit_fingerprint.NOFINGER:
            print("error")
            exit
        print(".", end="", flush=True)
    finger.image_2_tz(1)
    model = finger.get_model(1)
    #print(type(model))
    f = open("test.fingerprint","w+b")
    f.write(bytearray(model))
    print("successfully stored the fingerprint")


#return (result,timeout)
def verify_fingerprint(ref_data, timeout):
    print("Place finger on sensor")
    print("Scaning finger", end="", flush=True)
    stage = 0

    notmove_flag = True
    start_time = time.time() 
    while time.time() - start_time < timeout:
        if time.time() - start_time > timeout/2 and notmove_flag:
            notmove_flag = False
            picscreen.step_three_notmove()

        if stage == 0:
            if DEBUG_FLAG :
                print("fingerprint verification stage 1 get_image")
            try:
                res_code = finger.get_image()
            except Exception as e:
                print("Communication error")
                raise e 

            if res_code == adafruit_fingerprint.OK:
                print("Fingerprint taken, Processing...")
                stage = 1
            elif res_code == adafruit_fingerprint.NOFINGER:
                print(".", end="", flush=True)
            elif res_code == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error, Please try again")
                print("Place finger on sensor")
            else:
                print("Other error, Please try again")
                print("Place finger on sensor")

        if stage == 1:
            if DEBUG_FLAG :
                print("fingerprint verification stage 1 image_to_tz")           
            try:
                res_code = finger.image_2_tz(1)
            except Exception as e:
                print("Communication error")
                raise e         

            if res_code == adafruit_fingerprint.OK:
                print("Fingerprint processed, Matching...")
                stage = 2
            else:           
                if res_code == adafruit_fingerprint.IMAGEMESS or res_code == adafruit_fingerprint.FEATUREFAIL:
                    print("Unable to process Fingerprint, Please try again")
                    print("Place finger on sensor")
                    stage = 0
                elif res_code == adafruit_fingerprint.INVALIDIMAGE:
                    print("Image invalid, Please try again")
                    print("Place finger on sensor")
                else:
                    print("Other error")
                    return False, False

        if stage == 2:
            if DEBUG_FLAG :
                print("fingerprint verification stage 2 load_model")   
         
            if DEBUG_FLAG :
                match_result = finger.load_model(ref_data,2)
            else:
                try:
                    res_code = finger.load_model(ref_data,2)
                except Exception as e:
                    print("Communication error")
                    raise e  

            if res_code == adafruit_fingerprint.OK:
                pass
            else:   
                raise Exception("Unable to upload Fingerprint")
            
            if DEBUG_FLAG:
                print("get_match")  

            if DEBUG_FLAG :
                match_confidence = finger.get_match()
            else:
                try:
                    match_confidence = finger.get_match()
                except Exception as e:
                    print("Communication error")
                    raise e
            
            print("Matching done with Confidence = {}".format(match_confidence))
            if match_confidence > FINGERPRINT_VERIFICATION_THRESHOLD:
                return True
            else:
                picscreen.step_three_fail()
                buzzer.failSound()
                time.sleep(2)
                stage = 0
                start_time = time.time() 

    return False

if __name__ == "__main__":
    fingerprint_to_file()