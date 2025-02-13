from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds
import tensorflow as tf
from PIL import Image as im
import os

def train_model():
    
    imgs_path = __file__[:-len("/gem_cnn.py")]
    gem_imgs_path = imgs_path + "/gem_imgs"
    gem_imgs = os.listdir(gem_imgs_path)
    # imgs are 35x35

    imgs = []
    labels = []
    for gem_img in gem_imgs:
        img = im.open(f"{gem_imgs_path}/{gem_img}")
        imgs.append(keras.utils.img_to_array(img))
    
    print(imgs[0].shape)
    print(f"Loaded {len(imgs)} images")
    

    model = keras.Sequential([
        layers.Input(shape=(35, 35, 4)),

        layers.Conv2D(filters=32, kernel_size=3, padding="same", strides=1),
        layers.BatchNormalization(),
        layers.ReLU(),

        layers.Conv2D(filters=32, kernel_size=3, padding="same", strides=1),
        layers.BatchNormalization(),
        layers.ReLU(),
        layers.MaxPooling2D(pool_size=3, strides=2), # output is 17x17

        layers.Conv2D(filters=16, kernel_size=3, padding="same", strides=1),
        layers.BatchNormalization(),
        layers.ReLU(),
        layers.MaxPooling2D(pool_size=3, strides=2), # 8x8

        layers.Flatten(),

        layers.Dense(units=256, activation="relu"),
        layers.Dropout(rate=0.2),

        layers.Dense(units=32, activation="relu"),
        layers.Dropout(rate=0.2),

        layers.Dense(units=1, activation="softmax"),
        
    ])

# train_model()