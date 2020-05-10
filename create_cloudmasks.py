#Create cloud masks
#This code converts the predictions of the ANN to an image file which is the cloud mask. The input file is in a .csv format and its size is: rows= the total number of the spectra of an image, columns=1 i.e. the label (cloud [1] or water [0])

import os
import pandas as pd
from osgeo import gdal
from os.path import splitext
import numpy as np
import tifffile as tiff

directory = os.listdir('path to folder containing the .csv files') # path to files containing the predictions 
os.chdir('path to folder containing the .csv files')   

for file in directory:
   ypred = pd.read_csv(file, header=None) # these files do not contain a header
   ypred2=np.array(ypred)    
   
   sizex=1130*1830
   for i in range(sizex):
        if (ypred2[i,0]==1):
            ypred2[i,0]=255   
   
   rows='number of rows of image'
   columns= 'number of columns of image'
            
   reshape=np.reshape(ypred2,(rows,columns)) 
   reshape2=np.uint8(reshape)  
   file_name = os.path.basename(file)
   new_filename = file_name.split('.')[0]   
   tiff.imsave(new_filename + "mask.tif", reshape2) 







