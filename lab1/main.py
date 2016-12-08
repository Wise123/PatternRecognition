import numpy as np
import cv,cv2
import os, shutil
import sys
from PIL import Image
import subprocess
index=[]
images=[]
text=[]
cascade = cv.Load('C:\\haarcascade_frontalface_alt.xml')
cascad = cv.Load('C:\\haarcascade_mcs_eyepair_big.xml')

#cascade = cv.Load('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
#cascad = cv.Load('/usr/local/share/OpenCV/haarcascades/haarcascade_mcs_eyepair_big.xml')

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
    photo="photo"
    text="text"
    sr=""
    res=image_path[7:]
    st=res.find(".")
    while st<len(res):
        sr=sr+res[st]
        st=st+1
    if ((sr=='.jpg') or (sr=='.jpeg') or (sr=='.raw') or (sr=='.tiff') or (sr=='.png') or (sr=='.gif')):
        return photo
    if ((sr=='.txt') or (sr=='.docx') or (sr=='.xlsx') or (sr=='.pptx') or (sr=='.rtf') or (sr=='.odt') or (sr=='.pdf')):
        return text
image_paths = [os.path.join('./pics', f) for f in os.listdir('./pics')]
for image_path in image_paths:
    resstr=""
    resstr=resstr+image_path
    images.append(image_path)
    if (detectFileType(image_path)=="text"):
        resstr=resstr+' it is text '
        text.append(resstr)
        break
    gray = Image.open(image_path)
    image = np.array(gray, 'uint8')
    if (detectImage(image) == True):
        resstr=resstr+' have face '
    if (detectEye(image) == True):
        resstr=resstr+' have eyes '
    if (detectFileType(image_path)=="photo"):
        resstr=resstr+' it is foto '
    index.append(resstr)
    resstr=""
for i in range(len(text)):
    index.append(text[i])
for i in range(len(index)):
    print(index[i])
number = input("enter a number: ")
subprocess.call(images[number], shell=True)