# -*- coding: utf-8 -*-

# For data manipulation
import numpy as np
np.random.seed(12)

# Deep learning modules
import tensorflow as tf
# For working with system paths
import os

from train_utils import *

#We set the path to the folder where training set images are present.
base_path='./font_data/images'
Train_data_path = os.sep.join([base_path,'train'])
Test_data_path = os.sep.join([base_path,'valid'])

X_train, y_train, X_test, y_test = DataLoader(Train_data_path,Test_data_path)
y_train,y_test=tf.keras.utils.to_categorical(y_train),tf.keras.utils.to_categorical(y_test)

model=build_model(10,resize1)

model.fit(np.array(X_train),
          y_train,
          batch_size=16,
          verbose=2,
          epochs=50,
          shuffle=True,
          callbacks=[tf.keras.callbacks.ReduceLROnPlateau(monitor='loss', factor=0.5, patience=5, min_lr=0.000001)])

print("Test_Accuracy: {:.2f}%".format(model.evaluate(np.array(X_test), np.array(y_test))[1] * 100))

model.save('label_classifier.hdf5')