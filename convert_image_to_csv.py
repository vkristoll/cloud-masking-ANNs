#Convert a Sentinel-2 image with 13 bands to a .csv file. 
#Each row of the output file contains the 13 values of the spectral signature
#The output can be feeded to the ANN
    
import os
import pandas as pd
from osgeo import gdal
from os.path import splitext
import numpy as np
import time
directory = os.listdir('path to folder containing the images')
os.chdir('path to folder containing the images')

c=0
start_time = time.time()   

for file in directory:
   c=c+1
   print(" The file number is %s" %c) 
   print("--- %s seconds ---" % (time.time() - start_time)) 
   ds=gdal.Open(file) 
   imarray = np.array(ds.ReadAsArray())
   sizex= ... # enter size of image, i.e. rows x collumns
   reshape=np.reshape(imarray, (13,sizex)) # '13' is the number of bands
   reshape2=reshape.T
   reshape3=reshape2/10000 # scaling the values
   file_name = os.path.basename(file)
   new_filename = file_name.split('.')[0]
   np.savetxt(new_filename + "_converted.csv", reshape3, delimiter=',', header=" #B1,  #B2,  #B3,  #B4, #B5, #B6, #B7, #B8, #B8a, #B9, #B10, #B11, #B12",fmt='%10.4f')
