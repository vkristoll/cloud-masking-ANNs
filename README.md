# Cloud masking with artificial neural networks (ANNs)

This repository contains code related to the study analyzed in the paper cited below:

Kristollari, Viktoria, and Vassilia Karathanassi. "Artificial neural networks for cloud masking of Sentinel-2 ocean images with noise and sunglint." International Journal of Remote Sensing 41, no. 11 (2020): 4102-4135.

It can be accessed in: https://doi.org/10.1080/01431161.2020.1714776

If you cannot access the paper please contact me at: vkristoll@central.ntua.gr. Alternatively, the preprint can be downloaded from my personal website: http://users.ntua.gr/vkristoll/assets/manuscript_cloud_masking_revised_technical_V2preprint.pdf

![ANN cloud masking methodology](/images/ANN_cloud_masking_methodology.png)

## Steps to implement the code

Run:
>1. "read_h5file.py" to download Sentinel-2 spectra and extract cloud and water categories. Water spectra with noise can
be found in https://doi.org/10.6084/m9.figshare.8075396.v1
>
>2. "data_preprocessing.py" to create training and test data for the ANN. 
>
>3. "ANN_training.py" to train the network and save the weights in .hdf5 file.
>
>4. "predictions_evaluation.py" to evaluate predictions.
>
>5. the commands in the "gdal_commands" file to convert the Sentinel-2 images to .tiff files.
>
>6. "convert_image_to_csv.py" to convert Sentinel-2 .tiff files to .csv files.
>
>7. "predictions_on_images.py" to make predictions for Sentinel-2 images.
>
>8. "create_cloudmasks.py" to convert the predictions to cloudmasks.


*Detailed guidelines are included inside each script.*

### Optionally:

Run:
- "fft.py" to to apply the Fast Fourier Transform.
- "statistical metrics.py" to calculate several metrics.
- "finding_coordinates.py" to find coordinates in image, map and space when given a .csv file containing an index denoting the order of a pixel.


If you use this code, please cite the below paper.

```
@article{doi:10.1080/01431161.2020.1714776,
author = {Viktoria Kristollari and Vassilia Karathanassi},
title = {Artificial neural networks for cloud masking of Sentinel-2 ocean images with noise and sunglint},
journal = {International Journal of Remote Sensing},
volume = {41},
number = {11},
pages = {4102-4135},
year  = {2020},
publisher = {Taylor & Francis},
doi = {10.1080/01431161.2020.1714776},
URL = {  https://doi.org/10.1080/01431161.2020.1714776}    
}
```








