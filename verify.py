import os
import time
import io

import RPi.GPIO as GPIO
from picamera import PiCamera
import json

# Import other files
import picscreen
import led
import buzzer
import button
from button import Button
import image_process
import code_reader
import fingerprint_reader
import certificate_verification
import base64_convertor

# working directory
CWD_PATH = os.getcwd()

# important top-level constants
QRCODE_READ_TIMEOUT = 20
FACE_VERIFICATION_TIMEOUT = 20
FINGERPRINT_VERIFICATION_TIMEOUT = 20
BUTTON_PRESS_TIMEOUT = 10

#Debug
DEBUG_FLAG = False
PROCESS_FLAG = False

def cleanup(camera):
    GPIO.cleanup()
    camera.close()
    
def main():
    camera = PiCamera()
    # Camera warm-up time
    time.sleep(2)
    camera.vflip = True

    while True:
        print("Welcome to the ID verification service")
        picscreen.start()
        button.wait_for_button_press([Button.START])
        verified = False

        #Scan QR code
        quitFlag = False
        button_pressed = None
        while True:
            picscreen.step_one_start()
            code_data = code_reader.read_code(camera, QRCODE_READ_TIMEOUT)
            if code_data != None:
                print("-->QRCode Scanned")
                break
            else:
                #timeout
                picscreen.step_one_timeout()
                button_pressed = button.wait_for_button_press([Button.TRYAGAIN,Button.QUIT], BUTTON_PRESS_TIMEOUT)
                if button_pressed == button.QUIT:
                    quitFlag = True
                    break
        if quitFlag == True:
            continue

        #Verify QR code content and certificate authenticity
        picscreen.step_one_processing()
        valid, cert_str = certificate_verification.verify_cert_url(code_data)
        if valid:
            print("-->Certificate Verified")
        else:
            buzzer.failSound()
            picscreen.step_one_fail()
            button_pressed = button.wait_for_button_press([Button.TRYAGAIN,Button.QUIT], BUTTON_PRESS_TIMEOUT)
            time.sleep(5)
            continue
        cert_data = json.loads(cert_str)["data"]
        #QR Code Certificate Verification Success
        picscreen.step_one_success()
        buzzer.successSound()
       
        #Capture Image and do Image Cloud Verification
        quitFlag = False
        while True:
            #Fetch base Image from QR code
            if DEBUG_FLAG:
                test_image_path = os.path.join(CWD_PATH, "test3.jpg")
                base_image_stream = open(test_image_path, 'r+b')        
            else:
                base_image_b64 = cert_data["photo"].split(":string:")[1]
                base_image = base64_convertor.base64_to_byte(base_image_b64)
                if PROCESS_FLAG:
                    outfile = open("decoded_base.jpg", 'w+b')
                    outfile.write(base_image)
                    outfile.close()
                base_image_stream = io.BytesIO(base_image)

            picscreen.step_two_start()
            verified = image_process.image_id_verification(base_image_stream, camera, FACE_VERIFICATION_TIMEOUT)
            print("-->image verified: {}".format(verified))
            if not verified:
                picscreen.step_two_timeout()
                button_pressed = button.wait_for_button_press([Button.TRYAGAIN,Button.QUIT], BUTTON_PRESS_TIMEOUT)
                if button_pressed != Button.QUIT:
                    continue
                quitFlag = True
                break
            #Image Verification Success
            picscreen.step_two_success()
            buzzer.successSound()
            break
        if quitFlag:
            continue

        #Fetch and Decode Fingerprint data from QR code
        if DEBUG_FLAG:
            test_fingerprint_path = os.path.join(CWD_PATH, "test.fingerprint")
            base_fingerprint_file = open(test_fingerprint_path, 'r+b')
            base_fingerprint = list(bytearray(base_fingerprint_file.read()))
        else:
            base_fingerprint_b64 = cert_data["fingerprint"].split(":string:")[1]
            base_fingerprint_bytearray = base64_convertor.base64_to_byte(base_fingerprint_b64)
            base_fingerprint = list(base_fingerprint_bytearray)
            if PROCESS_FLAG:
                outfile = open("decoded_base_b64.fingerprint", 'w')
                outfile.write(base_fingerprint_b64)
                outfile.close()
                outfile = open("decoded_base_bytes.fingerprint", 'w+b')
                outfile.write(base_fingerprint_bytearray)
                outfile.close()
                outfile = open("decoded_base.fingerprint", 'w+b')
                outfile.write(base_image)
                outfile.close()

        #Scan Fingerprint and do Image Cloud Verification
        quitFlag = False
        while True:
            picscreen.step_three_start()
            time.sleep(2)
            picscreen.step_three_indexfinger()
            verified = fingerprint_reader.verify_fingerprint(base_fingerprint, FINGERPRINT_VERIFICATION_TIMEOUT)
            print("-->fingerprint verified: {}".format(verified))
            if not verified:
                picscreen.step_three_timeout()
                button_pressed = button.wait_for_button_press([Button.TRYAGAIN,Button.QUIT], BUTTON_PRESS_TIMEOUT)
                if button_pressed != Button.QUIT:
                    continue
                quitFlag = True
                break
            break
        if quitFlag:
            continue
        
        #Final Verification Success
        picscreen.step_three_success()
        buzzer.successSound()
        time.sleep(2)
        picscreen.alldone()

        #wait for next round
        #input_text = input("Verification success, press q to exist, press any other key to continue")
        #if input_text == "q":
        #    break
        print("Verification success")
        time.sleep(5)
    cleanup(camera)

if __name__ == "__main__":
    main()