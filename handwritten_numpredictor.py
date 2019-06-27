# -*- coding: utf-8 -*-
"""handWritten_NumPredictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LuIp8OLjW6LwzymiU-PhlnFQNlzX09iw

# Model that predicts 0-9 from Hand Written Images
"""

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

a = tf.__version__
print(a)

# Dataset of images consist of 28*28 handwritten image for 0 to 9

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizatrion of pixel Data:
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

# Making of a sequential model:
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))

# Output layer:
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))

# Compile of the Model:
model.compile(optimizer = 'adam',
             loss = 'sparse_categorical_crossentropy',
             metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

# Saving the model as .model file:
model.save('handWritten_NumPredictor.model')
