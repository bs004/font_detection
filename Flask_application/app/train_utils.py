# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout, Input, GlobalAveragePooling2D, GlobalMaxPooling2D, Concatenate, concatenate

import numpy as np
np.random.seed(12)
import os
import cv2
from PIL import Image

from tqdm import tqdm


def build_model(NUM_CLASSES,IMG_SIZE):
    inputs = Input(shape=(IMG_SIZE, IMG_SIZE, 3))
    #x = img_augmentation(inputs)
    model = tf.keras.applications.EfficientNetB0(include_top=False, input_tensor=inputs, weights="imagenet")

    # Freeze the pretrained weights
    model.trainable = False

    # Rebuild top
    # x1 = GlobalAveragePooling2D(name="avg_pool")(model.output)
    # x2 = GlobalMaxPooling2D(name="max_pool")(model.output)

    # x = concatenate([x1,x2])
    # x = BatchNormalization()(x)

    # top_dropout_rate = 0.3
    # x = Dropout(top_dropout_rate, name="top_dropout")(x)
    x = Flatten(name='Flatten')(model.output)
    top_dropout_rate = 0.3
    x = Dropout(top_dropout_rate, name="top_dropout")(x)
    outputs = Dense(NUM_CLASSES, activation="sigmoid", name="pred")(x)

    # Compile
    model = tf.keras.Model(inputs, outputs, name="EfficientNet")
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4)
    model.compile(
        optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy"]
    )
    return model

def DataLoader(Train_data,Test_data):
  Font_mapping={'Oswald':0,'Roboto':1,'Open_Sans':2,'Ubuntu':3,'PT_Serif':4,'Dancing_Script':5,'Fredoka_One':6,'Arimo':7,'Noto_Sans':8,'Patua_One':9}

  #We'll use this variable throuout the module to set or modify the size of the images.
  resize1 = 384
  #we have to initialise null list in order to create a list of images(images will be store as as NxNx3 because it is a coloured image)
  dataset_train = []
  label_train = []

  dataset_test = []
  label_test = []
  #will be used to change the dimensions wherever required
  chanDim=-1

  #storing images present in 'Train' folder
  Train_images = os.listdir(Train_data)
  for i, image_name in tqdm(enumerate(Train_images)):
      if (image_name.split('.')[1] == 'jpg'):
          image = cv2.imread(Train_data +'/'+ image_name)
          image = Image.fromarray(image, 'RGB')
          image = image.resize((resize1, resize1),Image.ANTIALIAS)#here we are doing downsampling and using a technique named anti alising
          dataset_train.append(np.array(image))
          label_train.append(Font_mapping['_'.join(image_name.split('.')[0].split('_')[:-1])])

  #storing images present in 'Test' folder
  Test_images = os.listdir(Test_data)
  for i, image_name in tqdm(enumerate(Test_images)):
      if (image_name.split('.')[1] == 'jpg'):
          image = cv2.imread(Test_data +'/'+ image_name)
          image = Image.fromarray(image, 'RGB')
          image = image.resize((resize1, resize1),Image.ANTIALIAS)#here we are doing downsampling and using a technique named anti alising
          dataset_test.append(np.array(image))
          label_test.append(Font_mapping['_'.join(image_name.split('.')[0].split('_')[:-1])])

  return dataset_train,label_train,dataset_test,label_test
