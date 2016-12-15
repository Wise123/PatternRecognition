import cv2
import os
index = []
images = []
text = []
face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')

def detectImage(image):
    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    if type(faces).__name__ == 'ndarray':
        for (x, y, w, h) in faces:
            pass
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
            return True
    else:
        return False


def detectEye(image):
    faces = eye_cascade.detectMultiScale(image, 1.3, 5)
    if type(faces).__name__ == 'ndarray':
        for (x, y, w, h) in faces:
            pass
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


    if detectImage(gray):
        resstr += ' has face'

    if detectEye(gray):
        resstr += ' has eyes'

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