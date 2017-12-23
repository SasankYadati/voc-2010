from keras.models import load_weights
from sklearn.metrics import confusion_matrix
import h5py
import numpy as np
from os import listdir
from os.path import isfile, join

model = Sequential()
model.add(Conv2D(24, (3, 3), input_shape=(142, 142, 3)))
model.add(Activation('relu'))

model.add(Conv2D(36, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))

model.add(Conv2D(48, (3, 3)))
model.add(Activation('relu'))

model.add(Conv2D(56, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))

model.add(Conv2D(64, (2, 2)))
model.add(Activation('relu'))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(20))
model.add(Activation('softmax'))
              
              
              
model.load_weights('first_try.h5', by_name=True)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
true=np.zeroes(20,1)
for x in onlyfiles:
	
	img = cv2.imread(x)
	img = cv2.resize(img,(142,142))
	img = np.reshape(img,[1,142,142,3])

	pred = model.predict_classes(img)
	if 'bird' in x:
		true[2][0] = 1
	elif 'boat' in x:
		true[3][0] = 1
	elif 'bottle' in x:
		true[4][0] = 1
	elif 'bus' in x:
		true[5][0] = 1
	elif 'car' in x:
		true[6][0] = 1
	elif 'cat' in x:
		true[7][0] = 1
	elif 'cow' in x:
		true[9][0] = 1
	elif 'diningtable' in x:
		true[10][0] = 1
	elif 'dog' in x:
		true[11][0] = 1
	elif 'horse' in x:
		true[12][0] = 1
	elif 'train' in x:
		true[18][0] = 1
	print(confusion_matrix(pred, true))
