#ANN training
import time
import numpy as np

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

#from keras.layers import Dropout
from keras import regularizers
from keras.callbacks import ModelCheckpoint

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
# L1 regularizer is used here in the hidden layers to prevent overfitting. L2 is an alternative 
classifier.add(Dense(units = 20, kernel_initializer = 'uniform', activation = 'relu', input_dim = 13, kernel_regularizer=regularizers.l1(0.001)))

# Adding the second hidden layer
classifier.add(Dense(units = 20, kernel_initializer = 'uniform', activation = 'relu', kernel_regularizer=regularizers.l1(0.001)))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#checkpoint
# The use of the checkpoint allows to save weights after every epoch in an .hdf5 file
filepath="weights.{epoch:02d}.hdf5"
checkpoint=keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=False, save_weights_only=True, mode='max')
callbacks_list = [checkpoint]
start_time = time.time()

# Fitting the ANN to the Training set
classifier.fit(X_train, Y_train, batch_size =1024, epochs = 100, shuffle= True, callbacks=callbacks_list )

print("--- %s seconds ---" % (time.time() - start_time))


# If the checkpoint was not used, the final weights can be saved and then loaded at a later time as shown below:
#classifier.save_weights("weights.h5")
#classifier.load_weights("weights.h5") 


#Extracting weights for first hidden layer and saving them in a .csv file
#weights, biases = classifier.layers[0].get_weights()
#np.savetxt('weights.csv', weights, delimiter=',')



