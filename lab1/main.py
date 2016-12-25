import cv2
import os
index = []
images = []
text = []
face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')


def detectFileType (image):
    dist = cv2.calcHist([image],[0],None,[256],[0,256])
    prev = ''
    for i in dist:
        if prev == '':
            prev = i.real[0]
        else:
            if abs(prev-i.real[0]) > 10000.0:
                return 'schema'
            prev = i.real[0]
    return "photo"


def detectImage(image):
    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    if type(faces).__name__ == 'ndarray':
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
            return True
    else:
        return False


def detectEye(image):
    faces = eye_cascade.detectMultiScale(image, 1.3, 5)
    if type(faces).__name__ == 'ndarray':
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
            return True
    else:
        return False


put = './pics'
image_paths = [os.path.join(os.path.realpath(put), f) for f in os.listdir(put)]

for image_path in image_paths:
    resstr = ""
    resstr += image_path
    images.append(image_path)
    img = cv2.imread(image_path)
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        print(image_path + ' is not an image')
        continue

    if (detectImage(gray) == True):
        resstr = resstr + ' have face '
    if (detectEye(gray) == True):
        resstr = resstr + ' have eyes '
    if (detectFileType(gray) == "schema"):
        resstr = resstr + ' it is schema '

    index.append(resstr)
    resstr = ""

for i in range(len(index)):
    print(index[i])

number = int(input("enter a number: "))
print(images[number])

im = cv2.imread(images[number])
cv2.imshow('img',im)
cv2.waitKey(0)
cv2.destroyAllWindows()