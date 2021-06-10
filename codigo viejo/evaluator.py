from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
import tensorflow as tf

model = tf.keras.models.load_model('./modelo/modelo.h5')
model.summary()

entrenamiento_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator(rescale=1. / 255)

data_validacion = './data/validation'

validacion_generador = test_datagen.flow_from_directory(
    data_validacion,
    target_size=(128, 128),
    batch_size=16,
    class_mode='categorical')

model.evaluate(validacion_generador)