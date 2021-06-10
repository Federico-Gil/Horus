import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
import tensorflow as tf

K.clear_session()


epocas= 10
longitud, altura = 50, 50
batch_size = 4
filtrosConv1 = 24
filtrosConv2 = 24
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2, 2)
tamano_filtro3 = (2, 2)
tamano_pool = (2, 2)
clases = 2

data_entrenamiento = './over2/training'
data_validacion = './over2/validation'


##Preparamos nuestras imagenes
#

entrenamiento_datagen = ImageDataGenerator(rescale=1. / 255,rotation_range=15,zoom_range=0.1,brightness_range=(0.2,0.8),shear_range=5)
test_datagen = ImageDataGenerator(rescale=1. / 255,rotation_range=15,zoom_range=0.1,brightness_range=(0.2,0.8),shear_range=5)

entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

validacion_generador = test_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')


cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, input_shape=(longitud, altura, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Convolution2D(filtrosConv2, tamano_filtro2))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(.5))
cnn.add(Dense(clases, activation='softmax'))

cnn.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy', tf.keras.metrics.Recall()])


cnn.fit(
    entrenamiento_generador,
    epochs=epocas,
    validation_data=validacion_generador)

target_dir = './modelo/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
cnn.save('./modelo/modelo.h5')


"""
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, input_shape=(longitud, altura, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Convolution2D(filtrosConv2, tamano_filtro2))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(.5))
cnn.add(Dense(clases, activation='softmax'))
"""