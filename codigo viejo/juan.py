import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

import numpy as np
import cv2
import os
import time

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

from tensorflow import keras

import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

longitud, altura = 128, 128
model = load_model('modelo/modelo.h5')

testing_img = np.zeros((251,128,128))

def predict():
    for i in range(0,250):
        file = "img_%s.jpg" %i
        if os.path.exists(file):
            testing_img[i]= (np.array(Image.open(file)))
        else:
            print(file, "NO Existe")
        array = model.predict(testing_img)
        result = array[i]
        answer = np.argmax(result)
        print(i)
        if answer == 0:
            print("pred: Centro")
        elif answer == 1:
            print("pred: Der")
        elif answer == 2:
            print("pred: Izq")
        elif answer == 3:
            print("pred: Up")
        elif answer == 4:
            print("pred: Down")
        elif answer == 5:
            print("pred: Blinkin")

predict()

