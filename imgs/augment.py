import numpy as np
from tensorflow.keras import layers
import tensorflow as tf

def _check_data_len_matches(data, targets):
   if len(data) != len(targets):
      print("WARNING: DATA LENGTH DOES NOT MATCH TARGETS")

def augment(data, targets, augmentType):
    _check_data_len_matches(data, targets)
    n = len(data)
    for i in range(n):
      data.append(augmentType(data[i]))
      targets.append(targets[i])

def shuffle_data(data, targets):
    _check_data_len_matches(data, targets)
    permutation = np.random.permutation(len(data))
    return data[permutation], targets[permutation]

def blur(img):
    noise_layer = layers.GaussianNoise(0.5)
    return noise_layer(img, training=True)

def shift_right(img, shift_amt = 5):
   return tf.roll(img, shift=shift_amt, axis=0)

def shift_down(img, shift_amt = 5):
   return tf.roll(img, shift=shift_amt, axis=1)
