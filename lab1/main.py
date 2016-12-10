import numpy as np
import cv,cv2
import os, shutil
import sys
from PIL import Image
import subprocess
index=[]
images=[]

cascade = cv.Load(os.path.realpath('haarcascade_frontalface_alt.xml'))
cascad = cv.Load(os.path.realpath('haarcascade_mcs_eyepair_big.xml'))

def detectImage(image):
    bitmap = cv.fromarray(image)
    faces = cv.HaarDetectObjects(bitmap, cascade, cv.CreateMemStorage(0))
    if faces:
        for (x,y,w,h),n in faces:
            pass
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)
            return True
    else:
        return False
def detectEye(image):
    bitmap = cv.fromarray(image)
    faces = cv.HaarDetectObjects(bitmap, cascad, cv.CreateMemStorage(0))
    if faces:
        for (x,y,w,h),n in faces:
            pass
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)
            return True
    else:
        return False
def detectFileType (image_path):
    hsv = cv2.cvtColor(image_path, cv2.COLOR_BGR2HSV)
    dist = cv2.calcHist([hsv],[0],None,[256],[0,256])
    ras = cv.CalcEMD2(dist, CV_DIST_L1)
    if (res>1):
        return "schema"
image_paths = [os.path.join('./pics', f) for f in os.listdir('./pics')]
for image_path in image_paths:
    resstr=""
    resstr=resstr+image_path
    images.append(image_path)
    gray = Image.open(image_path)
    image = np.array(gray, 'uint8')
    if (detectImage(image) == True):
        resstr=resstr+' have face '
    if (detectEye(image) == True):
        resstr=resstr+' have eyes '
    if (detectFileType(image_path)=="schema"):
        resstr=resstr+' it is schema '
    index.append(resstr)
    resstr=""
for i in range(len(index)):
    print(index[i])
number = input("enter a number: ")
subprocess.call(images[number], shell=True)