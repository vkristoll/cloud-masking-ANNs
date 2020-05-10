# calculate statistical metrics for every band of the Sentinel-2 images
# calculate SNR, mean, std, skewness, kurtosis
   
import os
import pandas as pd
from osgeo import gdal
import numpy as np
import scipy
import scipy.stats
directory = os.listdir('path to a folder containing the images')
os.chdir('path to a folder containing the images')   

for file in directory:    
   ds=gdal.Open(file) 
   file_name = os.path.basename(file)
   snr=np.zeros((13,2))
   mean=np.zeros((13,2))
   std=np.zeros((13,2))
   skew=np.zeros((13,2))
   kurtosis=np.zeros((13,2))

   num=[1,2,3,4,5,6,7,8,9,10,11,12,13]
   snr[:,0]=num;
   mean[:,0]=num; 
   std[:,0]=num; 
   skew[:,0]=num; 
   kurtosis[:,0]=num; 
   
      
   for i in range(13):
       array=ds.GetRasterBand(i+1).ReadAsArray()
       snr[i,1] = scipy.stats.signaltonoise(array, axis=None)
       mean[i,1] = np.mean(array,axis=(None))
       
   np.savetxt(file_name + "_snr.txt", snr, delimiter=',', fmt='%10.2f')
   np.savetxt(file_name + "_mean.txt", mean, delimiter=',', fmt='%10.2f') 
   np.savetxt(file_name + "_std.txt", std, delimiter=',', fmt='%10.2f')  
   np.savetxt(file_name + "_skew.txt", skew, delimiter=',', fmt='%10.2f') 
   np.savetxt(file_name + "_kurtosis.txt", kurtosis, delimiter=',', fmt='%10.2f') 


             

