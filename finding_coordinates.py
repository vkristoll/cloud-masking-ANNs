# Finding coordinates in image, map, space

import os
import pandas as pd   
import osgeo
from osgeo import gdal
from osgeo import osr
from os.path import splitext
import numpy as np
import math

ds = gdal.Open('Sentinel2_image.tif') 
xoffset, px_w, rot1, yoffset, px_h, rot2 = ds.GetGeoTransform()  

# get CRS from dataset 
crs = osr.SpatialReference()
crs.ImportFromWkt(ds.GetProjectionRef())

# create lat/long crs with WGS84 datum
crsGeo = osr.SpatialReference()
crsGeo.ImportFromEPSG(4326) # 4326 is the EPSG id of lat/long crs 
t = osr.CoordinateTransformation(crs, crsGeo)


directory = os.listdir('path_a') # folder with .csv files. Each row of a file contains an index denoting the order of a pixel in an image and its spectral signature  
os.chdir('path_a')  


for file in directory:
    coord= pd.read_csv(file)     
    coord2=np.array(coord)
    numrows=len(coord2)
    A=np.zeros((numrows,20))
    A[:,6:21]=coord2[:,1:16]
    for i in range (numrows):
        #coordinates in the image
        col=coord2[i,1]-(math.floor(coord2[i,1]/1830.0))*1830  #collumn=x # The size of a Sentinel-2 image is 1830x1830 pixels for 60 m spatial resolution
        row=math.ceil(coord2[i,1]/1830.0) #row=y
        # coordinates in map
        posX = px_w * col + rot1 * row + xoffset
        posY = rot2 * col + px_h * row + yoffset 
        # coordinates in space
        (long, lat, z) = t.TransformPoint(posX, posY) 
        A[i,0]=lat
        A[i,1]=long
        A[i,2]=posX
        A[i,3]=posY
        A[i,4]=col
        A[i,5]=row        
    file_name = os.path.basename(file)
    new_filename = file_name.split('.')[0]
    np.savetxt(new_filename + "coord.csv", A, delimiter=',', header=" Lat, #Lon, #Xmap, #Ymap, #col, #row, #order, #B1,  #B2,  #B3,  #B4, #B5, #B6, #B7, #B8, #B8a, #B9, #B10, #B11, #B12",fmt='%10.8f')

        






