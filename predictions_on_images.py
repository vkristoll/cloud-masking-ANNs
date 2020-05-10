# Making predictions for the spectra of Sentinel-2 images

# Importing the libraries
import numpy as np
import pandas as pd

# Defining the ANN architecture

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 20, kernel_initializer = 'uniform', activation = 'relu', input_dim = 13))

# Adding the second hidden layer
classifier.add(Dense(units = 20, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Load the weights from the trained ANN

classifier.load_weights("weights.hdf5") 


#Read the file used for training in order to extract the statistical parameters needed for the Z-score normalization of the values.

dataset_train=pd.read_csv("train_spectra.csv") # Read the spectra used for training the ANN

X_train = dataset.iloc[:, 'collumn of 1st band':'collumn of last band'].values

# Applying the Z-score normalization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train =sc.fit(X_train)


#Making predictions for the images

import os
import pandas as pd
import numpy as np
from os.path import splitext
directory = os.listdir('path to folder with .csv files containing spectra for the images')
os.chdir('path to folder with .csv files containing spectra for the images')

for file in directory:
# Importing the dataset
    X_test = pd.read_csv(file)
    # Feature Scaling
    X_test = sc.transform(X_test)  # normalizes the test data based on the statistical parameters of the training data
    # Part 3 - Making predictions and evaluating the model
    # Predicting the Test set results
    y_pred = classifier.predict(X_test)
    y_pred=np.rint(y_pred)
    
    file_name = os.path.basename(file)
    new_filename = file_name.split('.')[0]
    np.savetxt(new_filename + "predictions.csv", y_pred, delimiter=',',fmt='%10.0f')    
   
   


   







    
    





            
