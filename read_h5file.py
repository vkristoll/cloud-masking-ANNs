# import required libraries
import h5py as h5
import numpy as np

# Read H5 file
# This file carries a database with spectra for cloud masking applications. It was created during the study described in https://doi.org/10.3390/rs8080666
# It can be downloaded from https://git.gfz-potsdam.de/EnMAP/sentinel2_manual_classification_clouds

f = h5.File("20170412_s2_manual_classification_data.h5", "r")

# Get and print list of datasets within the H5 file
datasetNames = [n for n in f.keys()]
for n in datasetNames:
        print(n)
        
# extract reflectance data from the H5 file

#class_ids 
class_ids=f['class_ids']
class_idsData=class_ids[:]

#class_names
class_names=f['class_names']
class_namesData=class_names[:]

#spectra
spectra=f['spectra'] 
spectraData=spectra[:]   

#classes
classes=f['classes'] 
classesData=classes[:]  
