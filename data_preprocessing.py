# Data Preprocessing

# Importing the libraries
import numpy as np
import pandas as pd


# Importing the dataset
# Description of dataset: It's a .csv file. Each row contains 14 collumns: a) 13 collumns for the reflectance values of Sentinel-2 satellite spectra, b)one column for the label of the spectra which is either cloud (label:1) or water (label:0). 

dataset = pd.read_csv('add path to the .csv file') 
X_train = dataset.iloc[:, 'collumn of 1st band':'collumn of last band'].values
Y_train = dataset.iloc[:, 'collumn of label'].values


# Feature Scaling
# Applying Z-score normalization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) #Scaling the test set spectra according to statistical values of the train set

