import numpy as np
import cv2
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import os
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('cascade.xml')

dim = (128,128)
model = load_model('modelo/modelo_horus.h5')
model.summary()


cap = cv2.VideoCapture(0)
ret, img = cap.read()

blinking = 0
center = 1
left = 2
right = 3

def predict(file):
    x = load_img(file, target_size=dim)
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = model.predict(x)
    result = array[0]
    answer = np.argmax(result)
    
    if answer == blinking:
        print("pred: Cierro")
    elif answer == center:
        print("pred: Centro")
    elif answer == left:
        print("pred: Izq")
    elif answer == right:
        print("pred: Der")

    
    return answer
while ret:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eye = img
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            print("dou")
        else:
            ex,ey,ew,eh = eyes[0]
            ojos = roi_gray[ey:ey+ew,ex:ex+eh]
            ojos = cv2.resize(ojos, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow('img',ojos)
            cv2.imwrite('ojo.jpg',ojos)
            predict('ojo.jpg')

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    ret, img = cap.read()

cap.release()
cv2.destroyAllWindows()

# cd Facultad/TR