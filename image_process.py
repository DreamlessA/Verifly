# Import other files
import led
import picscreen
import buzzer

# Import general packages
import numpy as np
import argparse
import sys, os, time
from time import sleep
import dlib


# Import packages for image capture
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

# Import other dependencies
import io
import requests
import matplotlib.pyplot as plt
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

# This is needed since the working directory is the object_detection folder.
sys.path.append('..')

# Setup Azure face recognition service
KEY = os.environ['COGNITIVE_SERVICE_KEY']
ENDPOINT = os.environ['COGNITIVE_SERVICE_ENDPOINT']
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Setup PicCamera
CAP_WIDTH = 2592
CAP_HEIGHT = 1952

#import Constants
FACE_VERIFICATION_THRESHOLD = 0.6

#Debug
DEBUG_FLAG = False

# Components
def face_detection(image_stream):
    faces = face_client.face.detect_with_stream(image_stream, recognition_model='recognition_02', detection_model='detection_02')
    print("number of face: {}".format(len(faces)))
    if len(faces) == 1:
        print("face id: {}".format(faces[0].face_id))
        print("face location: x{} y{}".format(faces[0].face_rectangle.left,faces[0].face_rectangle.top))
        return faces[0].face_id
    else:
        return None

def face_verification(image_id1, image_id2):
    verify_result = face_client.face.verify_face_to_face(image_id1, image_id2)
    print('Confidence: {}'.format(verify_result.confidence))
    return verify_result.confidence >= FACE_VERIFICATION_THRESHOLD

def image_capture(camera):
    #image_stream = io.BytesIO()
    #camera.capture(image_stream, 'jpeg')
    with PiRGBArray(camera) as raw:
        #led.cameraLEDon()
        camera.capture(raw, format='bgr')
        #led.cameraLEDoff()
        image = raw.array

        #Diplay for debug 
        if DEBUG_FLAG: 
            image_display = cv2.resize(image, (1080, 720)) 
            cv2.namedWindow('imageWindow', cv2.WINDOW_AUTOSIZE)
            cv2.imshow("imageWindow",image_display)
            cv2.waitKey(0)
            cv2.destroyAllWindows()    

        return image

# takes bgr numpy image array
def build_image_stream(image):
    ret,buf = cv2.imencode('.jpg', image)
    image_stream = io.BytesIO(buf)    
    return image_stream

# takes rgb numpy image array
# use dlib hog detector for fast face detection
def dlib_face_detection(image_data):
    detector = dlib.get_frontal_face_detector()
    dets = detector(image_data, 1)
    # note: det,score,type of face = detector.run(img, scale, threshold(negative = lower threshold))
    # dets, scores, idx = detector.run(img, 1, -1)
    if DEBUG_FLAG :
        print("Number of faces detected: {}".format(len(dets)))
        for i, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                i, d.left(), d.top(), d.right(), d.bottom()))
    return len(dets) > 0

# takes greyscale bgr numpy image array
def cv2_face_detection(image_data):
    CWD_PATH = os.getcwd()
    face_cascade_path = os.path.join(CWD_PATH, "haarcascade_frontalface_default.xml")
    #face_cascade_path = os.path.join(CWD_PATH, "haarcascade_eye_tree_eyeglasses.xml")
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    print(face_cascade_path)
    faces = face_cascade.detectMultiScale(
        image_data,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    
    # note: det,score,type of face = detector.run(img, scale, threshold(negative = lower threshold))
    # dets, scores, idx = detector.run(img, 1, -1)
    if DEBUG_FLAG : 
        print("Number of faces detected: {}".format(len(faces)))  
        for i, d in enumerate(faces):   
            x,y,w,h = d
            print("Detection {}: X: {} Y: {} Width: {} Height: {}".format(
                i, x, y, w, h))
    return len(faces) > 0

#return (result,timeout)
def image_id_verification(base_image, camera, timeout):	
    # Setup
    camera.resolution = (CAP_WIDTH,CAP_HEIGHT)
    camera.framerate = 10

    pre_time = time.time()
    base_image_id = face_detection(base_image)
    post_time = time.time()
    print("->base image processed, taking {}".format(post_time-pre_time))

    verified = False
    start_time = time.time() 
    while time.time() - start_time < timeout:
        pre_time = time.time()
        image_bgr = image_capture(camera)
        post_time = time.time()
        print("->image captured, taking {}".format(post_time-pre_time)) 
        
        pre_time = time.time()  
        image_gray_small = cv2.resize(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY),(320,240))
        image_small_stream = build_image_stream(image_gray_small)   
        capture_face_id = face_detection(image_small_stream)
        post_time = time.time()
        print("->captured image pre-processed, taking {}".format(post_time-pre_time)) 

        if capture_face_id != None:
            picscreen.step_two_processing()
            pre_time = time.time() 
            image_stream = build_image_stream(image_bgr)          
            capture_image_id = face_detection(image_stream)
            post_time = time.time()
            print("->captured image processed, taking {}".format(post_time-pre_time)) 

            if capture_image_id != None:            
                start_time = time.time()
                pre_time = time.time()
                verified = face_verification(base_image_id, capture_image_id)
                post_time = time.time()
                print("->captured image verification done, taking {}".format(post_time-pre_time))
                if not verified:
                    picscreen.step_two_fail()
                    buzzer.failSound()
                    start_time = time.time() 
        else:
            print("->captured image no valid face, verification skipped")

        if verified:
            return True

    return False