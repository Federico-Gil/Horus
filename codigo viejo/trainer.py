#import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

# TensorFlow y tf.keras
from tensorflow import keras

import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

training_img = np.zeros((6951,128,128))
training_tags = np.zeros((6951,1))

# 1 - 1269 centre
# 1270,2465 right
# 2466,3724 left
# 3725,4936 up
# 4937,5963 down
# 5974,6951 blinking
classes = ['center','right','left','up','down','blinking']

for i in range(1,6951):
    filename = "dataset_old/img_%s.jpg" %i
    if os.path.exists(filename):
        training_img[i]= (np.array(Image.open(filename)))
    else:
        print(filename, "NO Existe")

training_img = training_img/255

for i in range(1,1269):
    training_tags[i] = 0

for i in range(1270,2465):
    training_tags[i] = 1 

for i in range(2466,3724):
    training_tags[i] = 2

for i in range(3725,4936):
    training_tags[i] = 3

for i in range(4937,5963):
    training_tags[i] = 4

for i in range(5974,6951):
    training_tags[i] = 5

print (np.shape(training_tags),np.shape(training_img))



#scaler = MinMaxScaler()
#training_tags = scaler.fit_transform(training_tags)
training_img = training_img.reshape(-1,128,128,1)

############# IA #################
model = keras.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(128, 128,1)),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(.2),
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(training_img, training_tags, epochs=7,batch_size=16)



"""
el que funca

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(128, 128)),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acurracy'])
model.summary()

model.fit(training_img, training_tags, epochs=7,batch_size=16)
"""
#winner so far 6
model.save('model_Orus_16.h5')

#test_images = [training_img[0],training_img[150],training_img[250],training_img[350],training_img[450],training_img[550]]
predictions = model.predict(training_img[220:222])
print(predictions)



"""
La Buena
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(128, 128)),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_img, training_tags, epochs=10,batch_size=32)
"""


#cementerio de modelos

"""
model = Sequential()
model.add(LSTM(units = 128, activation='tanh', return_sequences= True, input_shape=(32,32)))
model.add(Dropout(0.1))

model.add(LSTM(units = 64, activation='tanh', return_sequences= True, input_shape=(32,32)))
model.add(Dropout(0.2))

model.add(LSTM(units = 64, activation='tanh', return_sequences= True))
model.add(Dropout(0.3))

model.add(LSTM(units = 32, activation='tanh'))
model.add(Dropout(0.5))

model.add(Dense(units=6))

model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
model.summary()
model.fit(training_img,training_tags,epochs=20,batch_size=512)
"""