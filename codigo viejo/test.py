from sklearn.metrics import confusion_matrix , classification_report
import numpy as np
import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
from keras.models import load_model


data_validacion = './data/validation'

model = load_model("modelo/modelo.h5")

test_datagen = ImageDataGenerator(rescale=1. / 255)
validacion_generador = test_datagen.flow_from_directory(
    data_validacion,
    target_size=(128, 128),
    batch_size=16,
    class_mode='categorical')

y_pred = model.predict(validacion_generador)
y_pred_classes = [np.argmax(element) for element in y_pred]

print("Classification Report: \n", classification_report(validacion_generador, y_pred_classes))