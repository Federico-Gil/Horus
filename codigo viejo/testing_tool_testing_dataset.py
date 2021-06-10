import numpy as np
import cv2
import os
import time
import sys
import os

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

testing_img = np.zeros((251,128,128))
testing_tags = np.zeros((251,1))

for i in range(0,35):
    testing_tags[i] = 0

for i in range(36,90):
    testing_tags[i] = 1

testing_tags[88] = 5
testing_tags[89] = 5

testing_tags[91] = 0
testing_tags[92] = 0

for i in range(93,148):
    testing_tags[i] = 2

testing_tags[149] = 0

for i in range(150,193):
    testing_tags[i] = 3

testing_tags[194] = 0
testing_tags[195] = 0
testing_tags[196] = 0

for i in range(197,250):
    testing_tags[i] = 4

classes = ['center','right','left','up','down','blinking']

for i in range(0,250):
    filename = "testing_dataset/img_%s.jpg" %i
    if os.path.exists(filename):
        testing_img[i]= (np.array(Image.open(filename)))
    else:
        print(filename, "NO Existe")

pred = np.array(model.predict(testing_img[0:250]))
for i in pred:
    print(i)

aux = np.zeros((251,1))

for i in range(0,250):
    aux[i] = np.argmax(pred[i])

print(aux)

true_positives = 0
false_negatives = 0

for i in range(0,250):
    if np.round(aux[i]) == testing_tags[i]:
        true_positives+=1
    else:
        false_negatives+=1

print("Recall: ",true_positives/(true_positives + false_negatives))

"""
m = tf.keras.metrics.Recall()
m.update_state([0, 1, 1, 1], [1, 0, 1, 1])
print(m.result().numpy())
"""
#model.evaluate(testing_img, testing_tags, verbose=2)