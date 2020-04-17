# Final Project Computer Graphics 204382

# -*- coding: utf-8 -*-
"""graphic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ed2FL9kDsHUip2CKgyaBh16RNNxjCcq
"""

# description:classifies image

# pip install keras

# load data
from keras.datasets import cifar10
(x_train,y_train), (x_test,y_test) = cifar10.load_data()

# print the data types
print(type(x_train))
print(type(y_train))
print(type(x_test))
print(type(y_test))

# get the shapes
print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print('x_test shape:', x_test.shape)
print('y_test shape:', y_test.shape)
print(y_train)

# take a look at first image (at index=0) in the training data set
x_train[0]

# show image as picture
import matplotlib.pyplot as plt
img = plt.imshow(x_train[0])

# print the label of image
print('the label is:', y_train[0])

"""0=airplane, 1=automobile, 2=bird, 3=cat, 4=deer, 5=dog, 6=frog, 7=horse, 8=ship, 9=truck"""

# one-hot encoding: convert the labels into a set of 10 numbers into the neural network
from keras.utils import to_categorical
y_train_one_hot = to_categorical(y_train)
y_test_one_hot = to_categorical(y_test)

# print the new labels in the training data set
print(y_train_one_hot)

# print an example of the new labels
print('the one hot label is:',y_train_one_hot[0])

# nomalize the pixels in the image to values between 0&1
x_train = x_train/255
x_test = x_test/255

# build the cnn
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
# create the architecture
model = Sequential()
# convolution layer
model.add(Conv2D(32, (5,5), activation='relu', input_shape=(32,32,3)) )
# Maxpooling layer
model.add(MaxPooling2D(pool_size=(2,2)) )
# convolution layer
model.add(Conv2D(32, (5,5), activation='relu') )
# Maxpooling layer
model.add(MaxPooling2D(pool_size=(2,2)))
# flatten layer
model.add( Flatten() )
model.add( Dense(1000,activation='relu') )
model.add( Dense(10, activation='softmax') )

# compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# train the model
hist = model.fit(x_train, y_train_one_hot, batch_size=256, epochs=10, validation_split=0.3)

#save the model
model.save('my_model.h5')

#load the model
from keras.models import load_model
model = load_model('my_model.h5')
