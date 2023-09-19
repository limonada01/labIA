import tensorflow as tf
import keras
from keras import layers
#import numpy as np

cantPixelsX = 28
cantPixelsY = 28
nroCanales = 1 # 1: blanco y negro

modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(cantPixelsX,cantPixelsY,nroCanales)),#transforma los la matriz de pixels en un vector unidimensional
    tf.keras.layers.Dense(units=50, activation="relu"),
    tf.keras.layers.Dense(units=50, activation="relu"),
    tf.keras.layers.Dense(units=10, activation="softmax")

])