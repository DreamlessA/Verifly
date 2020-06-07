# Import other files
import picscreen

from pyzbar.pyzbar import decode
from PIL import Image
import time, io
import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera

# Setup PicCamera
CAP_WIDTH = 1088
CAP_HEIGHT = 720


#Debug
DEBUG_FLAG = False

def read_code(camera, timeout):
    #Setup
    camera.resolution = (CAP_WIDTH,CAP_HEIGHT)
    camera.framerate = 10

    print("Place QR code in front of camera")
    start_time = time.time()
    try:        
        #stream = io.BytesIO()
        rawCapture = PiRGBArray(camera, size=(CAP_WIDTH,CAP_HEIGHT))
        rawCapture.truncate(0)

        maxbright_flag = True
        for frame in camera.capture_continuous(rawCapture, format="rgb"):
            if time.time() - start_time > timeout:
                break
            if time.time() - start_time > timeout/2 and maxbright_flag:
                maxbright_flag = False
                picscreen.step_one_maxbright()

            image_data = frame.array

            #Diplay for debug 
            if DEBUG_FLAG:
                image_bgr = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
                image_display = cv2.resize(image_bgr, (1080, 720)) 
                cv2.namedWindow('imageWindow', cv2.WINDOW_AUTOSIZE)
                cv2.imshow("imageWindow",image_display)
                cv2.waitKey(0)
                cv2.destroyAllWindows() 

            pre_time = time.time()
            image = Image.frombytes('RGB', (CAP_WIDTH,CAP_HEIGHT), image_data)
            decoded_data = decode(image)
            post_time = time.time()
            print("->Image Scanned, taking {}".format(post_time-pre_time))

            if len(decoded_data) > 0:
                if DEBUG_FLAG:
                    print(decoded_data)
                code_data, code_type, rect, polygon = decoded_data[0]
                if code_type=='QRCODE':
                    code_str = code_data.decode('ascii')
                if DEBUG_FLAG:
                    print(code_str)
                return(code_str)
            print(".", end="", flush=True)
            rawCapture.truncate(0)
    
    except Exception as e:
        raise e

    return None

if __name__ == "__main__":
    while True:
        print(read_code(PiCamera(), 10))