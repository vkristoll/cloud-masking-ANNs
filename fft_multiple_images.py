# Code to run fft (Fast Fourier Transform)

import numpy as np
from osgeo import gdal
import os
from os.path import splitext
import tifffile as tiff

directory = os.listdir('path_a') # path_a: folder which contains a different subfolder for each Sentilel-2 product. Each of the subfolders contains 13 bands stored in 13 separate .tif files
os.chdir('path_a')   

for file in directory:
    file_name = os.path.basename(file) # Read name of a subfolder
    directory2 = os.listdir('path_a' + file_name) 
    os.chdir('path_a' + file_name) #Enter inside a subfolder directory
    for file in directory2:    
            img =gdal.Open(file)
            imarray = np.array(img.ReadAsArray())
            f = np.fft.fft2(imarray)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = 20*np.log(np.abs(fshift))
            file_name2 = os.path.basename(file)
            new_filename = file_name2.split('.')[0]
            tiff.imsave(new_filename + "_magnitude.tif", magnitude_spectrum )
   



           










            
            
            
            
            


