#Run fft for one band of a Sentinel-2 image

import numpy as np
from matplotlib import pyplot as plt
from osgeo import gdal

#Run fft
img =gdal.Open('T31TFH_20180311T103019_B10_cut.tif') # Read a Sentinel-2 band (e.g. B10)
imarray = np.array(img.ReadAsArray())
f = np.fft.fft2(imarray)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Plot the magnitude
plt.figure(figsize=(20,20)),plt.imshow(imarray, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.figure(figsize=(20,20)),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()          



