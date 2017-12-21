# the next two imports are to ignore few tensorflow warnings
# comment the next two lines on your system for more details on the warnings.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten, Dropout
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras import regularizers
from keras import metrics
from keras.utils.np_utils import to_categorical
from keras import optimizers
from scipy import misc

BATCH_SIZE = 64
SAMPLE_SIZE = 10000

train_datagen = ImageDataGenerator(
        rescale=1./255,
        fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
        'VOCdevkit/VOC2010/JPEGImages2/',  # this is the target directory
        target_size=(128, 128),  # all images will be resized to 150x150
        batch_size=BATCH_SIZE,
        class_mode='categorical')

# SAMPLE_SIZE = len(list(train_generator))


model = Sequential()
model.add(Conv2D(16, (3, 3), input_shape=(128, 128, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (5, 5)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(58, (7, 7)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(20))
model.add(Activation('sigmoid'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit_generator(
        train_generator,
        steps_per_epoch=SAMPLE_SIZE//BATCH_SIZE,
        verbose=1,
        epochs=30)
# n = 0
#
# for imgs, labels in train_generator:
#     print("Here")
#     if n > 2:
#         break
#     X_train = np.array(imgs)
#     y_train = np.array(labels)
#     model.fit(X_train, y_train)
#     n += 1

model.save_weights('first_try.h5')
