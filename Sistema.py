import numpy as np
import cv2
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import os
import statistics as stat
import time as t
import interfazButiaTelnet as Butia

#Cargamos el modulo detector de Rostros
predictor_caras = cv2.CascadeClassifier('predictor_caras.xml')

#Cargamos el modulo detector de Ojos
predictor_ojos = cv2.CascadeClassifier('predictor_ojos.xml')

#Cargamos nuestro modelo
model = load_model('modelo/modelo_horus.h5')

#Declaramos las dimenciones que tendran las imagenes con las que trataremos
dim = (128,128)

#Datos de conexion
HOST = '192.168.0.111'
PORT = 2009

#establecemos la conexion
Robot = Butia.connect(HOST,PORT)

def predict(ojos):
    x = load_img(ojos, target_size=dim)
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = model.predict(x)
    result = array[0]
    answer = np.argmax(result)
    return answer
pass

predicciones = [0,0,0]
i = 0

cap = cv2.VideoCapture(0)
ret, img = cap.read()

while ret:
    imagen_en_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = predictor_caras.detectMultiScale(imagen_en_gris, 1.3, 5)
    for (x,y,w,h) in faces:
        cara = imagen_en_gris[y:y+h, x:x+w]
        
        eyes = predictor_ojos.detectMultiScale(cara)
        if len(eyes) == 0:
            print("No se detectan Ojos")
        else:
            ex,ey,ew,eh = eyes[0]
            ojos = cara[ey:ey+ew,ex:ex+eh]
            ojos = cv2.resize(ojos, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow('img',ojos)
            cv2.imwrite('ojo.jpg',ojos)
            predicciones[i] = predict('ojo.jpg')
            i+=1
            if i == 3:
                i=0
                direccion = stat.mean(predicciones)
                Butia.mover(Robot,direccion)
    ret, img = cap.read()

cap.release()
cv2.destroyAllWindows()