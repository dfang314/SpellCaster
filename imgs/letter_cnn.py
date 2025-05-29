from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
from PIL import Image as im
import os
import augment

def train_model():
    
    imgs_path = __file__[:-len("/letter_cnn.py")]
    letter_imgs_path = imgs_path + "/letter_imgs"
    letter_imgs = os.listdir(letter_imgs_path)
    # imgs are 74x74

    imgs = []
    labels = []
    for letter_img in letter_imgs:
        img = im.open(f"{letter_imgs_path}/{letter_img}")
        imgs.append(keras.utils.img_to_array(img))

    with open(imgs_path + "/letter_labels") as label_file:
        labels = [int(label) for label in label_file]
    
    augment.augment(imgs, labels, augment.blur)
    augment.augment(imgs, labels, augment.shift_down)
    augment.augment(imgs, labels, lambda x:augment.shift_down(x, -5))
    augment.augment(imgs, labels, augment.shift_right)
    augment.augment(imgs, labels, lambda x:augment.shift_right(x, -5))
    imgs, labels = augment.shuffle_data(imgs, labels)

    # print(imgs[0].shape)
    # print(f"Loaded {len(imgs)} images")
    # print(f"Found labels {labels}")

    model = keras.Sequential([
        layers.Input(shape=(74, 74, 4)),

        layers.Conv2D(filters=64, kernel_size=2, padding="same", strides=1),
        layers.BatchNormalization(),
        layers.ReLU(),

        layers.Conv2D(filters=64, kernel_size=2, padding="same", strides=1),
        layers.BatchNormalization(),
        layers.ReLU(),

        layers.Conv2D(filters=32, kernel_size=2, padding="same", strides=1),
        layers.BatchNormalization(),
        layers.ReLU(),
        layers.MaxPooling2D(pool_size=3, strides=1),

        layers.Conv2D(filters=32, kernel_size=3, padding="same", strides=1),
        layers.BatchNormalization(),
        layers.ReLU(),
        layers.MaxPooling2D(pool_size=3, strides=1),

        layers.Flatten(),

        layers.Dense(units=1024, activation="relu"),
        layers.Dropout(rate=0.2),

        layers.Dense(units=128, activation="relu"),
        layers.Dropout(rate=0.2),

        layers.Dense(units=26, activation="softmax"),
        
    ])

    model.compile(
        optimizer='adam',
        loss= keras.losses.CategoricalCrossentropy(),
        metrics=['Accuracy'],
    )

    model.fit(
        x=tf.convert_to_tensor(imgs),
        y=tf.convert_to_tensor(labels),
        epochs=50,
        validation_split=0.1,
    )

    model.save("letter.keras")

    return model

def load_model():
    return keras.models.load_model("letter.keras")

# model = load_model()
# img = im.open(f"test.png")

# import generate_subimg as gen

# letter_imgs = gen.generate_letter_imgs(img)
# gem_imgs = [gen.generate_gem_img(letter_img) for letter_img in letter_imgs]
# for img in gem_imgs:
#     img.show()
#     print(model(tf.expand_dims(keras.utils.img_to_array(img), 0)))
